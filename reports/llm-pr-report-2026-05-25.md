# Daily PR Report — 2026-05-25

> rocprofiler-systems · [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

---

## Executive Summary

- **Total PRs:** 40
- **In Review:** 3 non-draft PRs with passing CI (approved or awaiting review)
- **CI Failures:** 13 PRs with failing CI (across needs-attention and draft categories)
- **Missing Tests:** 9 PRs with source changes but no test updates
- **Stale:** 3 PRs with 3+ days no activity (and several more approaching staleness)

> 📋 This is the first day of automated reporting — no prior baseline for comparison.

---

## Key Highlights

- 🚨 **Version bump PR [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) is approved and blocked only by a single CI failure** (`ubuntu-jammy g++/7.2`). This appears close to merge-ready and may warrant a targeted recheck or investigation of that one failing job.
- ✅ **Three PRs are healthy and ready for immediate merge action:** [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) (env_vars refactor, approved + passing CI) and [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) (docs update, approved + passing CI) are waiting only on final merge. [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) is passing but still awaiting review.
- ⚠️ **The C++20 modernization stack (`adjordje-amd`) is a coordinated multi-PR chain** — [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) → [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) → [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) — all targeting either `develop` or intermediate feature branches. All three have CI failures. The base PR (#4080) is 70 days old. This chain needs a dedicated review session.
- 🚨 **`jrmadsen` is the sole requested reviewer on 16+ PRs.** This is a significant review bottleneck; many PRs aged 13–70 days are waiting on a single reviewer.
- ❌ **[rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) (CLR/HRR capture & playback, 24 days old) has changes requested by `stellaraccident` and no tests for 20 changed source files** — this is the highest-risk open PR in the queue.

---

## PR Breakdown

### Needs Attention (13)

PRs with failing CI or changes requested.

| PR | Title | Author | CI | Review Status | Failing Checks / Blocker | Last Updated | Age |
|---|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | ❌ | Awaiting review | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-25 | 0d |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ | ✅ Approved (adjordje-amd) | `ubuntu-jammy g++/7.2` | 2026-05-25 | 5d |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Awaiting review | 32 CI jobs failing across all platforms (broad build failure) | 2026-05-12 | 13d |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | Replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Awaiting review | 5x `rhel (g++, 8.10, *)` failing | 2026-05-15 | 13d |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | Align per-link PMC + track names across emit and register sites | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | ✅ Approved (mradosav-amd) | TheRock CI Summary; rocprofiler-compute test shard 1 | 2026-05-11 | 19d |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | Replace SQLite3/rocpd backend with rocprofiler-hub library | [@anujshuk-amd](https://github.com/anujshuk-amd) | ❌ | Pending | TheRock CI Summary; Linux build packages | 2026-05-25 | 19d |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ❌ | ✅ Approved (dgaliffiAMD) | `ubuntu-noble g++/7.0` | 2026-05-21 | 20d |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | ❌ | ⚠️ Changes requested (stellaraccident) | TheRock CI Summary; Linux & Windows build packages | 2026-05-22 | 24d |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] Introduce 3 CLI options and rework some code | [@kcossett-amd](https://github.com/kcossett-amd) | ❌ | Pending | address sanitizer; TheRock CI; rocprofiler-compute shard 2 | 2026-05-07 | 32d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | ⚠️ Unknown | ⚠️ Changes requested (dgaliffiAMD) | Changes requested by dgaliffiAMD; CI status unknown | 2026-05-12 | 32d |
| [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) | [rocpd] Update rocprofiler-sdk-rocpd api to support versioning | [@yhuiYH](https://github.com/yhuiYH) | ❌ | ⚠️ Changes requested (jrmadsen) | Code Coverage mi325/ubuntu-22.04; changes requested by jrmadsen | 2026-05-25 | 33d |
| [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) | Add hip graph tests | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | ⚠️ Changes requested (kcossett-amd) | Changes requested by kcossett-amd | 2026-05-19 | 41d |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Pending | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-19 | 70d |

---

### In Review (3)

Passing CI, approved or awaiting review.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) | refactor(env_vars): use env_vars:: constants in place of ROCPROFSYS_* literals | [@marantic-amd](https://github.com/marantic-amd) | ✅ | ✅ Approved (dgaliffiAMD) | 2026-05-25 | 6d |
| [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) | docs: Update install instructions for 7.13 | [@peterjunpark](https://github.com/peterjunpark) | ✅ | ✅ Approved (dgaliffiAMD) | 2026-05-25 | 12d |
| [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) | Fix validation scripts to accept extra OMPT kernels from LLVM | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | Pending | 2026-05-25 | 34d |

---

### In Progress (1)

Active work, CI running.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) | Clean up jacobi-hip example | [@mradosav-amd](https://github.com/mradosav-amd) | ⏳ | ✅ Approved (kcossett-amd, dgaliffiAMD) | 2026-05-25 | 4d |

> [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) is approved by two reviewers and only waiting on rocprofiler-compute test shard 2 to complete — likely merge-ready shortly.

---

### Drafts (20)

| PR | Title | Author | CI | Age |
|---|---|---|---|---|
| [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) | refactor(trace-cache): rename UMP bandwidth metric | [@habajpai-amd](https://github.com/habajpai-amd) | ❌ | 0d |
| [rocm-systems#6355](https://github.com/ROCm/rocm-systems/pull/6355) | [tests] Apply strict `kwargs` checks and fix certain tests | [@kcossett-amd](https://github.com/kcossett-amd) | ⏳ | 4d |
| [rocm-systems#6300](https://github.com/ROCm/rocm-systems/pull/6300) | feat(rocprof-sys): add SPM beta scaffolding | [@habajpai-amd](https://github.com/habajpai-amd) | ❌ | 5d |
| [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) | refactor(rocprof-sys-causal): centralize runtime state | [@habajpai-amd](https://github.com/habajpai-amd) | ✅ | 5d |
| [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) | Update dyninst submodule & fix asan build failures | [@mradosav-amd](https://github.com/mradosav-amd) | ✅ | 5d |
| [rocm-systems#6254](https://github.com/ROCm/rocm-systems/pull/6254) | Config Robustness: Negative Tests for Invalid Values | [@habajpai-amd](https://github.com/habajpai-amd) | ✅ | 6d |
| [rocm-systems#6243](https://github.com/ROCm/rocm-systems/pull/6243) | Switch Perfetto processing in cached data to run in parallel | [@marantic-amd](https://github.com/marantic-amd) | ✅ | 6d |
| [rocm-systems#6240](https://github.com/ROCm/rocm-systems/pull/6240) | Unify control logic with different triggers | [@marantic-amd](https://github.com/marantic-amd) | ❌ | 6d |
| [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) | Add `rocprofsys_push_trace_with_args` and cache region arguments | [@kcossett-amd](https://github.com/kcossett-amd) | ✅ | 11d |
| [rocm-systems#6057](https://github.com/ROCm/rocm-systems/pull/6057) | Wall Clock migration from timemory | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | 12d |
| [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) | wire ccache (CMake auto-detect + CI cache) | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | 13d |
| [rocm-systems#6006](https://github.com/ROCm/rocm-systems/pull/6006) | rocprofsys exception hierarchy + clean stacktrace | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | 13d |
| [rocm-systems#5867](https://github.com/ROCm/rocm-systems/pull/5867) | Add OpenMP profiling doc | [@kcossett-amd](https://github.com/kcossett-amd) | ✅ | 18d |
| [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) | Add RHEL system deps workflow | [@sputhala-amd](https://github.com/sputhala-amd) | ⏳ | 20d |
| [rocm-systems#5736](https://github.com/ROCm/rocm-systems/pull/5736) | Support ELF's RELR relocation for binary rewrite | [@kcossett-amd](https://github.com/kcossett-amd) | ❌ | 21d |
| [rocm-systems#5414](https://github.com/ROCm/rocm-systems/pull/5414) | Add pytest for rocprof-sys-attach (attach/detach/re-attach) | [@adjordje-amd](https://github.com/adjordje-amd) | ✅ | 31d |
| [rocm-systems#5285](https://github.com/ROCm/rocm-systems/pull/5285) | Argparser refactor | [@marantic-amd](https://github.com/marantic-amd) | ✅ | 33d |
| [rocm-systems#5254](https://github.com/ROCm/rocm-systems/pull/5254) | Add clang-tidy in formatting workflow | [@sputhala-amd](https://github.com/sputhala-amd) | ❌ | 33d |
| [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) | Add initial strix halo changes for rocprofiler-systems CI | [@jbonnell-amd](https://github.com/jbonnell-amd) | ❌ | 48d |
| [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) | Fix `update_env` handling of `REPLACE` mode | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ | 54d |

---

## Risk Signals

### CI Instability

| PR | Title | Author | Failing Checks | Last Updated |
|---|---|---|---|---|
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | 32 jobs — all platforms (debian, ubuntu-noble, ubuntu-jammy, rhel, sanitizers) | 2026-05-12 |
| [rocm-systems#6006](https://github.com/ROCm/rocm-systems/pull/6006) | rocprofsys exception hierarchy + clean stacktrace | [@adjordje-amd](https://github.com/adjordje-amd) | 29 jobs — rhel, ubuntu-noble, ubuntu-jammy, debian, sanitizers | 2026-05-13 |
| [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) | Fix `update_env` handling of `REPLACE` mode | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | 32 jobs — TheRock + all platforms | 2026-05-24 |
| [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) | refactor(trace-cache): rename UMP bandwidth metric | [@habajpai-amd](https://github.com/habajpai-amd) | 34 jobs — TheRock + all platforms | 2026-05-25 |
| [rocm-systems#6240](https://github.com/ROCm/rocm-systems/pull/6240) | Unify control logic with different triggers | [@marantic-amd](https://github.com/marantic-amd) | 27 jobs — TheRock, rocprofiler-systems tests, debian, ubuntu-jammy, rhel, python, fixedwidth | 2026-05-25 |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | Replace SQLite3/rocpd backend with rocprofiler-hub | [@anujshuk-amd](https://github.com/anujshuk-amd) | TheRock CI Summary; Linux build packages | 2026-05-25 |
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-25 |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | Replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | 5x rhel (g++, 8.10, all versions) | 2026-05-15 |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-19 |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | Align per-link PMC + track names | [@adjordje-amd](https://github.com/adjordje-amd) | TheRock CI Summary; rocprofiler-compute test shard 1 | 2026-05-11 |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] 3 CLI options | [@kcossett-amd](https://github.com/kcossett-amd) | address sanitizer; TheRock; rocprofiler-compute shard 2 | 2026-05-07 |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ubuntu-noble g++/7.0 | 2026-05-21 |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ubuntu-jammy g++/7.2 | 2026-05-25 |

> **13/40 PRs have CI failures.** Several PRs (#5995, #6006, #4620, #6387) show broad platform-wide failures suggestive of a fundamental build issue rather than isolated test failures — these may share a common root cause worth investigating.

---

### Test Gap Summary

9 PRs have source changes without corresponding test updates.

| PR | Title | Author | Source Files Changed | Recommended Test Level | Risk of No Tests | Suggested Action |
|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | `pthread_mutex_gotcha.cpp`, `pthread_mutex_gotcha.hpp` | Unit + Integration | **High** — bug fix in threading/gotcha layer | Add a unit test exercising pause/resume across pthread_mutex operations; check existing gotcha tests for extension points |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | `buffer_storage.cpp`, `buffer_storage.hpp` | Unit | **Medium** — behavioral change in flush thread lifecycle | Add unit tests for flush thread start/stop/join semantics under `std::jthread`; existing buffer tests should be extended |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | 20 files — `hip_capture.cpp/h`, `hip_capture_writer.cpp/h`, `hip_capture_generated.cpp`, etc. | System + Integration | **High** — new feature (HIP capture/playback), 20 changed files, no tests at all | This is the highest test-gap risk in the queue. Needs dedicated capture/playback test harness; changes requested by reviewer likely reference this gap |
| [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) | Add `rocprofsys_push_trace_with_args` and cache region arguments | [@kcossett-amd](https://github.com/kcossett-amd) | 13 files — `api.cpp/hpp`, `dl.cpp/hpp`, `module_function.cpp/hpp`, etc. | Unit + Integration | **High** — new public API surface with annotation caching | Add unit tests for the new `push_trace_with_args` API and verify argument caching behavior; 13 source files with no test coverage is a significant gap |
| [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) | refactor(rocprof-sys-causal): centralize runtime state | [@habajpai-amd](https://github.com/habajpai-amd) | `impl.cpp`, `rocprof-sys-causal.cpp`, `rocprof-sys-causal.hpp` | Unit | **Medium** — refactor of runtime state management | Check `tests/causal/` for existing causal profiler tests to extend; centralized state changes can be subtle |
| [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) | Update dyninst submodule & fix asan build failures | [@mradosav-amd](https://github.com/mradosav-amd) | `Packages.cmake`, `markers.h` | Integration | **Low** — submodule bump + build fix | Passing CI is the primary signal; consider verifying asan suppression correctness manually |
| [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) | wire ccache (CMake auto-detect + CI cache) | [@adjordje-amd](https://github.com/adjordje-amd) | `BuildSettings.cmake`, `DyninstTBB.cmake` | Integration (CI) | **Low** — build system / CI infrastructure change | CI build time comparison before/after is the meaningful test; no unit tests applicable |
| [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) | Add RHEL system deps workflow | [@sputhala-amd](https://github.com/sputhala-amd) | `symbol.cpp` | System (CI) | **Medium** — new CI workflow + `symbol.cpp` change | The `symbol.cpp` change warrants a unit test; CI workflow correctness is validated by the run itself |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | `transpose.new.cpp` | Unit | **High** — external contribution bug fix with correctness impact | This is an external contribution fixing a kernel computation bug — correctness tests are essential; check `tests/examples/` for transpose test coverage |

> **23 PRs include test updates. 9 PRs are missing tests.** The highest-risk gaps are in [#5690](https://github.com/ROCm/rocm-systems/pull/5690) (20 source files, no tests, new feature), [#6116](https://github.com/ROCm/rocm-systems/pull/6116) (13 source files, new public API), and [#5098](https://github.com/ROCm/rocm-systems/pull/5098) (external contribution bug fix, no tests).

---

## Stale PRs

### Stale (25+ days no activity)

| PR | Title | Author | Last Updated | Age | Recommendation |
|---|---|---|---|---|---|
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | Align per-link PMC + track names | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-11 | 19d (14d no activity) | Approved by mradosav-amd but CI is failing — author should investigate rocprofiler-compute test failure and rebase/push to unblock. |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] 3 CLI options | [@kcossett-amd](https://github.com/kcossett-amd) | 2026-05-07 | 32d (18d no activity) | CI has been failing for 18 days with no update; ping [@kcossett-amd](https://github.com/kcossett-amd) to address sanitizer and compute test failures. |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-19 | 70d | At 70 days old this is the oldest open PR; it is the base of a C++20 chain — needs urgent review scheduling or a decision on the modernization timeline. |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | 2026-05-19 | 39d (6d no activity) | External contribution; CI is passing but no reviewer has engaged — ping [@jrmadsen](https://github.com/jrmadsen) to review or add tests and merge. |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | 2026-05-12 | 32d (13d no activity) | Changes requested by [@dgaliffiAMD](https://github.com/dgaliffiAMD) 13 days ago with no response; ping author to address feedback or close if superseded. |

### Going Stale (3–24 days no activity)

| PR | Title | Author | Last Updated | Age |
|---|---|---|---|---|
| [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) | Improve Generated Output summary. Cleanup of noisy logs | [@marantic-amd](https://github.com/marantic-amd) | 2026-05-21 | 6d (4d no activity) |
| [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) | Replace get_env and set_env from timemory | [@mradosav-amd](https://github.com/mradosav-amd) | 2026-05-20 | 7d (5d no activity) |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | Replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-15 | 13d (9d no activity) |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | 2026-05-21 | 20d (4d no activity) |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-12 | 13d (13d no activity)