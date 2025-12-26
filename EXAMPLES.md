# EXAMPLES.md

## ContinuumPort CP-Core — Practical Examples

This document provides **minimal, concrete examples** of how CP-Core is used to preserve *semantic continuity of work* across models, tools, and sessions.

These examples are **illustrative**, not normative.
They demonstrate *what CP-Core carries* — and, equally important, *what it does not*.

---

## Example 1: Cross-Model Task Continuation

**Scenario**
A user starts a task with one AI model and continues it later with another model, without losing task intent or constraints.

### CP-Core Payload

```json
{
  "v": 1,
  "lang": "en",
  "summary": "Draft an outline for a technical blog post explaining semantic continuity in AI systems.",
  "entities": ["ContinuumPort", "CP-Core"],
  "progress": "Introduction drafted. Next step: define non-goals and boundaries.",
  "constraints": [
    "No discussion of AI identity or memory",
    "Technical tone",
    "Audience: developers"
  ]
}
```

### Result (Conceptual)

* Model A creates the introduction.
* Model B receives the CP-Core payload.
* Model B continues directly with *non-goals and boundaries*, without re-prompting or restating intent.

**No conversation history is transferred.**
Only task-relevant semantic state is preserved.

---

## Example 2: Tool → Model → Tool Workflow

**Scenario**
A multi-step workflow involving tools and AI models.

1. Tool A generates structured output.
2. AI Model interprets and refines.
3. Tool B executes the next step.

### CP-Core Payload Between Steps

```json
{
  "v": 1,
  "summary": "Prepare a deployment checklist for a local AI service.",
  "progress": "Infrastructure requirements identified.",
  "constraints": [
    "Local-first",
    "No external cloud dependencies",
    "Security considerations required"
  ]
}
```

### Outcome

* Each step consumes the same CP-Core payload.
* No system needs access to prior conversations.
* Debugging is straightforward because the context is explicit and human-readable.

---

## Example 3: Multi-Agent Collaboration

**Scenario**
Multiple agents collaborate on a shared task.

* Agent A: planning
* Agent B: implementation
* Agent C: review

Each agent receives the same CP-Core payload.

```json
{
  "v": 1,
  "summary": "Design a minimal API for CP-Core validation.",
  "progress": "API endpoints sketched.",
  "constraints": [
    "JSON Schema validation",
    "No authentication layer",
    "Stateless design"
  ]
}
```

### Key Property

Agents may respond differently, but **directional intent remains stable**.

CP-Core does not synchronize agent behavior — it synchronizes *task understanding*.

---

## Example 4: What CP-Core Does NOT Carry

The following are **intentionally excluded** from all examples:

* User identity or persona
* Emotional state or sentiment
* Autobiographical memory
* Behavioral preferences
* Model-specific tuning instructions

If such data is required, it must be handled **outside** ContinuumPort.

---

## Summary

CP-Core enables:

* Explicit, portable task context
* Model-agnostic continuity
* Privacy-first workflows
* Simple debugging and inspection

CP-Core does **not** enable:

* AI memory
* Identity persistence
* Emotional continuity
* Autonomous agency

ContinuumPort preserves **continuity of work**, not continuity of presence.

---
