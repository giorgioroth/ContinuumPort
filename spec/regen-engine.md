# Regen Engine Specification and Protocol Versioning

This specification intentionally favors restraint over capability, as described in DESIGN_RATIONALE.md.

> **Status:** Draft  
> This document is normative for Regen Engine conformance, but subject to revision during early adoption.

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
└── formatter.py

product_layer/       # Non-normative (implementation-specific)
├── api/
├── auth/
├── metrics/
└── deployment/

experimental/        # Non-normative (outside standard)
├── embeddings/
├── optimizers/
└── adapters/
```

### Conformance Test

A Regen implementation is conformant if:

1. ✅ It correctly processes any valid CP-Core
2. ✅ It does not semantically modify original intent
3. ✅ It does not introduce non-standard dependencies in the regeneration flow
4. ✅ It clearly documents what is normative vs. non-normative
5. ✅ It enables portable regeneration between different implementations

---

## Part 2: Protocol Versioning

### Necessity of Versioning

ContinuumPort, like any infrastructure protocol, will evolve over time. Versioning MUST ensure:

- **Backward compatibility** whenever possible
- **Clear detection** of incompatibilities
- **Controlled migration** between versions
- **Stability for industrial adoption**

### Proposed Versioning Schema

ContinuumPort adopts **Semantic Versioning** (SemVer) adapted for protocols:

```
MAJOR.MINOR.PATCH
```

**MAJOR** (backward incompatible):
- Changes to CP-Core structure that break existing parsing
- Removal of mandatory fields
- Fundamental changes to standard semantics

**MINOR** (backward compatible):
- Addition of new optional fields
- Extensions to semantic vocabulary
- Normative clarifications that do not break existing implementations

**PATCH** (corrections):
- Documentation errors
- Editorial clarifications
- Improved examples

### Version Identification in CP-Core

Each CP-Core container **MUST** contain the field:

```json
{
  "cp_version": "1.0.0",
  "intent": { ... },
  ...
}
```

### Compatibility Rules

**Regen implementations MUST:**

1. **Explicitly declare** supported CP versions
2. **Reject with clear message** containers with incompatible major versions
3. **Process with graceful degradation** newer minor versions (ignoring unknown fields)
4. **Log warnings** for deprecated versions

### Standard Evolution Process

**Change Proposals:**

1. **Public RFC** (Request for Comments) in repository
2. **Discussion period** (minimum 30 days for MAJOR, 14 for MINOR)
3. **Reference implementation** before finalization
4. **Complete documentation** of rationale and impact

**Deprecation Policy:**

- MAJOR versions are supported for **minimum 24 months** after next MAJOR version release
- Deprecation is announced **minimum 12 months** in advance
- Documentation includes explicit **migration guides**

### Alpha/Beta Versions

For active development:

```
1.0.0-alpha.1
1.0.0-beta.2
1.0.0-rc.1  (release candidate)
1.0.0       (stable)
```

**Pre-release versions:**
- Offer no stability guarantees
- May have breaking changes between iterations
- MUST NOT be used in production

### Backward Compatibility Commitment

ContinuumPort commits to:

- **Minimum 2 years** of support for stable MAJOR versions
- **Transparent deprecation** with documented alternatives
- **Automated testing** of compatibility between consecutive versions
- **Clear upgrade paths** for existing implementations

---

## Part 3: Formal Terminology

ContinuumPort documentation adopts RFC 2119 terminology for clarity:

- **MUST / REQUIRED / SHALL** = mandatory for conformance
- **MUST NOT / SHALL NOT** = forbidden for conformance
- **SHOULD / RECOMMENDED** = strongly recommended, justified exceptions allowed
- **MAY / OPTIONAL** = left to implementor discretion

---

## Integration Recommendations

This specification SHOULD be integrated as:

- **Option 1**: `spec/regen-engine.md` + `spec/versioning.md` (separate documents)
- **Option 2**: Extended section in `DESIGN_RATIONALE.md`
- **Option 3**: New top-level `SPECIFICATION.md` with both sections

The choice depends on repository structure and documentation philosophy.

A Regen Engine implementation is compliant if and only if removing all non-normative layers (authentication, embeddings, adapters, scoring) does not change the semantic intent reconstructed from CP-Core.

---

**Document Status**: Draft  
**Last Updated**: 2025-12-25  
**Author**: Gh.Rotaru (Giorgio Roth)
