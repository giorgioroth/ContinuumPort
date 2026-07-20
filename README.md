# ContinuumPort

Your system failed. What does that leave intact?

Most persistent systems cannot guarantee structural integrity under adversarial or partial-failure conditions. ContinuumPort enforces it explicitly — within a declared execution boundary.

---

## The problem

In persistent systems, execution fails mid-sequence. When it does, the state may reflect a committed prefix — neither the initial state nor the intended result. This is not an edge case. It is a structural property of unconstrained execution.

Reactive recovery — rollback, retry, or compensation — addresses failures after execution has begun. For non-invertible transitions or externally visible side effects, restoration cannot be guaranteed.

ContinuumPort addresses this at the execution layer: invalid sequences are excluded from the admissible execution space before any state is committed.

---

## Quickstart

```bash
git clone https://github.com/giorgioroth/ContinuumPort
cd ContinuumPort/quickstart
python run.py                   # I4 — no partial state escape
python run_determinism.py       # I5 — deterministic outcome
python run_address_invariant.py # I2 — domain integrity
```

No dependencies. Runs in seconds.

---

## What the demos show

**I4 — Partial state escape**

```
[FaultyAdapter]
Action 1 succeeds. Action 2 fails.
State after: {'account': 'active', 'balance': 100, 'processed': True}
✗ VIOLATED — partial state escaped

[ContinuumPort]
State after: {'account': 'active', 'balance': 100}
✓ ENFORCED — internal state restored to pre-execution snapshot
```

**I5 — Determinism**

```
[FaultyAdapter]   Run 1: {'x': 2}   Run 2: {'x': 1}   ✗ VIOLATED
[ContinuumPort]   Run 1: {'x': 2}   Run 2: {'x': 2}   ✓ ENFORCED
```

**Composition attack**

```
Same engine. Same actions. Different geometry.
Incomplete geometry → authorized=True  → budget=-50
Complete geometry   → authorized=False → BLOCKED
```

The engine does not decide what is safe. The declared geometry does.

**Domain integrity**

The system does not reject the action. The action does not exist.

Invalid input is structurally inadmissible — it never enters the execution domain.

---

## Invariants and their enforcement basis

The five invariants do not have the same epistemic status. The distinction matters.

| Property | Enforcement basis |
|---|---|
| I1 — No unauthorized execution | Formally demonstrated: authority gate is a necessary condition in GF(S); no admissible sequence bypasses it. Full proof: [Trajectory Integrity in Persistent AI Systems](https://doi.org/10.17605/OSF.IO/B8SGR), §3–§5 |
| I2 — No out-of-domain execution | Formally demonstrated: domain boundary is encoded in the geometry; out-of-domain input has no image in the execution space. Full proof: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), §3–§5 |
| I3 — No invalid state transition | Formally demonstrated: geometry constraints are enforced before commitment; violating transitions are inadmissible by construction. Full proof: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), Theorem 5.1 |
| I4 — No partial state escape | Formally demonstrated: atomic commit/rollback is enforced at the execution layer; no intermediate state is observable. Full proof: [same source](https://doi.org/10.17605/OSF.IO/B8SGR), Theorem 5.1, Corollary 5.4 |
| I5 — Deterministic outcome | Empirically validated: 1,922 automated tests (adversarial, invariant, authority, provenance, concurrency, and executable-principle validation), 0 failures; audit replay mechanism assumed by construction (no test independently verifies replay determinism across all adapter implementations) |

Violations of I1–I4 are structurally inadmissible: they do not reach execution. I5 is continuously validated through adversarial testing; the audit replay assumption is documented in the invariant table above.

This is not a convention. It is enforcement — **within the declared execution boundary, by a compliant adapter enforcing the compliance interface below.** An adapter that either fails to implement that interface, or bypasses it, is outside this guarantee entirely; enforcement applies to compliant adapters, not to arbitrary code. The FaultyAdapter demos above show what enforcement looks like when the boundary condition is not met.

---

## Tests

**1,922 automated tests across adversarial, invariant, authority, provenance, concurrency, and executable-principle validation. 0 failures.**

The self-contained quickstart demos above run on a clean checkout of this repository with no dependencies. The full validation suite (1,922 tests) runs against the Regen Engine kernel, which is proprietary (Beta license) and is not included in this public repository. Evaluation access to the suite is available on request (access@continuumport.com).

<img width="2946" height="1634" alt="image" src="https://github.com/user-attachments/assets/8d61a01a-0b25-4324-9725-881b54ef8d14" />


The run shown above was produced in the author's Windows environment.

Paper 4 (*Adversarial Execution Governance*) reports on the cumulative corpus as submitted, once Batches 1–12 were complete: 1806 tests. Batch 13 (24 concurrent-pressure tests, C1–C5) and additional tests added since — including coverage from Part III of *AI Architectural Thinking* — bring the current suite total to 1922. These later additions are not yet reflected in Paper 4's reported figure; the current suite total is the authoritative, continuously-verified count.

The adversarial corpus was developed across 13 batches with the assistance of Claude (Anthropic), ChatGPT (OpenAI), and Gemini (Google) — in that order of contribution. The validation suite is the primary empirical research artifact of this project.

The validation suite includes:

- replay attacks
- state drift injection
- geometry swap attacks
- capability rebinding
- TOCTOU patterns
- composition attacks
- hash canonicalization failures
- authority desynchronization
- rollback desynchronization
- cross-cycle state trap scenarios
- malformed capsule reconstruction
- deterministic integrity verification
- hostile observation (H1–H5)
- commitment graph attacks (G1–G6)
- causal opacity (O1–O5)
- provenance enforcement (P1–P5)
- authority laundering (L1–L6)
- admissibility erosion (E1–E5)
- concurrent adversarial pressure (C1–C5)

Under enforcement, these attack patterns are blocked by the declared geometry or fail the admissibility check. Finite exhaustion of a test corpus demonstrates coverage of enumerated patterns — it does not establish structural impossibility for categories that extend beyond the formal model (see Scope and limits).

---

## Scope and limits

ContinuumPort enforces correctness of execution under declared constraints.

It does not guarantee:

- Correctness of intent
- Correctness of declared constraints
- External side effects beyond the execution boundary

Undeclared risks are not blocked.

These limits are explicit and documented in [`EXECUTION_MODEL_LIMITS.md`](https://github.com/giorgioroth/ContinuumPort/blob/848566f15c94f6f092a1a242316f4d7bd5329d2a/docs/EXECUTION_MODEL_LIMITS.md#L4)

---

## Architecture

[Architecture diagram](https://giorgioroth.github.io/ContinuumPort/)

```
Actions
   ↓
Authority check
   ↓
Geometry enforcement
   ↓
Execution (atomic)
   ↓
Commit / Rollback
```

ContinuumPort defines the constrained execution model. Regen Engine enforces it.

Formal model: GF(S) — the maximal prefix-closed, failure-free execution space. Only sequences inside GF(S) are admissible for execution. Corrupted states are structurally inadmissible, not merely detected after the fact.

---

## Why "Execution-Governance Kernel"

**This guarantee holds for any adapter implementing the compliance interface below correctly ("compliant"). An adapter that does not implement it, or that bypasses it, is outside this guarantee — there is no enforcement over code that never enters through the kernel.** Within that boundary, the Regen Engine functions as an execution-governance kernel — a non-bypassable enforcement layer through which all state-affecting transitions must pass.

This is not middleware. It is not a validator that can be disabled. It is not a hook that can be skipped.

The distinction matters:

- **Non-bypassable execution governance** — no state-affecting transition can occur outside the enforcement layer, for a compliant adapter. There is no alternative path to execution for a compliant adapter.
- **Centralized admissibility enforcement** — all transitions are evaluated against the declared geometry before commitment. Authority, invariants, and epistemic state are verified at a single, mandatory point.
- **Invariant-preserving state transitions** — the system does not detect violations after the fact. Transitions that would violate declared invariants are structurally inadmissible. They do not execute.
- **Fail-closed execution semantics** — under uncertainty, divergence, or insufficient data, the system halts. It does not degrade gracefully into permissive behavior. It stops.

Loggers can be bypassed. Validators can be disabled. Middleware can be removed.

A compliant adapter cannot route around an execution-governance kernel. Every transition from a compliant adapter passes through it, or the transition does not occur.

This is the architectural property that distinguishes the Regen Engine from advisory systems, monitoring layers, or behavioral guardrails — and why "Execution-Governance Kernel" is the correct term for what it does, within the declared boundary.

---

## Compliance interface

```python
class RegenAdapter(ABC):
    def reset(self, state: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def execute(self, actions: list[dict]) -> ExecutionResult: ...
    def simulate(self, state: dict, action: dict) -> dict: ...
```

See EXECUTION_MODEL_LIMITS.md §2.9 for the trust assumptions this contract relies on.

---

## Repository structure

This public repository contains the specification, the self-contained demos, and the published books and essays:

```
quickstart/       — self-contained runnable demos (no dependencies)
docs/             — formal specification, scope boundaries, invariant-test documentation
cp-core/          — CP-Core normative schema and handoff specification
regen-engine/     — engine demonstrations (attack, side-effects)
```

The Regen Engine kernel and the full compliance/validation suite are proprietary (Beta license) and are not included in this public repository. Evaluation access is available on request: access@continuumport.com

---

[![CP-Core](https://img.shields.io/badge/CP--Core-Apache%202.0-green)](LICENSE) 
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/3.%20LICENSE_REGEN.md) 
[![Status](https://img.shields.io/badge/status-normative-blue)](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md) 


---

[![PRINCIPLES](https://img.shields.io/badge/PRINCIPLES%20-orange)](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/PRINCIPLES.md)


## Further reading

- [AI Architectural Thinking](https://github.com/giorgioroth/ContinuumPort/blob/main/AI_Architectural_Thinking.md) — the conceptual framework (62 chapters)
- [EXECUTION_MODEL_LIMITS.md](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md) — explicit scope boundaries
- [Blog](https://gi0rgioroth.blogspot.com/) — context and philosophy
- [continuumport.com](https://continuumport.com/)

---

*Gh. Rotaru (Giorgio Roth) — Independent researcher, 2026*

contact: access@continuumport.com
