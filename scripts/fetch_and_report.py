#!/usr/bin/env python3
"""
Fetch open PRs for rocprofiler-systems and generate a categorized markdown report.
Mirrors the logic in generate-pr-report.js.

Supports authenticated (GITHUB_TOKEN) and unauthenticated GitHub API access.
With a token (e.g. on GitHub Actions) the rate limit is 5000 req/hour,
enough to fully enrich all PRs with CI + review data.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

OWNER = os.environ.get("REPO_OWNER", "ROCm")
REPO = os.environ.get("REPO_NAME", "rocm-systems")
REPO_URL = f"https://github.com/{OWNER}/{REPO}"
PR_LABEL = os.environ.get("PR_LABEL", "project: rocprofiler-systems")

API_BASE = f"https://api.github.com/repos/{OWNER}/{REPO}"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
remaining_calls = {"core": 4999 if GITHUB_TOKEN else 59, "search": 29 if GITHUB_TOKEN else 10}


def api_get(url, is_search=False):
    kind = "search" if is_search else "core"
    if remaining_calls[kind] <= 0:
        return None
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "rocprof-report-script",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            remaining_calls[kind] = int(resp.headers.get("X-RateLimit-Remaining", remaining_calls[kind] - 1))
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        if e.code == 403:
            remaining_calls[kind] = 0
            print(f"  Rate limited on {kind} API", file=sys.stderr)
        else:
            print(f"  HTTP {e.code} for {url}", file=sys.stderr)
        return None
    except Exception as ex:
        print(f"  Error: {ex}", file=sys.stderr)
        return None


def days_since(iso_date):
    dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    return (datetime.now(timezone.utc) - dt).days


def is_wip_title(title):
    return bool(re.search(r"\b(WIP|DO NOT (MERGE|REVIEW)|NOT READY)\b", title, re.IGNORECASE))


def categorize(pr):
    if pr["isDraft"]:
        return "draft"
    if is_wip_title(pr["title"]):
        return "wip_not_draft"
    ci = pr.get("ciStatus", {}).get("overall", "unknown")
    review = pr.get("reviewInfo", {}).get("reviewDecision", "unknown")
    if ci == "failing" or review == "changes_requested":
        return "needs_attention"
    if pr["daysSinceUpdate"] >= 3:
        return "stale"
    if ci == "passing" and review in ("approved", "pending"):
        return "healthy"
    return "in_progress"


# ── Phase 1: Search API to get all PR numbers + basic data ──

def fetch_search_results():
    q = f"repo:{OWNER}/{REPO} is:pr is:open label:\"{PR_LABEL}\""
    url = f"https://api.github.com/search/issues?q={urllib.request.quote(q)}&per_page=100&sort=updated&order=desc"
    print(f"Searching: {q}")
    data = api_get(url, is_search=True)
    if not data:
        return []
    items = data.get("items", [])
    print(f"  Found {data.get('total_count', '?')} PRs ({len(items)} returned)")
    return items


# ── Phase 2: pulls.list to get full PR objects (head.sha, additions, etc.) ──

def fetch_pulls_pages(target_numbers):
    """Fetch open PR pages until we've found all target PRs or run out of pages."""
    found = {}
    page = 1
    max_pages = 10
    while page <= max_pages and len(found) < len(target_numbers):
        if remaining_calls["core"] <= 10:
            break
        url = f"{API_BASE}/pulls?state=open&per_page=100&sort=updated&direction=desc&page={page}"
        print(f"  Fetching pulls page {page}... (core remaining: {remaining_calls['core']})")
        data = api_get(url)
        if not data or len(data) == 0:
            break
        for pr in data:
            if pr["number"] in target_numbers:
                found[pr["number"]] = pr
        page += 1
        time.sleep(0.2)
    print(f"  Matched {len(found)}/{len(target_numbers)} PRs from pulls.list")
    return found


# ── Phase 3: CI status and reviews (individual calls) ──

def fetch_ci_status(head_sha):
    if remaining_calls["core"] <= 2:
        return {"overall": "unknown", "failing": [], "inProgress": []}
    url = f"{API_BASE}/commits/{head_sha}/check-runs?per_page=50"
    data = api_get(url)
    if not data:
        return {"overall": "unknown", "failing": [], "inProgress": []}
    runs = data.get("check_runs", [])
    if not runs:
        return {"overall": "no_checks", "failing": [], "inProgress": []}
    failing = [r["name"] for r in runs if r.get("conclusion") in ("failure", "timed_out")]
    in_progress = [r["name"] for r in runs if r.get("status") != "completed"]
    all_passed = all(r.get("conclusion") in ("success", "skipped", "neutral") for r in runs)
    if in_progress:
        overall = "in_progress"
    elif failing:
        overall = "failing"
    elif all_passed:
        overall = "passing"
    else:
        overall = "unknown"
    return {"overall": overall, "failing": failing, "inProgress": in_progress}


def fetch_reviews(pr_number):
    if remaining_calls["core"] <= 2:
        return {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}
    url = f"{API_BASE}/pulls/{pr_number}/reviews"
    data = api_get(url)
    if not data:
        return {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}
    latest_by_user = {}
    for review in data:
        if review.get("state") != "COMMENTED":
            latest_by_user[review["user"]["login"]] = review["state"]
    states = list(latest_by_user.values())
    if "CHANGES_REQUESTED" in states:
        decision = "changes_requested"
    elif "APPROVED" in states:
        decision = "approved"
    else:
        decision = "pending"
    return {
        "reviewDecision": decision,
        "approvedBy": [u for u, s in latest_by_user.items() if s == "APPROVED"],
        "changesRequestedBy": [u for u, s in latest_by_user.items() if s == "CHANGES_REQUESTED"],
    }


# ── Main data collection ──

def collect_all_data():
    authenticated = bool(GITHUB_TOKEN)
    print(f"  Authenticated: {'yes (5000 req/hr)' if authenticated else 'no (60 req/hr)'}")

    search_items = fetch_search_results()
    if not search_items:
        print("No PRs found!")
        return []

    target_numbers = set(item["number"] for item in search_items)
    search_map = {item["number"]: item for item in search_items}

    pulls_map = fetch_pulls_pages(target_numbers)

    enriched = []
    need_enrichment = []

    for num in sorted(target_numbers, reverse=True):
        s = search_map[num]
        p = pulls_map.get(num)

        pr_data = {
            "number": num,
            "title": s["title"],
            "url": s.get("html_url", f"{REPO_URL}/pull/{num}"),
            "author": s["user"]["login"],
            "createdAt": s["created_at"],
            "updatedAt": s["updated_at"],
            "ageInDays": days_since(s["created_at"]),
            "daysSinceUpdate": days_since(s["updated_at"]),
            "isDraft": s.get("draft", False),
            "labels": [l["name"] for l in s.get("labels", [])],
        }

        if p:
            pr_data["branch"] = p["head"]["ref"]
            pr_data["targetBranch"] = p["base"]["ref"]
            pr_data["headSha"] = p["head"]["sha"]
            pr_data["additions"] = p.get("additions", 0)
            pr_data["deletions"] = p.get("deletions", 0)
            pr_data["changedFiles"] = p.get("changed_files", 0)
            pr_data["requestedReviewers"] = [r["login"] for r in p.get("requested_reviewers", [])]

        if authenticated:
            need_enrichment.append(pr_data)
        elif pr_data["isDraft"]:
            pr_data["ciStatus"] = {"overall": "unknown", "failing": [], "inProgress": []}
            pr_data["reviewInfo"] = {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}
            pr_data["category"] = "draft"
        elif is_wip_title(pr_data["title"]):
            pr_data["ciStatus"] = {"overall": "unknown", "failing": [], "inProgress": []}
            pr_data["reviewInfo"] = {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}
            pr_data["category"] = "wip_not_draft"
        elif pr_data["daysSinceUpdate"] >= 3 and not p:
            pr_data["ciStatus"] = {"overall": "unknown", "failing": [], "inProgress": []}
            pr_data["reviewInfo"] = {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}
            pr_data["category"] = "stale"
        else:
            need_enrichment.append(pr_data)

        enriched.append(pr_data)

    print(f"\n  PRs needing CI/review enrichment: {len(need_enrichment)}")
    print(f"  Core API calls remaining: {remaining_calls['core']}")

    for pr_data in need_enrichment:
        sha = pr_data.get("headSha")
        num = pr_data["number"]
        sys.stdout.write(f"  #{num}... ")
        sys.stdout.flush()

        if sha and remaining_calls["core"] > 4:
            pr_data["ciStatus"] = fetch_ci_status(sha)
        else:
            pr_data["ciStatus"] = {"overall": "unknown", "failing": [], "inProgress": []}

        if remaining_calls["core"] > 2:
            pr_data["reviewInfo"] = fetch_reviews(num)
        else:
            pr_data["reviewInfo"] = {"reviewDecision": "unknown", "approvedBy": [], "changesRequestedBy": []}

        pr_data["category"] = categorize(pr_data)
        print(f"[{pr_data['category']}]")
        time.sleep(0.1)

    for pr_data in enriched:
        if "category" not in pr_data:
            pr_data["category"] = categorize(pr_data)

    return enriched


# ── Report generation ──

def generate_report(pr_data):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    groups = {
        "needs_attention": [p for p in pr_data if p["category"] == "needs_attention"],
        "stale":           [p for p in pr_data if p["category"] == "stale"],
        "wip_not_draft":   [p for p in pr_data if p["category"] == "wip_not_draft"],
        "healthy":         [p for p in pr_data if p["category"] == "healthy"],
        "in_progress":     [p for p in pr_data if p["category"] == "in_progress"],
        "draft":           [p for p in pr_data if p["category"] == "draft"],
    }

    ci_emoji = {"passing": "✅", "failing": "❌", "in_progress": "⏳", "no_checks": "—", "unknown": "❓", "unavailable": "—"}
    review_emoji = {"approved": "✅", "changes_requested": "🔄", "pending": "⏳", "unknown": "❓"}

    def pr_link(pr):
        return f"[{REPO}#{pr['number']}]({REPO_URL}/pull/{pr['number']})"

    def author_link(pr):
        return f"[@{pr['author']}](https://github.com/{pr['author']})"

    def pr_table(prs):
        if not prs:
            return "_None._\n"
        lines = ["| PR | Title | Author | CI | Review Status | Last Updated | Age |",
                 "|---|---|---|---|---|---|---|"]
        for p in prs:
            ci = ci_emoji.get(p.get("ciStatus", {}).get("overall", "unknown"), "❓")
            rv = review_emoji.get(p.get("reviewInfo", {}).get("reviewDecision", "unknown"), "❓")
            failing = p.get("ciStatus", {}).get("failing", [])
            ci_note = ci
            if failing:
                ci_note += f" ({', '.join(failing[:2])}{'...' if len(failing) > 2 else ''})"
            changes_by = p.get("reviewInfo", {}).get("changesRequestedBy", [])
            rv_note = rv
            if changes_by:
                rv_note += f" ({', '.join(changes_by[:2])})"
            approved_by = p.get("reviewInfo", {}).get("approvedBy", [])
            if approved_by:
                rv_note += f" ({', '.join(approved_by[:2])})"
            title_short = p["title"][:60] + ("..." if len(p["title"]) > 60 else "")
            lines.append(
                f"| {pr_link(p)} | {title_short} | {author_link(p)} | {ci_note} | {rv_note} | {p['daysSinceUpdate']}d ago | {p['ageInDays']}d |"
            )
        return "\n".join(lines) + "\n"

    def draft_list(prs):
        if not prs:
            return "_None._\n"
        return "\n".join(f"- 📝 {pr_link(p)} — {p['title'][:70]} ([@{p['author']}](https://github.com/{p['author']}), {p['ageInDays']}d old)" for p in prs) + "\n"

    total_ci = {"passing": 0, "failing": 0, "in_progress": 0, "no_checks": 0, "unknown": 0, "unavailable": 0}
    all_failing_checks = []
    for p in pr_data:
        ci_ov = p.get("ciStatus", {}).get("overall", "unknown")
        total_ci[ci_ov] = total_ci.get(ci_ov, 0) + 1
        all_failing_checks.extend(p.get("ciStatus", {}).get("failing", []))

    exec_summary_parts = [f"There are **{len(pr_data)}** open PRs with the `{PR_LABEL}` label."]
    if groups["needs_attention"]:
        exec_summary_parts.append(f"**{len(groups['needs_attention'])}** PRs need immediate attention due to failing CI or requested changes.")
    if groups["stale"]:
        exec_summary_parts.append(f"**{len(groups['stale'])}** PRs are stale (3+ days without updates).")
    exec_summary_parts.append(
        f"CI health: {total_ci['passing']} passing, {total_ci['failing']} failing, "
        f"{total_ci['in_progress']} in progress, {total_ci['no_checks'] + total_ci['unknown'] + total_ci['unavailable']} unknown/no checks."
    )

    failing_check_names = sorted(set(all_failing_checks))

    actions = []
    action_num = 0
    for p in groups["needs_attention"]:
        action_num += 1
        reasons = []
        if p.get("ciStatus", {}).get("overall") == "failing":
            reasons.append("fix failing CI")
        if p.get("reviewInfo", {}).get("reviewDecision") == "changes_requested":
            who = ", ".join(p.get("reviewInfo", {}).get("changesRequestedBy", []))
            reasons.append(f"address review feedback from {who}" if who else "address review feedback")
        actions.append(f"{action_num}. {pr_link(p)} — {' and '.join(reasons)}.")
    for p in groups["stale"][:5]:
        action_num += 1
        actions.append(f"{action_num}. {pr_link(p)} — Stale for {p['daysSinceUpdate']} days. Ping author [@{p['author']}](https://github.com/{p['author']}) for an update or consider closing.")
    for p in groups["wip_not_draft"]:
        action_num += 1
        actions.append(f"{action_num}. {pr_link(p)} — WIP in title but not marked as Draft. Convert to draft PR.")

    report = f"""# rocprofiler-systems — Daily PR Report {today}
> Filtered from [{OWNER}/{REPO}]({REPO_URL}) · label: `{PR_LABEL}`

## Executive Summary
{' '.join(exec_summary_parts)}

## ⚠️ Needs Attention
({len(groups['needs_attention'])} PRs) — Failing CI or changes requested.

{pr_table(groups['needs_attention'])}

## 🕰️ Stale (3+ days no activity)
({len(groups['stale'])} PRs) — No updates for 3+ days.

{pr_table(groups['stale'])}

## ⚡ WIP / Not Marked as Draft
({len(groups['wip_not_draft'])} PRs) — Title suggests WIP but PR is not marked as draft.

{pr_table(groups['wip_not_draft'])}

## ✅ Healthy
({len(groups['healthy'])} PRs) — Passing CI, approved or awaiting review.

{pr_table(groups['healthy'])}

## ⏳ In Progress
({len(groups['in_progress'])} PRs) — Active work, CI running.

{pr_table(groups['in_progress'])}

## 📝 Drafts
({len(groups['draft'])} PRs)

{draft_list(groups['draft'])}

## CI Health Snapshot
Out of {len(pr_data)} open PRs: **{total_ci['passing']}** passing, **{total_ci['failing']}** failing, **{total_ci['in_progress']}** in progress, and **{total_ci['no_checks'] + total_ci['unknown'] + total_ci['unavailable']}** with no checks or unknown status.{' Failing check names: ' + ', '.join(f'`{c}`' for c in failing_check_names[:15]) + '.' if failing_check_names else ''}

## What Changed Since Yesterday
(No previous report — this is day one.)

## Recommended Actions
{chr(10).join(actions) if actions else '_No urgent actions needed._'}

---
*Auto-generated: {today}*
"""
    return report


if __name__ == "__main__":
    print("=== rocprofiler-systems PR Report Generator ===\n")
    pr_data = collect_all_data()
    if not pr_data:
        print("No data collected. Exiting.")
        sys.exit(1)

    report = generate_report(pr_data)

    import os
    reports_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    dated_file = os.path.join(reports_dir, f"pr-report-{today}.md")
    latest_file = os.path.join(reports_dir, "pr-report-latest.md")

    with open(dated_file, "w", encoding="utf-8") as f:
        f.write(report)
    with open(latest_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nSaved: {dated_file}")
    print(f"Latest: {latest_file}")
    print(f"API calls remaining — Core: {remaining_calls['core']}, Search: {remaining_calls['search']}")
