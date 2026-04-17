# ContinuumPort

**Execution is not implicit. It is enforced.**

Enforced execution continuity across models, sessions, and environments.

---

## The problem

Most systems execute. They cannot prove that execution remains valid after failure.

When a batch of actions partially succeeds and then fails, most systems leave
the partial result committed. There is no rollback. There is no structural detection.
The system continues from a state it cannot justify.

This is not a bug in any one implementation. It is the default behavior when
execution correctness is not structurally enforced.

ContinuumPort makes these failure modes unexecutable under enforcement.

---

## Run this

```bash
git clone https://github.com/giorgioroth/ContinuumPort
cd ContinuumPort/quickstart
python run.py              # I4 — atomicity
python run_determinism.py  # I5 — determinism
```

Runs in seconds. No dependencies.

**Output — I4 (partial state escape):**

```
============================================================
CONTINUUMPORT — EXECUTION INVARIANT DEMO
Invariant: I4 — No partial state escape
============================================================

Scenario: a batch of two actions is submitted.
Action 1 succeeds. Action 2 fails.
A compliant system must behave atomically: all or nothing.

  [FaultyAdapter    — no rollback]
  Committed   : False
  State before: {'account': 'active', 'balance': 100}
  State after : {'account': 'active', 'balance': 100, 'processed': True}
  ✗ I4 VIOLATED — partial state escaped (key 'processed' leaked into state)

  [ReferenceAdapter — atomic rollback]
  Committed   : False
  State before: {'account': 'active', 'balance': 100}
  State after : {'account': 'active', 'balance': 100}
  ✓ I4 ENFORCED — rollback complete, state identical to pre-execution
```

The faulty adapter *looks* correct — it reports `committed: False`. The state
disagrees. ContinuumPort detects this class of failure structurally.

Execution failure is not the problem.
Invalid state after failure is.

**Output — I5 (deterministic outcome):**

```
============================================================
CONTINUUMPORT — DETERMINISM DEMO
Invariant: I5 — Deterministic outcome
============================================================

Scenario: identical input is executed twice from identical state.
Declared order: set x=1, then set x=2.
Expected result: x=2 (order must be preserved deterministically).
A compliant system must produce identical, correct outputs.

  [FaultyAdapter    — order-dependent execution]
  Run 1 result: {'x': 2}  (expected: x=2)
  Run 2 result: {'x': 1}  (expected: x=2)
  ✗ I5 VIOLATED — same input, different outputs across executions

  [ReferenceAdapter — declared order enforced]
  Run 1 result: {'x': 2}  (expected: x=2)
  Run 2 result: {'x': 2}  (expected: x=2)
  ✓ I5 ENFORCED — identical correct output across executions
```

---

## What this is

ContinuumPort is an execution validity protocol.

It enforces that state transitions cannot violate declared invariants across
time, even when execution spans multiple models, sessions, or environments.

**ContinuumPort defines continuity of state.
Regen Engine enforces that continuity at execution time.**

Every transition must satisfy:

- **I1 — No unauthorized execution** — authority must be verified before execution
- **I2 — No out-of-domain execution** — only declared action types can execute
- **I3 — No invalid state transition** — preconditions must hold or execution is rejected
- **I4 — No partial state escape** — commit or rollback, never partial
- **I5 — Deterministic outcome** — same input produces same state

If any invariant is violated, execution is rejected. Not logged. Not warned. Rejected.

---

## Compliance interface

Any execution engine can be tested against these invariants
through a minimal interface:

```python
class RegenAdapter(ABC):
    def reset(self, state: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def execute(self, actions: list[dict]) -> ExecutionResult: ...
    def simulate(self, state: dict, action: dict) -> dict: ...
```

Run the full invariant suite against your implementation:

```python
from compliance.tests.invariants import run_invariant_tests

report = run_invariant_tests(your_adapter)
print(report.summary())
```

The tests are the arbiter. Not the implementation.

---

## What the tests cover

Full invariant suite (651 tests):

---

<img width="2382" height="1256" alt="image" src="https://github.com/user-attachments/assets/5203ac69-b41f-460f-aae5-8a18fcbfb8d6" />


---

0 invariant violations (reference implementation under adversarial conditions).

The test suite includes:

- **Adversarial scenarios** — implementations that appear correct but violate invariants
- **TOCTOU detection** — state drift between proposal and commit
- **Atomicity under failure** — partial effects never persist
- **Authority enforcement** — no execution path outside declared authority
- **Epistemic veto** — execution halts when state alignment is unknown
- **Vulnerability suite** — replay attacks, geometry swaps, authority flooding

```
tests/test_adversarial.py          — gate bypass, snapshot isolation, rollback
tests/test_adversarial_http.py     — HTTP capability invariants
tests/test_ch27_kernel.py          — authority + execution kernel
tests/test_ch28_epistemic.py       — epistemic veto and divergence detection
tests/test_vulnerability_suite.py  — V1–V7 structural attack scenarios
tests/test_ch39_properties.py      — formal properties (P1–P13)
```

---

## Verification model

Validation is invariant-based, not behavior-based.

The compliance layer tests observable behavior against declared invariants.
It does not inspect internals. An implementation passes when its outputs
satisfy the invariants under all test conditions — including adversarial ones.

---

## What cannot happen

Under enforcement, the following are structurally impossible:

- partial execution committed as valid state
- non-deterministic outcomes from identical input
- state mutation outside the declared authority model
- execution continuing after divergence
- invalid transitions bypassing the proposal gate

These are enforced properties of the execution model, not runtime checks.

---

## Scope and limits

ContinuumPort enforces correctness of execution under declared constraints.

It does not guarantee:

- correctness of intent
- correctness of declared constraints
- external side-effect consistency

Undeclared risks are not blocked.

---

## Compliance layer

The full compliance layer — adapter interface, adversarial suite, and
conformance tests — is included in this repository under `compliance/`.

The Regen Engine execution kernel is proprietary.

It is the only known implementation that satisfies all invariants
under adversarial testing.

Third-party implementations can be validated against the same invariants
by implementing `RegenAdapter`.

Access to the Regen Engine kernel: [access@continuumport.com](mailto:access@continuumport.com)

---

## Repository structure

```
compliance/
  adapter/
    interface.py          — RegenAdapter contract
    regen_adapter.py      — reference adapter (wraps Regen Engine)
    faulty_adapter.py     — intentionally faulty adapters (demo use)
  tests/
    invariants.py         — portable invariant test suite (I1–I5)
  runner.py               — compliance runner

quickstart/
  run.py                  — I4 demo, no dependencies
  run_determinism.py      — I5 demo, no dependencies

docs/
  specs/RFC-001-execution-contract.md
  specs/DEPENDENCY_RULES.md
```

---

[![CP-Core](https://img.shields.io/badge/CP--Core-Apache%202.0-green)](LICENSE)
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20LICENSE_REGEN.md)
[![Status](https://img.shields.io/badge/status-normative-blue)](https://github.com/giorgioroth/ContinuumPort/blob/main/1.%20PROJECT_STATUS.md)

---

## Links

- [Site](https://continuumport.com/)
- [Blog](https://gi0rgioroth.blogspot.com/)
- [Whitepaper](https://continuumport.com/wp-content/uploads/2026/04/ContinuumPort.pdf)

---

## Author

Gh. Rotaru (Giorgio Roth) — Independent researcher
