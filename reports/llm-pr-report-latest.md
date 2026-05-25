# rocprofiler-systems — Daily PR Report 2026-05-25
> Filtered from [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

---

## Executive Summary

There are **41 open PRs** for rocprofiler-systems today, with **12 requiring immediate attention** due to failing CI or change requests. The most significant risk is the C++20 modernization stack — a chain of PRs from [@adjordje-amd](https://github.com/adjordje-amd) ([#4080](https://github.com/ROCm/rocm-systems/pull/4080), [#5992](https://github.com/ROCm/rocm-systems/pull/5992), [#5995](https://github.com/ROCm/rocm-systems/pull/5995)) shows cascading CI failures across the full matrix, and the oldest is 70 days old with no resolution in sight. CI health is poor overall: of the 20 non-draft PRs that are open and not in-progress, the majority carry at least one failing check, with RHEL builds being a persistent failure pattern across many branches.

---

## ⚠️ Needs Attention (12 PRs)

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) | Clean up jacobi-hip example | [@mradosav-amd](https://github.com/mradosav-amd) | ⏳ in_progress | 🔄 Changes requested by @kcossett-amd | 0d ago | 4d |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ failing | ✅ Approved by @adjordje-amd | 0d ago | 5d |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace hand-rolled flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ failing | ⚠️ No review | 13d ago | 13d |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ failing | ⚠️ No review | 9d ago | 13d |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | align per-link PMC + track names across emit and register sites | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ failing | ✅ Approved by @mradosav-amd | 14d ago | 18d |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ❌ failing | ✅ Approved by @dgaliffiAMD | 4d ago | 19d |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | ❌ failing | 🔄 Changes requested by @stellaraccident | 2d ago | 24d |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] Introduce 3 CLI options and rework some code | [@kcossett-amd](https://github.com/kcossett-amd) | ❌ failing | ⚠️ Pending | 17d ago | 31d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | ⚠️ unknown | 🔄 Changes requested by @dgaliffiAMD | 13d ago | 31d |
| [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) | [rocpd] Update rocprofiler-sdk-rocpd api to support versioning | [@yhuiYH](https://github.com/yhuiYH) | ❌ failing | 🔄 Changes requested by @jrmadsen | 0d ago | 33d |
| [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) | Add hip graph tests | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ passing | 🔄 Changes requested by @kcossett-amd | 6d ago | 41d |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ failing | ⚠️ Pending | 5d ago | **70d** |

### Notable CI failures per PR:

- **[#6349](https://github.com/ROCm/rocm-systems/pull/6349):** CI still running across debian/RHEL matrix; blocked by changes requested from @kcossett-amd — author should address feedback before CI completes.
- **[#6288](https://github.com/ROCm/rocm-systems/pull/6288):** 🚨 Approved but blocked by `ubuntu-jammy (g++, ON, ON, OFF, ON, Release, ON, 7.2)` failure. Should be mergeable once this single flaky check is resolved.
- **[#5995](https://github.com/ROCm/rocm-systems/pull/5995):** ❌ 33 failing checks across the full matrix (all distros/ROCm versions). Targets `users/adjordje-amd/cpp20-concepts` (a non-`develop` branch). Stale for 13 days with no reviewer action.
- **[#5992](https://github.com/ROCm/rocm-systems/pull/5992):** ❌ 5 RHEL 8.10 failures (all ROCm versions). C++20 concepts hitting RHEL gcc compatibility issues. Stale 9 days.
- **[#5819](https://github.com/ROCm/rocm-systems/pull/5819):** ❌ `TheRock CI Summary` + `Test rocprofiler-compute (shard 1 of 2)`. Approved but blocked by test failure for 14 days.
- **[#5777](https://github.com/ROCm/rocm-systems/pull/5777):** ❌ `ubuntu-noble (g++, ON, Release, ON, 7.0)` — single failure on an approved PR. Should be quick to fix.
- **[#5690](https://github.com/ROCm/rocm-systems/pull/5690):** ❌ Linux and Windows package build failures. Changes requested by @stellaraccident; cross-project PR (clr/hip-tests/rccl).
- **[#5351](https://github.com/ROCm/rocm-systems/pull/5351):** ❌ address sanitizer failure + TheRock + rocprofiler-compute test (shard 2). No review, stale 17 days.
- **[#5267](https://github.com/ROCm/rocm-systems/pull/5267):** ❌ Code Coverage on mi325/ubuntu-22.04. Changes requested by @jrmadsen — active today (updated 0d ago).
- **[#4080](https://github.com/ROCm/rocm-systems/pull/4080):** 🚨 70 days old. `TheRock CI Summary` + `Test rocprofiler-systems (shard 1 of 1)` failing. Root PR for the entire C++20 stack — must be resolved to unblock #5992 and #5995.

---

## 🕰️ Stale — 3+ days no activity (5 PRs)

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) | Improve Generated Output summary. Cleanup of noisy logs | [@marantic-amd](https://github.com/marantic-amd) | ✅ passing | ⚠️ Pending | **3d ago** | 6d |
| [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) | refactor(env_vars): use env_vars:: constants in place of ROCPROFSYS_* literals | [@marantic-amd](https://github.com/marantic-amd) | ✅ passing | ⚠️ No review | **6d ago** | 6d |
| [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) | Replace get_env and set_env from timemory inside rocprofiler-systems | [@mradosav-amd](https://github.com/mradosav-amd) | ✅ passing | ✅ Approved by @marantic-amd | **5d ago** | 6d |
| [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) | docs: Update install instructions for 7.13 | [@peterjunpark](https://github.com/peterjunpark) | ✅ passing | ✅ Approved by @dgaliffiAMD | **4d ago** | 12d |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | ✅ passing | ⚠️ No review | **6d ago** | 39d |

> ⚠️ **Key observations:**
> - **[#6203](https://github.com/ROCm/rocm-systems/pull/6203)** and **[#6035](https://github.com/ROCm/rocm-systems/pull/6035)** are both approved with passing CI — these should be **merged immediately**. They are blocked only by reviewer inaction.
> - **[#5098](https://github.com/ROCm/rocm-systems/pull/5098)** is an external contribution (39 days old), passing CI, with no review at all. Needs triage.
> - **[#6236](https://github.com/ROCm/rocm-systems/pull/6236)** has had zero activity since creation (6 days, no review assigned via GitHub).

---

## ⚡ WIP / Not Marked as Draft (0 PRs)

No PRs currently fall into this category. ✅

---

## ✅ Healthy (1 PR)

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) | Fix validation scripts to accept extra OMPT kernels from LLVM | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ passing | ⚠️ Pending (4 reviewers requested) | 2d ago | 34d |

> **Note:** This PR has been open 34 days with passing CI and reviewers requested ([@jrmadsen](https://github.com/jrmadsen), [@kcossett-amd](https://github.com/kcossett-amd), [@habajpai-amd](https://github.com/habajpai-amd), [@marantic-amd](https://github.com/marantic-amd)) — it deserves a review today.

---

## ⏳ In Progress (2 PRs)

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | ⏳ in_progress | ⚠️ No review yet | 0d ago | 0d |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | Replace SQLite3/rocpd backend with rocprofiler-hub library | [@anujshuk-amd](https://github.com/anujshuk-amd) | ⏳ in_progress | ⚠️ Pending | 0d ago | 19d |

> **[#6388](https://github.com/ROCm/rocm-systems/pull/6388)** was opened today. **[#5808](https://github.com/ROCm/rocm-systems/pull/5808)** is a significant architectural change (SQLite3 → rocprofiler-hub) and has been in progress for 19 days — worth a status check once CI completes.

---

## 📝 Drafts (21 PRs)

- [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) — `refactor(trace-cache): rename UMP bandwidth metric` ([@habajpai-amd](https://github.com/habajpai-amd)) — ❌ CI failing, age: 0d
- [rocm-systems#6361](https://github.com/ROCm/rocm-systems/pull/6361) — `Enable task_detach part of openmp-fortran-host test` ([@kcossett-amd](https://github.com/kcossett-amd)) — ⏳ CI in progress / partial failures, age: 3d
- [rocm-systems#6355](https://github.com/ROCm/rocm-systems/pull/6355) — `Apply strict kwargs checks and fix certain test regexes` ([@kcossett-amd](https://github.com/kcossett-amd)) — ⏳ CI in progress / 1 failure, age: 3d
- [rocm-systems#6300](https://github.com/ROCm/rocm-systems/pull/6300) — `feat(rocprof-sys): add SPM beta scaffolding` ([@habajpai-amd](https://github.com/habajpai-amd)) — ❌ CI failing (ROCm 6.3/6.4 only), age: 5d
- [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) — `refactor(rocprof-sys-causal): centralize runtime state` ([@habajpai-amd](https://github.com/habajpai-amd)) — ✅ CI passing, age: 5d
- [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) — `Update dyninst submodule & fix asan build failures` ([@mradosav-amd](https://github.com/mradosav-amd)) — ✅ CI passing, age: 5d
- [rocm-systems#6254](https://github.com/ROCm/rocm-systems/pull/6254) — `Config Robustness: Negative Tests for Invalid Values` ([@habajpai-amd](https://github.com/habajpai-amd)) — ✅ CI passing, age: 5d
- [rocm-systems#6243](https://github.com/ROCm/rocm-systems/pull/6243) — `Switch Perfetto processing in cached data to run in parallel` ([@marantic-amd](https://github.com/marantic-amd)) — ⏳ CI in progress / 2 amdclang++ failures, age: 6d
- [rocm-systems#6240](https://github.com/ROCm/rocm-systems/pull/6240) — `Unify control logic with different triggers` ([@marantic-amd](https://github.com/marantic-amd)) — ❌ CI failing (widespread), age: 6d
- [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) — `Add rocprofsys_push_trace_with_args and cache region arguments` ([@kcossett-amd](https://github.com/kcossett-amd)) — ✅ CI passing, age: 10d
- [rocm-systems#6057](https://github.com/ROCm/rocm-systems/pull/6057) — `Wall Clock migration from timemory` ([@sputhala-amd](https://github.com/sputhala-amd)) — ✅ CI passing, age: 12d
- [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) — `wire ccache (CMake auto-detect + CI cache)` ([@adjordje-amd](https://github.com/adjordje-amd)) — ❌ CI failing (1 RHEL check), age: 13d
- [rocm-systems#6006](https://github.com/ROCm/rocm-systems/pull/6006) — `rocprofsys exception hierarchy + clean stacktrace` ([@adjordje-amd](https://github.com/adjordje-amd)) — ❌ CI failing (widespread RHEL + noble + jammy), age: 13d
- [rocm-systems#5867](https://github.com/ROCm/rocm-systems/pull/5867) — `Add OpenMP profiling doc` ([@kcossett-amd](https://github.com/kcossett-amd)) — ✅ CI passing, age: 17d ⚠️ no activity in 17d
- [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) — `Add RHEL system deps workflow` ([@sputhala-amd](https://github.com/sputhala-amd)) — ❌ CI failing, age: 20d ⚠️ no activity in 18d
- [rocm-systems#5736](https://github.com/ROCm/rocm-systems/pull/5736) — `Support ELF's RELR relocation for binary rewrite` ([@kcossett-amd](https://github.com/kcossett-amd)) — ❌ CI failing, age: 21d ⚠️ no activity in 18d
- [rocm-systems#5414](https://github.com/ROCm/rocm-systems/pull/5414) — `Add pytest for rocprof-sys-attach (attach/detach/re-attach)` ([@adjordje-amd](https://github.com/adjordje-amd)) — ✅ CI passing, age: 31d
- [rocm-systems#5285](https://github.com/ROCm/rocm-systems/pull/5285) — `Users/marantic amd/argparser refactor` ([@marantic-amd](https://github.com/marantic-amd)) — ✅ CI passing, age: 33d
- [rocm-systems#5254](https://github.com/ROCm/rocm-systems/pull/5254) — `Add clang-tidy in formatting workflow` ([@sputhala-amd](https://github.com/sputhala-amd)) — ❌ CI failing (`clang-tidy`, `source`), age: 33d · labeled **Stale**
- [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) — `Add initial strix halo changes for rocprofiler-systems CI` ([@jbonnell-amd](https://github.com/jbonnell-amd)) — ❌ CI failing (gfx1151), age: 47d
- [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) — `Fix update_env handling of REPLACE mode` ([@dgaliffiAMD](https://github.com/dgaliffiAMD)) — ❌ CI failing (widespread), age: 53d · labeled **Stale**

---

## CI Health Snapshot

Of the **41 open PRs**, roughly **8 non-draft PRs have passing CI** (including those awaiting review), **11 non-draft PRs have failing CI**, **2 non-draft PRs have CI in progress**, and **1 has unknown CI status** (no checks recorded). Among drafts, **8 are passing**, **9 are failing**, and **3 are in progress**. The most persistent failure pattern is **RHEL 8.10 g++ builds** across all ROCm versions (6.3–7.2), affecting PRs in the C++20 modernization stack (#4080, #5992, #5995, #6006, #6009). Other recurring failures include:

- **`TheRock CI Summary`** — a composite gate failing on several PRs (#4080, #5690, #5819, #5995, #5351, #4620, #5736, #5762, #6240)
- **`ubuntu-noble-sanitizers`** (address/thread/undefined) — failing on #5995, #5351
- **`ubuntu-noble (g++, ON, Release, ON, 7.0)`** — a commonly failing single check on otherwise-approved PRs (#5777, #5819 area, #6387)
- **`Linux / Build Linux Packages`** (TheRock build gate) — failing on #5690, #5995, #6387, #4620
- **`Code Coverage • mi325 • ubuntu-22.04`** — failing on #5267

---

## What Changed Since Yesterday

*(No previous report — this is day one. Baseline established as of 2026-05-25.)*

---

## Recommended Actions

1. 🚨 **Merge [#6203](https://github.com/ROCm/rocm-systems/pull/6203) and [#6035](https://github.com/ROCm/rocm-systems/pull/6035) today** — both are approved, CI is green, and they've been waiting 5–6 days. Any maintainer can merge these now.

2. 🚨 **Unblock [#6288](https://github.com/ROCm/rocm-systems/pull/6288) (version bump to 1.7.0)** — approved by @adjordje-amd, only one CI failure (`ubuntu-jammy / g++ / 7.2`). [@dgaliffiAMD](https://github.com/dgaliffiAMD) or [@jrmadsen](https://github.com/jrmadsen) should investigate and re-trigger or hotfix this check.

3. 🚨 **[@adjordje-amd](https://github.com/adjordje-amd): Resolve CI failures on [#4080](https://github.com/ROCm/rocm-systems/pull/4080) (C++20 support, 70 days old)** — this is the root of the entire C++20 stack. `Test rocprofiler-systems` is the blocking shard. Fixing this unblocks #5992 and #5995.

4. ⚠️ **[@ajanicijamd](https://github.com/ajanicijamd): Fix the single `ubuntu-noble / 7.0` failure on [#5777](https://github.com/ROCm/rocm-systems/pull/5777)** — this is approved by @dgaliffiAMD and has been lingering 19 days over what appears to be an isolated CI failure.

5. ⚠️ **[@adjordje-amd](https://github.com/adjordje-amd): Address the approved-but-stuck [#5819](https://github.com/ROCm/rocm-systems/pull/5819)** — approved by @mradosav-amd 14 days ago but `Test rocprofiler-compute (shard 1)` is failing. Investigate whether this is a flaky test or a real regression.

6. ⚠️ **[@jrmadsen](https://github.com/jrmadsen): Review [#5214](https://github.com/ROCm/rocm-systems/pull/5214)** — passing CI, 34 days old, and you are a requested reviewer. This is the healthiest open PR and should be quick to review.

7. ⚠️ **[@yhuiYH](https://github.com/yhuiYH): Address changes requested by @jrmadsen on [#5267](https://github.com/ROCm/rocm-systems/pull/5267)** — this rocpd versioning PR has been open 33 days and was updated today, suggesting active work. Confirm the Code Coverage failure is also addressed.

8. ⚠️ **Triage external contribution [#5098](https://github.com/ROCm/rocm-systems/pull/5098)** ([@jared-mcd-han](https://github.com/jared-mcd-han)) — 39 days old, passing CI, no review. Assign a reviewer or close with explanation.

9. 📋 **[@kcossett-amd](https://github.com/kcossett-amd): Address your own changes-requested on [#4993](https://github.com/ROCm/rocm-systems/pull/4993)** ([@sputhala-amd](https://github.com/sputhala-amd)) — CI is passing, the PR just needs feedback addressed. This has been blocked 41 days.

10. 📋 **Consider closing or suspending stale drafts**: [#4620](https://github.com/ROCm/rocm-systems/pull/4620) (53d), [#5254](https://github.com/ROCm/rocm-systems/pull/5254) (33d), [#5762](https://github.com/ROCm/rocm-systems/pull/5762) (20d), [#5736](https://github.com/ROCm/rocm-systems/pull/5736) (21d) — all have failing CI with no recent activity and are already labeled `Stale` or effectively abandoned. Cleaning these up will reduce noise.

---

*Auto-generated: 2026-05-25*