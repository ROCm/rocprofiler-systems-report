# Contributing

Thanks for helping improve the ROCm PR report dashboards.

## Getting started

1. Fork the repo and create a branch from `main`.
2. Use Python 3.12+ (stdlib only — no `requirements.txt`).
3. Set environment variables for local runs:
   - `GITHUB_TOKEN` — GitHub API access (recommended for full PR enrichment)
   - `ANTHROPIC_API_KEY` — or AMD LLM Gateway credentials (`ANTHROPIC_BASE_URL`, `AMD_LLM_GATEWAY_KEY`)

See [README.md](README.md) for example commands.

## What to change

| Goal | Where to edit |
|------|---------------|
| Report structure, tone, or sections | `prompts/pr-report-prompt.md` |
| PR fetching, categorization, or test-coverage logic | `scripts/fetch_and_report.py` |
| LLM integration or report output | `scripts/generate_llm_report.py` |
| HTML styling or conversion | `scripts/md_to_html.py` |
| Schedule, subprojects, or deployment | `.github/workflows/daily-pr-reports.yml` |
| Dashboard landing page | `docs/index.html` |

To track a new subproject, add an entry to the workflow matrix in `.github/workflows/daily-pr-reports.yml` and a card on `docs/index.html`.

## Pull requests

- Keep changes focused — one logical change per PR.
- Test locally when touching scripts (`generate_llm_report.py` and/or `md_to_html.py`).
- Do not commit API keys or tokens.
- Open a PR against `main` with a short description of what changed and why.

## Questions

Open a [GitHub issue](https://github.com/ROCm/Rocprof-systems-report/issues) for bugs, report-quality feedback, or feature requests.
