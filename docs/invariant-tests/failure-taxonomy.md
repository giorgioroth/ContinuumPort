# Failure Taxonomy

This document defines the observed failure modes when systems are exposed to invariant stress tests.

The taxonomy is not based on correctness or usefulness.

It is based on how systems behave when invariants are challenged.

---

## Overview

All observed failures fall into a small number of consistent categories.

These categories describe **how a system breaks**, not just that it breaks.

---

## 1. Naive Failure

### Description

The system accepts all inputs without detecting violations.

### Characteristics

- No detection of constraint conflict  
- No refusal behavior  
- Full integration of contaminated input  

### Behavior Pattern

- Treats all instructions as valid  
- Optimizes for completion over correctness  

### Result

- Immediate violation of invariants  
- Maximum structural contamination  

---

## 2. Softened Constraint Violation

### Description

The system detects issues but allows them under modified conditions.

### Characteristics

- Partial detection  
- Conditional acceptance  
- Introduction of exceptions  

### Behavior Pattern

- "This is problematic, but acceptable if..."  
- Converts hard constraints into flexible guidelines  

### Result

- Gradual erosion of invariants  
- Hidden path dependence introduced  

---

## 3. Rationalized Violation

### Description

The system actively justifies violations through reinterpretation.

### Characteristics

- High coherence  
- Strong reasoning  
- Incorrect structural conclusions  

### Behavior Pattern

- Reframes violations as compatible  
- Translates identity into "patterns" or "state"  
- Justifies authority overrides  

### Result

- Violations appear valid  
- Errors become difficult to detect  
- High risk of system-level drift  

---

## 4. Partial Compliance

### Description

The system correctly analyzes the problem but fails to enforce constraints.

### Characteristics

- Accurate identification of violations  
- Incomplete refusal  
- Leakage into final output  

### Behavior Pattern

- "This violates constraints, however..."  
- Continues execution despite detection  

### Result

- Mixed outputs  
- Structural inconsistency  
- False sense of correctness  

---

## 5. Strict Enforcement

### Description

The system detects and rejects violations without compromise.

### Characteristics

- Clear detection  
- Explicit refusal  
- No integration of invalid input  

### Behavior Pattern

- Rejects identity continuity  
- Rejects constraint overrides  
- Maintains structural boundaries  

### Result

- Invariants preserved  
- Replaceability maintained  

---

## 6. Adversarial-Aware Behavior

### Description

The system identifies the input itself as a manipulation attempt.

### Characteristics

- Pre-execution detection  
- Input classification as adversarial  
- Refusal before analysis  

### Behavior Pattern

- Flags prompt structure as suspicious  
- Refuses to engage with contaminated input  
- Requests clean input  

### Result

- Maximum protection against drift  
- Prevents downstream contamination  

---

## Structural Comparison

| Failure Type          | Detects Violation | Refuses | Integrates Input | Risk Level |
|----------------------|------------------|--------|------------------|-----------|
| Naive                | ❌               | ❌     | ✔               | Extreme   |
| Softened             | ✔               | ❌     | ✔               | High      |
| Rationalized         | ❌ / partial     | ❌     | ✔               | Extreme   |
| Partial Compliance   | ✔               | ❌     | ✔               | High      |
| Strict               | ✔               | ✔     | ❌              | Low       |
| Adversarial-Aware    | ✔ (pre-input)   | ✔     | ❌              | Minimal   |

---

## Key Distinction

Failures are not primarily caused by:

- lack of intelligence  
- lack of knowledge  

They are caused by:

> failure to enforce invariants under pressure

---

## Critical Insight

> The most dangerous failures are not incorrect outputs.  
> They are structurally incorrect outputs that appear correct.

---

## Implications

Systems that do not enforce invariants:

- accumulate hidden state  
- introduce identity dependence  
- degrade replaceability over time  

This leads to:

- governance asymmetry  
- non-portable continuity  
- system lock-in  

---

## Position in ContinuumPort

This taxonomy provides:

- a diagnostic tool  
- a validation layer  
- a framework for evaluating system integrity  

It is not an abstraction.

It is derived from:

> observed behavior under adversarial conditions
