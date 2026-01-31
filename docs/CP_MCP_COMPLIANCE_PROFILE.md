

# CP–MCP COMPLIANCE PROFILE

**Requirements for Model Context Protocol (MCP) Servers Compatible with ContinuumPort**

**Status:** Normative Draft (RFC Open)
**Scope:** Model Context Protocol (MCP) servers intended to operate in ContinuumPort-compliant environments
**Audience:** MCP implementers, infrastructure engineers, enterprise AI architects
**Version:** 1.0-draft
**Author:** Giorgio Roth
**Date:** January 2026

---

## 1. Purpose

This document defines the **normative requirements** for a Model Context Protocol (MCP) server to be considered **ContinuumPort-compliant**.

It explicitly specifies:

* what an MCP server **MAY transport**,
* what it **MUST reject**,
* and what responsibilities it **MUST actively enforce**.

This document is **not** an implementation guide.
It is a **boundary and enforcement profile**.

---

## 2. Foundational Axiom

A ContinuumPort-compliant MCP server **does not manage conversations**.

It manages **explicit semantic work state**.

```
MCP ≠ conversational router  
MCP = transport and enforcement layer for explicit semantic work continuity
```

Any MCP server that assumes or simulates:

* conversational continuity,
* relational memory, or
* identity persistence

is **non-compliant by design**.

---

## 3. Accepted Payload Classes (MUST ACCEPT)

A CP-compliant MCP server **MUST accept and transport only** the following classes of data, **as explicitly serialized structures**.

### 3.1 Explicit Intent

Intent **MUST** be:

* declarative,
* goal-oriented,
* free of emotional, motivational, or personal framing.

Intent **MUST NOT** be:

* interrogative,
* speculative,
* conversational,
* or referential to subjective experience or preference.

Illustrative example:

> “Complete section X based on decisions Y under constraints Z.”

---

### 3.2 Work State

Including, but not limited to:

* stabilized decisions
* active hypotheses
* constraints
* partial results
* intermediate artifacts

All work state **MUST** be:

* explicit
* inspectable
* serializable
* non-narrative

The MCP server **does not interpret** or validate correctness.
It transports state **as declared**.

---

### 3.3 Next Actions

Including:

* remaining tasks
* blockers
* dependencies
* immutable boundaries (“must not change”)

Continuation **MUST** be expressed as **work progression**, not conversational flow.

---

## 4. Explicitly Forbidden Payload Classes (MUST REJECT)

A CP-compliant MCP server **MUST actively reject** payloads containing or implying any of the following.

### 4.1 Identity

* persistent user profiles
* personal identifiers
* authorial voice retention
* semantic personalization markers
  (e.g. “as you usually do”)

---

### 4.2 Presence

* implicit temporal anchoring
  (e.g. “as before”, “last time”)
* conversational thread continuity
* assumed shared history

---

### 4.3 Emotional or Relational Context

* affective state
* empathy cues
* role attribution
  (“mentor”, “partner”, “assistant”)
* relational calibration

---

### 4.4 Conversational History

* transcripts
* dialogue summaries
* compressed conversational memory
* inferred or implicit conversational state

**CP-Core replaces the entire conversational memory layer by design.**

---

## 5. Correct MCP ↔ AI Execution Flow

### 5.1 Non-Compliant Flow (Illustrative)

```
User → MCP → AI
        (conversation, memory, tone)
```

---

### 5.2 CP-Compliant Flow

```
User
 ↓
CP-Core (explicit, versioned work state)
 ↓
MCP Server (transport + enforcement)
 ↓
AI Model (stateless execution)
```

The AI model **MUST operate without knowledge of**:

* operator identity
* prior interaction history
* relational or emotional context

---

## 6. Mandatory MCP Server Responsibilities

A CP-compliant MCP server **is not passive**.

It **MUST** function as:

* a semantic gatekeeper,
* a boundary enforcer,
* a structural validator.

### Mandatory behaviors:

* validate CP-Core schema compliance
* reject non-structural or narrative payloads
* strip non-explicit fields
* refuse implicit inference or “helpful guessing”
* **fail closed on ambiguity**

A compliant MCP server **must say “no” frequently**.

---

## 7. Security and Risk Implications

This compliance profile intentionally prevents:

* conversational escalation
* role-play vulnerabilities
* relational manipulation
* social engineering through continuity
* identity-based exploitation

The system exposes **no persistent actor surface** for manipulation.
Only explicit structure is executed.

---

## 8. Relationship to MCP

ContinuumPort **does not compete with MCP**.

* MCP defines **how systems connect**.
* ContinuumPort defines **what is permitted to cross the boundary**.

This profile constrains MCP usage to prevent **unsafe semantic coupling**.

---

## 9. Compliance Determination

An MCP server is ContinuumPort-compliant **only if it**:

* enforces all acceptance rules,
* rejects all forbidden payload classes, and
* does not simulate continuity of presence.

**Partial compliance SHALL be treated as non-compliance.**

---

## Closing Principle

ContinuumPort does not make MCP more flexible.
It makes it **accountable**.

---

## Boundary Formula

**MCP transports context.
ContinuumPort defines its limits.**


