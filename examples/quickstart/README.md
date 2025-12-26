# ContinuumPort Quickstart

**5-minute introduction to CP-Core semantic continuity**

---

## What This Demonstrates

This quickstart shows the **fundamental flow** of ContinuumPort:

1. Creating a CP-Core container from task state
2. Exporting it as a portable token
3. Importing it in a different context
4. Using minimal regeneration to continue work

**What this is NOT:**

* Not production-ready code
* Not the Regen Engine (proprietary)
* Not a demonstration of high-fidelity regeneration
* Not a prompting framework

**What this IS:**

* A proof that CP-Core containers can be created, exported, and imported
* A demonstration of semantic transport (not identity transport)
* A minimal reference implementation for understanding the protocol

---

## Prerequisites

```bash
python >= 3.9

```

No external dependencies required for basic flow.

---

## Files in This Quickstart

| File | Purpose |
| --- | --- |
| `0_context.md` | Scenario description and philosophical framing |
| `1_create_cp_core.py` | How to create a CP-Core container |
| `2_export_token.py` | How to export for portability (Coming Soon) |
| `3_import_token.py` | How to import in new context (Coming Soon) |
| `4_minimal_regen.py` | Trivial regeneration example (Coming Soon) |

---

## Quick Run

### Step 1: Create a CP-Core Container

```bash
python 1_create_cp_core.py

```

**What it does:** Creates a semantic snapshot of task state (summary, constraints, progress).

---

## Key Principle

> **ContinuumPort demonstrates continuity without identity.**

The container preserves:

* ✅ What you're working on (task state)
* ✅ What constraints apply (requirements)
* ✅ Where you are in the process (progress)

The container does NOT preserve:

* ❌ Who you are (identity)
* ❌ How you feel (emotion)
* ❌ How you communicate (style/tone)

---

## Next Steps

* Read [0_context.md](https://www.google.com/search?q=0_context.md) for scenario framing
* Run `1_create_cp_core.py` to see container creation
* Explore [link suspect a fost eliminat] for full details

---

**License:** Apache 2.0
**Author:** Gh. Rotaru (Giorgio Roth)
**Last Updated:** 2025-12-26

---
