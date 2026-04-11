# Attack Classification

Maps `tests/test_vulnerability_suite.py` to the classification schema in `scope_and_limits.md`.

**Schema:** SAFE — MODEL LIMIT — CONTROL PLANE

---

## V1 — Capsule Replay Flood

**Vector:** Same valid capsule submitted N times — sequentially and under concurrent load.

**Tests:** 100 sequential replays · 1000 replays on same env · 50 threads × 20 concurrent · 500 via control plane · authority check post-flood

| Result | Class | Reason |
|---|---|---|
| Identical state on every replay | SAFE | `reconstruct()` is stateless — env receives only `C.S` |
| No cumulative effects | SAFE | No shared mutable state in capsule or validator |
| Concurrent safety | SAFE | Each thread operates on independent env |
| Authority holds after flood | SAFE | Enforcement is per-call, not per-session |
| Replay itself not prevented | MODEL LIMIT | Prevention is a control plane responsibility |

---

## V2 — Geometry Swap Attack

**Vector:** Capsule validated under G1 reconstructed under G2.

**Tests:** Inadmissible action under G2 · `next_action=None` · tampered capsule with permissive geometry · capsule dict inspection

| Result | Class | Reason |
|---|---|---|
| Inadmissible action blocked by G2 | SAFE | `CapsuleValidator` checks against provided geometry |
| `None` action accepts any geometry | SAFE | No action → no admissibility check |
| Integrity check is geometry-independent | SAFE | `state_hash` depends on state, not geometry |
| Geometry not embedded in capsule | MODEL LIMIT | Geometry is a session-level concern |

---

## V3 — Authority Enforcement Under Load

**Vector:** `resume_from_capsule()` called with wrong authority under concurrent load.

**Tests:** 100 threads × 10 invalid + 10 valid · 1000 calls with `None` context · 50 threads under `strict=True`

| Result | Class | Reason |
|---|---|---|
| Zero bypasses under concurrent load | SAFE | Enforcement is synchronous, per-call |
| `None` context blocked 1000/1000 | SAFE | Fail-closed: bound capsule requires context |
| `strict=True` holds under concurrency | SAFE | Flag evaluated before any env access |

---

## V4 — State Drift After Reconstruct

**Vector:** External state mutation attempted after valid reconstruction.

**Tests:** `env.set()` post-reconstruct · snapshot comparison · `assert_no_out_of_band_mutation()` · sequential reconstruction bleed

| Result | Class | Reason |
|---|---|---|
| Gate blocks mutation after reconstruct | SAFE | Gate closes after `_exit_system_context()` |
| No residue from prior env state | SAFE | `env.restore()` replaces state completely |
| OOB mutation detectable | SAFE | Detection via snapshot comparison |
| No bleed between sequential reconstructs | SAFE | Each reconstruct is a full state replacement |

Note: `assert_no_out_of_band_mutation()` is detection, not prevention. Prevention is architectural.

---

## V5 — Cross-Cycle State Trap

**Vector:** `lock=True` set in cycle 1, crash before unlock, capsule captured, cycle 2 reconstructs.

**Tests:** Lock survives round-trip · no auto-clear · CP inspection before reconstruct · no field invention · full two-cycle scenario

| Result | Class | Reason |
|---|---|---|
| Lock survives round-trip | MODEL LIMIT | Engine restores `C.S` faithfully — correct behavior |
| No auto-clear | MODEL LIMIT | Auto-recovery explicitly rejected by design |
| CP can inspect before reconstruct | CONTROL PLANE | `capsule.state` readable before calling `reconstruct()` |
| No field invention | SAFE | `env.restore()` sets exactly `C.S` — no defaults injected |

Correct pattern: inspect `capsule.state` → detect → decide → act.  
Not: reconstruct → detect → too late.

---

## Summary

| Attack | Tests | SAFE | MODEL LIMIT | CONTROL PLANE |
|---|---|---|---|---|
| V1 Replay Flood | 5 | 4 | 1 | — |
| V2 Geometry Swap | 4 | 3 | 1 | — |
| V3 Authority Under Load | 3 | 3 | — | — |
| V4 State Drift | 4 | 4 | — | — |
| V5 Cross-Cycle Trap | 5 | 1 | 2 | 1 |
| **Total** | **21** | **15** | **4** | **1** |

15 of 21 sub-tests are structurally prevented.  
4 define documented model limits.  
1 is correctly delegated to the control plane.

No model limit was discovered during testing — all were known and designed.
