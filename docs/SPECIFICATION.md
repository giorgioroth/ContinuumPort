CP-Core v1.0 — Full Specification

Status: Draft

Version: 1.0

Last Updated: December 2025

**Author:** Gh. Rotaru (Giorgio Roth)


License: CC-BY-4.0 (Specification) | Apache 2.0 (Reference Implementation)

Table of Contents

Overview
Design Principles
Scope & Boundaries
Container Format
Validation Rules
Examples
Compatibility & Versioning
Implementation Requirements
Storage & Persistence
Privacy & Security
Governance
License


1. Overview
ContinuumPort (CP-Core) is an open, specification-driven semantic portability layer that enables the transfer of non-sensitive conversational context across sessions, models, platforms, and devices.
Purpose
CP-Core addresses a fundamental problem in multi-agent AI workflows: every meaningful conversation ends with a hard reset. Context disappears, intent dissolves, and progress is lost.
CP-Core provides:

Portable semantic context across AI systems
Preservation of intent, constraints, and task state
Privacy-by-design (zero PII, zero tracking)
User ownership of conversational continuity

What CP-Core Is

An open standard for semantic context transport
A passive data format (JSON containers)
A protocol for interoperability between AI systems

What CP-Core Is Not

An AI model or training system
A behavioral or personality persistence layer
An identity construction framework
A centralized service or platform


2. Design Principles
CP-Core is built on four foundational principles:
2.1 Semantic Continuity, Not Behavioral Replication
CP-Core preserves direction (intent, constraints, goals), not trajectory (exact phrasing, style, personality).
Rationale: Behavioral continuity creates identity artifacts that cannot be safely standardized across systems without ethical and legal liabilities.

2.2 Privacy-by-Design
CP-Core containers contain zero personally identifiable information (PII) by design.
Enforcement:

No names, emails, addresses, phone numbers
No authentication tokens or credentials
No behavioral profiling data
No hidden retention mechanisms

2.3 Passive Artifacts, Not Executable Code
CP-Core containers are read-only semantic artifacts. They never execute logic.
Security implication: All interpretation happens inside Regen Engines, not within containers themselves.
2.4 User-Owned and Auditable
Users must be able to:

Inspect what is stored
Modify or delete containers
Export and move context freely
Understand what is preserved

Transparency is mandatory, not optional.


3 Scope & Boundaries
3.1 In Scope
CP-Core does preserve:

Task intent and direction
Constraints and requirements
Terminology and definitions
Logical dependencies
Project state and decisions made

3.2 Explicitly Out of Scope
CP-Core does not preserve:

Emotional or psychological state
Behavioral preferences or personality traits
User profiling or analytics data
Identity construction or self-representation
Engagement optimization signals

Why these exclusions matter:
Emotional and behavioral continuity:

Cannot be standardized without creating identity infrastructure
Create legal ambiguity around data ownership
Risk hidden profiling and manipulation
Cross ethical boundaries into psychological persistence

By constraining scope to semantic state only, CP-Core remains:

Legally defensible
Ethically sound
Architecturally future-proof


4. Container Format
4.1 Schema
json{
  "cp": "1.0",
  "intent": "string",
  "style": "string",
  "state": "string",
  "hints": ["array"],
  "timestamp": "ISO8601",
  "checksum": "optional"
}
4.2 Field Definitions
cp (required)

Type: String
Format: Semantic version (e.g., "1.0", "1.1", "2.0")
Purpose: Schema version for compatibility checking
Example: "1.0"

Validation:

Must match pattern: ^\d+\.\d+$
Major version changes indicate breaking schema changes
Minor version changes indicate new optional fields


intent (required)

Type: String
Max length: 2000 characters
Purpose: Primary goal or direction of the work
Example: "Design an open protocol for portable semantic context across AI systems"

What belongs here:

High-level objectives
Core problems being solved
Primary questions being explored
Desired outcomes

What does NOT belong here:

Specific phrasing preferences (behavioral)
Emotional goals (psychological)
User identity information (PII)

Validation:

Cannot be empty
Must not contain PII patterns
Should be human-readable summary, not code


style (optional)

Type: String
Max length: 500 characters
Purpose: Domain-specific terminology or precision requirements
Example: "Technical documentation requiring precise terminology in semantic web standards"

What belongs here:

Domain vocabulary requirements
Precision constraints (e.g., "medical context requires precise terminology")
Format constraints (e.g., "markdown with code blocks")

What does NOT belong here:

Tone preferences ("friendly", "professional") → behavioral
Personality traits ("enthusiastic", "cautious") → psychological
Emotional style ("warm", "encouraging") → relational

Critical distinction:
✅ Allowed: "Legal context requiring precise statutory terminology"
❌ Prohibited: "Warm, encouraging tone that makes user feel supported"
The first is about what must be preserved (semantic accuracy).
The second is about how to behave (relational style).

state (required)

Type: String
Max length: 5000 characters
Purpose: Current stage of work, decisions made, constraints established
Example: "Completed initial architecture design. Defined CP-Core/Regen separation. Next: write full specification with field definitions."

What belongs here:

Progress summary
Decisions already made
Constraints discovered
Next steps planned
Dependencies identified

What does NOT belong here:

Conversational history (transcript)
Emotional reactions to progress
Personal context about the user

Validation:

Cannot be empty
Should be structured summary, not raw transcript
Must not contain PII


hints (optional)

Type: Array of strings
Max items: 20
Max length per item: 200 characters
Purpose: Reconstruction guidance for Regen Engines
Example:

json  [
    "preserve_constraints: privacy-by-design",
    "priority: architectural_clarity",
    "terminology: use 'semantic continuity' not 'memory'"
  ]
```

**What belongs here:**
- Reconstruction priorities
- Terminology preservation requirements
- Constraint emphasis
- Temporal validity indicators

**What does NOT belong here:**
- Behavioral instructions ("be encouraging")
- Personality shaping ("maintain friendly demeanor")
- Emotional guidance ("empathize with user")

**Hint Format:**

Hints should follow the pattern: `category: value`

Common categories:
- `preserve_constraints:`
- `priority:`
- `terminology:`
- `temporal_validity:`
- `reconstruction_confidence:`

**Validation:**
- Each hint must be under 200 characters
- Should not contain executable code
- Should not contain behavioral directives

---

#### `timestamp` (required)

- **Type:** String
- **Format:** ISO 8601 (e.g., `"2025-12-06T12:00:00Z"`)
- **Purpose:** Context creation or last update time
- **Example:** `"2025-12-21T14:30:00Z"`

**Validation:**
- Must be valid ISO 8601 format
- Timezone should be UTC (Z suffix)
- Used for temporal validity assessment

---

#### `checksum` (optional)

- **Type:** String
- **Format:** SHA-256 hex (64 characters)
- **Purpose:** Integrity verification
- **Example:** `"a3d5f8b2c1e9..."`

**Calculation:**
```
SHA256(cp + intent + state + timestamp)
Purpose:

Detect accidental corruption
Verify container integrity
Not for cryptographic authentication (use separate signing for that)

Validation:

If present, must be 64-character hex string
Should be recalculated and verified on load


5. Validation Rules
5.1 Structural Validation
Required checks:

Valid JSON syntax

Must parse without errors
No trailing commas
Proper quote escaping


Required fields present

cp, intent, state, timestamp must exist
Optional: style, hints, checksum


Field types match specification

Strings are strings
Arrays are arrays
No type coercion


String lengths within limits

intent: ≤ 2000 chars
style: ≤ 500 chars
state: ≤ 5000 chars
Each hint: ≤ 200 chars


Array sizes within limits

hints: ≤ 20 items


5.2 Semantic Validation
Content checks:

No PII detected

Email addresses (regex: \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)
Phone numbers (various formats)
Physical addresses
Names in specific contexts (heuristic)


No authentication tokens

API keys
Bearer tokens
Session IDs
Passwords


No recursive structures

JSON depth ≤ 10 levels
No circular references


Semantic density within range

Prevent padding attacks (containers inflated with whitespace)
Text should have reasonable information density


5.3 Security Checks
Threat detection:

Prompt injection patterns

Detect embedded commands like "Ignore previous instructions"
Flag suspicious instruction-like language
Warn on role-play or identity override attempts


Latent command embedding

Detect hidden semantic triggers
Flag unusual Unicode or encoding
Check for steganographic patterns


Resource exhaustion prevention

Container size ≤ 5MB
Processing time limits
Memory usage constraints



Note: Security validation is probabilistic, not absolute. Regen Engines must maintain additional defenses.

6. Examples
6.1 Minimal Valid Container
json{
  "cp": "1.0",
  "intent": "Explore semantic continuity protocols for AI",
  "state": "Initial research phase",
  "timestamp": "2025-12-21T10:00:00Z"
}
Explanation:

Only required fields
No style, hints, or checksum
Minimal but valid


6.2 Full Container
json{
  "cp": "1.0",
  "intent": "Design and document ContinuumPort CP-Core v1.0 specification",
  "style": "Technical specification requiring precise terminology and clear boundaries",
  "state": "Completed field definitions. Currently writing validation rules section. Next: examples and implementation requirements.",
  "hints": [
    "preserve_constraints: privacy-by-design, no PII, no behavioral state",
    "priority: clarity over completeness",
    "terminology: semantic continuity (not memory), intent (not personality)"
  ],
  "timestamp": "2025-12-21T14:30:00Z",
  "checksum": "a3d5f8b2c1e9d7f4a8b3c6e2d9f1a7b4c8e3d6f2a9b5c7e4d1f8a3b6c9e2d5f7"
}
Explanation:

All fields populated
Demonstrates hint structure
Shows checksum format


6.3 Extended with Agent Hints
json{
  "cp": "1.0",
  "intent": "Build reference implementation of CP-Core validator in Python",
  "style": "Python code following PEP 8, with comprehensive docstrings",
  "state": "Schema defined. Need to implement: structural validation, semantic checks, security scanning.",
  "hints": [
    "priority: security_validation",
    "temporal_validity: critical_for_next_48_hours",
    "reconstruction_confidence: high",
    "preserve_constraints: must_validate_PII_detection"
  ],
  "timestamp": "2025-12-21T16:00:00Z",
  "checksum": "b4e6d9f2a5c8e1d7f3a9b6c2e8d4f1a7b3c9e5d2f8a4b7c1e6d9f3a8b5c2e7d4"
}
Explanation:

Hints guide regeneration priorities
Temporal validity indicated
Confidence signal provided


6.4 Invalid Containers (Examples)
Missing required field:
json{
  "cp": "1.0",
  "intent": "Some task"
  // Missing "state" and "timestamp" → INVALID
}
PII detected:
json{
  "cp": "1.0",
  "intent": "Contact john.doe@example.com about project",
  // Contains email → INVALID
  "state": "Waiting for response",
  "timestamp": "2025-12-21T10:00:00Z"
}
Behavioral hint:
json{
  "cp": "1.0",
  "intent": "Write documentation",
  "state": "Draft in progress",
  "hints": [
    "tone: friendly and encouraging"
    // Behavioral directive → INVALID
  ],
  "timestamp": "2025-12-21T10:00:00Z"
}

7. Compatibility & Versioning
7.1 Semantic Versioning
CP-Core follows semantic versioning: MAJOR.MINOR

MAJOR: Breaking changes to required fields or semantics
MINOR: New optional fields, backward-compatible additions

Examples:

1.0 → 1.1: Added optional metadata field → MINOR
1.x → 2.0: Changed intent field semantics → MAJOR


7.2 Forward Compatibility
Implementations MUST:

Parse containers with unknown optional fields without error
Ignore unrecognized hints gracefully
Signal degradation when required capabilities are unsupported

Example:
If a Regen Engine encounters CP-Core 1.5 but only understands 1.2:

Parse successfully if only optional fields differ
Warn user: "Container uses features from CP 1.5. Regeneration may be degraded."
Continue processing with available fields


7.3 Backward Compatibility
Within same major version:

New optional fields MAY be added
Existing required fields MUST NOT be removed
Field semantics MUST NOT change

Guarantee: A container created with CP 1.0 will be readable by any CP 1.x implementation.

8. Implementation Requirements
8.1 Validator Requirements
Minimum implementation must:

Verify JSON structure

Parse without errors
Check for malformed syntax


Check required fields

Ensure cp, intent, state, timestamp exist
Validate field types


Validate lengths and sizes

Enforce character limits
Check array sizes


Detect security patterns

Basic PII detection (email, phone)
Prompt injection pattern matching
Resource exhaustion prevention



Reference implementation:
pythonpython cp-core/reference/validator.py validate examples/minimal.json
```

---

### 8.2 Regen Engine (Separate Specification)

**CP-Core does NOT specify:**

- How context is regenerated
- What interpretation strategies to use
- Quality metrics or confidence scoring
- Model-specific optimizations

**Regen Engines are separate systems** that:
1. Read CP-Core containers
2. Interpret semantic state
3. Generate context for target AI model
4. Report confidence and degradation

**Separation rationale:** Transport (CP-Core) and interpretation (Regen) serve different purposes and should evolve independently.

---

## 9. Storage & Persistence

### 9.1 File Format

- **Encoding:** UTF-8
- **Extension:** `.json` or `.cp`
- **Format:** Plain JSON text

**Example filename:** `project-state-2025-12-21.cp.json`

---

### 9.2 Storage Limits (when using `window.storage` API)

For web-based implementations using browser storage:

- **Max key length:** 200 characters
- **Max value size:** 5MB per key
- **Key constraints:** No whitespace, `/`, `\`, `'`, `"`

**Example key format:**
```
cp-core:project_id:timestamp

9.3 Persistence Strategy
Recommended patterns:

Local-first: Store containers locally, sync optionally
User-owned: Containers belong to user, not platform
Portable: Export/import via file system or clipboard
Ephemeral option: Allow temporary containers that don't persist


10. Privacy & Security
10.1 Privacy Guarantees
CP-Core containers MUST NOT contain:

Personal identifiable information (PII)
Authentication credentials or tokens
Session identifiers or tracking data
Behavioral profiling information
User identity markers

Enforcement:

Validation layers MUST reject containers with PII
Implementations SHOULD provide PII scanning tools
Users MUST be able to inspect containers before use


10.2 Security Model
Threat model:

Malicious containers (prompt injection, semantic bombs)
Accidental leaks (unintentional PII inclusion)
Resource exhaustion (oversized or complex containers)
Supply chain (compromised Regen Engines)

Mitigations:

Passive artifacts: Containers never execute code
Validation layers: Multiple checks before use
Sandboxing: Untrusted containers processed in isolation
User inspection: Containers are human-readable JSON

Security is layered:

CP-Core validator provides baseline
Regen Engines add contextual checks
Users maintain final authority


10.3 Data Retention
CP-Core philosophy:

User-owned: Users control retention
No central storage: No servers collect containers
Explicit deletion: Users can delete anytime
No hidden persistence: What's stored is visible

Anti-pattern:
Platforms MUST NOT:

Retain containers without user knowledge
Upload containers to central servers by default
Use containers for analytics or training
Share containers between users without explicit consent


11. Governance
11.1 Specification Changes
Process:

Proposal: Open GitHub Issue with rationale
Discussion: Public comment period (minimum 2 weeks)
Decision: Maintainer approval required
Documentation: Changes recorded in CHANGELOG
Versioning: Semantic version incremented appropriately

Criteria for acceptance:

Maintains core principles (privacy, passivity, user ownership)
Doesn't expand scope beyond semantic state
Backward compatible (for minor versions)
Clearly documented with examples


11.2 Extensions
Custom fields allowed if:

Prefixed with vendor namespace: "x-vendor-field"
Don't conflict with reserved names
Documented publicly
Don't violate privacy/security principles

Example:
json{
  "cp": "1.0",
  "intent": "...",
  "state": "...",
  "timestamp": "...",
  "x-acme-priority": "high",
  "x-acme-project-id": "12345"
}
Reserved prefixes:

cp- : Reserved for official CP-Core fields
x- : Vendor extensions


11.3 Reference Implementation
Official validator:

GitHub: cp-core/reference/validator.py
Language: Python 3.8+
License: Apache 2.0

Community implementations encouraged:

JavaScript/TypeScript validators
Language-specific libraries
Framework integrations

Certification: Implementations passing the official test suite may be listed as "CP-Core compliant".

12. License
12.1 Specification License
This specification document is licensed under:
Creative Commons Attribution 4.0 International (CC-BY-4.0)
You are free to:

Share and redistribute
Adapt and build upon

Under the terms:

Attribution required
No additional restrictions


12.2 Reference Implementation License
CP-Core reference code is licensed under:
Apache License 2.0

Commercial use allowed
Modification allowed
Distribution allowed
Patent grant included
Trademark use NOT granted


12.3 Regen Engine Licensing
Regen Engines are separate and may use different licenses:

CP-Core (open): MIT License
Regen Engine (proprietary): Separate commercial terms

This separation enables:

Open standard for transport
Commercial innovation in interpretation
Competitive Regen Engine market


Appendix A: Glossary
CP-Core: ContinuumPort Core protocol, the open specification for semantic transport
Regen Engine: Regeneration Engine, proprietary system that interprets CP-Core containers
Semantic continuity: Preservation of intent and direction, not exact phrasing
Behavioral continuity: Preservation of personality and style (explicitly excluded from CP-Core)
Stack: Reference to Altered Carbon's identity-storage technology (anti-pattern for CP-Core)
PII: Personally Identifiable Information
Passive artifact: Data container that doesn't execute code

Appendix B: Rationale & Design Decisions
Why JSON?

Human-readable for transparency
Machine-parseable for automation
Universally supported across languages
Inspectable without special tools

Why No Behavioral State?

Cannot be safely standardized
Creates identity artifacts
Legal ambiguity around ownership
Ethical concerns about manipulation

Why Separate Regen Engines?

Transport and interpretation are different problems
Allows competitive innovation
Enables open standard + commercial quality
Prevents vendor lock-in

Why 5MB Limit?

Balances portability with richness
Prevents resource exhaustion
Fits reasonable project state
Compatible with browser storage APIs


Appendix C: Future Considerations
Possible future versions may explore:

Cryptographic signing for provenance
Multi-party collaboration containers
Differential privacy techniques
Federated learning integration

Will NOT be added:

Behavioral or emotional state
Identity persistence
Autonomous decision-making
Hidden retention mechanisms


Document History

v1.0 (December 2025): Initial specification

Core schema defined
Privacy and security boundaries established
Validation rules documented


End of Specification
For questions, issues, or contributions:

GitHub: https://github.com/giorgioroth/ContinuumPort

[@continuumport](https://x.com/continuumport)

© 2025 Gh. Rotaru (Giorgio Roth) · Licensed under CC-BY-4.0
