


# ContinuumPort

**Semantic continuity for AI systems — without lock-in, without identity persistence.**

ContinuumPort is an **open protocol** for portable semantic context. It enables the transfer of user intent, task constraints, and progress state between AI systems, while explicitly refusing to transport identity, emotion, or behavioral conditioning.

## 🗺️ How to Read This Repository

* **The Big Picture**: Start with this `README.md` for a high-level overview.
* **Philosophy & Ethics**: Read `DESIGN_RATIONALE.md` and `docs/boundaries.md` to understand the "why".
* **Deep Theory**: Explore `docs/essays/` for the foundational concepts behind the protocol.
* **Technical Rules**: Check the `spec/` folder for normative implementation requirements.
* **Live Examples**: See `examples/quickstart/` for a Python-based reference of CP-Core in action.

---

## 🧠 The Philosophy

ContinuumPort is built on the principle that **Continuity ≠ Presence**.
We believe that transporting dialogue history is a bottleneck for both privacy and performance.

* **[Why We Don't Move the Dialogue]([https://www.google.com/search?q=docs/essays/why-we-dont-move-the-dialogue.md](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/essays/why-we-dont-move-the-dialogue.md)** — Understanding the "Extractable Core" vs. "Conversation Noise".
* **Restraint by Design**: We deliberately refuse to standardize identity or emotion, focusing strictly on task-related semantic state.

---

## ✅ What It IS / ❌ What It IS NOT

### ContinuumPort IS:

* An **Open protocol** (MIT licensed).
* **Privacy-by-design** (standardized exclusion of identity).
* **Model-agnostic** and platform-independent.
* A **Transport container** for task state (CP-Core).

### ContinuumPort IS NOT:

* **NOT a prompting strategy**: Prompt construction is explicitly out of scope.
* **NOT a memory system** or an identity layer.
* **NOT a behavioral optimization engine** or a "consciousness" simulator.

---

## Documentation

### Core Philosophy and Boundaries
- [Design Rationale](DESIGN_RATIONALE.md) — Why these limits exist
- [Boundaries](docs/boundaries.md) — What we deliberately do NOT standardize
- [Emergent Behaviors](docs/emergent-behaviors.md) — Allowed but non-guaranteed behaviors

### Technical Specification

[Protocol Specification](spec/regen-engine.md) — Implementation and versioning rules

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

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Spec Status](https://img.shields.io/badge/Spec-Draft-yellow)](https://github.com/giorgioroth/ContinuumPort/blob/main/docs/SPECIFICATION.md)

[LICENSE](https://github.com/giorgioroth/ContinuumPort/blob/main/LICENSE.md)

[LICENSE_REGEN.md](https://github.com/giorgioroth/ContinuumPort/blob/main/LICENSE_REGEN.md)


ContinuumPort is open infrastructure.
Free to use, fork, implement, and extend — within the documented boundaries.

---

**ContinuumPort: continuity of work, never continuity of self.**

---

## Defensible Architecture (FAQ for Skeptics)

### 1. "Isn't this just a glorified JSON summary?"

**Yes.** And that is its greatest strength. ContinuumPort does not aim for structural complexity, but for **normative restriction**. While a standard "summary" is informal and often contaminated with behavioral instructions or persona drift, CP-Core is a strictly defined transport layer. It standardizes the *data*, not the *formatting*.

### 2. "Why not just use a well-crafted system prompt?"

System prompts are model-dependent, fragile, and constitute a "prompting trick" rather than a robust architecture. ContinuumPort separates the **Semantic State** (the *what*) from the **Regen Engine** (the *how*). By treating task continuity as a data serialization problem, we achieve true multimodel portability. **Prompt construction is explicitly out of scope for the protocol.**

### 3. "Does this really protect privacy if the state is plain text?"

Its primary privacy contribution is the **Prevention of Identity Leakage**. By explicitly forbidding the storage of user style, emotional tone, or personal history, the protocol ensures that even if a container is intercepted, it contains only "work in progress," not a "psychological profile" of the user. We standardize the exclusion of identity.

### 4. "Without the 'Regen Engine', isn't the protocol useless?"

A protocol is a contract, not a product. TCP/IP doesn't send emails; it moves packets. ContinuumPort moves semantic state. By separating the **Transport Layer (CP-Core)** from the **Interpretation Layer (Regen Engine)**, we allow the ecosystem to build diverse, conformant engines that all speak the same semantic language.

### 5. "What prevents vendors from adding their own 'tracking' fields?"

The specification allows for extensions, but they are marked as **Non-Normative**. A Regen Engine is conformant **if and only if** removing all non-normative layers (tracking, embeddings, proprietary metadata) does not change the reconstructed semantic intent. We provide the standard that allows users to detect and strip away vendor lock-in.

---

**Documentation is the product. CP-Core is the contract.**

**ContinuumPort: continuity of work, never continuity of self.**

---
