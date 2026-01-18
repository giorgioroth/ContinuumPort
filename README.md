# 🧭 ContinuumPort

**Normative framework for semantic continuity of work across AI systems**

---

## Canonical Description

ContinuumPort is a normative and architectural framework for the continuity of work when using AI systems.

It defines how semantic work state can be transferred across sessions, models, languages, and environments **without relying on memory, identity, presence, or conversational history**.

Continuity is achieved exclusively through explicit, portable structure.

---

## Core Principle

**Only intention and working state are portable.**  
Identity, emotion, presence, relationship continuity, and behavioral memory are explicitly excluded.

Semantic continuity is treated as a structural property of work, not as a behavioral property of an AI system.

---

## What ContinuumPort Is

ContinuumPort provides:

* a normative definition of semantic work continuity;
* a minimal structural container (CP-Core) for capturing work state;
* explicit constraints on what must *not* be transferred;
* a handoff primitive that enables work to resume without author presence.

AI models are treated as ephemeral, interchangeable tools.  
Continuity does not belong to the model, the session, or the vendor.

---

## What ContinuumPort Is Not

ContinuumPort is **not**:

* a memory system;
* a conversation archive;
* an identity or personality persistence mechanism;
* a user profiling framework;
* a semantic web or data interoperability standard;
* a commercial product or service.

It intentionally refuses to carry anything that would simulate presence or self.

---

## CP-Core

The core artifact defined by ContinuumPort is **CP-Core**: a structured, human-readable container representing the semantic state of work.

A CP-Core may include:

* intent (objective of the work);
* established decisions or conclusions;
* open questions requiring continuation;
* explicit constraints and exclusions;
* a single next expected action.

A CP-Core explicitly excludes:

* chat transcripts;
* autobiographical or relational context;
* implicit assumptions tied to a specific agent;
* emotional or behavioral state.

---

## Normative Constraint: Author Absence Invariance

A ContinuumPort-compliant system **must not** require the ongoing presence, availability, or authority of the original author in order to function or continue semantic work.

Continuity must derive solely from explicit structure and constraints.

---

## Repository Scope

This repository contains:

* the CP-Core normative definitions;
* frozen normative constraints (e.g. CP-NORM-H01);
* schemas and reference examples;
* documentation explaining design boundaries.

Project scope and status are defined in `PROJECT_STATUS.md`.

---

## Implementations

ContinuumPort defines **normative structure**, not implementation behavior.

Independent implementations may exist that consume CP-Core artifacts and regenerate working context. Such implementations are **not required** for understanding or using the normative framework.

**Regen Engine** is a proprietary implementation maintained separately under its own license. It is one possible implementation of CP-Core, not a requirement.

This repository does not mandate, bundle, or privilege any specific implementation.

---

## Status

ContinuumPort is an exploratory, non-commercial research project.

Normative content marked as **FROZEN** is stable and will not be modified.  
Any future changes require new normative identifiers.

---

## License

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-normative-orange)](PROJECT_STATUS.md)

---

## Author

Gh. Rotaru (Giorgio Roth)

Independent researcher

---

## Closing Note

ContinuumPort is a proposal for the **correct limitation** of AI systems, not their expansion.

Its value derives precisely from what it refuses to carry.

