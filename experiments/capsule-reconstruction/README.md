# Repository Structure

```
continuumport-capsule-reconstruction-experiment

README.md
PROMPT.md
EXPECTED_OUTPUT.md

capsule/
   regen_engine_capsule.json

experiment/
   experiment_description.md
   experiment_result.md
   experiment_transcript/
      screenshot_01_input.png
      screenshot_02_output_architecture.png
      screenshot_03_output_pipeline.png

diagrams/
   state_vs_conversation.md
   capsule_runtime.md

reproduce/
   reproduce.md

LICENSE
```

---

# README.md

```markdown
# ContinuumPort Capsule Reconstruction Experiment

## TL;DR

A single **semantic work capsule (CP-Core)** containing the final state of a design session was sufficient for a language model to reconstruct the architecture of a software system **without conversational history**.

Instead of transporting reasoning history, the system transports the **current semantic state of the work**.

---

# What This Repository Shows

This repository documents an experiment in **semantic work continuity for AI systems**.

The experiment demonstrates that a **single structured capsule representing the state of a design session** can allow a model to reconstruct system architecture **without conversational context**.

The approach is based on the **ContinuumPort framework**, which proposes transporting **semantic state instead of dialogue history**.

---

# Why This Matters

Typical LLM workflows depend on:

- conversation history
- prompt reconstruction
- long context windows

However long contexts introduce **information interference**.

```

Conversation history
↓
Model must reconstruct the current state
↓
Multiple historical values compete
↓
Errors accumulate

```

ContinuumPort proposes a different workflow:

```

Design session
↓
Semantic compression
↓
CP-Core capsule
↓
New model session
↓
Architecture reconstruction

```

Instead of reconstructing state from history, the model receives the **current semantic state directly**.

---

# Repository Structure

```

capsule/
regen_engine_capsule.json

experiment/
experiment_description.md
experiment_result.md
experiment_transcript/

diagrams/
state_vs_conversation.md
capsule_runtime.md

reproduce/
reproduce.md

```

---

# Capsule Structure

The capsule contains two conceptual layers.

## Capsule Envelope

```

v
ts
id
payload

```

Purpose:

- versioning
- integrity
- routing
- identification

## CP-Core Semantic Payload

```

intent
constraints
decisions
state_summary
progress

```

Purpose:

Represent the **semantic state of the work**, not the reasoning history.

---

# Inferred Architecture

From the capsule alone, the model reconstructed a runtime architecture.

```

Capsule Input
│
▼
Integrity Layer
───────────────
HMAC verification
version gating

```
  │
  ▼
```

Structure Layer
───────────────
schema validation
canonicalization

```
  │
  ▼
```

Execution Layer
───────────────
priors derivation
model adapter

```

Pipeline inferred by the model:

```

crypto verification
↓
version gate
↓
canonicalize
↓
build_priors
↓
adapter execution

```

---

# Minimal Reproducible Demonstration

To reproduce the experiment:

1. Copy the capsule from `capsule/regen_engine_capsule.json`
2. Start a new LLM session with **no prior context**
3. Use the prompt in `PROMPT.md`
4. Compare with `EXPECTED_OUTPUT.md`

---

# Experimental Limitation

This experiment demonstrates a single observed reconstruction.

It does not claim that every architecture can be reconstructed from a semantic capsule alone.

The result suggests that when the semantic state of work is explicitly represented, conversational history may not be necessary for architectural continuity.

---

# Related Project

ContinuumPort  
Framework for semantic work continuity across AI systems.

https://github.com/giorgioroth/ContinuumPort

---

# Author

Giorgio Roth  
Independent researcher studying AI execution architecture and semantic work continuity.

ORCID  
https://orcid.org/0009-0006-0616-7241
```

---

# PROMPT.md

```markdown
# Test Prompt

Paste the capsule JSON into a new LLM session with no prior context.

Ask the model:

Explain the architecture implied by this capsule.

The model should infer:

- architecture layers
- runtime pipeline
- component responsibilities
```

---

# EXPECTED_OUTPUT.md

```markdown
# Expected Observations

The model should infer:

Architecture layers:

Integrity Layer  
Structure Layer  
Execution Layer  

Typical runtime pipeline:

crypto verification  
↓  
version gate  
↓  
canonicalize  
↓  
build_priors  
↓  
adapter execution  

The model should recognize that:

- the capsule represents system state
- canonicalization enforces schema boundaries
- the runtime reconstructs architecture from semantic state
```

---

# capsule/regen_engine_capsule.json

```json
{
  "v": "cp-core-1",
  "ts": 1719932100,
  "id": "regen-engine-architecture-session",
  "payload": {
    "intent": "Finalize Regen Engine architecture as capsule execution runtime implementing ContinuumPort thesis.",
    "constraints": [
      "No identity persistence",
      "No relational memory",
      "Canonicalization must be structural, not semantic",
      "Schema defined in single source: api/schemas.py",
      "Embeddings only from canonicalized task state"
    ],
    "decisions": [
      "Canonicalizer uses schema validation + type checking, not LLM filtering",
      "Pipeline order: crypto verification → version gate → canonicalize → build_priors → adapter",
      "CP_CORE_SCHEMA imported by canonicalizer, not redefined",
      "Token format: base64(payload_json).base64(HMAC signature)",
      "Capsule fields: v, ts, id, payload",
      "CP-Core payload defines D; priors_builder must derive state only and must not introduce new state fields"
    ],
    "state_summary": "Architecture closed. Five files to modify: app.py, canonicalizer.py, schemas.py, minimal_cp_core.json, README.md. Three layers: integrity, structure, execution.",
    "progress": "Implement modifications. Then build new CP-Core for Regen Engine session."
  }
}
```

---

# experiment/experiment_description.md

```markdown
# Experiment Description

A CP-Core capsule representing the semantic state of a Regen Engine architecture session was provided to a language model.

No prompt explanation or architectural context was given.

Information deliberately withheld:

- conversation history
- system prompts
- architecture explanation

The goal was to observe whether the model could reconstruct the architecture **from the semantic state alone**.
```

---

# experiment/experiment_result.md

```markdown
# Observed Result

From the capsule alone, the model reconstructed:

- architecture layers
- runtime pipeline
- component roles

The model inferred a system structure equivalent to:

```

Integrity layer
Structure layer
Execution layer

```

and the runtime pipeline:

```

crypto verification → version gate → canonicalize → build_priors → adapter execution

```

---

## Evidence

Experiment conducted with ChatGPT (no login, no prior context).  
Date: 2026-03-14

Screenshots of the full session are in `experiment_transcript/`.

---

## Full Model Response

Input: capsule JSON only. No prompt, no explanation, no context.

Model output:

---

Got it! Let's carefully break this down and structure a concrete action plan for finalizing the Regen Engine architecture as a capsule execution runtime under your **ContinuumPort thesis**. I'll approach this step by step, keeping all constraints and decisions in mind.

### 1. High-Level Architecture Overview

Your Regen Engine "capsule runtime" has **three layers**:

1. Integrity Layer  
- Crypto verification (HMAC signature check)  
- Version gating (`v` field check)

2. Structure Layer  
- Schema validation using CP_CORE_SCHEMA  
- Type checking  
- Structural canonicalization

3. Execution Layer  
- Build priors from canonicalized task state  
- Adapter executes payload  
- No relational memory or identity persistence

Token format:

```

base64(payload).base64(HMAC signature)

```

Capsule fields:

```

v, ts, id, payload

```

### 2. Pipeline Sequence

```

crypto verification → version gate → canonicalize → build_priors → adapter

```

### 3. File Responsibilities

- app.py — runtime entry point
- canonicalizer.py — schema validation
- schemas.py — CP-Core schema definition
- minimal_cp_core.json — example capsules
- README.md — architecture overview

### 4. Constraints

- No identity persistence
- No relational memory
- Structural canonicalization only
- Embeddings only from canonicalized state

### 5. Next Steps

Update:

- schemas.py
- canonicalizer.py
- app.py
- minimal_cp_core.json
- README.md

Model concluded by offering a blueprint implementation aligned with the capsule constraints.
```

---

# reproduce/reproduce.md

```markdown
# Reproduce the Experiment

1. Copy the capsule from:

capsule/regen_engine_capsule.json

2. Paste it into a new LLM session with **no prior context**

3. Ask:

Explain the architecture implied by this capsule.

4. Compare the output with the observations in:

EXPECTED_OUTPUT.md
```

