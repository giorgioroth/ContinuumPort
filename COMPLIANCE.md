

# What Makes a Regen Engine Compliant

This document defines **compliance criteria**, not implementation guidance.
Any system claiming to implement a *Regen Engine* for ContinuumPort **must satisfy all requirements below**.
Failure to meet any requirement constitutes a **non-compliant implementation**, regardless of performance or features.

---

## 1. Core Principle

A Regen Engine is **not** defined by automation, speed, or intelligence.

A Regen Engine is compliant **if and only if** it preserves **semantic continuity** without introducing **author dependency, hidden authority, or memory coupling**.

---

## 2. Mandatory Compliance Requirements

### R1 — Author Absence Invariance

A Regen Engine **MUST NOT** require the presence, availability, approval, or authority of the original author in order to:

* route tasks
* validate results
* resume work
* resolve ambiguity

If removal of the author halts or degrades the system, the engine is **non-compliant**.

---

### R2 — CP-Core as Sole Source of Truth

The Regen Engine **MUST** derive all operational context exclusively from:

* CP-Core structure
* explicit task state
* documented constraints

It **MUST NOT** rely on:

* chat history
* implicit memory
* user identity
* hidden prompts
* proprietary internal state

If context cannot be reconstructed from CP-Core alone, the engine fails compliance.

---

### R3 — Deterministic Task Progression

Given the same CP-Core input, the engine **MUST**:

* route tasks consistently
* enforce `task_state` and `next` deterministically
* avoid arbitrary branching based on model personality or heuristics

Non-deterministic behavior that alters task flow without explicit instruction is **non-compliant**.

---

### R4 — Model-Agnostic Operation

A compliant Regen Engine:

* **MUST NOT** depend on a specific AI model
* **MUST** support replacement of models without semantic loss
* **MUST** normalize outputs into CP-Core–compatible structure

If replacing the model breaks continuity, the engine is coupled and **non-compliant**.

---

### R5 — Transport Neutrality

Semantic state transport **MUST** be independent of mechanism:

* manual (human copy/paste)
* scripted
* automated service
* distributed system

The engine **MUST NOT** assume privileged transport channels.

If continuity only works under a specific transport, the engine is **non-compliant**.

---

### R6 — Explicit Failure Surface

A compliant engine **MUST**:

* fail explicitly
* fail visibly
* fail with recoverable state

Silent degradation, hallucinated continuity, or simulated memory constitute **hard failure**.

---

### R7 — Auditability Without Intimacy

The engine **MAY** log:

* task transitions
* CP-Core versions
* routing decisions

It **MUST NOT** log:

* user identity
* emotional signals
* inferred intent beyond CP-Core
* behavioral fingerprints

Auditability must never create surveillance.

---

## 3. What a Regen Engine Is Explicitly NOT Required to Do

A compliant Regen Engine is **NOT required** to:

* be automatic
* be fast
* be user-friendly
* be commercial
* be centralized
* be always-on

Manual orchestration **is compliant**.
Automation is an optimization, not a requirement.

---

## 4. Minimal Compliance Test

> Remove the original author.
> Remove chat history.
> Replace the AI model.
> Restart the system.

If semantic work can be resumed correctly using only CP-Core revealed state, the engine **passes**.

Otherwise, it **fails**.

---

## 5. Consequence of Compliance

Once compliant, a Regen Engine:

* cannot become personality-driven
* cannot capture authority
* cannot enforce dependency
* cannot evolve into a platform of control

These constraints are **irreversible by design**.

---

## 6. Final Statement

ContinuumPort defines **what continuity is**.
Regen Engine defines **how continuity is executed**.

Compliance ensures that execution **never mutates the definition**.

Any engine that violates this is not “an alternative approach” —
it is a **different system**.

---
