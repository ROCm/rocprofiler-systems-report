# Daily PR Report — 2026-05-25

> rocprofiler-systems · [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

---

## Executive Summary

- **Total PRs:** 40
- **In Review:** 4 non-draft PRs with passing CI (approved or awaiting review)
- **CI Failures:** 13 PRs with failing CI (across needs-attention and draft categories)
- **Missing Tests:** 9 PRs with source changes but no test updates
- **Stale:** 3 PRs with 3+ days no activity (non-draft); several drafts also dormant 13–19 days

*This is the first report — no overnight delta available.*

---

## Key Highlights

- **Three PRs are approved and ready to merge** but are blocked by CI failures: [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) (version bump 1.7.0, one jammy failure), [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) (XGMI PMC names, one rocprofiler-compute test failure), and [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) (AI NIC Pensando Phase 2, one noble build failure). All three have approvals and should be unblocked as soon as their single failing checks are resolved.
- **[rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) (CLR/HRR capture and playback)** is 24 days old, has changes requested by `stellaraccident`, is missing tests across 20 source files, and CI is still running/failing. This cross-project PR (also touching `clr`, `hip-tests`, `rccl`) is the most complex and highest-risk open PR in the queue.
- **[rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) (C++20 support)** is 70 days old — the oldest active (non-draft) PR — with failing CI and no review decision. It is the base for a chain of dependent PRs (#5992, #5995) that are also failing, suggesting a compounding integration risk.
- **[rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) (rocpd API versioning)** is 33 days old with changes requested and a failing code-coverage check. The author has no requested reviewers currently assigned, which may be slowing resolution.
- **Two newly opened PRs today**: [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) (pthread_mutex_gotcha fix) and draft [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) (UMP metric rename) — both with immediate CI failures that need investigation.

---

## PR Breakdown

### Needs Attention (13)

PRs with failing CI or changes requested.

| PR | Title | Author | CI | Review Status | Failing Checks / Blocker | Last Updated | Age |
|---|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | ❌ | Awaiting review | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-25 | 0d |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ | ✅ Approved (adjordje-amd) | ubuntu-jammy (g++, Release, 7.2) | 2026-05-25 | 5d |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Awaiting review | 33 checks across debian/noble/jammy/rhel/sanitizers/TheRock | 2026-05-12 | 13d |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Awaiting review | rhel g++ 8.10 (all ROCm versions) | 2026-05-15 | 13d |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | align per-link PMC + track names across emit and register sites | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | ✅ Approved (mradosav-amd) | TheRock CI; rocprofiler-compute test shard 1 | 2026-05-11 | 19d |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | Replace SQLite3/rocpd backend with rocprofiler-hub library | [@anujshuk-amd](https://github.com/anujshuk-amd) | ❌ | Pending | TheRock CI; Linux Build Linux Packages | 2026-05-25 | 19d |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ❌ | ✅ Approved (dgaliffiAMD) | ubuntu-noble (g++, Release, 7.0) | 2026-05-21 | 20d |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | ⏳ | ⚠️ Changes requested (stellaraccident) | Linux Build Linux Packages failing; Windows build in progress | 2026-05-25 | 24d |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] Introduce 3 CLI options and rework some code | [@kcossett-amd](https://github.com/kcossett-amd) | ❌ | Pending | ubuntu-noble-sanitizers address; TheRock CI; rocprofiler-compute test shard 2 | 2026-05-07 | 32d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | ⚠️ Unknown | ⚠️ Changes requested (dgaliffiAMD) | Changes requested by dgaliffiAMD; CI status unknown | 2026-05-12 | 32d |
| [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) | [rocpd] Update rocprofiler-sdk-rocpd api to support versioning | [@yhuiYH](https://github.com/yhuiYH) | ❌ | ⚠️ Changes requested (jrmadsen) | Code Coverage mi325 ubuntu-22.04; changes requested | 2026-05-25 | 33d |
| [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) | Add hip graph tests | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | ⚠️ Changes requested (kcossett-amd) | Changes requested by kcossett-amd | 2026-05-19 | 41d |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | ❌ | Pending | TheRock CI; rocprofiler-systems test shard 1 | 2026-05-19 | 70d |

---

### In Review (4)

Passing CI, approved or awaiting review.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) | Clean up jacobi-hip example | [@mradosav-amd](https://github.com/mradosav-amd) | ✅ | ✅ Approved (kcossett-amd, dgaliffiAMD) | 2026-05-25 | 4d |
| [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) | refactor(env_vars): use env_vars:: constants in place of ROCPROFSYS_* literals | [@marantic-amd](https://github.com/marantic-amd) | ✅ | ✅ Approved (dgaliffiAMD) | 2026-05-25 | 6d |
| [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) | docs: Update install instructions for 7.13 | [@peterjunpark](https://github.com/peterjunpark) | ✅ | ✅ Approved (dgaliffiAMD) | 2026-05-25 | 12d |
| [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) | Fix validation scripts to accept extra OMPT kernels from LLVM | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | Pending | 2026-05-25 | 34d |

---

### In Progress (1)

Active work, CI running.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#6355](https://github.com/ROCm/rocm-systems/pull/6355) | [tests] Apply strict `kwargs` checks and fix certain tests | [@kcossett-amd](https://github.com/kcossett-amd) | ⏳ | Pending (32 jobs running) | 2026-05-25 | 4d |

---

### Drafts (19)

| PR | Title | Author | CI | Age |
|---|---|---|---|---|
| [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) | refactor(trace-cache): rename UMP bandwidth metric | [@habajpai-amd](https://github.com/habajpai-amd) | ❌ | 0d |
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
| [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) | Add RHEL system deps workflow | [@sputhala-amd](https://github.com/sputhala-amd) | ❌ | 20d |
| [rocm-systems#5736](https://github.com/ROCm/rocm-systems/pull/5736) | Support ELF's RELR relocation for binary rewrite | [@kcossett-amd](https://github.com/kcossett-amd) | ❌ | 21d |
| [rocm-systems#5414](https://github.com/ROCm/rocm-systems/pull/5414) | Add pytest for rocprof-sys-attach (attach/detach/re-attach) | [@adjordje-amd](https://github.com/adjordje-amd) | ✅ | 31d |
| [rocm-systems#5285](https://github.com/ROCm/rocm-systems/pull/5285) | Argparser refactor | [@marantic-amd](https://github.com/marantic-amd) | ✅ | 33d |
| [rocm-systems#5254](https://github.com/ROCm/rocm-systems/pull/5254) | Add clang-tidy in formatting workflow | [@sputhala-amd](https://github.com/sputhala-amd) | ❌ | 33d |
| [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) | Add initial strix halo changes for rocprofiler-systems CI | [@jbonnell-amd](https://github.com/jbonnell-amd) | ❌ | 48d |
| [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) | Fix `update_env` handling of `REPLACE` mode | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ | 54d |

---

## Risk Signals

### CI Instability

**13/40 PRs have CI failures.**

| PR | Title | Author | Failing Checks | Last Updated |
|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | TheRock CI Summary; rocprofiler-systems test shard 1 | 2026-05-25 |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ubuntu-jammy (g++, Release, 7.2) | 2026-05-25 |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | 33 checks: debian/noble/jammy/rhel/sanitizers/TheRock/gfx950 | 2026-05-12 |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | rhel g++ 8.10 (7.0, 6.4, 6.3, 7.2, 7.1) | 2026-05-15 |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | align per-link PMC + track names | [@adjordje-amd](https://github.com/adjordje-amd) | TheRock CI; rocprofiler-compute test shard 1 | 2026-05-11 |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | Replace SQLite3/rocpd backend with rocprofiler-hub | [@anujshuk-amd](https://github.com/anujshuk-amd) | TheRock CI; Linux Build Linux Packages | 2026-05-25 |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ubuntu-noble (g++, Release, 7.0) | 2026-05-21 |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | Linux Build Linux Packages (+ Windows in progress) | 2026-05-25 |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] Introduce 3 CLI options | [@kcossett-amd](https://github.com/kcossett-amd) | ubuntu-noble-sanitizers address; TheRock CI; rocprofiler-compute shard 2 | 2026-05-07 |
| [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) | [rocpd] Update rocprofiler-sdk-rocpd api to support versioning | [@yhuiYH](https://github.com/yhuiYH) | Code Coverage mi325 ubuntu-22.04 | 2026-05-25 |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | TheRock CI; rocprofiler-systems test shard 1 | 2026-05-19 |
| [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) *(draft)* | refactor(trace-cache): rename UMP bandwidth metric | [@habajpai-amd](https://github.com/habajpai-amd) | 34 checks across all distros/sanitizers | 2026-05-25 |
| [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) *(draft)* | Fix `update_env` handling of `REPLACE` mode | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | 32 checks across rhel/jammy/noble/debian/TheRock | 2026-05-24 |

---

### Test Gap Summary

**23 PRs include test updates. 9 PRs are missing tests.**

| PR | Title | Author | Source Files Changed | Recommended Test Level | Risk of No Tests | Suggested Action |
|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | Fix pthread_mutex_gotcha roctx pause resume | [@mradosav-amd](https://github.com/mradosav-amd) | `pthread_mutex_gotcha.cpp`, `pthread_mutex_gotcha.hpp` | Unit | **High** — bug fix in gotcha interception logic | Add unit test for pause/resume sequencing; check `tests/` for existing gotcha tests |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | `buffer_storage.cpp`, `buffer_storage.hpp` | Unit + Integration | **High** — threading model change in flush path | Add thread-lifecycle and flush-ordering tests; check `tests/trace_cache/` |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) | clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | 20 files: `hip_capture*.cpp/h`, `hip_code_object.*`, `hip_context.cpp`, generated files | System | **High** — new major feature (capture/playback), 20 source files | Add end-to-end capture/playback tests; this is the highest-risk gap in the queue |
| [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) *(draft)* | Add `rocprofsys_push_trace_with_args` | [@kcossett-amd](https://github.com/kcossett-amd) | 13 files: `api.cpp/hpp`, `dl.cpp/hpp`, `module_function.*`, `rocprof-sys-instrument.*`, `main.c` | Integration | **High** — new public API surface | Add API-level tests for push_trace_with_args; look for existing `tests/library/` patterns |
| [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) *(draft)* | refactor(rocprof-sys-causal): centralize runtime state | [@habajpai-amd](https://github.com/habajpai-amd) | `impl.cpp`, `rocprof-sys-causal.cpp`, `rocprof-sys-causal.hpp` | Unit | **Medium** — internal refactor of runtime state | Add state-machine unit tests; check `tests/causal/` for extension points |
| [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) *(draft)* | Update dyninst submodule & fix asan build failures | [@mradosav-amd](https://github.com/mradosav-amd) | `Packages.cmake`, `markers.h` | Integration | **Medium** — submodule update may alter instrumentation behavior | Verify existing instrumentation tests pass; extend if markers.h semantics changed |
| [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) *(draft)* | wire ccache (CMake auto-detect + CI cache) | [@adjordje-amd](https://github.com/adjordje-amd) | `BuildSettings.cmake`, `DyninstTBB.cmake` | Integration (CI) | **Low** — build-system only change | Verify CI build times improve; no functional test needed, but CI job validation sufficient |
| [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) *(draft)* | Add RHEL system deps workflow | [@sputhala-amd](https://github.com/sputhala-amd) | `symbol.cpp` | Unit | **Medium** — symbol resolution change on RHEL | Add symbol-parsing unit test targeting RHEL paths; check `tests/unwind/` |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | `transpose.new.cpp` | Unit | **High** — correctness bug fix in compute kernel | Add a numerical correctness test for transpose output; this is an external contribution and warrants review |

---

## Stale PRs

### Stale (25+ days no activity)

| PR | Title | Author | Last Updated | Age | Recommendation |
|---|---|---|---|---|---|
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [runtime-instrument] Introduce 3 CLI options | [@kcossett-amd](https://github.com/kcossett-amd) | 2026-05-07 | 32d | CI failing on sanitizers and TheRock; author should rebase and fix failing checks — this is a substantive, non-draft PR that needs forward progress. |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | 2026-05-19 | 39d | External contribution with no review and missing tests; ping author to add tests, then assign a reviewer — or consider closing if unmaintained. |
| [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) | Improve Generated Output summary. Cleanup of noisy logs | [@marantic-amd](https://github.com/marantic-amd) | 2026-05-21 | 6d | CI passing, 15 test files updated — solid PR waiting on review; nudge reviewer to take a look this week. |

### Going Stale (3–24 days no activity)

| PR | Title | Author | Last Updated | Age |
|---|---|---|---|---|
| [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) | Replace get_env and set_env from timemory | [@mradosav-amd](https://github.com/mradosav-amd) | 2026-05-20 | 7d |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | replace SFINAE traits with C++20 concepts | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-15 | 9d |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | align per-link PMC + track names | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-11 | 14d |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | trace_cache/buffer_storage: replace flush thread with std::jthread | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-12 | 13d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | 2026-05-12 | 13d |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | 2026-05-21 | 4d |
| [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) | Add hip graph tests | [@sputhala-amd](https://github.com/sputhala-amd) | 2026-05-19 | 6d |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | 2026-05-19 | 70d |

---

## LLM Observations

- **C++20 modernization chain with cascading risk.** There is a dependent PR stack: [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) (C++20 support, 70d old) → [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) (C++20 concepts) → [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) (std::jthread). All three are failing CI. Because #5992 targets the branch produced by #4080, and #5995 targets the branch produced by #5992, none of them can land independently in their current state. The root failure in #4080 needs to be resolved first, or the chain rebased onto `develop`.

- **Three "near-merge" PRs with single-point CI failures.** [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288), [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819),