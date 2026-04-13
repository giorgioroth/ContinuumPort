
# ContinuumPort

**Execution is not implicit. It is enforced.**

Enforced execution continuity across models, sessions, and environments.

Most systems execute.

They cannot prove that execution is still valid.

They drift.
They partially apply.
They continue after divergence.

ContinuumPort makes these failure modes unexecutable.

It does not decide what is correct.
It makes invalid execution impossible.

---

## Run this

```bash
git clone https://github.com/giorgioroth/ContinuumPort
cd ContinuumPort

# runs in seconds

# Linux / macOS
REGEN_SIGNING_KEY=demo-key python -m compliance.demo

# Windows PowerShell
$env:REGEN_SIGNING_KEY="demo-key"; python -m compliance.demo
```

```
Regen Compliance — adversarial demo
============================================

[FAIL] FaultyAdapter_Partial
  → I4 — atomicity_on_failure

[FAIL] FaultyAdapter_NonDeterministic
  → I5 — determinism

[FAIL] FaultyAdapter_SnapshotAlias
  → I4 — snapshot_isolation

[FAIL] FaultyAdapter_D3
  → Ch.50 — d3_semantic_alignment

============================================
4/4 adapters FAILED (expected)
All adversarial cases detected.
Regen Engine: COMPLIANT — invariants enforced
```

Four plausible implementations. All fail.
Each violates a different invariant.
The tests are the arbiter.
Not the implementation.

---

## What this is

ContinuumPort is an execution validity protocol.

It enforces that state transitions cannot violate declared invariants,
even across models, sessions, and environments.

It ensures that state transitions remain enforceable across time,
even when execution spans multiple models, sessions, or environments.

It does not decide what is correct.
It ensures that invalid execution is rejected before commit.

---

## Core mechanism

ContinuumPort defines continuity of state.
Regen Engine enforces execution of that state.

Every transition must satisfy:

* **atomicity** — commit or rollback, nothing in between
* **determinism** — same input → same output
* **isolation** — no external mutation through snapshots
* **semantic alignment** — simulate(state, action) ≡ execute(state, action)

If any invariant is violated:

```
execution is rejected (no state transition occurs)
```

---

## Or: real-time enforcement

```bash
# Linux / macOS
REGEN_SIGNING_KEY=demo-key python -m compliance.mini_loop_demo

# Windows PowerShell
$env:REGEN_SIGNING_KEY="demo-key"; python -m compliance.mini_loop_demo
```

This shows execution being:

* accepted
* rejected (geometry violation)
* halted (epistemic divergence)

---

## Test your own system

If your system claims correctness:

```bash
python compliance/runner.py your_adapter.py
```

If it passes → it is Regen-Compliant.
If it fails → it violates a formal invariant.

**Partial compliance does not exist.**

---

## Invariants

| ID    | Guarantee                               |
| ----- | --------------------------------------- |
| I2    | Atomicity — no partial state            |
| I4    | Snapshot isolation                      |
| I5    | Determinism                             |
| Ch.50 | Semantic alignment (simulate ≡ execute) |

---

## What cannot happen

The following are structurally impossible under enforcement:

* partial execution
* non-deterministic outcomes
* state mutation outside the gate
* simulation/execution divergence
* invalid transitions committing

---

## Scope

ContinuumPort enforces correctness of execution under declared constraints.

It does not guarantee:

* correctness of intent
* correctness of declared constraints
* external side-effect consistency

Undeclared risks are not blocked.

---

## Structure

```
compliance/
  adapter/
    interface.py
    regen_adapter.py
    faulty_adapter.py
  tests/
    invariants.py
  runner.py
  demo.py
  mini_loop_demo.py

execution/
tests/
```

---

## Status

```
651 tests passed.
0 invariant violations.
```
---

<img width="2382" height="1256" alt="image" src="https://github.com/user-attachments/assets/829a1c5e-102d-48ee-a464-43dbf8ac95d1" />


---

## Final

The system does not assume.
It enforces.
Nothing outside the invariants executes.




---

[![CP-Core](https://img.shields.io/badge/CP--Core-Apache%202.0-green)](LICENSE)
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20LICENSE_REGEN.md)
[![Status](https://img.shields.io/badge/status-normative-blue)](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md)

---

## Links

- Blog: https://gi0rgioroth.blogspot.com/
- Site: https://continuumport.com/
- Repository: https://github.com/giorgioroth/ContinuumPort

---

## Author

Gh. Rotaru (Giorgio Roth)  
Independent researcher

[continuumport@gmail.com](mailto:continuumport@gmail.com)




