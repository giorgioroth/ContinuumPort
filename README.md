# ContinuumPort

**Your system failed. What guarantees that nothing changed?**

Most persistent systems cannot guarantee that structurally under adversarial or partial-failure conditions. ContinuumPort enforces it explicitly.

---

## The problem

In persistent systems, execution fails mid-sequence. When it does, the state may reflect a committed prefix — neither the initial state nor the intended result. This is not an edge case. It is a structural property of unconstrained execution.

Reactive recovery — rollback, retry, compensation — operates after commitment. In systems with non-invertible transitions or external side effects, restoration cannot be guaranteed.

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

## Structural guarantees

| Property | Guarantee |
|---|---|
| I1 — No unauthorized execution | Authority gate cannot be bypassed |
| I2 — No out-of-domain execution | Invalid input is structurally inadmissible |
| I3 — No invalid state transition | Geometry constraints enforced before commit |
| I4 — No partial state escape | Full rollback or full commit, nothing in between |
| I5 — Deterministic outcome | Same input + same state = same result, always |

If any invariant is violated, execution does not proceed.

This is not convention. It is enforcement.

---

## Tests

**1830 adversarial and invariant-validation tests. 0 failures. Full suite: 10.88s.**


<img width="2958" height="1418" alt="image" src="https://github.com/user-attachments/assets/c6d2be3e-fbe9-4019-9743-238d601a1d92" />


Verified cross-platform — Linux and Windows.

The adversarial corpus was developed across 13 batches with the assistance of Claude (Anthropic), ChatGPT (OpenAI), and Gemini (Google) — in that order of contribution. The test suite is the primary research artifact of this project.

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
- causal opacity and provenance enforcement (O1–O5)
- authority laundering (L1–L6)
- admissibility erosion (E1–E5)
- concurrent adversarial pressure (C1–C5)

Under enforcement, these outcomes are structurally unreachable.

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

Formal model: GF(S) — the maximal prefix-closed, failure-free execution space. Only sequences inside GF(S) are admissible for execution. Corrupted states are structurally unreachable, not detected.

---

## Why "Execution-Governance Kernel"

The Regen Engine functions as an execution-governance kernel — a non-bypassable enforcement layer through which all state-affecting transitions must pass.

This is not middleware. It is not a validator that can be disabled. It is not a hook that can be skipped.

The distinction matters:

- **Non-bypassable execution governance** — no state-affecting transition can occur outside the enforcement layer. There is no alternative path to execution.
- **Centralized admissibility enforcement** — all transitions are evaluated against the declared geometry before commitment. Authority, invariants, and epistemic state are verified at a single, mandatory point.
- **Invariant-preserving state transitions** — the system does not detect violations after the fact. Transitions that would violate declared invariants are structurally inadmissible. They do not execute.
- **Fail-closed execution semantics** — under uncertainty, divergence, or insufficient data, the system halts. It does not degrade gracefully into permissive behavior. It stops.

Loggers can be bypassed. Validators can be disabled. Middleware can be removed.

An execution-governance kernel cannot be routed around. Every transition passes through it, or the transition does not occur.

This is the architectural property that distinguishes the Regen Engine from advisory systems, monitoring layers, or behavioral guardrails — and why "Execution-Governance Kernel" is the correct term for what it does.

---

## Compliance interface

```python
class RegenAdapter(ABC):
    def reset(self, state: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def execute(self, actions: list[dict]) -> ExecutionResult: ...
    def simulate(self, state: dict, action: dict) -> dict: ...
```

---

## Repository structure

```
regen-engine/     — execution kernel (Python)
compliance/       — invariant validation suite
quickstart/       — runnable demos
docs/             — formal specification
```

---

[![CP-Core](https://img.shields.io/badge/CP--Core-Apache%202.0-green)](LICENSE)
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20LICENSE_REGEN.md)
[![Status](https://img.shields.io/badge/status-normative-blue)](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md)

---

## Further reading

- [Paper 1 — OSF](https://osf.io/b8sgr) · [DOI: 10.17605/OSF.IO/B8SGR](https://doi.org/10.17605/OSF.IO/B8SGR) — execution geometry and persistent state governance
- [Paper 2 — OSF](https://osf.io/m8ybn) · [DOI: 10.17605/OSF.IO/M8YBN](https://doi.org/10.17605/OSF.IO/M8YBN) — epistemic admissibility in persistent conversational systems
- [Paper 3 — OSF](https://osf.io/qwf8a) · [DOI: 10.17605/OSF.IO/QWF8A](https://doi.org/10.17605/OSF.IO/QWF8A) — execution authority revocation under epistemic divergence
- [Paper 4 — OSF](https://osf.io/w7q9n) · [DOI: 10.17605/OSF.IO/W7Q9N](https://doi.org/10.17605/OSF.IO/W7Q9N) — adversarial execution governance
- [AI Architectural Thinking](https://github.com/giorgioroth/ContinuumPort/blob/main/AI_Architectural_Thinking.md) — the conceptual framework (58 chapters)
- [EXECUTION_MODEL_LIMITS.md](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/EXECUTION_MODEL_LIMITS.md) — explicit scope boundaries
- [Blog](https://gi0rgioroth.blogspot.com/) — context and philosophy
- [continuumport.com](https://continuumport.com/)

---

*Gh. Rotaru (Giorgio Roth) — Independent researcher, 2026*

contact: access@continuumport.com
