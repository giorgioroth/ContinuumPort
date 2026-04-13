# REGEN-COMPLIANCE v1.0

## 1. Scope

Defines the conditions under which a system is Regen-Compliant.  
This document is normative.

---

## 2. System Model

A system MUST implement:

- deterministic execution  
- atomic state transitions  
- snapshot isolation  
- simulation/execution separation  

---

## 3. Core Invariants

I2 — Atomicity  
Execution MUST be all-or-nothing.

I4 — Snapshot Isolation  
Snapshots MUST NOT mutate system state.

I5 — Determinism  
Identical inputs MUST produce identical outputs.

Ch.50 — Semantic Alignment  
simulate(state, action) ≡ execute(state, action)

---

## 4. Conformance

A system is Regen-Compliant if:

- ALL invariants hold  
- AND all compliance tests pass  

Formal condition:

```

∀ t ∈ execution:
invariants(t) = true

```

---

## 5. Failure Model

Any invariant violation MUST result in:

- execution rejection  
- no state transition  
- no partial effects  

Failure classes:

- REGEN-FAIL-001 — PartialCommit  
- REGEN-FAIL-002 — NonDeterminism  
- REGEN-FAIL-003 — SnapshotLeak  
- REGEN-FAIL-004 — SemanticDrift  

---

## 6. Non-Guarantees

This specification does NOT guarantee:

- correctness of intent  
- correctness of constraints  
- external side-effect consistency  
- real-world safety  

---

## 7. Verification

Compliance MUST be verified via execution of the official test suite.
```

