# Terminology & Positioning  
## ContinuumPort Canonical Definitions

**Status:** Normative  
**Scope:** Semantic work continuity and handoff  
**Audience:** Engineers, system designers, researchers, implementers  

This document is authoritative.

---

## 1. Purpose of This Document

This document defines the **canonical terminology and conceptual positioning** of ContinuumPort.

Its purpose is to:

- eliminate ambiguity,
- prevent reinterpretation,
- fix the meaning of core concepts used throughout the ContinuumPort ecosystem.

This document is **NOT** explanatory.  
This document is **NOT** a proposal.  

This document is a **normative reference**.

Any implementation, discussion, or extension of ContinuumPort **MUST** conform to the definitions stated herein.

---

## 2. Core Distinction: Work vs. Presence

ContinuumPort is founded on a **strict separation** between **semantic work** and **presence**.

### 2.1 Semantic Work

**Semantic Work** refers to information required to continue a task **meaningfully and reproducibly**.

Semantic work **MAY** include:

- objectives and intent,
- established decisions,
- constraints and invariants,
- open questions,
- blocked items,
- next expected actions.

Semantic work **MUST** be expressible **independently of the original author** and **independently of the interaction context**.

---

### 2.2 Presence

**Presence** refers to information tied to an individual or to the interaction itself.

Presence includes, but is not limited to:

- identity,
- emotion,
- personality,
- conversational history,
- relational tone,
- autobiographical context,
- implicit or latent memory.

Presence **MUST NOT** be transferred as part of a ContinuumPort handoff.

---

## 3. CP-NORM-H01

**CP-NORM-H01** is a **normative semantic boundary specification**.

It defines:

- what semantic content **MAY** survive a handoff,
- what content **MUST** be excluded,
- where continuity **MUST** terminate.

CP-NORM-H01 **DOES NOT** define:

- workflows,
- productivity techniques,
- user experience patterns,
- implementation details.

It establishes a **limit**, not a method.

---

## 4. Normative Boundary

A **Normative Boundary** is a fixed point at which semantic transfer is constrained **by rule**, not by convenience.

At a normative boundary:

- certain information is explicitly **ALLOWED**,
- certain information is explicitly **DESTROYED**,
- continuation is conditional on **compliance**, not success.

CP-NORM-H01 defines such a boundary for semantic work continuity.

---

## 5. CP Boundary Trigger

The **CP Boundary Trigger** is an **explicit, user-initiated event** that activates the normative boundary defined by CP-NORM-H01.

The CP Boundary Trigger:

- is **NOT** a feature,
- is **NOT** a memory operation,
- is **NOT** a convenience mechanism.

It is a **boundary activation event**.

Any interface element colloquially referred to as a “CP button” is an **implementation of the CP Boundary Trigger**.

---

## 6. Semantic Handoff

A **Semantic Handoff** is the result of applying the CP Boundary Trigger.

A valid semantic handoff **MUST**:

- contain **only semantic work**,
- exclude **all presence-related information**,
- be **self-sufficient** for continuation,
- avoid reliance on implicit context.

A semantic handoff **MUST** be **auditable** and **portable**.

---

## 7. Semantic Freeze Point

The **Semantic Freeze Point** is the moment at which:

- interaction terminates,
- semantic work is stabilized,
- no further conversational influence is permitted.

The Semantic Freeze Point is **normative**, not heuristic.

It **MUST NOT** emerge gradually and **MUST NOT** be inferred implicitly.

---

## 8. Continuity Model

ContinuumPort provides **semantic work continuity**, not conversational continuity.

This means:

- continuity **MUST** apply only after meaning has stabilized,
- exploration and informal reasoning **MUST** occur before the boundary,
- continuation **MUST** begin from declared structure, not interaction history.

ContinuumPort **DOES NOT** preserve cognitive process.  
It preserves **outcome-relevant meaning** only.

---

## 9. Non-Scope

ContinuumPort explicitly **DOES NOT** address:

- emotional continuity,
- identity persistence,
- agent personhood,
- companionship systems,
- conversational memory,
- autonomous agent lifecycle continuity.

Any system requiring these properties is **OUTSIDE THE SCOPE** of CP-NORM-H01.

---

## 10. Applicability Limits

CP-NORM-H01 is **NOT DESIGNED** for domains where:

- full state continuity is mandatory,
- intermediate exploration is part of the result,
- loss of execution trace invalidates reproducibility.

Examples include:

- drug discovery,
- bioinformatics,
- experimental machine learning,
- applied mathematics,
- high-cost exploratory research.

In such domains, continuity requirements are **exhaustive**, not semantic.

---

## 11. Normative Nature

CP-NORM-H01 is **normative** in nature.

It:

- does **NOT** persuade,
- does **NOT** optimize,
- does **NOT** evolve through feedback.

It establishes a boundary and **accepts the consequences** of that boundary.

Disagreement with CP-NORM-H01 **CANNOT** be resolved through preference or utility arguments.  
It **MUST** be resolved by proposing an alternative norm with explicitly accepted losses.

---

## 12. Positioning Statement (Canonical)

ContinuumPort does **NOT** aim to make AI systems more friendly.  
It aims to make AI-assisted work **more responsible**.

It does **NOT** increase continuity.  
It constrains continuity to what can be safely transferred.

It does **NOT** preserve interaction.  
It preserves **work**.

---

**End of document.**
