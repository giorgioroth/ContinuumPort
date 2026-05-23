# Architecture of Work Continuity in Human–AI Systems

Version: v1.1

Status: Preprint

Date: May 2026

*This document describes an ongoing research framework and may evolve.*

Download PDF [Whitepaper](https://continuumport.com/wp-content/uploads/2026/05/Whitepaper_ContinuumPort.pdf)

## Authority, Persistence, and Semantic Handoff

**Giorgio Roth** Independent Researcher ContinuumPort Initiative [https://continuumport.com/](https://continuumport.com/)

---

## Abstract

Human–AI collaboration increasingly involves long-running tasks such as software engineering, research, and system design. However, continuity of work across sessions remains poorly defined. Existing systems typically rely on conversational persistence, context replay, or implicit model memory—mechanisms that conflate continuity of work with continuity of agent presence.

This paper proposes a unified architectural framework for work continuity in human–AI systems. The framework integrates two complementary components:

1. A structural model of persistent AI systems defined by the system state:
   `Σ = (D, A, Auth)`
   representing declarative state, adaptive memory, and execution authority.

2. A normative semantic handoff mechanism implemented through directional continuity and the CP-Core capsule structure, which preserves only task-relevant semantic state at session boundaries.

The architecture separates system persistence from work transfer by introducing the concept of a semantic freeze point, at which interaction terminates and a minimal transferable work state is emitted.

By constraining what may persist across sessions, the framework enables deterministic continuation of work across heterogeneous AI systems without requiring persistent agent identity, conversational replay, or implicit memory.

---

## 1. Introduction

Human–AI interaction increasingly supports complex work that unfolds across multiple sessions. Users expect tasks initiated in one interaction to continue in subsequent sessions, often across different systems or models.

Current approaches attempt to preserve continuity through mechanisms such as:

- retained conversational history
- extended context windows
- implicit model memory
- persistent agent identity

While these techniques improve short-term usability, they introduce structural weaknesses when work must be resumed, audited, or transferred.

Most importantly, these approaches conflate two distinct forms of continuity:

- continuity of work
- continuity of agent presence

This paper argues that these concepts must be separated.

Work continuity should be grounded in explicit semantic state, not in the persistence of conversational interaction or simulated identity.

To formalize this separation, we introduce a unified architecture consisting of:

- a system-level persistence model
- a task-level semantic handoff mechanism

Together these define a minimal and portable framework for long-running human–AI collaboration.

---

## 2. Persistent AI Systems

A persistent AI system maintains internal state across time. At the architectural level, the state of such a system can be represented as:

`Σ = (D, A, Auth)`

Where:

**D — Declarative State**

Explicit knowledge relevant to current tasks, such as goals, decisions, and structured representations of work.

**A — Adaptive Memory**

Implicit or learned information accumulated through interaction or training.

**Auth — Execution Authority**

Constraints that determine which actions are permitted within the system, including safety policies, resource limits, and governance rules.

This structure captures the operational state of a persistent AI system.

However, not all elements of Σ should transfer across session boundaries.

---

## 3. The Continuity Problem

When long-running work spans multiple sessions, several failure modes appear.

**Fragile Context**
Conversation history may be truncated or lost, preventing reliable continuation.

**Opaque Memory**
Implicit model memory cannot be inspected, audited, or transferred.

**Responsibility Leakage**
Decisions appear to be remembered by the system rather than explicitly restated.

**Identity Reification**
Users begin to treat the AI as a persistent entity rather than as a computational process.

These issues arise because continuity is implemented through interaction persistence rather than explicit work state.

---

## 4. Work vs Presence

The proposed framework introduces a strict separation between two domains.

**Semantic Work**
Transferable task information:

- objectives
- decisions
- constraints
- unresolved questions
- current state

**Presence**
Non-transferable interaction elements:

- identity
- personality
- conversational tone
- emotional context
- autobiographical memory

Presence is intentionally treated as non-transferable by design.

This separation ensures that work continuity does not depend on simulated agent identity.

---

## 5. Minimal Transferable Work State

For work to continue across sessions, a minimal semantic representation must be preserved.

We define the transferable work state as:

`W = (I, S, C, N)`

Where:

**I — Intent**
The objective of the task.

**S — Semantic State**
Established decisions and current progress.

**C — Constraints**
Boundaries that must not be violated.

**N — Next Action**
The immediate continuation step.

This structure represents the minimal state required for continuation.

Conceptually: `W ⊂ Σ`

That is, the transferable work state represents a projection of the full system state.

---

## 6. The Semantic Freeze Point

To separate interaction from work continuity, the framework introduces a semantic freeze point.

At the freeze point:

- conversational interaction terminates
- work-relevant state is extracted
- non-transferable elements are discarded
- a semantic capsule is generated

This boundary prevents conversational artifacts from contaminating the continuation state.

---

## 7. CP-Core: Semantic Capsule

The ContinuumPort project operationalizes transferable work state through CP-Core, a minimal semantic capsule.

The capsule contains five fields:

| Field | Role |
|-------|------|
| intent | task objective |
| constraints | boundaries |
| decisions | established semantic state |
| state_summary | current task state |
| progress | continuation status |

CP-Core intentionally performs lossy semantic compression.

Information that cannot be expressed within this structure is discarded.

---

## 8. Directional Continuity

Traditional continuity systems attempt to reproduce past interaction with high fidelity.

The framework proposed here instead enforces directional continuity.

Continuation systems must preserve:

- intent
- constraints
- established decisions

Implementation details may diverge.

Two systems continuing the same capsule are not required to produce identical outputs, but they must remain within the same constraint envelope.

---

## 9. Relationship Between System Persistence and Work Handoff

The relationship between persistent system state and transferable work state can be represented as:

```
Persistent System State
Σ = (D, A, Auth)

↓

Session Boundary

↓

Semantic Freeze Point

↓

Transferable Work State
W = (I, S, C, N)

↓

CP-Core Capsule

↓

Next System Instance
```

Only a subset of Σ is transferred.

Adaptive memory A is intentionally excluded.

---

## 10. Behavioral Validation

The framework was evaluated through long-running collaborative interactions involving multiple AI systems across separate sessions.

Observed behaviors included:

- automatic termination of conversational continuation
- extraction of structured work state
- generation of consistent handoff capsules
- successful continuation in fresh sessions

Failures occurred when:

- capsules were underspecified
- users relied on conversational context instead of explicit state

These failures were detectable and reproducible, satisfying falsifiability requirements.

---

## 11. Implications for Human–Computer Interaction

The framework suggests a shift in HCI design.

Instead of persistent conversational agents, systems can support long-running work through artifact-based continuity.

Users interact with systems that:

- execute tasks within a session
- emit semantic capsules at session boundaries
- resume work from structured artifacts

This approach reduces anthropomorphic confusion while increasing accountability.

---

## 12. Conclusion

This paper presents a unified framework for work continuity in human–AI systems.

By separating persistent system architecture from transferable work state, the framework enables reliable continuation of complex tasks across sessions and systems.

The key principle is that continuity should be a property of work, not of agents.

Explicit semantic handoff structures such as CP-Core allow systems to resume work deterministically without requiring persistent identity, conversational memory, or opaque internal state.

As AI-assisted collaboration becomes more widespread, such explicit handoff mechanisms may become foundational infrastructure for long-running human–AI workflows.

---

## Appendix A — CP-Core Capsule Schema

Machine-readable schema for semantic capsules.

**CP-Core**
```json
{
  "intent": "string",
  "constraints": ["list"],
  "decisions": ["list"],
  "state_summary": "string",
  "progress": "string"
}
```

---

## Appendix B — CP-NORM-H01 Specification

Normative definition of the semantic handoff protocol.

The protocol defines:

- semantic freeze conditions
- capsule generation rules
- continuation constraints
- directional consistency requirements

This specification forms the normative basis for cross-system work continuation in ContinuumPort.

---

## Related Research

**JAIR Submission #22885** — *On Structural Admission of Partial State Corruption in Unconstrained Persistent Systems*
Formal characterization of execution admissibility in persistent autonomous systems. 
→ [PreprintOSF](https://osf.io/b8sgr/overview)

**SSRN #6765719** — *Execution Geometry and Persistent State Governance: From Formal Model to Deployed Enforcement*
→ [papers.ssrn.com/sol3/papers.cfm?abstract_id=6765719](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6765719)   (coming soon)

