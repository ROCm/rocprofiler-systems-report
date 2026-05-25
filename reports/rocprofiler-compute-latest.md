# Daily PR Report — 2026-05-25

> rocprofiler-systems · [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-compute`

---

## Executive Summary

- **Total PRs:** 28
- **In Review:** 7 non-draft PRs awaiting or with active review (includes needs-attention)
- **CI Failures:** 7 PRs with failing CI (across all categories)
- **Missing Tests:** 1 PR with source changes but no test updates
- **Stale:** 0 PRs with no recent activity (per automated threshold)

*This is the first report — no prior baseline for overnight comparison.*

---

## Key Highlights

- **Ready to merge:** [rocm-systems#6397](https://github.com/ROCm/rocm-systems/pull/6397) (pip install docs) is approved with passing CI and no source changes — low-risk merge candidate.
- **Approved but CI is broken:** [rocm-systems#6270](https://github.com/ROCm/rocm-systems/pull/6270) has approval from `xuchen-amd` but is failing on Ubuntu 22.04 gfx950 and gfx1151 test shards — CI must be resolved before merge.
- **Long-running PRs with unresolved review blocks:** [rocm-systems#5499](https://github.com/ROCm/rocm-systems/pull/5499) (28 days old) and [rocm-systems#4008](https://github.com/ROCm/rocm-systems/pull/4008) (74 days old) both have changes requested and significant CI failures — these are accumulating risk.
- **gfx115x support cluster:** Three PRs are concurrently addressing gfx1150/gfx1152 support — [rocm-systems#6319](https://github.com/ROCm/rocm-systems/pull/6319), [rocm-systems#5668](https://github.com/ROCm/rocm-systems/pull/5668) (draft), and [rocm-systems#5573](https://github.com/ROCm/rocm-systems/pull/5573) (draft) — coordination may be needed to avoid conflicts.
- **Large draft pipeline in flight:** 15 draft PRs represent a significant queue of upcoming review work, including a notable PC sampling collector series ([rocm-systems#6390](https://github.com/ROCm/rocm-systems/pull/6390), [rocm-systems#6392](https://github.com/ROCm/rocm-systems/pull/6392), [rocm-systems#5482](https://github.com/ROCm/rocm-systems/pull/5482)) that appear to be a stacked/dependent chain.

---

## PR Breakdown

### Needs Attention (7)

PRs with failing CI or changes requested.

| PR | Title | Author | CI | Review Status | Failing Checks / Blocker | Last Updated | Age |
|---|---|---|---|---|---|---|---|
| [rocm-systems#6319](https://github.com/ROCm/rocm-systems/pull/6319) | enable gfx1150 and gfx1152 | [@ywang103-amd](https://github.com/ywang103-amd) | ⏳ in progress | Changes requested | Changes requested by `vedithal-amd` | 2026-05-25 | 5d |
| [rocm-systems#6270](https://github.com/ROCm/rocm-systems/pull/6270) | Restrict profiler env-var debug logs to delta | [@vedithal-amd](https://github.com/vedithal-amd) | ❌ failing | Approved | TheRock CI Summary, Test rocprofiler-compute (shard 1/2), Ubuntu 22.04 gfx950, Ubuntu 22.04 gfx1151 | 2026-05-25 | 6d |
| [rocm-systems#6113](https://github.com/ROCm/rocm-systems/pull/6113) | Improvements in marker injection for torch-trace | [@ggottipa-amd](https://github.com/ggottipa-amd) | ✅ passing | Changes requested | Changes requested by `vedithal-amd` | 2026-05-25 | 11d |
| [rocm-systems#5499](https://github.com/ROCm/rocm-systems/pull/5499) | remove explicit pop from yaml | [@xuchen-amd](https://github.com/xuchen-amd) | ⏳ in progress | Changes requested | pre-commit, build-rhel 8.10, build-rhel 9.4, build-ubuntu-jammy; changes requested by `vedithal-amd` | 2026-05-25 | 28d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | ⚠️ unknown | Changes requested | Changes requested by `dgaliffiAMD`; CI status unknown | 2026-05-12 | 32d |
| [rocm-systems#4008](https://github.com/ROCm/rocm-systems/pull/4008) | [rocprofv3] Output flag (-o) bug fix with multiple processes | [@itrowbri](https://github.com/itrowbri) | ❌ failing | Changes requested | 11 failing checks across multiple platforms and shards; changes requested by `MythreyaK`; labeled WIP | 2026-05-12 | 74d |
| [rocm-systems#1793](https://github.com/ROCm/rocm-systems/pull/1793) | [NFC] Fix stale hyperlinks in rocm-systems | [@saiislam](https://github.com/saiislam) | ❌ failing | Approved | Failing: `rdc` check | 2026-05-12 | 195d |

---

### In Review (2)

Passing CI, approved or awaiting review.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6397](https://github.com/ROCm/rocm-systems/pull/6397) | docs: add pip install instructions for `rocm[profiler]` | [@peterjunpark](https://github.com/peterjunpark) | ✅ passing | Approved by `vedithal-amd` | 2026-05-25 | 0d |
| [rocm-systems#6341](https://github.com/ROCm/rocm-systems/pull/6341) | Q2 Sprint 3 May 25 - Jun 12 | [@vedithal-amd](https://github.com/vedithal-amd) | ✅ passing | Pending | 2026-05-25 | 4d |

---

### In Progress (4)

Active work, CI running.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6403](https://github.com/ROCm/rocm-systems/pull/6403) | Remove config_delta and arch promotion workflow | [@vedithal-amd](https://github.com/vedithal-amd) | ⏳ in progress | Pending | 2026-05-25 | 0d |
| [rocm-systems#6386](https://github.com/ROCm/rocm-systems/pull/6386) | replace glob.glob with pathlib (PTH) | [@xuchen-amd](https://github.com/xuchen-amd) | ⏳ in progress | Pending | 2026-05-25 | 1d |
| [rocm-systems#6385](https://github.com/ROCm/rocm-systems/pull/6385) | derive --list-blocks parser offsets from header | [@xuchen-amd](https://github.com/xuchen-amd) | ⏳ in progress | Pending | 2026-05-25 | 1d |
| [rocm-systems#6333](https://github.com/ROCm/rocm-systems/pull/6333) | parametrize analyze workload tests | [@xuchen-amd](https://github.com/xuchen-amd) | ⏳ in progress (some failing) | Pending | 2026-05-25 | 4d |

> ⚠️ Note: [rocm-systems#6333](https://github.com/ROCm/rocm-systems/pull/6333) has partial failures (Ubuntu 24.04 gfx950/gfx1151, build-ubuntu-jammy, build-rhel) alongside ongoing CI — watch closely.

---

### Drafts (15)

| PR | Title | Author | CI | Age |
|---|---|---|---|---|
| [rocm-systems#6395](https://github.com/ROCm/rocm-systems/pull/6395) | Remove gfx950 bandwidth requests metrics | [@jamessiddeley-amd](https://github.com/jamessiddeley-amd) | ✅ passing | 0d |
| [rocm-systems#6392](https://github.com/ROCm/rocm-systems/pull/6392) | CI check: pc_sampling_collector and tool refactor | [@abchoudh-amd](https://github.com/abchoudh-amd) | ⚠️ unknown | 0d |
| [rocm-systems#6390](https://github.com/ROCm/rocm-systems/pull/6390) | PC sampling collector: code-object dump + review fixes | [@abchoudh-amd](https://github.com/abchoudh-amd) | ❌ failing | 0d |
| [rocm-systems#6373](https://github.com/ROCm/rocm-systems/pull/6373) | Skip analyze of unprofiled blocks | [@vedithal-amd](https://github.com/vedithal-amd) | ⏳ in progress | 3d |
| [rocm-systems#6345](https://github.com/ROCm/rocm-systems/pull/6345) | Add hardcoded-secret pre-commit hook | [@abchoudh-amd](https://github.com/abchoudh-amd) | ❌ failing | 4d |
| [rocm-systems#6247](https://github.com/ROCm/rocm-systems/pull/6247) | gfx950 metric description doc sync | [@abchoudh-amd](https://github.com/abchoudh-amd) | ❌ failing | 6d |
| [rocm-systems#6235](https://github.com/ROCm/rocm-systems/pull/6235) | Clarify gfx950 L2-Fabric and destination bandwidth metric descriptions | [@abchoudh-amd](https://github.com/abchoudh-amd) | ❌ failing | 6d |
| [rocm-systems#6234](https://github.com/ROCm/rocm-systems/pull/6234) | Cache ROCPROF_* env vars to fix shell-script profiling crash | [@abchoudh-amd](https://github.com/abchoudh-amd) | ✅ passing | 6d |
| [rocm-systems#6189](https://github.com/ROCm/rocm-systems/pull/6189) | Reorganize tests into unit and integration | [@vedithal-amd](https://github.com/vedithal-amd) | ❌ failing | 8d |
| [rocm-systems#6086](https://github.com/ROCm/rocm-systems/pull/6086) | Make rocpd database output the default profiling format | [@jamessiddeley-amd](https://github.com/jamessiddeley-amd) | ✅ passing | 11d |
| [rocm-systems#6049](https://github.com/ROCm/rocm-systems/pull/6049) | Gate PC sampling behind --pc-sampling --experimental | [@vedithal-amd](https://github.com/vedithal-amd) | ✅ passing | 12d |
| [rocm-systems#5668](https://github.com/ROCm/rocm-systems/pull/5668) | Add gfx1150 test coverage | [@jbonnell-amd](https://github.com/jbonnell-amd) | ❌ failing | 25d |
| [rocm-systems#5573](https://github.com/ROCm/rocm-systems/pull/5573) | support of gfx1152 metrics with all public counters | [@ywang103-amd](https://github.com/ywang103-amd) | ❌ failing | 26d |
| [rocm-systems#5482](https://github.com/ROCm/rocm-systems/pull/5482) | Support for code objects tracing in native collector | [@svolkov-amd](https://github.com/svolkov-amd) | ❌ failing | 28d |
| [rocm-systems#2599](https://github.com/ROCm/rocm-systems/pull/2599) | Enhance Lintian Support - add feature toggling build flag, Fix for ASAN package issue | [@arvindcheru](https://github.com/arvindcheru) | ❌ failing | 132d |

---

## Risk Signals

### CI Instability

| PR | Title | Author | Failing Checks | Last Updated |
|---|---|---|---|---|
| [rocm-systems#6270](https://github.com/ROCm/rocm-systems/pull/6270) | Restrict profiler env-var debug logs to delta | [@vedithal-amd](https://github.com/vedithal-amd) | TheRock CI Summary, Test rocprofiler-compute shard 1/2, Ubuntu 22.04 gfx950, Ubuntu 22.04 gfx1151 | 2026-05-25 |
| [rocm-systems#5499](https://github.com/ROCm/rocm-systems/pull/5499) | remove explicit pop from yaml | [@xuchen-amd](https://github.com/xuchen-amd) | pre-commit, build-rhel 8.10, build-rhel 9.4, build-ubuntu-jammy | 2026-05-25 |
| [rocm-systems#4008](https://github.com/ROCm/rocm-systems/pull/4008) | [rocprofv3] Output flag (-o) bug fix | [@itrowbri](https://github.com/itrowbri) | 11 checks: TheRock CI, rocprofiler-compute/sdk shards, gfx1151, gfx950, mi325 (rhel/sles/ubuntu), Code Coverage, source | 2026-05-12 |
| [rocm-systems#1793](https://github.com/ROCm/rocm-systems/pull/1793) | [NFC] Fix stale hyperlinks in rocm-systems | [@saiislam](https://github.com/saiislam) | rdc | 2026-05-12 |
| [rocm-systems#6390](https://github.com/ROCm/rocm-systems/pull/6390) | PC sampling collector: code-object dump + review fixes *(draft)* | [@abchoudh-amd](https://github.com/abchoudh-amd) | TheRock CI Summary, Test rocprofiler-compute shard 2/2, Ubuntu 24.04 gfx1151, Ubuntu 24.04 gfx950, cmake, cxx | 2026-05-25 |
| [rocm-systems#6345](https://github.com/ROCm/rocm-systems/pull/6345) | Add hardcoded-secret pre-commit hook *(draft)* | [@abchoudh-amd](https://github.com/abchoudh-amd) | TheRock CI Summary, Build Linux Packages, Ubuntu 22.04 gfx1151, pre-commit | 2026-05-25 |
| [rocm-systems#5482](https://github.com/ROCm/rocm-systems/pull/5482) | Support for code objects tracing in native collector *(draft)* | [@svolkov-amd](https://github.com/svolkov-amd) | Ubuntu 22.04 gfx950, Ubuntu 22.04 gfx1151 | 2026-05-25 |

**7/28 PRs have CI failures** (across needs-attention and draft categories).

---

### Test Gap Summary

🚨 **1 PR has source changes without corresponding test updates.**

| PR | Title | Author | Source Files Changed | Recommended Test Level | Risk of No Tests | Suggested Action |
|---|---|---|---|---|---|---|
| [rocm-systems#2599](https://github.com/ROCm/rocm-systems/pull/2599) | Enhance Lintian Support - add feature toggling build flag | [@arvindcheru](https://github.com/arvindcheru) | 11 `utils.cmake` / `rocprofiler_utils.cmake` files | Unit / Integration | **Medium** — build flag toggling can silently affect package output and install behavior across multiple projects | Add CMake-level tests verifying the flag is honored; check adjacent `tests/` CMake infrastructure for extension points |

**19 PRs include test updates. 1 PR is missing tests.**

---

## Stale PRs

### Stale (25+ days no activity)

| PR | Title | Author | Last Updated | Age | Recommendation |
|---|---|---|---|---|---|
| [rocm-systems#5668](https://github.com/ROCm/rocm-systems/pull/5668) | Add gfx1150 test coverage *(draft)* | [@jbonnell-amd](https://github.com/jbonnell-amd) | 2026-04-30 | 25d | Likely superseded by [rocm-systems#6319](https://github.com/ROCm/rocm-systems/pull/6319); author should confirm if this draft should be closed or rebased. |
| [rocm-systems#5573](https://github.com/ROCm/rocm-systems/pull/5573) | support of gfx1152 metrics with all public counters *(draft)* | [@ywang103-amd](https://github.com/ywang103-amd) | 2026-05-08 | 26d (17d since update) | Has changes requested by `cfallows-amd` and CI failing; ping author to address feedback or close in favor of [rocm-systems#6319](https://github.com/ROCm/rocm-systems/pull/6319). |
| [rocm-systems#5482](https://github.com/ROCm/rocm-systems/pull/5482) | Support for code objects tracing in native collector *(draft)* | [@svolkov-amd](https://github.com/svolkov-amd) | 2026-05-25 | 28d | Still receiving automated CI updates; appears to be the base for [rocm-systems#6390](https://github.com/ROCm/rocm-systems/pull/6390) and [rocm-systems#6392](https://github.com/ROCm/rocm-systems/pull/6392) — confirm intended chain and update PR description. |
| [rocm-systems#2599](https://github.com/ROCm/rocm-systems/pull/2599) | Enhance Lintian Support *(draft)* | [@arvindcheru](https://github.com/arvindcheru) | 2026-05-14 | 132d | Very long-running draft with failing CI and no test coverage; strongly recommend a triaging decision — either assign for active work or close and re-open when prioritized. |
| [rocm-systems#1793](https://github.com/ROCm/rocm-systems/pull/1793) | [NFC] Fix stale hyperlinks in rocm-systems | [@saiislam](https://github.com/saiislam) | 2026-05-12 | 195d | Approved by two reviewers but blocked by a single failing `rdc` check; this fix-it PR has been open nearly 6 months — investigate whether the `rdc` failure is pre-existing flake and consider merging or closing. |

### Going Stale (3–24 days no activity)

| PR | Title | Author | Last Updated | Age |
|---|---|---|---|---|
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | 2026-05-12 | 32d (13d since update) |
| [rocm-systems#4008](https://github.com/ROCm/rocm-systems/pull/4008) | [rocprofv3] Output flag (-o) bug fix | [@itrowbri](https://github.com/itrowbri) | 2026-05-12 | 74d (13d since update) |
| [rocm-systems#6235](https://github.com/ROCm/rocm-systems/pull/6235) | Clarify gfx950 L2-Fabric bandwidth metric descriptions *(draft)* | [@abchoudh-amd](https://github.com/abchoudh-amd) | 2026-05-20 | 6d (5d since update) |

---

## LLM Observations

- **PC sampling is a cross-cutting theme with a stacked PR chain.** [rocm-systems#5482](https://github.com/ROCm/rocm-systems/pull/5482) (native collector code-object tracing) appears to be the base for [rocm-systems#6390](https://github.com/ROCm/rocm-systems/pull/6390) (code-object dump + review fixes) and [rocm-systems#6392](https://github.com/ROCm/rocm-systems/pull/6392) (CI check refactor), all by overlapping authors. Reviewers should be aware of the dependency order; merging out of sequence would likely cause conflicts. [rocm-systems#6049](https://github.com/ROCm/rocm-systems/pull/6049) (gate PC sampling behind `--experimental`) is a related UX change that should be coordinated with this chain.

- **gfx115x support is being pursued on multiple parallel tracks with potential for conflict.** [rocm-systems#6319](https://github.com/ROCm/rocm-systems/pull/6319) (enable gfx1150+gfx1152, non-draft, changes requested) overlaps significantly with [rocm-systems#5668](https://github.com/ROCm/rocm-systems/pull/5668) (gfx1150 test coverage, draft, 25d old) and [rocm-systems#5573](https://github.com/ROCm/rocm-systems/pull/5573) (gfx1152 metrics, draft, 26d old). All three touch `soc_gfx115x.py` and related GPU specs — the team should decide whether #5668 and #5573 are being superseded by #6319 and close them accordingly.

- **Analysis pipeline is under active renovation from multiple directions simultaneously.** [rocm-systems#6373](https://github.com/ROCm/rocm-systems/pull/6373) (skip analyze of unprofiled blocks) touches `analysis_base.py`, `analysis_db.py`, `evaluation_pipeline.py`, and `parser.py` — the same core files touched by [rocm-systems#5499](https://github.com/ROCm/rocm-systems/pull/5499) (remove explicit pop from yaml) and [rocm-systems#6403](https://github.com/ROCm/rocm-systems/pull/6403) (remove config_delta). Merge order matters here; whichever lands first will require rebases of the others.

- **[rocm-systems#6270](https://github.com/ROCm/rocm-systems/pull/6270) is a merge-ready PR blocked only by CI.** It has a clean approval and the change is focused (restrict env-var debug logs to delta only), but Ubuntu 22.04 gfx950 and gfx1151 are failing on Test rocprofiler-compute. Given that the same platforms are failing on several other PRs (e.g., [rocm-systems#6247](https://github.com/ROCm/rocm-systems/pull/6247), [rocm-systems#6235](https://github.com/ROCm/rocm-systems/pull/6235)), this may be a systemic CI infrastructure issue rather than a code regression — worth investigating whether these are pre-existing flakes.

- **Test infrastructure is itself under active refactoring**, with [rocm-systems#6189](https://github.com/ROCm/rocm-systems/pull/6189) (reorganize tests into unit/integration) and [rocm-systems#6333](https://github.com/ROCm/rocm-systems/pull/6333) (parametrize analyze workload tests) both in flight. Landing #6189 will likely require rebases of most other PRs with test file changes. The team should consider prioritizing or blocking this PR to reduce churn.

---

## Appendix

### Raw Stats

| Metric | Count |
|---|---|
| Total open PRs | 28 |
| Needs attention | 7 |
| Healthy / In review | 2 |
| In progress | 4 |
| Stale (3+ days no activity) | 0 *(per automated threshold)* |
| Drafts | 15 |
| WIP not draft | 0 |
| PRs with test updates | 19 |
| PRs missing tests | 1 |

### Quick Links

- [All open PRs](https://github.com/ROCm/rocm-systems/pulls?q=is%3Apr+is%3Aopen+label%3A%22project%3A+rocprofiler-compute%22)
- [Failing CI](https://github.com/ROCm/rocm-systems/pulls?q=is%3Apr+is%3Aopen+label%3A%22project%3A+rocprofiler-compute%22+status%3Afailure)

---
*Auto-generated: 2026-05-25*