# ContinuumPort

**Your system failed.**
**What guarantees that nothing changed?**

Most persistent systems cannot guarantee that structurally. ContinuumPort enforces it explicitly.

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

```
The system does not reject the action.
The action does not exist.
```

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

**823 tests. 0 failures (reference implementation).** 

<img width="2646" height="1268" alt="image" src="https://github.com/user-attachments/assets/2cbf3281-a579-4922-9e47-540988dec554" /> 

---

Adversarial scenarios include: replay attacks, state drift injection, geometry swap attacks, capability rebinding, TOCTOU patterns, composition attacks, authority bypass under concurrent load.

Under enforcement, these outcomes are structurally unreachable.

---

## Scope and limits

ContinuumPort enforces correctness of execution under declared constraints.

It does not guarantee:
- Correctness of intent
- Correctness of declared constraints
- External side effects beyond the execution boundary

**Undeclared risks are not blocked.**

These limits are explicit and documented in `EXECUTION_MODEL_LIMITS.md`.

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

Formal model: `GF(S)` — the maximal prefix-closed, failure-free execution space. Only sequences inside `GF(S)` are admissible for execution. Corrupted states are structurally unreachable, not detected.

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

- [Formal paper](https://doi.org/10.17605/OSF.IO/B8SGR) — peer-accessible preprint (OSF)
- [EXECUTION_MODEL_LIMITS.md](EXECUTION_MODEL_LIMITS.md) — explicit scope boundaries
- [Blog](https://gi0rgioroth.blogspot.com) — context and philosophy

---

*Gh. Rotaru (Giorgio Roth) — Independent researcher, 2026* 

*contact: access@continuumport.com* 
