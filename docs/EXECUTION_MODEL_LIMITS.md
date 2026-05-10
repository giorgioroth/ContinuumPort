# EXECUTION_MODEL_LIMITS.md

**ContinuumPort / Regen Engine — Explicit Scope Boundaries**

This document defines what the ContinuumPort execution model guarantees, and what it explicitly does not guarantee. These limits are structural, not provisional.

---

## §1 — What the Model Guarantees

Within the execution boundary of a declared geometry G over a persistent execution system S = (States, Trans, δ, s₀):

- **No partial state corruption.** Any sequence producing a state change followed by execution failure is excluded from the admissible execution space. Corrupting executions are structurally absent, not detected.
- **Atomic commit semantics.** Atomicity is enforced at the level of the modeled execution state. No partially committed internal execution state becomes admissible.
- **Geometry enforcement.** Only sequences in G are executed. Sequences outside G are not rejected — they do not exist in the admissible execution space.
- **Deterministic outcome.** Under the deterministic execution model, identical admissible input from identical state produces identical modeled outcome.
- **Authority enforcement.** Execution is gated by declared authority. Unauthorized transitions are excluded from admissible execution.
- **TOCTOU detection.** State drift observable within the modeled execution boundary is detected before commit; execution is not committed under detected drift.

These guarantees hold under the formal model of Definition 2.1 (persistent execution system with non-total deterministic transitions). See the formal paper for proofs.

---

## §2 — What the Model Does Not Guarantee

### §2.1 — Semantic correctness of declared constraints

The model enforces declared constraints. It does not evaluate whether those constraints are correct, complete, or appropriate for the domain. A geometry that permits an incorrect sequence will enforce that permission.

> **Enforcement of declared constraints does not imply correctness of those constraints.**

### §2.2 — Goal alignment

The model does not reason about objectives, intentions, or outcomes. A system aligned to incorrect objectives will execute those objectives correctly under this model.

### §2.3 — External side effects

State transitions may invoke external systems (APIs, file writes, network calls). The model enforces internal state integrity. External effects beyond the execution boundary are not guaranteed to be reversible or consistent.

> Internal rollback is complete. External consistency requires additional mechanisms.

### §2.4 — Concurrent or distributed execution

The model assumes deterministic sequential transitions. Concurrent execution, distributed state, or non-deterministic environments are outside the scope of the formal model. The present formalization addresses the sequential deterministic case. Whether analogous necessity results extend to richer models remains future work.

### §2.5 — Probabilistic transitions

The model assumes deterministic δ. Probabilistic or stochastic transitions are not modeled.

### §2.6 — Byzantine environments

The model does not address adversarial participants, Byzantine failures, or environments where transitions may be manipulated by external actors outside the execution boundary.

### §2.7 — Semantic identity across cycles

Constraints declared in one execution cycle may drift in interpretation across regeneration. Constraint identity does not guarantee semantic identity across sessions. This is identified as a semantic governance gap (see Appendix B of the formal paper).

### §2.8 — Correctness of declared policies

The policy constraint layer (GP(S)) enforces declared policies. It does not verify that those policies are sound, complete, or consistent with each other.

---

## §3 — Undeclared Risks

> **Undeclared risks are not blocked.**

The geometry is the responsibility of the engineer who defines it. The engine enforces declared admissibility constraints at the execution layer. Risks not captured in the declared geometry are not addressed by the engine.

---

## §4 — Implementation Boundary

The formal guarantees apply to the execution model as specified. The reference implementation (Regen Engine) is a constructive witness for enforceability — it demonstrates that the constraints are implementable without requiring future-state evaluation or non-local execution knowledge.

The reference implementation is proprietary. The formal model and specification are public.

---

## §5 — External State Consistency

Referenced from [`AI_Architectural_Thinking.md Ch. 39.13`](https://github.com/giorgioroth/ContinuumPort/blob/main/AI_Architectural_Thinking.md#3913--explicit-non-guarantees)  

The model tracks internal state transitions. External state — state held by systems outside the execution boundary — is not guaranteed to be consistent with internal state after a rollback or execution failure.

The observation layer [Ch. 28](https://github.com/giorgioroth/ContinuumPort/blob/main/AI_Architectural_Thinking.md#chapter-28--observation-veto-and-recovery) can detect post-commit divergence between expected and observed external state, but cannot undo external effects that have already occurred.

---

## §6 — Summary Table

| Guarantee | Status |
|---|---|
| No partial state corruption (internal) | ✓ Guaranteed under model |
| Atomic commit or full rollback | ✓ Guaranteed under model |
| Geometry enforcement | ✓ Guaranteed under model |
| Deterministic outcome | ✓ Guaranteed under model |
| Authority enforcement | ✓ Guaranteed under model |
| TOCTOU detection | ✓ Guaranteed under model |
| Correctness of declared constraints | ✗ Not guaranteed |
| External side effect consistency | ✗ Not guaranteed |
| Goal alignment | ✗ Not guaranteed |
| Concurrent/distributed correctness | ✗ Outside model scope |
| Semantic identity across cycles | ✗ Future formalization |
| Byzantine resistance | ✗ Outside model scope |

---

## References

- [![Formal Paper](https://img.shields.io/badge/Formal%20Paper-OSF%20Preprint-blue)](https://doi.org/10.17605/OSF.IO/B8SGR)
- [![Repository](https://img.shields.io/badge/Repository-ContinuumPort-yellow)](https://github.com/giorgioroth/ContinuumPort)
- [![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20LICENSE_REGEN.md)

---

*Gh. Rotaru (Giorgio Roth) — Independent Researcher, 2026*
*access@continuumport.com*
