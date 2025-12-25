# Regen Engine Specification and Protocol Versioning

> **Status:** Draft  
> This document is normative for Regen Engine conformance, but subject to revision during early adoption.

## Part 1: Regen Engine Specification

### Normative Definition

A **Regen Engine** conforming to ContinuumPort is defined as a minimal software component that performs the following functions:

1. **CP-Core Parsing**: reading and syntactic validation of the CP-Core container
2. **Semantic Extraction**: identification of user intent, constraints, and task state
3. **Prompt Construction**: formatting context into a form consumable by the target model
4. **Neutral Transfer**: transmission of context without proprietary interpretation or optimization

### Mandatory Architectural Constraints

A conformant Regen Engine **MUST NOT**:

- **Impose semantic interpretation**: meaning must be derived from CP-Core, not added by Regen
- **Canonicalize content**: there is no "correct form" of intent beyond CP-Core syntax
- **Optimize behavior**: Regen does not decide the "best" regeneration
- **Adapt per-model with proprietary logic**: format differences are permitted, interpretation differences are not
- **Store state between sessions**: Regen is stateless by design
- **Perform embedding or vector analysis** as part of the normative flow

### Permitted Non-Normative Components

The following components **MAY exist** in implementations but **are NOT part of the standard**:

**Product Infrastructure:**
- API layers (REST, GraphQL, etc.)
- Authentication and authorization
- Rate limiting and throttling
- Metrics and observability
- Containerization (Docker, Kubernetes)

**Optional Optimizations:**
- Prompt caching
- Compression
- Embeddings for diagnostics (not for interpretation)
- Model-specific adapters (strictly for format differences, not interpretation)

**Critical Condition**: these components MUST be explicitly documented as **"Non-Standard Extensions"** and **MUST NOT become mandatory dependencies** for conformance.

### Mandatory Conceptual Separation

Implementations MUST maintain clear separation between:

```
regen_core/          # Normative (part of standard)
├── parser.py
├── regenerator.py
