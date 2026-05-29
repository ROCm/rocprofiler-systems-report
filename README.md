# Rocprof-systems-report

Automated daily pull-request reports for ROCm profiler subprojects, published as HTML dashboards on GitHub Pages.

## Overview

This repository generates LLM-assisted PR health reports for labeled subprojects in [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems). Each weekday, a GitHub Actions workflow fetches open PRs, enriches them with CI and review status, and produces a structured markdown report that is converted to HTML and deployed to GitHub Pages.

**Live dashboards:** [rocm.github.io/Rocprof-systems-report](https://rocm.github.io/Rocprof-systems-report/)

Currently tracked subprojects:

- **rocprofiler-systems** — system-level profiling tools
- **rocprofiler-compute** — compute profiling tools

## What the reports cover

- Executive summary with PR counts and overnight deltas
- PRs needing attention (failing CI, changes requested)
- Stale and WIP PRs
- Test coverage gaps (source changes without test updates)
- Per-PR CI status, review state, and age

## How it works

1. **`fetch_and_report.py`** — queries the GitHub API, categorizes PRs, and writes raw markdown reports to `reports/`
2. **`generate_llm_report.py`** — fills a prompt template (`prompts/pr-report-prompt.md`) with PR data and calls an Anthropic-compatible LLM to produce the final report
3. **`md_to_html.py`** — converts markdown reports to styled HTML for the dashboard
4. **`.github/workflows/daily-pr-reports.yml`** — runs the pipeline on weekdays at 08:00 UTC and publishes to the `gh-pages` branch

## Running locally

Requires Python 3.12+. Set `GITHUB_TOKEN` and either `ANTHROPIC_API_KEY` or AMD LLM Gateway credentials.

```bash
# Generate a report for rocprofiler-systems (default label)
python scripts/generate_llm_report.py

# Override target subproject
PR_LABEL="project: rocprofiler-compute" REPORT_PREFIX=rocprofiler-compute python scripts/generate_llm_report.py

# Convert latest report to HTML
python scripts/md_to_html.py reports/rocprofiler-systems-latest.md docs/reports/rocprofiler-systems-latest.html
```

The prompt template in `prompts/pr-report-prompt.md` is fully editable — adjust report structure and tone without changing code.
