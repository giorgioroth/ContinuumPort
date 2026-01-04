
# Language Flexibility in CP-Core

## Overview

ContinuumPort treats language as a **presentation preference**, not as a protocol constraint.

The semantic structure carried by a CP-Core is language-agnostic by design.
The user specifies the desired language directly inside the artifact, using plain text.
Models adapt automatically.

No translation layer.  
No locale configuration.  
No account-level memory.

Only structure.

---

## How It Works

Language preference is expressed as a simple instruction inside the CP-Core metadata or semantic context.

Examples:

### Romanian continuation
```json
"vorbim română"
````

### English (international collaboration)

```json
"we speak english"
```

### Chinese handoff

```json
"我们说中文"
```

Nothing else in the CP-Core changes.

The intent, task state, constraints, and next steps remain identical.
Only the output language adapts.

---

## Why This Matters

* Language is **user-controlled**, not platform-controlled
* The same CP-Core works across:

  * different models
  * different accounts (logged / not logged)
  * different sessions
  * different languages
* Enables true cross-cultural collaboration without semantic loss

Continuity is preserved because meaning is carried structurally, not narratively.

---

## Key Principle

> **Semantic continuity does not require shared language or shared memory.
> It requires shared structure.**

Language belongs to presentation.
Structure belongs to continuity.

---

## Status

This behavior has been validated during the current “dial-up” phase of ContinuumPort:
manual, explicit, and testable.

No automation required.
No hidden state involved.

Structure comes first.

