# rocprofiler-systems — Daily PR Report 2026-04-08
> Filtered from [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

## Executive Summary
There are **59** open PRs with the `project: rocprofiler-systems` label. **18** PRs need immediate attention due to failing CI or requested changes. **2** PRs are stale (3+ days without updates). CI health: 16 passing, 40 failing, 3 in progress, 0 unknown/no checks.

## ⚠️ Needs Attention
(18 PRs) — Failing CI or changes requested.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#4758](https://github.com/ROCm/rocm-systems/pull/4758) | [Rocprof-systems]: PAPI build failure fix on Cray | [@sputhala-amd](https://github.com/sputhala-amd) | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-sdk / Test rocprofiler-sdk (shard 1 of 1)) | ✅ (dgaliffiAMD) | 0d ago | 1d |
| [rocm-systems#4663](https://github.com/ROCm/rocm-systems/pull/4663) | [Rocprof-systems][Test]: Validation modifications for APUs | [@sputhala-amd](https://github.com/sputhala-amd) | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)...) | ❓ | 0d ago | 5d |
| [rocm-systems#4581](https://github.com/ROCm/rocm-systems/pull/4581) | [rocprofiler-systems] Bump CMake to 3.25; remove nested .git... | [@mradosav-amd](https://github.com/mradosav-amd) | ❌ (TheRock CI Summary, Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-sdk / Test rocprofiler-sdk (shard 1 of 1)) | ⏳ | 0d ago | 7d |
| [rocm-systems#4563](https://github.com/ROCm/rocm-systems/pull/4563) | Bump pygments from 2.18.0 to 2.20.0 in /projects/rocprofiler... | [@dependabot[bot]](https://github.com/dependabot[bot]) | ❌ (trigger-rocm-ci) | ✅ (dgaliffiAMD) | 7d ago | 8d |
| [rocm-systems#4528](https://github.com/ROCm/rocm-systems/pull/4528) | Bump cryptography from 44.0.1 to 46.0.6 in /projects/rocprof... | [@dependabot[bot]](https://github.com/dependabot[bot]) | ❌ (trigger-rocm-ci) | ❓ | 6d ago | 10d |
| [rocm-systems#4456](https://github.com/ROCm/rocm-systems/pull/4456) | [rocprofiler-systems] Remove get_is_continuous_integration | [@mradosav-amd](https://github.com/mradosav-amd) | ❌ (Ubuntu 24.04 • gfx950) | ❓ | 11d ago | 12d |
| [rocm-systems#4446](https://github.com/ROCm/rocm-systems/pull/4446) | [rocprofiler-systems] Fix sanitizer issues: buffer teardown ... | [@mradosav-amd](https://github.com/mradosav-amd) | ❌ (Ubuntu 24.04 • gfx950) | ❓ | 12d ago | 12d |
| [rocm-systems#4331](https://github.com/ROCm/rocm-systems/pull/4331) | Configurable JSON profiling/tracing presets | [@marantic-amd](https://github.com/marantic-amd) | ✅ | 🔄 (mradosav-amd) | 0d ago | 15d |
| [rocm-systems#4159](https://github.com/ROCm/rocm-systems/pull/4159) | Add formatting.yml workflow to include formatting for rocpro... | [@jbonnell-amd](https://github.com/jbonnell-amd) | ❌ (TheRock CI Summary, Linux (aqlprofile, hip-tests, rocgdb, rocprofiler-compute, rocprofiler-systems, rocr-debug-agent, rocrtst) / Test / Test rocrtst / Test rocrtst (shard 1 of 1)) | ⏳ | 6d ago | 21d |
| [rocm-systems#4145](https://github.com/ROCm/rocm-systems/pull/4145) | Added always-visible pre-run validation warnings. Added a po... | [@marantic-amd](https://github.com/marantic-amd) | ✅ | 🔄 (mradosav-amd) (dgaliffiAMD) | 0d ago | 21d |
| [rocm-systems#4036](https://github.com/ROCm/rocm-systems/pull/4036) | [Rocprof-systems]: Enable KFD event tracing support | [@sputhala-amd](https://github.com/sputhala-amd) | ✅ | 🔄 (adjordje-amd) (prbasyal-amd) | 0d ago | 26d |
| [rocm-systems#3412](https://github.com/ROCm/rocm-systems/pull/3412) | [rocprofiler-systems] Enable re-attach | [@adjordje-amd](https://github.com/adjordje-amd) | ⏳ (Ubuntu 24.04 • gfx950) | 🔄 (dgaliffiAMD) | 0d ago | 46d |
| [rocm-systems#3247](https://github.com/ROCm/rocm-systems/pull/3247) | Cherry-pick PR #3180: [Azure External CI] Disable Azure CI o... | [@JeniferC99](https://github.com/JeniferC99) | ❌ (TheRock CI Summary, Windows (hip-tests, rocprofiler-tests) / Test / Test libhipcxx_hipcc...) | ✅ (rahulc-gh, dgaliffiAMD) | 4d ago | 54d |
| [rocm-systems#3101](https://github.com/ROCm/rocm-systems/pull/3101) | Add exceptions to catch errors | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ❌ (TheRock CI Summary, Windows (hip-tests, rocprofiler-tests) / Test / Test hip-tests...) | ✅ (mradosav-amd, habajpai-amd) | 40d ago | 61d |
| [rocm-systems#2624](https://github.com/ROCm/rocm-systems/pull/2624) | docs: bump rocm-docs-core to 1.31.2 | [@peterjunpark](https://github.com/peterjunpark) | ❌ (Jenkins, TheRock CI Summary...) | ✅ (amd-jnovotny, dgaliffiAMD) | 4d ago | 82d |
| [rocm-systems#2594](https://github.com/ROCm/rocm-systems/pull/2594) | refactor: centralize output utilities from binaries into com... | [@habajpai-amd](https://github.com/habajpai-amd) | ✅ | 🔄 (mradosav-amd) | 1d ago | 84d |
| [rocm-systems#2542](https://github.com/ROCm/rocm-systems/pull/2542) | Improvement thread storage from std::array to stable_vector ... | [@anujshuk-amd](https://github.com/anujshuk-amd) | ❌ (Azure CI Summary) | 🔄 (jrmadsen) | 40d ago | 89d |
| [rocm-systems#112](https://github.com/ROCm/rocm-systems/pull/112) | Extract correct gpu type for smi power metrics | [@systems-assistant[bot]](https://github.com/systems-assistant[bot]) | ❌ (rocm-ci-caller, opensuse (g++, 15.6, Release)) | ✅ (dgaliffiAMD) | 40d ago | 244d |


## 🕰️ Stale (3+ days no activity)
(2 PRs) — No updates for 3+ days.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#4500](https://github.com/ROCm/rocm-systems/pull/4500) | Fix fragile LibDwarf/LibElf regex version parsing | [@Muhamed-Husic](https://github.com/Muhamed-Husic) | ✅ | ❓ | 11d ago | 11d |
| [rocm-systems#3962](https://github.com/ROCm/rocm-systems/pull/3962) | [rocprofiler-systems] Have CTest call Pytest | [@kcossett-amd](https://github.com/kcossett-amd) | ✅ | ⏳ | 6d ago | 27d |


## ⚡ WIP / Not Marked as Draft
(0 PRs) — Title suggests WIP but PR is not marked as draft.

_None._


## ✅ Healthy
(5 PRs) — Passing CI, approved or awaiting review.

| PR | Title | Author | CI | Review Status | Last Updated | Age |
|---|---|---|---|---|---|---|
| [rocm-systems#4647](https://github.com/ROCm/rocm-systems/pull/4647) | Users/lloginov amd/mpi filter output | [@lloginov-amd](https://github.com/lloginov-amd) | ✅ | ⏳ | 0d ago | 5d |
| [rocm-systems#4622](https://github.com/ROCm/rocm-systems/pull/4622) | [rocprofiler-systems] Filter procedures by modules and gate ... | [@kcossett-amd](https://github.com/kcossett-amd) | ✅ | ⏳ | 1d ago | 6d |
| [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) | Fix `update_env` handling of `REPLACE` mode | [@dgaliffiAMD](https://github.com/dgaliffiAMD) | ✅ | ⏳ | 0d ago | 6d |
| [rocm-systems#4612](https://github.com/ROCm/rocm-systems/pull/4612) | [rocprofiler-systems] Adapt CPU metrics to PMC collector app... | [@marantic-amd](https://github.com/marantic-amd) | ✅ | ⏳ | 0d ago | 6d |
| [rocm-systems#4436](https://github.com/ROCm/rocm-systems/pull/4436) | Bump rocm-docs-core from 1.32.1 to 1.33.1 in /projects/rocpr... | [@dependabot[bot]](https://github.com/dependabot[bot]) | ✅ | ✅ (alexxu-amd) | 0d ago | 13d |


## ⏳ In Progress
(0 PRs) — Active work, CI running.

_None._


## 📝 Drafts
(34 PRs)

- 📝 [rocm-systems#4808](https://github.com/ROCm/rocm-systems/pull/4808) — [Test] gitmodule file in workflows ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 0d old)
- 📝 [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) — Add initial strix halo changes for rocprofiler-systems CI ([@jbonnell-amd](https://github.com/jbonnell-amd), 0d old)
- 📝 [rocm-systems#4762](https://github.com/ROCm/rocm-systems/pull/4762) — Added changes to support runtime version selection of schema in rocpds ([@anujshuk-amd](https://github.com/anujshuk-amd), 0d old)
- 📝 [rocm-systems#4728](https://github.com/ROCm/rocm-systems/pull/4728) — [rocprofiler-systems] Add amdclang as compiler for rocprofiler-systems ([@mradosav-amd](https://github.com/mradosav-amd), 1d old)
- 📝 [rocm-systems#4639](https://github.com/ROCm/rocm-systems/pull/4639) — [DNM] [WIP] Test different rocprofiler-systems workflow approach ([@mradosav-amd](https://github.com/mradosav-amd), 5d old)
- 📝 [rocm-systems#4629](https://github.com/ROCm/rocm-systems/pull/4629) — Add docker-compose.yml and update rocprofiler-systems Docker matrix to ([@njobypet](https://github.com/njobypet), 6d old)
- 📝 [rocm-systems#4605](https://github.com/ROCm/rocm-systems/pull/4605) — Update compiler on rhel-8 dockers ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 7d old)
- 📝 [rocm-systems#4592](https://github.com/ROCm/rocm-systems/pull/4592) — Added color codes for CMake and C++ compilers ([@ajanicijamd](https://github.com/ajanicijamd), 7d old)
- 📝 [rocm-systems#4591](https://github.com/ROCm/rocm-systems/pull/4591) — [DNM] [Test] [rocprofiler-systems] Use `dyninst_13-no-boost` branch of ([@kcossett-amd](https://github.com/kcossett-amd), 7d old)
- 📝 [rocm-systems#4514](https://github.com/ROCm/rocm-systems/pull/4514) — Update version of binutils used by Dyninst to 2.46.0 ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 11d old)
- 📝 [rocm-systems#4511](https://github.com/ROCm/rocm-systems/pull/4511) — AI NIC Pensando Phase 2 ([@ajanicijamd](https://github.com/ajanicijamd), 11d old)
- 📝 [rocm-systems#4494](https://github.com/ROCm/rocm-systems/pull/4494) — [rocprofiler-systems] Add sanitizer workflows (address, thread, undefi ([@mradosav-amd](https://github.com/mradosav-amd), 11d old)
- 📝 [rocm-systems#4487](https://github.com/ROCm/rocm-systems/pull/4487) — [Test] Add TBB as a submodule and update to 2022.3 ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 12d old)
- 📝 [rocm-systems#4423](https://github.com/ROCm/rocm-systems/pull/4423) — [DNM] Users/adjordje amd/ci cd test ([@adjordje-amd](https://github.com/adjordje-amd), 13d old)
- 📝 [rocm-systems#4385](https://github.com/ROCm/rocm-systems/pull/4385) — [TEST] Update Dyninst module to a version that does not depend on Boos ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 14d old)
- 📝 [rocm-systems#4170](https://github.com/ROCm/rocm-systems/pull/4170) — Users/dgaliffi/output summary tests ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 21d old)
- 📝 [rocm-systems#4144](https://github.com/ROCm/rocm-systems/pull/4144) — Users/anujshuk amd/rocpdsna analysis dev -Just for understanding ([@anujshuk-amd](https://github.com/anujshuk-amd), 21d old)
- 📝 [rocm-systems#4088](https://github.com/ROCm/rocm-systems/pull/4088) — [WIP]feat: Unified Memory Profiling ([@habajpai-amd](https://github.com/habajpai-amd), 22d old)
- 📝 [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) — [DNM] Cpp20 ([@adjordje-amd](https://github.com/adjordje-amd), 23d old)
- 📝 [rocm-systems#3627](https://github.com/ROCm/rocm-systems/pull/3627) — Add sdma-test to ctest suite ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 39d old)
- 📝 [rocm-systems#3608](https://github.com/ROCm/rocm-systems/pull/3608) — [Rocprof-systems]: TransferBench test sampling interval fix ([@sputhala-amd](https://github.com/sputhala-amd), 39d old)
- 📝 [rocm-systems#3585](https://github.com/ROCm/rocm-systems/pull/3585) — [Rocprof-systems]: Fix CPU agent init when ROCm is enabled but no GPUs ([@sputhala-amd](https://github.com/sputhala-amd), 40d old)
- 📝 [rocm-systems#3504](https://github.com/ROCm/rocm-systems/pull/3504) — [TEST] Add support for Python version-specific installation in CMake ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 42d old)
- 📝 [rocm-systems#3432](https://github.com/ROCm/rocm-systems/pull/3432) — [rocprofiler-systems] Replace ROCPROFSYS_VERBOSE with ROCPROFSYS_LOG_L ([@dgaliffiAMD](https://github.com/dgaliffiAMD), 45d old)
- 📝 [rocm-systems#3269](https://github.com/ROCm/rocm-systems/pull/3269) — Fix/lulesh skip push pop check ([@anujshuk-amd](https://github.com/anujshuk-amd), 50d old)
- 📝 [rocm-systems#2433](https://github.com/ROCm/rocm-systems/pull/2433) — Update timemory submodule to include Libunwind Repository from jrmadse ([@anujshuk-amd](https://github.com/anujshuk-amd), 105d old)
- 📝 [rocm-systems#2407](https://github.com/ROCm/rocm-systems/pull/2407) — integrate ghc::filesystem project-wide ([@habajpai-amd](https://github.com/habajpai-amd), 109d old)
- 📝 [rocm-systems#1809](https://github.com/ROCm/rocm-systems/pull/1809) — [rocprofiler-systems] [rocprof-sys-avail] Add support for listing avai ([@kcossett-amd](https://github.com/kcossett-amd), 147d old)
- 📝 [rocm-systems#1452](https://github.com/ROCm/rocm-systems/pull/1452) — Update os-release from 9.4 to 9 in rocprofiler-systems-redhat.yml ([@jbonnell-amd](https://github.com/jbonnell-amd), 172d old)
- 📝 [rocm-systems#1445](https://github.com/ROCm/rocm-systems/pull/1445) — [rocprofiler-systems] Add OpenMP Offload Doc ([@kcossett-amd](https://github.com/kcossett-amd), 172d old)
- 📝 [rocm-systems#758](https://github.com/ROCm/rocm-systems/pull/758) — Users/tcgu amd/rocprofsys attach ([@tcgu-amd](https://github.com/tcgu-amd), 224d old)
- 📝 [rocm-systems#106](https://github.com/ROCm/rocm-systems/pull/106) — Added event flow for hipEventRecord and hipEventSynchronize functions ([@systems-assistant[bot]](https://github.com/systems-assistant[bot]), 244d old)
- 📝 [rocm-systems#104](https://github.com/ROCm/rocm-systems/pull/104) — Check system executable path validity to avoid codeQL error ([@systems-assistant[bot]](https://github.com/systems-assistant[bot]), 244d old)
- 📝 [rocm-systems#103](https://github.com/ROCm/rocm-systems/pull/103) — Enable rocprofiler-systems testsuite to run with packaged binary ([@systems-assistant[bot]](https://github.com/systems-assistant[bot]), 244d old)


## CI Health Snapshot
Out of 59 open PRs: **16** passing, **40** failing, **3** in progress, and **0** with no checks or unknown status. Failing check names: `Azure CI Summary`, `Build (AlmaLinux8)`, `Documentation / Markdown`, `Documentation / Spelling`, `Jenkins`, `Linux (aqlprofile, hip-tests, rocgdb, rocprofiler-compute, rocprofiler-systems, rocr-debug-agent, rocrtst) / Test / Test rocrtst / Test rocrtst (shard 1 of 1)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Build Linux Packages`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-sdk / Test rocprofiler-sdk (shard 1 of 1)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-sdk, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-systems) / Build Linux Packages`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler-systems) / Test / Test rocprofiler-systems / Test rocprofiler-systems (shard 1 of 1)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler_systems) / Build Linux Packages`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler_systems) / Test / Test rocprofiler_compute / Test rocprofiler_compute (shard 1 of 1)`, `Linux (aqlprofile, rocprofiler-compute, rocprofiler_systems) / Test / Test rocprofiler_systems / Test rocprofiler_systems (shard 1 of 1)`, `Linux (hip-tests, rocprofiler-tests) / Build Linux Packages`.

## What Changed Since Yesterday
(No previous report — this is day one.)

## Recommended Actions
1. [rocm-systems#4758](https://github.com/ROCm/rocm-systems/pull/4758) — fix failing CI.
2. [rocm-systems#4663](https://github.com/ROCm/rocm-systems/pull/4663) — fix failing CI.
3. [rocm-systems#4581](https://github.com/ROCm/rocm-systems/pull/4581) — fix failing CI.
4. [rocm-systems#4563](https://github.com/ROCm/rocm-systems/pull/4563) — fix failing CI.
5. [rocm-systems#4528](https://github.com/ROCm/rocm-systems/pull/4528) — fix failing CI.
6. [rocm-systems#4456](https://github.com/ROCm/rocm-systems/pull/4456) — fix failing CI.
7. [rocm-systems#4446](https://github.com/ROCm/rocm-systems/pull/4446) — fix failing CI.
8. [rocm-systems#4331](https://github.com/ROCm/rocm-systems/pull/4331) — address review feedback from mradosav-amd.
9. [rocm-systems#4159](https://github.com/ROCm/rocm-systems/pull/4159) — fix failing CI.
10. [rocm-systems#4145](https://github.com/ROCm/rocm-systems/pull/4145) — address review feedback from mradosav-amd.
11. [rocm-systems#4036](https://github.com/ROCm/rocm-systems/pull/4036) — address review feedback from adjordje-amd.
12. [rocm-systems#3412](https://github.com/ROCm/rocm-systems/pull/3412) — address review feedback from dgaliffiAMD.
13. [rocm-systems#3247](https://github.com/ROCm/rocm-systems/pull/3247) — fix failing CI.
14. [rocm-systems#3101](https://github.com/ROCm/rocm-systems/pull/3101) — fix failing CI.
15. [rocm-systems#2624](https://github.com/ROCm/rocm-systems/pull/2624) — fix failing CI.
16. [rocm-systems#2594](https://github.com/ROCm/rocm-systems/pull/2594) — address review feedback from mradosav-amd.
17. [rocm-systems#2542](https://github.com/ROCm/rocm-systems/pull/2542) — fix failing CI and address review feedback from jrmadsen.
18. [rocm-systems#112](https://github.com/ROCm/rocm-systems/pull/112) — fix failing CI.
19. [rocm-systems#4500](https://github.com/ROCm/rocm-systems/pull/4500) — Stale for 11 days. Ping author [@Muhamed-Husic](https://github.com/Muhamed-Husic) for an update or consider closing.
20. [rocm-systems#3962](https://github.com/ROCm/rocm-systems/pull/3962) — Stale for 6 days. Ping author [@kcossett-amd](https://github.com/kcossett-amd) for an update or consider closing.

---
*Auto-generated: 2026-04-08*
