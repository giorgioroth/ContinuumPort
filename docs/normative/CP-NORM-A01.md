
## Status
**CANONICAL — FROZEN**

---

## ID
**CP-NORM-A01**

## Title
**Author Absence Invariance**

---

## Normative Statement

A ContinuumPort-compliant system **MUST NOT** require the ongoing presence, availability, intervention, or authority of the original author, designer, or initiator in order to function, validate, resume, or continue semantic work.

---

## Normative Scope

A system is considered **NON-COMPLIANT** if it:

- requires the author to be:
  - present in the interaction,
  - reachable for clarification,
  - referenced as an authority for correctness,
  - invoked as a dependency for recovery or continuation;
- degrades, blocks, or alters behavior when the author is absent;
- embeds assumptions of:
  - author oversight,
  - author approval,
  - or author-mediated validation.

A system is considered **COMPLIANT** if:

- semantic continuity persists independently of author presence;
- exported context is sufficient for continuation by:
  - another agent,
  - another user,
  - or a future session;
- authority is derived exclusively from:
  - structure,
  - explicit constraints,
  - and documented intent — not personal presence.

---

## Rationale (Informative)

Continuity that depends on author presence constitutes **presence continuity**, not **work continuity**.

Requiring the author to remain available introduces:

- a single point of failure,
- implicit authority dependency,
- and a latent control channel.

ContinuumPort explicitly rejects systems whose operation, correctness, or legitimacy collapses in the author’s absence.

---

## Explicit Non-Goals

This rule does **NOT** require:

- anonymity of authorship;
- erasure of historical attribution;
- prevention of voluntary author participation.

It strictly forbids **functional dependency** on author presence.

---

## Relationship to CP-Core Principles

This rule:

- enforces **Continuity ≠ Presence**;
- reinforces **User as the Sole Point of Continuity**;
- extends **NON_ABUSE.md** into a structural invariance;
- operationalizes *Automating Author Absence* as a protocol constraint.

---

## Security Implications

Systems violating this rule risk:

- dependency capture;
- authority centralization;
- coercive continuity;
- silent user disempowerment.

Such systems are **EXPLICITLY NON-COMPLIANT** with CP-Core.

---

## Compliance Test (Informative)

A minimal compliance test is:

> Remove the author from the system entirely.  
> If semantic work cannot be resumed correctly, the system fails this rule.

---

## Notes

This rule is intentionally adoption-hostile.

It optimizes for:
- longevity over traction,
- resilience over loyalty,
- structure over personality.

Once applied, a system cannot become:
- author-dependent,
- personality-driven,
- or cult-forming.

That constraint is irreversible by design.
