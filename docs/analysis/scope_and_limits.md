# Scope and Limits

Defines the correctness boundary of the ContinuumPort execution model.

---

## Scope

ContinuumPort enforces correctness at the level of **state transitions**.

Guaranteed:

- no transition executes unless admissible under geometry
- execution is atomic — commit or full rollback
- no partial effects externally observable before commit
- all state mutation occurs only through the execution layer
- authority is explicit, injected, non-escalating
- execution is deterministic given state and input

These guarantees hold within a single execution cycle.

---

## Not Guaranteed

- **Intent correctness** — admissibility is not semantic correctness
- **Cross-cycle replay prevention** — replay detection is a control plane responsibility
- **Idempotency of external effects** — repeated side effects are not neutralized
- **Global ordering across cycles** — no sequencing beyond a single cycle
- **Geometry correctness** — invalid rules in geometry are enforced, not detected
- **External system consistency** — network calls may succeed independently of rollback
- **Geometry equivalence across sessions** — capsules carry no geometry reference

---

## Behavior Classification

### SAFE
Structurally prevented. No external coordination required.

| Behavior | Mechanism |
|---|---|
| Invalid state transition | Geometry admissibility check |
| Unauthorized action | AuthorityGate — fail-closed |
| State mutation outside gate | Environment gate |
| Drift between proposal and commit | TOCTOU check |
| Partial state escape | Atomic rollback |
| Authority escalation | Domain filter — monotonically reductive |
| Cross-authority capsule replay | Authority binding in control plane |

### MODEL LIMIT
Allowed by design. Defines the boundary — not a defect.

| Behavior | Note |
|---|---|
| Replay of valid action across cycles | Control plane must track |
| Geometry substitution between sessions | Not embedded in capsule |
| Logical lock survival after crash | Engine restores state faithfully |
| Intent-level incorrectness | Outside the model's scope |
| Non-idempotent external effects | Documented, not prevented |

### CONTROL PLANE RESPONSIBILITY
Must be handled outside the execution layer.

| Behavior | Mechanism |
|---|---|
| Replay detection | Nonce or sequence tracking |
| Authority lifecycle | Key rotation, revocation |
| External reconciliation | Observation layer + snapshot comparison |
| Geometry consistency across sessions | Session management policy |
| Logical lock recovery | Inspect capsule state before reconstruction |

---

## Capsules

Guaranteed:

- integrity validation before reconstruction (state hash)
- no implicit transfer of execution history
- authority mismatch detection at control plane entry

Not guaranteed:

- geometry equivalence across sessions
- replay prevention without external coordination

---

## Hard Line

If a behavior is not in SAFE, it is not prevented by the execution model.

What the system does not prevent, it documents.  
What it documents, it tests.
