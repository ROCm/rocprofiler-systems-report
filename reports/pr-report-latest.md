# rocprofiler-systems — Daily PR Report 2026-05-25
> Filtered from [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

## Executive Summary
There are **41** open PRs with the `project: rocprofiler-systems` label. **14** PRs need immediate attention due to failing CI or requested changes. **6** PRs are stale (3+ days without updates). **9** PRs have source changes without corresponding test updates. CI health: 16 passing, 20 failing, 4 in progress, 1 unknown/no checks.

## ⚠️ Needs Attention
(14 PRs) — Failing CI or changes requested.

| PR | Title | Author | Test Coverage | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | [rocprofiler-systems] Fix pthread_mutex_gotcha roctx pause r... | [@mradosav-amd](https://github.com/mradosav-amd) | 🚨 (2 source file(s) changed, 0 test files) | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)) | ❓ | 0d ago | 0d |
| [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) | [rocprofiler-systems] Clean up jacobi-hip example | [@mradosav-amd](https://github.com/mradosav-amd) | ✅ | ⏳ | 🔄 (kcossett-amd) | 0d ago | 4d |
| [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) | [rocprofiler-systems] Update version to 1.7.0 | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | — | ❌ (ubuntu-jammy (g++, ON, ON, OFF, ON, Release, ON, 7.2)) | ✅ (adjordje-amd) | 0d ago | 5d |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | [rocprofiler-systems] trace_cache/buffer_storage: replace ha... | [@adjordje-amd](https://github.com/adjordje-amd) | 🚨 (2 source file(s) changed, 0 test files) | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Build Linux Packages...) | ❓ | 13d ago | 13d |
| [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) | [rocprofiler-systems] replace SFINAE traits with C++20 conce... | [@adjordje-amd](https://github.com/adjordje-amd) | ✅ | ❌ (rhel (g++, 8.10, 7.0, Release), rhel (g++, 8.10, 6.4, Release)...) | ❓ | 9d ago | 13d |
| [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) | [rocprofiler-systems] align per-link PMC + track names acros... | [@adjordje-amd](https://github.com/adjordje-amd) | ✅ | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-compute / Test rocprofiler-compute (shard 1 of 2)) | ✅ (mradosav-amd) | 14d ago | 18d |
| [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) | [rocprofiler-systems] Replace SQLite3/rocpd backend with roc... | [@anujshuk-amd](https://github.com/anujshuk-amd) | ✅ | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Build Linux Packages) | ⏳ | 0d ago | 19d |
| [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) | AI NIC changes for Pensando Phase 2 | [@ajanicijamd](https://github.com/ajanicijamd) | ✅ | ❌ (ubuntu-noble (g++, ON, Release, ON, 7.0)) | ✅ (dgaliffiAMD) | 4d ago | 19d |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) |   clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | 🚨 (20 source file(s) changed, 0 test files) | ❌ (TheRock CI Summary, Linux (hip-tests, rocgdb, rocprofiler-sdk, rocr-debug-agent, rocrtst) / Build Linux Packages...) | 🔄 (stellaraccident) (dgaliffiAMD) | 2d ago | 24d |
| [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) | [rocprofiler-systems] [runtime-instrument] Introduce 3 CLI o... | [@kcossett-amd](https://github.com/kcossett-amd) | ✅ | ❌ (ubuntu-noble-sanitizers (g++, ON, address), TheRock CI Summary...) | ⏳ | 17d ago | 31d |
| [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) | [rocdecode, rocjpeg] removed install section | [@spolifroni-amd](https://github.com/spolifroni-amd) | — | ❓ | 🔄 (dgaliffiAMD) (LakshmiKumar23, AryanSalmanpour) | 13d ago | 31d |
| [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) | [rocprofiler-sdk] [rocpd] Update rocprofiler-sdk-rocpd api t... | [@yhuiYH](https://github.com/yhuiYH) | ✅ | ❌ (Code Coverage • mi325 • ubuntu-22.04) | 🔄 (jrmadsen) | 0d ago | 33d |
| [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) | [Rocprofiler-systems]: Add hip graph tests | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | ✅ | 🔄 (kcossett-amd) | 6d ago | 41d |
| [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) | [rocprofiler-systems] C++20 support | [@adjordje-amd](https://github.com/adjordje-amd) | ✅ | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)) | ⏳ | 5d ago | 70d |


## 🕰️ Stale (3+ days no activity)
(6 PRs) — No updates for 3+ days.

| PR | Title | Author | Test Coverage | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|---|
| [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) | [rocprofiler-systems] Improve Generated Output summary. Clea... | [@marantic-amd](https://github.com/marantic-amd) | ✅ | ✅ | ⏳ | 3d ago | 6d |
| [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) | [rocprof-sys] refactor(env_vars): use env_vars:: constants i... | [@marantic-amd](https://github.com/marantic-amd) | ✅ | ✅ | ❓ | 6d ago | 6d |
| [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) | [rocprofiler-systems] Replace get_env and set_env from timem... | [@mradosav-amd](https://github.com/mradosav-amd) | ✅ | ✅ | ✅ (marantic-amd) | 5d ago | 7d |
| [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) | docs(rocprofiler-systems): Update install instructions for 7... | [@peterjunpark](https://github.com/peterjunpark) | — | ✅ | ✅ (dgaliffiAMD) | 4d ago | 12d |
| [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) | [rocprof-systems]: Fix validation scripts to accept extra OM... | [@sputhala-amd](https://github.com/sputhala-amd) | — | ✅ | ⏳ | 3d ago | 34d |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | 🚨 (1 source file(s) changed, 0 test files) | ✅ | ❓ | 6d ago | 39d |


## ⚡ WIP / Not Marked as Draft
(0 PRs) — Title suggests WIP but PR is not marked as draft.

_None._


## ✅ Healthy
(0 PRs) — Passing CI, approved or awaiting review.

_None._


## ⏳ In Progress
(0 PRs) — Active work, CI running.

_None._


## 📝 Drafts
(21 PRs)

- 📝 [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) — refactor(trace-cache): rename UMP bandwidth metric ([@habajpai-amd](https://github.com/habajpai-amd), 0d old)
- 📝 [rocm-systems#6361](https://github.com/ROCm/rocm-systems/pull/6361) — [rocprofiler-systems] Enable `task_detach` part of openmp-fortran-host ([@kcossett-amd](https://github.com/kcossett-amd), 3d old)
- 📝 [rocm-systems#6355](https://github.com/ROCm/rocm-systems/pull/6355) — [rocprofiler-systems] [tests] Apply strict `kwargs` checks and fix cer ([@kcossett-amd](https://github.com/kcossett-amd), 3d old)
- 📝 [rocm-systems#6300](https://github.com/ROCm/rocm-systems/pull/6300) — feat(rocprof-sys): add SPM beta scaffolding ([@habajpai-amd](https://github.com/habajpai-amd), 5d old)
- 📝 [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) — refactor(rocprof-sys-causal): centralize runtime state ([@habajpai-amd](https://github.com/habajpai-amd), 5d old)
- 📝 [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) — [rocprofiler-systems] Update dyninst submodule & fix asan build failur ([@mradosav-amd](https://github.com/mradosav-amd), 5d old)
- 📝 [rocm-systems#6254](https://github.com/ROCm/rocm-systems/pull/6254) — Config Robustness: Negative Tests for Invalid Values ([@habajpai-amd](https://github.com/habajpai-amd), 5d old)
- 📝 [rocm-systems#6243](https://github.com/ROCm/rocm-systems/pull/6243) — [rocprofiler-systems] Switch Perfetto processing in cached data to run ([@marantic-amd](https://github.com/marantic-amd), 6d old)
- 📝 [rocm-systems#6240](https://github.com/ROCm/rocm-systems/pull/6240) — [rocpfiler-systems] Unify control logic with different triggers ([@marantic-amd](https://github.com/marantic-amd), 6d old)
- 📝 [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) — [rocprofiler-systems] Add `rocprofsys_push_trace_with_args` and cache  ([@kcossett-amd](https://github.com/kcossett-amd), 10d old)
- 📝 [rocm-systems#6057](https://github.com/ROCm/rocm-systems/pull/6057) — [rocprofiler-systems]: Wall Clock migration from timemory ([@sputhala-amd](https://github.com/sputhala-amd), 12d old)
- 📝 [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) — [rocprofiler-systems] wire ccache (CMake auto-detect + CI cache) ([@adjordje-amd](https://github.com/adjordje-amd), 13d old)
- 📝 [rocm-systems#6006](https://github.com/ROCm/rocm-systems/pull/6006) — [rocprofiler-systems] rocprofsys exception hierarchy + clean stacktrac ([@adjordje-amd](https://github.com/adjordje-amd), 13d old)
- 📝 [rocm-systems#5867](https://github.com/ROCm/rocm-systems/pull/5867) — [rocprofiler-systems] Add OpenMP profiling doc ([@kcossett-amd](https://github.com/kcossett-amd), 18d old)
- 📝 [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) — [rocprofiler-systems]: Add RHEL system deps workflow ([@sputhala-amd](https://github.com/sputhala-amd), 20d old)
- 📝 [rocm-systems#5736](https://github.com/ROCm/rocm-systems/pull/5736) — [rocprofiler-systems] Support ELF's RELR relocation for binary rewrite ([@kcossett-amd](https://github.com/kcossett-amd), 21d old)
- 📝 [rocm-systems#5414](https://github.com/ROCm/rocm-systems/pull/5414) — [rocprofiler-systems] Add pytest for rocprof-sys-attach (attach/detach ([@adjordje-amd](https://github.com/adjordje-amd), 31d old)
- 📝 [rocm-systems#5285](https://github.com/ROCm/rocm-systems/pull/5285) — Users/marantic amd/argparser refactor ([@marantic-amd](https://github.com/marantic-amd), 33d old)
- 📝 [rocm-systems#5254](https://github.com/ROCm/rocm-systems/pull/5254) — [rocrof-systems]: Add clang-tidy in formatting workflow ([@sputhala-amd](https://github.com/sputhala-amd), 33d old)
- 📝 [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) — Add initial strix halo changes for rocprofiler-systems CI ([@jbonnell-amd](https://github.com/jbonnell-amd), 48d old)
- 📝 [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) — Fix `update_env` handling of `REPLACE` mode ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 53d old)


## CI Health Snapshot
Out of 41 open PRs: **16** passing, **20** failing, **4** in progress, and **1** with no checks or unknown status. Failing check names: `Code Coverage • mi325 • ubuntu-22.04`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Build Linux Packages`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-compute / Test rocprofiler-compute (shard 1 of 2)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-compute / Test rocprofiler-compute (shard 2 of 2)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)`, `Linux (hip-tests, rocgdb, rocprofiler-sdk, rocr-debug-agent, rocrtst) / Build Linux Packages`, `TheRock CI Summary`, `Ubuntu 22.04 • gfx1151`, `Ubuntu 24.04 • gfx950`, `Windows (hip-tests, rocgdb, rocprofiler-sdk, rocr-debug-agent, rocrtst) / Build Windows Packages`, `clang-tidy (.clang-tidy)`, `debian (g++, ON, Release, ON, 12, 6.4)`, `debian (g++, ON, Release, ON, 12, 7.0)`, `debian (g++, ON, Release, ON, 12, 7.1)`, `debian (g++, ON, Release, ON, 12, 7.2)`.

## 🧪 Test Coverage Analysis
Out of 41 open PRs: **23** include test updates, **9** have source changes without tests, **9** are config/docs only, **0** could not be analyzed.

### PRs Missing Test Coverage
| PR | Title | Author | Source Files Changed | Test Files | Detail |
|---|---|---|---|---|---|
| [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) | [rocprofiler-systems] Fix pthread_mutex_gotcha roc... | [@mradosav-amd](https://github.com/mradosav-amd) | 2 | 0 | `pthread_mutex_gotcha.cpp`, `pthread_mutex_gotcha.hpp` |
| [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) | refactor(rocprof-sys-causal): centralize runtime s... | [@habajpai-amd](https://github.com/habajpai-amd) | 3 | 0 | `impl.cpp`, `rocprof-sys-causal.cpp`, `rocprof-sys-causal.hpp` |
| [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) | [rocprofiler-systems] Update dyninst submodule & f... | [@mradosav-amd](https://github.com/mradosav-amd) | 2 | 0 | `Packages.cmake`, `markers.h` |
| [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) | [rocprofiler-systems] Add `rocprofsys_push_trace_w... | [@kcossett-amd](https://github.com/kcossett-amd) | 13 | 0 | `MacroUtilities.cmake`, `module_function.cpp`, `module_function.hpp`, `rocprof-sys-instrument.cpp`, `rocprof-sys-instrument.hpp` +8 more |
| [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) | [rocprofiler-systems] wire ccache (CMake auto-dete... | [@adjordje-amd](https://github.com/adjordje-amd) | 2 | 0 | `BuildSettings.cmake`, `DyninstTBB.cmake` |
| [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) | [rocprofiler-systems] trace_cache/buffer_storage: ... | [@adjordje-amd](https://github.com/adjordje-amd) | 2 | 0 | `buffer_storage.cpp`, `buffer_storage.hpp` |
| [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) | [rocprofiler-systems]: Add RHEL system deps workfl... | [@sputhala-amd](https://github.com/sputhala-amd) | 1 | 0 | `symbol.cpp` |
| [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) |   clr/hrr: In-tree full capture and playback | [@gandryey](https://github.com/gandryey) | 20 | 0 | `hip_code_object.cpp`, `hip_code_object.hpp`, `hip_context.cpp`, `gen_hrr_api_args.py`, `hip_capture.cpp` +15 more |
| [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) | Fix output index calculation in transpose_a kernel | [@jared-mcd-han](https://github.com/jared-mcd-han) | 1 | 0 | `transpose.new.cpp` |


## What Changed Since Yesterday
(No previous report — this is day one.)

## Recommended Actions
1. [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) — fix failing CI.
2. [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) — address review feedback from kcossett-amd.
3. [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) — fix failing CI.
4. [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) — fix failing CI.
5. [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) — fix failing CI.
6. [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) — fix failing CI.
7. [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) — fix failing CI.
8. [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) — fix failing CI.
9. [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) — fix failing CI and address review feedback from stellaraccident.
10. [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) — fix failing CI.
11. [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) — address review feedback from dgaliffiAMD.
12. [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) — fix failing CI and address review feedback from jrmadsen.
13. [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) — address review feedback from kcossett-amd.
14. [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) — fix failing CI.
15. [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) — Stale for 3 days. Ping author [@marantic-amd](https://github.com/marantic-amd) for an update or consider closing.
16. [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) — Stale for 6 days. Ping author [@marantic-amd](https://github.com/marantic-amd) for an update or consider closing.
17. [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) — Stale for 5 days. Ping author [@mradosav-amd](https://github.com/mradosav-amd) for an update or consider closing.
18. [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) — Stale for 4 days. Ping author [@peterjunpark](https://github.com/peterjunpark) for an update or consider closing.
19. [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) — Stale for 3 days. Ping author [@sputhala-amd](https://github.com/sputhala-amd) for an update or consider closing.
20. [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) — 2 source file(s) changed with no test updates. Author [@mradosav-amd](https://github.com/mradosav-amd) should add tests.
21. [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) — 3 source file(s) changed with no test updates. Author [@habajpai-amd](https://github.com/habajpai-amd) should add tests.
22. [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) — 2 source file(s) changed with no test updates. Author [@mradosav-amd](https://github.com/mradosav-amd) should add tests.
23. [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) — 13 source file(s) changed with no test updates. Author [@kcossett-amd](https://github.com/kcossett-amd) should add tests.
24. [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) — 2 source file(s) changed with no test updates. Author [@adjordje-amd](https://github.com/adjordje-amd) should add tests.
25. [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) — 2 source file(s) changed with no test updates. Author [@adjordje-amd](https://github.com/adjordje-amd) should add tests.
26. [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) — 1 source file(s) changed with no test updates. Author [@sputhala-amd](https://github.com/sputhala-amd) should add tests.
27. [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) — 20 source file(s) changed with no test updates. Author [@gandryey](https://github.com/gandryey) should add tests.
28. [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) — 1 source file(s) changed with no test updates. Author [@jared-mcd-han](https://github.com/jared-mcd-han) should add tests.

---
*Auto-generated: 2026-05-25*
