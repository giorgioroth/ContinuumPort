# CP-START — Proposed Successor to CP-NORM-H01

**Status:** DRAFT — NOT CANONICAL — NOT FROZEN  
**Identifier:** To be assigned by the human author before adoption.  

This is a proposed replacement for the CP-START normative text. It does not amend the tagged CP-NORM-H01 release or assert that a successor has been adopted. Any adopted successor requires a new CP-NORM identifier and review of the companion handoff artifact.

---

## Normative Scope

This document specifies conditions under which a semantic handoff is conforming within ContinuumPort. Rationale, examples, and commentary may explain the choice of boundary but do not create additional normative requirements.

The requirements concern a handoff of work state. They do not establish continuity of a person, a relationship, or an agent's identity.

## Execution Boundary

CP-START is a declaration that a handoff is requested and a structure for the state to be handed off. The document and its companion JSON artifact do not, by their presence alone, validate semantic content, stop a running process, export or delete data, resume work, or prevent another application path from acting.

An implementation claiming enforced handoff conformance MUST show that the required checks are performed on the path it claims to govern. A designated engine such as Regen may perform those checks, but enforcement MUST NOT be inferred from the existence of a CP-START document or payload.

## Scope of Conformance

Within this proposed norm, a conforming handoff MUST be explicitly initiated with CP-START. A continuation that does not use CP-START is non-conforming to this norm, regardless of whether its output appears useful or familiar.

This is a rule for conformance within ContinuumPort. It is not a claim that other methods of transferring work state are impossible or invalid outside this norm.

CP-START describes the handoff boundary. Whether a system actually suspends execution, transfers data, terminates the current context, or resumes in another context depends on its implementation and is outside the guarantee of this document.

## Permitted Work State

A conforming handoff MUST represent task intent, structured working state, and explicit constraints. The companion handoff artifact separates established decisions from actionable open questions, allows blockers to be absent, and calls for one concrete next action. Whether those fields are complete and truthful is a separate validation question.

The handoff MUST NOT rely on inferred session memory, account state, or a presumed relationship with the user to reconstruct those fields.

The handoff MUST NOT transport personality, emotional state, autobiographical memory, conversational style, or relationship history as a means of recreating the prior user or agent. A task record may still contain sensitive information. Conformance with this norm does not certify that the record is public, anonymous, or safe to disclose; confidentiality and data minimization require separate controls.

Exclusion from the handoff does not imply deletion from its source. This norm specifies no source-data deletion procedure.

## Explicit Constraints

CP-START MAY carry constraints on the continuation, including working language, discourse mode, output format, and execution posture. Such constraints MUST be expressed in the handoff structure; they MUST NOT be inferred from previous conversations, user identity, or account history.

An implementation claiming to enforce those constraints MUST demonstrate the behavior at its declared execution boundary. The presence of a constraint in a payload is a requirement on a conforming implementation, not evidence that every model or application will follow it.

## Non-Goals

This norm does not define model internals, user interfaces, storage, authentication, confidentiality, deletion, execution architecture, or application-wide mediation. It does not certify that every effect in an application passes through a particular gate.

It does not prohibit informal or personal interaction outside the handoff. It limits the content and authority that may be attributed to a conforming transfer of work state.

## Status of Claims

The normative rules define what a conforming handoff must satisfy. Whether a particular implementation satisfies them requires inspection and tests of that implementation, including the paths on which a handoff can be bypassed. A schema or a successful conversational continuation alone does not establish that result.

Continuity of work MUST NOT be presented as continuity of a person.

## Provenance and Adoption

The human author decides whether to adopt a successor norm and assigns its identifier. Model-assisted drafting does not confer normative authority on this proposal. Until adoption, the tagged CP-NORM-H01 release remains the published frozen reference for that identifier.
