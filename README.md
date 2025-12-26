# ContinuumPort

**Semantic continuity for AI systems — without lock-in, without identity persistence.**

# CP-Core is not a prompting strategy. 
# It is a transport container for task state that remains agnostic to how prompts are constructed.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Spec Status](https://img.shields.io/badge/Spec-Draft-yellow)](spec/specification.md)

---

## What is ContinuumPort?

ContinuumPort is an **open protocol** for portable semantic continuity across AI systems.

It enables transfer of:
- user intent
- task constraints
- progress state
- semantic direction

**Without** transferring:
- identity
- emotional state
- autobiographical memory
- behavioral conditioning

Think of it as **"semantic USB for AI"** — portable context, not portable presence.

---

## Core Principle

> **Continuity ≠ Presence**

ContinuumPort preserves **what you're working on**, not **who you are**.

It is intentionally minimal, privacy-first, and designed with restraint.

---

## Why ContinuumPort Exists

Current AI systems lock your context inside:
- specific platforms (ChatGPT, Claude, Gemini)
- specific accounts
- specific models

**ContinuumPort breaks this lock-in.**

You own your context. You decide where it goes.

---

## What Makes It Different

### ✅ What ContinuumPort IS:
- Open protocol (MIT licensed)
- Privacy-by-design (zero PII)
- Model-agnostic
- Platform-independent
- Explicitly bounded (refuses identity/emotion transport)

### ❌ What ContinuumPort IS NOT:
- A memory system
- An identity layer
- An AI model or service
- A behavioral optimization engine
- A "consciousness" simulator

---

## Documentation

### Core Philosophy and Boundaries
- [Design Rationale](DESIGN_RATIONALE.md) — Why these limits exist
- [Boundaries](docs/boundaries.md) — What we deliberately do NOT standardize
- [Emergent Behaviors](docs/emergent-behaviors.md) — Allowed but non-guaranteed behaviors

### Technical Specification
- [Regen Engine & Versioning](spec/regen-engine.md) — Normative implementation requirements

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/giorgioroth/continuumport.git
cd continuumport

# Explore the documentation
cat DESIGN_RATIONALE.md
cat spec/regen-engine.md
```

*(Reference implementation and examples coming soon)*

---

## Status

**Current Status:** Draft / Early Development

- ✅ Core philosophy documented
- ✅ Boundaries defined
- ✅ Regen Engine spec published
- 🚧 CP-Core format specification (in progress)
- 🚧 Reference implementation (planned)
- 🚧 Example containers (planned)

---

## Key Design Decisions

### 1. **Restraint by Design**
ContinuumPort deliberately refuses to standardize identity, emotion, or memory — even though these are technically feasible.

### 2. **Normative vs. Non-Normative**
Only CP-Core format and minimal Regen behavior are normative.
Everything else (embeddings, auth, optimizations) is implementation-specific.

### 3. **Test of Conformance**
*A Regen Engine is conformant if and only if removing all non-normative layers does not change the semantic intent reconstructed from CP-Core.*

Read the full rationale: [DESIGN_RATIONALE.md](DESIGN_RATIONALE.md)

---

## Use Cases

**Allowed:**
- Continuing work across different AI systems
- Switching models without losing task context
- Multi-agent collaboration on long-term projects
- Personal context ownership and portability

**Prohibited:**
- Identity persistence or "self" simulation
- Emotional continuity or attachment formation
- Behavioral conditioning or personality shaping
- Hidden data retention or opaque interpretation

---

## Contributing

Contributions are welcome, especially:

- Feedback on spec clarity
- Use case proposals
- Implementation suggestions
- Documentation improvements

For major changes, please open an issue first.

All contributions must respect ContinuumPort's core boundaries.

---

## Roadmap

- [ ] CP-Core format specification (JSON schema)
- [ ] Reference Regen Engine implementation
- [ ] Example CP-Core containers
- [ ] Validation tools
- [ ] Community RFC process
- [ ] v1.0 stable release

---

## Contact

**Author:** Gh. Rotaru (Giorgio Roth)

**Email:** continuumport@gmail.com

**X/Twitter:** [@continuumport](https://x.com/continuumport)

---

## License

**MIT License**

[LICENSE](https://github.com/giorgioroth/ContinuumPort/blob/main/LICENSE.md)

[LICENSE_REGEN.md](https://github.com/giorgioroth/ContinuumPort/blob/main/LICENSE_REGEN.md)


ContinuumPort is open infrastructure.
Free to use, fork, implement, and extend — within the documented boundaries.

---

**ContinuumPort: continuity of work, never continuity of self.**

---

## 🛡️ Defensible Architecture (FAQ for Skeptics)

### 1. "Isn't this just a glorified JSON summary?"
**Yes.** And that is its greatest strength. ContinuumPort does not aim for structural complexity, but for **normative restriction**. While a standard "summary" is informal and often contaminated with behavioral instructions or persona drift, CP-Core is a strictly defined transport layer. It standardizes the *data*, not the *formatting*.

### 2. "Why not just use a well-crafted system prompt?"
System prompts are model-dependent and fragile. ContinuumPort separates the **Semantic State** (the *what*) from the **Regen Engine** (the *how*). By treating task continuity as a data serialization problem rather than a prompting trick, we achieve true multimodel portability.

### 3. "Does this really protect privacy if the state is plain text?"
Its primary privacy contribution is the **Prevention of Identity Leakage**. By explicitly forbidding the storage of user style, emotional tone, or personal history, the protocol ensures that even if a container is intercepted, it contains only "work in progress," not a "psychological profile" of the user.

### 4. "Without the 'Regen Engine', isn't the protocol useless?"
A protocol is a contract, not a product. TCP/IP doesn't send emails; it moves packets. ContinuumPort moves semantic state. By separating the **Transport Layer (CP-Core)** from the **Interpretation Layer (Regen Engine)**, we allow the ecosystem to build diverse engines that all speak the same language.

### 5. "What prevents vendors from adding their own 'tracking' fields?"
The specification allows for extensions, but they are marked as **Non-Normative**. Any compliant ContinuumPort implementation is instructed to prioritize the Core fields and ignore behavioral extensions. We provide the first standard that allows users to detect and strip away vendor lock-in.
