#!/usr/bin/env python3
"""
LLM-powered PR report generator.

Fetches PR data (reusing fetch_and_report), reads a user-editable prompt
template from prompts/pr-report-prompt.md, fills in variables, sends to
an Anthropic-compatible LLM, and saves the markdown report.

Supports:
  - Direct Anthropic API (api.anthropic.com)
  - AMD LLM Gateway (llm-api.amd.com)
  - Any Anthropic-compatible endpoint

Required env vars:
  GITHUB_TOKEN              - GitHub API token (auto-provided on Actions)
  ANTHROPIC_API_KEY         - Anthropic API key (or "dummy" for gateway)

Optional env vars:
  ANTHROPIC_BASE_URL        - Override API base URL (default: https://api.anthropic.com)
  AMD_LLM_GATEWAY_KEY       - AMD gateway subscription key header
  LLM_MODEL                 - Model name (default: Claude-Sonnet-4.6)
  LLM_MAX_TOKENS            - Max response tokens (default: 8192)
  PROMPT_FILE               - Path to prompt template (default: prompts/pr-report-prompt.md)
  REPO_OWNER / REPO_NAME / PR_LABEL  - Override target repo/label
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

sys.path.insert(0, SCRIPT_DIR)
from fetch_and_report import (
    collect_all_data,
    save_report,
    get_yesterday_report,
    OWNER,
    REPO,
    REPO_URL,
    PR_LABEL,
)


def load_prompt_template(path=None):
    if path is None:
        path = os.path.join(PROJECT_ROOT, "prompts", "pr-report-prompt.md")
    path = os.environ.get("PROMPT_FILE", path)
    if not os.path.isabs(path):
        path = os.path.join(PROJECT_ROOT, path)
    print(f"Loading prompt template: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def build_prompt(template, pr_data, yesterday_report=None):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    groups = {
        "needs_attention": [p for p in pr_data if p["category"] == "needs_attention"],
        "stale":           [p for p in pr_data if p["category"] == "stale"],
        "wip_not_draft":   [p for p in pr_data if p["category"] == "wip_not_draft"],
        "healthy":         [p for p in pr_data if p["category"] == "healthy"],
        "in_progress":     [p for p in pr_data if p["category"] == "in_progress"],
        "draft":           [p for p in pr_data if p["category"] == "draft"],
    }

    if yesterday_report:
        yesterday_section = (
            "## Yesterday's Report (context carryover)\n\n"
            + yesterday_report[:4000]
            + "\n\n---"
        )
    else:
        yesterday_section = "(No previous report — this is day one.)"

    def slim_pr(p):
        """Strip bulky file lists from testCoverage to keep the prompt compact."""
        pr = dict(p)
        tc = pr.get("testCoverage")
        if tc:
            pr["testCoverage"] = {
                "verdict": tc.get("verdict", "unknown"),
                "sourceCount": tc.get("sourceCount", 0),
                "testCount": tc.get("testCount", 0),
                "detail": tc.get("detail", ""),
                "sourceFiles": [os.path.basename(f) for f in tc.get("sourceFiles", [])[:10]],
                "testFiles": [os.path.basename(f) for f in tc.get("testFiles", [])[:5]],
            }
        return pr

    slim_groups = {k: [slim_pr(p) for p in v] for k, v in groups.items()}
    pr_data_json = json.dumps(slim_groups, indent=2, default=str)

    missing_tests = [p for p in pr_data if p.get("testCoverage", {}).get("verdict") == "missing_tests"]
    has_tests = [p for p in pr_data if p.get("testCoverage", {}).get("verdict") == "has_tests"]

    variables = {
        "today": today,
        "owner": OWNER,
        "repo": REPO,
        "repo_url": REPO_URL,
        "pr_label": PR_LABEL,
        "total_prs": str(len(pr_data)),
        "needs_attention_count": str(len(groups["needs_attention"])),
        "stale_count": str(len(groups["stale"])),
        "wip_not_draft_count": str(len(groups["wip_not_draft"])),
        "healthy_count": str(len(groups["healthy"])),
        "in_progress_count": str(len(groups["in_progress"])),
        "draft_count": str(len(groups["draft"])),
        "missing_tests_count": str(len(missing_tests)),
        "has_tests_count": str(len(has_tests)),
        "pr_data_json": pr_data_json,
        "yesterday_section": yesterday_section,
    }

    prompt = template
    for key, value in variables.items():
        prompt = prompt.replace("{{" + key + "}}", value)

    return prompt


def call_llm(prompt):
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY is not set.", file=sys.stderr)
        print("Set it to your Anthropic key, or 'dummy' if using AMD gateway.", file=sys.stderr)
        sys.exit(1)

    base_url = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
    model = os.environ.get("LLM_MODEL", "Claude-Sonnet-4.6")
    max_tokens = int(os.environ.get("LLM_MAX_TOKENS", "8192"))
    gateway_key = os.environ.get("AMD_LLM_GATEWAY_KEY", "")

    url = f"{base_url.rstrip('/')}/v1/messages"

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }
    if gateway_key:
        headers["Ocp-Apim-Subscription-Key"] = gateway_key

    body = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")

    print(f"Calling LLM: {base_url} / model={model} / max_tokens={max_tokens}")
    if gateway_key:
        print("  Using AMD LLM Gateway header")

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read())
            text = data["content"][0]["text"]
            usage = data.get("usage", {})
            print(f"  LLM response: {usage.get('input_tokens', '?')} input / {usage.get('output_tokens', '?')} output tokens")
            return text
    except urllib.error.HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        print(f"ERROR: LLM API returned HTTP {e.code}", file=sys.stderr)
        print(f"  Response: {body_text[:500]}", file=sys.stderr)
        sys.exit(1)
    except Exception as ex:
        print(f"ERROR: LLM API call failed: {ex}", file=sys.stderr)
        sys.exit(1)


def main():
    prefix = os.environ.get("REPORT_PREFIX", "llm-pr-report")
    print(f"=== LLM-Powered PR Report Generator ({PR_LABEL}) ===\n")

    reports_dir = os.path.join(PROJECT_ROOT, "reports")

    print("Phase 1: Collecting PR data from GitHub...")
    pr_data = collect_all_data()
    if not pr_data:
        print("No PR data collected. Exiting.")
        sys.exit(1)

    print(f"\nPhase 2: Building prompt...")
    template = load_prompt_template()
    yesterday_report = get_yesterday_report(reports_dir, prefix=prefix)
    prompt = build_prompt(template, pr_data, yesterday_report)

    print(f"  Prompt length: {len(prompt):,} chars")

    print(f"\nPhase 3: Generating report via LLM...")
    report = call_llm(prompt)

    print(f"\nPhase 4: Saving report...")
    dated_file, latest_file = save_report(
        report, reports_dir, prefix=prefix
    )

    print(f"  Saved: {dated_file}")
    print(f"  Latest: {latest_file}")
    print("\nDone.")


if __name__ == "__main__":
    main()
