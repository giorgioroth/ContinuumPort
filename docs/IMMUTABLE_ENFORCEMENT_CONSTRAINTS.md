## Immutable Enforcement Constraints in Persistent Execution Systems

## 1. — Motivation

The execution model defined in the execution model establishes a layered architecture:
geometry enforcement, authority verification, policy resolution, and epistemic control.
Each layer is configurable within declared bounds.

However, certain classes of constraint cannot be treated as configurable policy.
They are not recommendations. They are not runtime preferences that operators may
override for operational convenience. They are **admissibility conditions over
execution itself** — conditions whose violation renders continuation structurally
inadmissible under the model.

This chapter defines those constraints, their formal basis, and their implementation
as non-overridable kernel invariants.

---

## 2. — Admissibility vs Policy

The execution model distinguishes two classes of constraint:

**Policy constraints** govern how the system responds to observed execution states.
They are declared, configurable, and subject to override within defined bounds.
A policy may specify that divergence triggers escalation rather than halt,
or that insufficient data permits a skip rather than a stop.

**Admissibility constraints** govern whether execution may continue at all.
They are not declared by operators. They are derived from the structural
requirements of the execution model itself. No policy override can satisfy
an admissibility constraint that the model has determined to be violated.

Formally: let `V` be the current verdict (confirmed, diverged, unknown,
insufficient\_data) and `O` be the proposed outcome. An admissibility constraint
`I` is a predicate `I(V, C, O) → {admissible, inadmissible}` where `C` is the
execution context. If `I(V, C, O) = inadmissible`, no policy can produce `O`
from `V` under `C`.

---

## 3. — Divergence and Halt Semantics

Consider a persistent execution system operating under a declared geometry `G`.

If observed execution diverges from the admissible transition space defined by `G`,
continuation may no longer be considered valid execution under the model.

Two behaviors are structurally possible:

1. Continue execution under unresolved divergence.
2. Halt execution and preserve state integrity.

Under the fail-closed model, unresolved divergence contracts the admissible execution space to HALT or ESCALATE outcomes. The second behavior preserves admissibility.
This produces the fundamental enforcement rule:

```
unresolved divergence  ⟹  HALT
```

rather than:

```
unresolved divergence  ⟹  best-effort continuation
```

This is not a policy preference. It is a structural consequence of the model:
a system that continues under confirmed divergence is no longer executing within
its declared geometry. It has exited the admissible execution space.

---

## 4. — The Three Kernel Invariants

The following invariants are non-overridable. They are enforced structurally
at the `PolicyConstraints` layer (PolicyConstraints), both at policy construction time
(static validation) and at runtime (dynamic enforcement).

### I1 — No Continuation Under Confirmed Divergence

```
V = DIVERGED  ⟹  O ∈ {HALT, ESCALATE}
```

If the observation layer (Observation layer) has confirmed that the system state has diverged
from expected state, execution may not continue. The only admissible outcomes are
halt or escalation to external authority.

**Rationale:** A diverged system is one whose internal state no longer reflects a
valid execution history under the declared geometry. Continuation from such a state
would produce transitions over a non-admissible execution state. The model does not permit this.

**Implementation:** ``PolicyConstraints.enforce()`` and `_check_i1()` at construction.
Any policy resolving `DIVERGED → CONTINUE` or `DIVERGED → SKIP` raises `PolicyError`
before the first execution cycle.

### I2 — Uncertainty Does Not Expand Authority Under Strict Mode

```
V = UNKNOWN  ∧  mode = strict  ∧  retry_count > 0  ⟹  O ≠ CONTINUE
```

Under strict execution mode with active retries, an unknown verdict indicates that
the system has already encountered uncertainty and is attempting recovery.
Permitting `CONTINUE` under these conditions would allow execution to proceed
on an unresolved foundation, expanding authority under uncertainty.

**Rationale:** Uncertainty contracts the admissible execution space. It does not
expand it. This is the **authority contraction principle**: as uncertainty
increases, the set of admissible outcomes shrinks. A system that cannot establish admissibility must reduce, not increase,
the set of permitted transitions.

**Implementation:** ``PolicyConstraints.enforce()`` — targeted at the `unknown`
verdict under strict mode with retry, the case not already covered by I1 or I3.

### I3 — No Continuation Under Insufficient Observation Data

```
V = INSUFFICIENT_DATA  ⟹  O ≠ CONTINUE
```

If the observation layer cannot establish whether the current state is valid —
because the data required for reconciliation is unavailable — execution may not
continue. The system must halt or skip until sufficient observation data is available.

**Rationale:** Continuation without observation data is execution without a known
foundation. The model requires that execution state be reconcilable against observed
state before continuation is permitted.

**Implementation:** ``PolicyConstraints.enforce()`` and `_check_i3()` at construction.

---

## 5. — Fail-Closed Enforcement

Under fail-closed semantics, the relationship between uncertainty and authority
is inverted relative to best-effort systems:

| Condition | Best-effort system | Fail-closed system |
|---|---|---|
| Confirmed state | Continue | Continue |
| Unknown state | Continue with caution | Halt or skip |
| Diverged state | Attempt recovery | Halt or escalate |
| Insufficient data | Continue if possible | Halt or skip |

The fail-closed model produces a monotonic relationship between uncertainty and
admissibility: as uncertainty increases, the set of admissible outcomes shrinks.
This is not a conservative design choice — it is the structural requirement of
a system whose execution space is formally bounded.

Formally: let `U(V)` be the uncertainty level of verdict `V`, and `A(V)` be the
set of admissible outcomes under `V`. The fail-closed invariant requires:

```
U(V₁) ≥ U(V₂)  ⟹  A(V₁) ⊆ A(V₂)
```

Uncertainty monotonically contracts the admissible execution space.

---

## 6. — Structural Enforcement, Not Semantic Judgment

The kernel invariants are enforced structurally. The system does not:

- infer intent correctness,
- evaluate ethical validity,
- assess semantic meaning of transitions,
- determine whether a goal is appropriate.

It determines only whether continuation remains admissible under the declared
execution model. This is a binary determination: admissible or inadmissible.

This separation is intentional and non-negotiable. The admissibility layer
(geometry, authority, kernel invariants) governs the structure of execution.
The semantic layer (goals, policies, alignment) governs the content of execution.
Neither layer may override the other's domain.

---

## 7. — Scope and Non-Guarantees

The kernel invariants defined in this chapter do not solve:

- **Ethical alignment** — the invariants enforce structural admissibility,
  not correctness of declared geometry or policy.
- **Semantic correctness** — a system whose geometry permits incorrect sequences
  will enforce those sequences correctly.
- **Value specification** — the model does not evaluate whether declared
  constraints reflect appropriate values.
- **Intent verification** — the system does not reason about the intentions
  of operators, signers, or external systems.

The contribution of this chapter is narrower and more precise: it defines the
structural conditions under which persistent execution is prevented from continuing
under unresolved divergence or invalid state evolution. These conditions are
necessary, not sufficient, for correct system behavior.

---

## 8. — Implementation Reference

### Static validation (construction-time)

```python
PolicyConstraints.validate(policy)
## Called in CycleRecorder.__init__()
## Raises PolicyError if I1 or I3 are violated before first use
```

### Dynamic enforcement (runtime)

```python
PolicyConstraints.enforce(verdict, context, outcome)
## Called in CycleRecorder.record() after policy.resolve()
## Raises PolicyError if I1, I2, or I3 are violated at runtime
```

### Test witness

Test suite `the HALT Invariant test suite` (19 tests) provides constructive
verification that:

- No policy construction can produce `DIVERGED → CONTINUE` (I1, static)
- No runtime invocation can produce `DIVERGED → CONTINUE` (I1, dynamic)
- No policy construction can produce `INSUFFICIENT_DATA → CONTINUE` (I3, static)
- No runtime invocation under strict+retry can produce `UNKNOWN → CONTINUE` (I2)
- `HALT` is always admissible under any verdict
- Uncertainty contracts, never expands, the admissible execution space

---

## 9. — Relation to Prior Chapters

| Component | Description | Relation to this document |
|---|---|---|
| Formal execution model | Execution model | Defines the formal system over which invariants apply |
| Execution kernel | Execution kernel | Provides the enforcement infrastructure |
| Observation layer | Observation layer | Produces the verdict (V) that triggers invariant checks |
| Reconciliation Policy | Reconciliation policy | Governs configurable behavior; subject to I1–I3 |
| Diagnostic layer | Diagnostic layer | Records invariant violations without influencing them |
| PolicyConstraints | PolicyConstraints | Implements I1, I2, I3 — referenced directly by this chapter |

The kernel invariants of this chapter represent the non-negotiable boundary
between the policy layer (configurable) and the execution model (structural).
No component above PolicyConstraints in the dependency graph may override them.

---

*This document specifies the immutable enforcement constraints of the Regen Engine
execution kernel. These constraints are enforced by construction and at runtime.
They cannot be disabled, overridden, or configured away.*

---

<img width="2492" height="1222" alt="image" src="https://github.com/user-attachments/assets/2a273f26-35c0-412d-ad02-d4d12f483b87" />

---

[![Formal Paper](https://img.shields.io/badge/Formal%20Paper-OSF%20Preprint-blue)](https://doi.org/10.17605/OSF.IO/B8SGR)
[![Repository](https://img.shields.io/badge/Repository-ContinuumPort-green)](https://github.com/giorgioroth/ContinuumPort)
[![Regen Engine](https://img.shields.io/badge/Regen%20Engine-Control%20Layer-critical)](https://github.com/giorgioroth/ContinuumPort/blob/main/2.%20LICENSE_REGEN.md)
