# Daily PR Report — 2026-05-25

> rocprofiler-systems · [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems) · label: `project: rocprofiler-systems`

---

## Executive Summary

- **Total PRs:** 41
- **In Review:** 2 non-draft PRs with passing CI (approved or awaiting review)
- **Needs Attention:** 14 PRs with failing CI or changes requested
- **CI Failures:** 13 PRs with at least one failing CI check
- **Missing Tests:** 9 PRs with source changes but no test updates
- **Stale (3+ days no activity):** 4 PRs
- **Drafts:** 21 PRs in draft state

> This is the first report for this project — no overnight comparison available.

---

## Key Highlights

- **Approved but blocked by CI:** Three ready-to-merge PRs — [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349), [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819), and [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) — are approved but have failing CI checks that need resolution before merging.
- **Version bump PR stuck:** [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) ("Update version to 1.7.0") is approved by `adjordje-amd` and is a config-only change, but is blocked by a single failing ubuntu-jammy build — worth a quick triage.
- **Long-lived C++20 stack:** A chain of PRs by [@adjordje-amd](https://github.com/adjordje-amd) — [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) (70 days), [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) (13 days), [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) (13 days) — form a sequential dependency chain targeting a C++20 migration. The base PR is 70 days old and still failing CI tests; this chain needs coordinated review and unblocking.
- **Changes requested, no response:** [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) has changes requested from [@jrmadsen](https://github.com/jrmadsen) and is 33 days old. [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) has changes requested from [@kcossett-amd](https://github.com/kcossett-amd) and is 41 days old with passing CI — author should address feedback.
- **External contribution going stale:** [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) is an external contribution (39 days old, 6 days since last update) with passing CI and no review decision — needs a maintainer to look at it promptly.

---

## PR Breakdown

### Needs Attention (14)

PRs with failing CI or changes requested — require action from author or reviewer.

- [rocm-systems#6388](https://github.com/ROCm/rocm-systems/pull/6388) — **Fix pthread_mutex_gotcha roctx pause resume** by [@mradosav-amd](https://github.com/mradosav-amd) · CI: ❌ failing (rocprofiler-systems test shard) · Review: pending · Updated 0d ago · ⚠️ Missing tests for `pthread_mutex_gotcha.cpp/.hpp`

- [rocm-systems#6349](https://github.com/ROCm/rocm-systems/pull/6349) — **Clean up jacobi-hip example** by [@mradosav-amd](https://github.com/mradosav-amd) · CI: ❌ failing (rocprofiler-compute test shard 2) · Review: ✅ approved by `kcossett-amd` · Updated 0d ago

- [rocm-systems#6288](https://github.com/ROCm/rocm-systems/pull/6288) — **Update version to 1.7.0** by [@dgaliffiAMD](https://github.com/dgaliffiAMD) · CI: ❌ failing (ubuntu-jammy g++ 7.2) · Review: ✅ approved by `adjordje-amd` · Updated 0d ago

- [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) — **trace_cache/buffer_storage: replace hand-rolled flush thread with std::jthread** by [@adjordje-amd](https://github.com/adjordje-amd) · CI: ❌ failing (32+ checks across all distros) · Review: pending (no decision) · Updated 13d ago · ⚠️ Missing tests for `buffer_storage.cpp/.hpp`

- [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) — **replace SFINAE traits with C++20 concepts** by [@adjordje-amd](https://github.com/adjordje-amd) · CI: ❌ failing (rhel g++ 8.10, all ROCm versions) · Review: pending · Updated 9d ago · Targets `users/adjorjde-amd/std-cpp20` (not `develop`)

- [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) — **align per-link PMC + track names across emit and register sites** by [@adjordje-amd](https://github.com/adjordje-amd) · CI: ❌ failing (rocprofiler-compute test shard 1) · Review: ✅ approved by `mradosav-amd` · Updated 14d ago

- [rocm-systems#5808](https://github.com/ROCm/rocm-systems/pull/5808) — **Replace SQLite3/rocpd backend with rocprofiler-hub library** by [@anujshuk-amd](https://github.com/anujshuk-amd) · CI: ❌ failing (TheRock CI Summary, Linux Build Linux Packages) · Review: pending (3 reviewers assigned) · Updated 0d ago

- [rocm-systems#5777](https://github.com/ROCm/rocm-systems/pull/5777) — **AI NIC changes for Pensando Phase 2** by [@ajanicijamd](https://github.com/ajanicijamd) · CI: ❌ failing (ubuntu-noble g++ 7.0) · Review: ✅ approved by `dgaliffiAMD` · Updated 4d ago

- [rocm-systems#5690](https://github.com/ROCm/rocm-systems/pull/5690) — **clr/hrr: In-tree full capture and playback** by [@gandryey](https://github.com/gandryey) · CI: ❌ failing (Linux + Windows build packages) · Review: 🚨 changes requested by `stellaraccident` · Updated 2d ago · ⚠️ Missing tests across 20 source files

- [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) — **[runtime-instrument] Introduce 3 CLI options and rework some code** by [@kcossett-amd](https://github.com/kcossett-amd) · CI: ❌ failing (asan, TheRock, rocprofiler-compute shard 2) · Review: pending · Updated 18d ago

- [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) — **[rocdecode, rocjpeg] removed install section** by [@spolifroni-amd](https://github.com/spolifroni-amd) · CI: ⚠️ unknown · Review: 🚨 changes requested by `dgaliffiAMD` · Updated 13d ago · Docs-only change; 9 reviewers assigned

- [rocm-systems#5267](https://github.com/ROCm/rocm-systems/pull/5267) — **[rocpd] Update rocprofiler-sdk-rocpd api to support versioning** by [@yhuiYH](https://github.com/yhuiYH) · CI: ❌ failing (Code Coverage mi325 ubuntu-22.04) · Review: 🚨 changes requested by `jrmadsen` · Updated 0d ago · 33 days old

- [rocm-systems#4993](https://github.com/ROCm/rocm-systems/pull/4993) — **Add hip graph tests** by [@sputhala-amd](https://github.com/sputhala-amd) · CI: ✅ passing · Review: 🚨 changes requested by `kcossett-amd` · Updated 6d ago · 41 days old — CI passing, just needs author to address review feedback

- [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) — **C++20 support** by [@adjordje-amd](https://github.com/adjordje-amd) · CI: ❌ failing (TheRock CI, rocprofiler-systems test shard) · Review: pending · Updated 5d ago · ⚠️ **70 days old** — base PR for C++20 chain

---

### In Review (2)

Passing CI, approved or awaiting review — nearest to merge.

- [rocm-systems#6035](https://github.com/ROCm/rocm-systems/pull/6035) — **docs(rocprofiler-systems): Update install instructions for 7.13** by [@peterjunpark](https://github.com/peterjunpark) · CI: ✅ passing · Review: ✅ approved by `dgaliffiAMD` · Updated 0d ago · Docs-only; still awaiting `jrmadsen` and `sputhala-amd`

- [rocm-systems#5214](https://github.com/ROCm/rocm-systems/pull/5214) — **Fix validation scripts to accept extra OMPT kernels from LLVM** by [@sputhala-amd](https://github.com/sputhala-amd) · CI: ✅ passing · Review: pending · Updated 0d ago · 34 days old — test-only changes, needs review from `jrmadsen`

---

### In Progress (0)

No PRs currently have CI actively running as their primary state (non-draft).

---

### Drafts (21)

- [rocm-systems#6387](https://github.com/ROCm/rocm-systems/pull/6387) — **refactor(trace-cache): rename UMP bandwidth metric** by [@habajpai-amd](https://github.com/habajpai-amd) · 0d old
- [rocm-systems#6361](https://github.com/ROCm/rocm-systems/pull/6361) — **Enable `task_detach` part of openmp-fortran-host test** by [@kcossett-amd](https://github.com/kcossett-amd) · 4d old
- [rocm-systems#6355](https://github.com/ROCm/rocm-systems/pull/6355) — **Apply strict `kwargs` checks and fix certain test regexes** by [@kcossett-amd](https://github.com/kcossett-amd) · 4d old · CI: ⏳ in progress
- [rocm-systems#6300](https://github.com/ROCm/rocm-systems/pull/6300) — **feat(rocprof-sys): add SPM beta scaffolding** by [@habajpai-amd](https://github.com/habajpai-amd) · 5d old
- [rocm-systems#6297](https://github.com/ROCm/rocm-systems/pull/6297) — **refactor(rocprof-sys-causal): centralize runtime state** by [@habajpai-amd](https://github.com/habajpai-amd) · 5d old
- [rocm-systems#6295](https://github.com/ROCm/rocm-systems/pull/6295) — **Update dyninst submodule & fix asan build failures** by [@mradosav-amd](https://github.com/mradosav-amd) · 5d old
- [rocm-systems#6254](https://github.com/ROCm/rocm-systems/pull/6254) — **Config Robustness: Negative Tests for Invalid Values** by [@habajpai-amd](https://github.com/habajpai-amd) · 6d old
- [rocm-systems#6243](https://github.com/ROCm/rocm-systems/pull/6243) — **Switch Perfetto processing in cached data to run in parallel** by [@marantic-amd](https://github.com/marantic-amd) · 6d old
- [rocm-systems#6240](https://github.com/ROCm/rocm-systems/pull/6240) — **Unify control logic with different triggers** by [@marantic-amd](https://github.com/marantic-amd) · 6d old
- [rocm-systems#6116](https://github.com/ROCm/rocm-systems/pull/6116) — **Add `rocprofsys_push_trace_with_args` and cache region arguments** by [@kcossett-amd](https://github.com/kcossett-amd) · 11d old
- [rocm-systems#6057](https://github.com/ROCm/rocm-systems/pull/6057) — **Wall Clock migration from timemory** by [@sputhala-amd](https://github.com/sputhala-amd) · 12d old
- [rocm-systems#6009](https://github.com/ROCm/rocm-systems/pull/6009) — **wire ccache (CMake auto-detect + CI cache)** by [@adjordje-amd](https://github.com/adjordje-amd) · 13d old
- [rocm-systems#6006](https://github.com/ROCm/rocm-systems/pull/6006) — **rocprofsys exception hierarchy + clean stacktrace** by [@adjordje-amd](https://github.com/adjordje-amd) · 13d old
- [rocm-systems#5867](https://github.com/ROCm/rocm-systems/pull/5867) — **Add OpenMP profiling doc** by [@kcossett-amd](https://github.com/kcossett-amd) · 18d old
- [rocm-systems#5762](https://github.com/ROCm/rocm-systems/pull/5762) — **Add RHEL system deps workflow** by [@sputhala-amd](https://github.com/sputhala-amd) · 20d old · CI: ⏳ in progress (with some failures)
- [rocm-systems#5736](https://github.com/ROCm/rocm-systems/pull/5736) — **Support ELF's RELR relocation for binary rewrite** by [@kcossett-amd](https://github.com/kcossett-amd) · 21d old
- [rocm-systems#5414](https://github.com/ROCm/rocm-systems/pull/5414) — **Add pytest for rocprof-sys-attach (attach/detach/re-attach)** by [@adjordje-amd](https://github.com/adjordje-amd) · 31d old
- [rocm-systems#5285](https://github.com/ROCm/rocm-systems/pull/5285) — **Argparser refactor** by [@marantic-amd](https://github.com/marantic-amd) · 33d old
- [rocm-systems#5254](https://github.com/ROCm/rocm-systems/pull/5254) — **Add clang-tidy in formatting workflow** by [@sputhala-amd](https://github.com/sputhala-amd) · 33d old · labeled `Stale`
- [rocm-systems#4769](https://github.com/ROCm/rocm-systems/pull/4769) — **Add initial strix halo changes for rocprofiler-systems CI** by [@jbonnell-amd](https://github.com/jbonnell-amd) · 48d old
- [rocm-systems#4620](https://github.com/ROCm/rocm-systems/pull/4620) — **Fix `update_env` handling of `REPLACE` mode** by [@dgaliffiAMD](https://github.com/dgaliffiAMD) · 54d old · labeled `Stale`

---

## Risk Signals

### CI Instability

**13/41 PRs have CI failures** (including drafts). Key patterns:

| PR | Notable Failing Checks |
|---|---|
| [#6388](https://github.com/ROCm/rocm-systems/pull/6388) | TheRock CI Summary; rocprofiler-systems test shard 1 |
| [#6349](https://github.com/ROCm/rocm-systems/pull/6349) | TheRock CI Summary; rocprofiler-compute shard 2 |
| [#6288](https://github.com/ROCm/rocm-systems/pull/6288) | ubuntu-jammy (g++, 7.2) |
| [#5995](https://github.com/ROCm/rocm-systems/pull/5995) | 32+ checks: full matrix of debian, ubuntu-noble, ubuntu-jammy, rhel, sanitizers |
| [#5992](https://github.com/ROCm/rocm-systems/pull/5992) | rhel g++ 8.10 (all ROCm versions 6.3–7.2) |
| [#5819](https://github.com/ROCm/rocm-systems/pull/5819) | TheRock CI Summary; rocprofiler-compute shard 1 |
| [#5808](https://github.com/ROCm/rocm-systems/pull/5808) | TheRock CI Summary; Linux Build Linux Packages |
| [#5777](https://github.com/ROCm/rocm-systems/pull/5777) | ubuntu-noble (g++, Release, 7.0) |
| [#5690](https://github.com/ROCm/rocm-systems/pull/5690) | TheRock CI Summary; Linux + Windows Build Linux/Windows Packages |
| [#5351](https://github.com/ROCm/rocm-systems/pull/5351) | ubuntu-noble-sanitizers (asan); TheRock CI Summary; rocprofiler-compute shard 2 |
| [#5267](https://github.com/ROCm/rocm-systems/pull/5267) | Code Coverage · mi325 · ubuntu-22.04 |
| [#4080](https://github.com/ROCm/rocm-systems/pull/4080) | TheRock CI Summary; rocprofiler-systems test shard 1 |

> ⚠️ **Note:** Several PRs share the same failing checks (TheRock CI Summary, rocprofiler-compute/systems test shards). This may indicate a shared upstream test flakiness or environment issue rather than per-PR bugs — worth investigating whether these failures are correlated.

---

### Test Gap Summary

**23 PRs include test updates. 9 PRs are missing tests.**

| PR | Changed Source Files | Risk | Recommended Test Level | Notes |
|---|---|---|---|---|
| [#6388](https://github.com/ROCm/rocm-systems/pull/6388) | `pthread_mutex_gotcha.cpp`, `pthread_mutex_gotcha.hpp` | **High** — Bug fix in gotcha/threading layer | **Integration** | This is a concurrency bug fix; threading edge cases should have regression tests. Look for existing gotcha tests to extend. |
| [#5995](https://github.com/ROCm/rocm-systems/pull/5995) | `buffer_storage.cpp`, `buffer_storage.hpp` | **Medium** — Replaces flush thread implementation | **Unit** | Replacing a hand-rolled thread with `std::jthread` is non-trivial; flush behavior under termination should be tested. |
| [#5690](https://github.com/ROCm/rocm-systems/pull/5690) | `hip_code_object.cpp/hpp`, `hip_context.cpp`, `hip_capture.cpp/h`, `hip_capture_generated.cpp`, `hip_capture_writer.cpp/h`, `hrr_api_args.h`, `gen_hrr_api_args.py` (20 files total) | **High** — Major new feature (capture/playback) | **Integration + System** | 20 source files with no tests is a significant gap for a complex capture/playback feature. Strongly recommend adding tests before merge. |
| [#5349](https://github.com/ROCm/rocm-systems/pull/5349) | None (docs/config only) | **Low** | N/A | Doc-only change; no test needed. |
| [#6297](https://github.com/ROCm/rocm-systems/pull/6297) *(draft)* | `impl.cpp`, `rocprof-sys-causal.cpp`, `rocprof-sys-causal.hpp` | **Medium** — Runtime state refactor | **Unit** | Centralizing runtime state can introduce subtle initialization bugs. |
| [#6295](https://github.com/ROCm/rocm-systems/pull/6295) *(draft)* | `Packages.cmake`, `markers.h` | **Low** — Submodule + build fix | **Unit** | Low risk; `markers.h` change may warrant a smoke test. |
| [#6116](https://github.com/ROCm/rocm-systems/pull/6116) *(draft)* | `module_function.cpp/hpp`, `rocprof-sys-instrument.cpp/hpp`, `dl.cpp/hpp`, `main.c`, `api.cpp/hpp`, `MacroUtilities.cmake` (13 files) | **High** — New public API (`rocprofsys_push_trace_with_args`) | **Integration** | New public API with no tests is a significant gap. Should have at minimum a round-trip API test. |
| [#6009](https://github.com/ROCm/rocm-systems/pull/6009) *(draft)* | `BuildSettings.cmake`, `DyninstTBB.cmake` | **Low** — Build system change | N/A | CMake-only; CI serves as functional test. |
| [#5762](https://github.com/ROCm/rocm-systems/pull/5762) *(draft)* | `symbol.cpp` | **Low** — CI workflow addition | **Unit** | Single source file change; consider extending any existing `symbol` unit tests. |

> 🚨 **Highest priority test gaps:** [#5690](https://github.com/ROCm/rocm-systems/pull/5690) (20 source files, new capture/playback subsystem), [#6116](https://github.com/ROCm/rocm-systems/pull/6116) (new public API), and [#6388](https://github.com/ROCm/rocm-systems/pull/6388) (threading bug fix).

---

## Stale PRs

### Long-stale (14+ days no activity)

These PRs have not been updated in 2+ weeks and need active follow-up:

- [rocm-systems#5819](https://github.com/ROCm/rocm-systems/pull/5819) — **align per-link PMC + track names** by [@adjordje-amd](https://github.com/adjordje-amd) · 14d since update · 19d old · Approved, failing one CI test shard — **recommend: author investigate rocprofiler-compute shard 1 failure and ping reviewer.**
- [rocm-systems#5351](https://github.com/ROCm/rocm-systems/pull/5351) — **[runtime-instrument] Introduce 3 CLI options** by [@kcossett-amd](https://github.com/kcossett-amd) · 18d since update · 32d old · **Recommend: author address CI failures (asan, compute shard) and request re-review.**
- [rocm-systems#5995](https://github.com/ROCm/rocm-systems/pull/5995) — **replace flush thread with std::jthread** by [@adjordje-amd](https://github.com/adjordje-amd) · 13d since update · 13d old · Catastrophic CI failure (whole matrix) — **recommend: likely needs rebase; author should investigate root cause.**
- [rocm-systems#4080](https://github.com/ROCm/rocm-systems/pull/4080) — **C++20 support** by [@adjordje-amd](https://github.com/adjordje-amd) · 5d since update · **70d old** — Base of the entire C++20 chain. Persistent CI failure. **Recommend: this is the highest-age PR in the queue and blocks the entire C++20 stack; escalate for review.**

### Going stale (3–13 days no activity, non-draft)

- [rocm-systems#6237](https://github.com/ROCm/rocm-systems/pull/6237) — **Improve Generated Output summary** by [@marantic-amd](https://github.com/marantic-amd) · 4d since update · CI passing, review pending — ping [@jrmadsen](https://github.com/jrmadsen).
- [rocm-systems#6236](https://github.com/ROCm/rocm-systems/pull/6236) — **refactor(env_vars): use env_vars:: constants** by [@marantic-amd](https://github.com/marantic-amd) · 6d since update · CI passing, no review decision — ping reviewer.
- [rocm-systems#6203](https://github.com/ROCm/rocm-systems/pull/6203) — **Replace get_env and set_env from timemory** by [@mradosav-amd](https://github.com/mradosav-amd) · 5d since update · CI passing, approved by `marantic-amd` — **ready to merge pending `jrmadsen` review**.
- [rocm-systems#5098](https://github.com/ROCm/rocm-systems/pull/5098) — **Fix output index calculation in transpose_a kernel** by [@jared-mcd-han](https://github.com/jared-mcd-han) · 6d since update · 39d old · External contribution, CI passing, no review — **recommend: assign a reviewer promptly; external contributors should not wait this long.**
- [rocm-systems#5349](https://github.com/ROCm/rocm-systems/pull/5349) — **[rocdecode, rocjpeg] removed install section** by [@spolifroni-amd](https://github.com/spolifroni-amd) · 13d since update · 32d old · Changes requested by `dgaliffiAMD` — author needs to respond.
- [rocm-systems#5992](https://github.com/ROCm/rocm-systems/pull/5992) — **replace SFINAE with C++20 concepts** by [@adjordje-amd](https://github.com/adjordje-amd) · 9d since update · RHEL 8.10 CI failures across all ROCm versions — may indicate a compiler compatibility issue with RHEL's g++ version.

---

## LLM Observations

- **C++20 migration chain is a coordination risk.** Four PRs form an explicit dependency stack: [#4080](https://github.com/ROCm/rocm-systems/pull/4080) → [#5992](https://github.com/ROCm/rocm-systems/pull/5992) → [#5995](https://github.com/ROCm/rocm-systems/pull/5995), plus [#6006](https://github.com/ROCm/rocm-systems/pull/6006) (exception hierarchy, also by `adjordje-amd`). All target non-`develop` branches or each other. If the base PR (#4080, 70 days old) doesn't land soon, the entire stack will continue to accumulate drift. A focused review session on this chain is recommended.

- **`rocpd`/database layer has multiple concurrent PRs that may conflict.** [#5808](https://github.com/ROCm/rocm-systems/pull/5808) (replace SQLite3/rocpd with rocprofiler-hub), [#5267](https://github.com/ROCm/rocm-systems/pull/5267) (rocpd versioning API update), and [#5819](https://github.com/ROCm/rocm-systems/pull/5819) (per-link PMC, touches `rocpd_processor.cpp`) all modify overlapping areas of the database/rocpd layer. These should be reviewed in dependency order to avoid merge conflicts; [#5267](https://github.com/ROCm/rocm-systems/pull/5267) and [#5808](https://github.com/ROCm/rocm-systems/pull/5808) in particular may be touching the same files.

- **Perfetto/output processing is a hotspot with several concurrent drafts.** [#6243](https://github.com/ROCm/rocm-systems/pull/6243) (parallel Perfetto processing), [#6240](https://github.com/ROCm/rocm-systems/pull/6240) (unify control logic), [#6237](https://github.com/ROCm/rocm-systems/pull/6237) (output summary improvements), and [#6387](https://github.com/ROCm/rocm-systems/pull/6387) (UMP bandwidth metric rename) all touch the Perfetto processing layer. At least three of these are still drafts, but they risk conflicting; the team should coordinate sequencing.

- **`jrmadsen` is the sole requested reviewer on the vast majority of open PRs.** Across needs-attention and stale PRs, `jrmadsen` appears as the primary (and often only) requested reviewer on at least 10 PRs. This is a clear review bottleneck. Consider distributing review load or identifying additional qualified reviewers for subsystems like environment variables, Perfetto processing, and test infrastructure.

- **Positive signal: test coverage is generally good for non-trivial PRs.** Despite 9 PRs missing tests, 23 PRs do include test updates, and several large PRs — [#6237](https://github.com/ROCm/rocm-systems/pull/6237) (15 test files), [#6243](https://github.com/ROCm/rocm-systems/pull/6243) (16 test files), [#5992](https://github.com/ROCm/rocm-systems/pull/5992) — show strong test discipline. The team appears to be investing in test infrastructure, which is encouraging.

---

## Appendix

### Raw Stats

| Metric | Count |
|---|---|
| Total open PRs | 41 |
| Needs attention (failing CI or changes requested) | 14 |
| Healthy / In review | 2 |
| In progress (CI running, non-draft) | 0 |
| Stale (3+ days no activity, non-draft) | 4 |
| Drafts | 21 |
| WIP not draft | 0 |
| PRs with test updates | 23 |
| PRs missing tests (source changed, no tests) | 9 |

### Quick Links

- [All open PRs](https://github.com/ROCm/rocm-systems/pulls?q=is%3Apr+is%3Aopen+label%3A%22project%3A+rocprofiler-systems%22)
- [Failing CI](https://