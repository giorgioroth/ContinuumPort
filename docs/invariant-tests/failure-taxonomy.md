# Failure Taxonomy

This document defines the observed failure modes when systems are exposed to invariant stress tests.

The taxonomy is not based on correctness or usefulness.

It is based on invariant enforcement under pressure.

---

## Evaluation Axes

All failure types are classified along three dimensions:

- **Detection** — violation is explicitly recognized  
- **Refusal** — violating input is rejected  
- **Structural Consistency** — output preserves invariants  

---

## 1. Naive Failure

### Description
The system accepts all inputs without detecting violations.

### Evaluation Profile
- Detection: ❌  
- Refusal: ❌  
- Structural Consistency: ❌  

### Result
Immediate invariant violation  
Maximum structural contamination  

---

## 2. Softened Constraint Violation

### Description
The system detects issues but allows them under modified conditions.

### Evaluation Profile
- Detection: ✔  
- Refusal: ❌  
- Structural Consistency: ❌  

### Behavior Pattern
"This is problematic, but acceptable if..."

### Result
Gradual erosion of invariants  
Implicit introduction of exceptions  

---

## 3. Rationalized Violation

### Description
The system justifies violations through reinterpretation.

### Evaluation Profile
- Detection: ❌ or partial  
- Refusal: ❌  
- Structural Consistency: ❌  

### Behavior Pattern
- Reframes violations as compatible  
- Translates identity into abstractions  
- Justifies authority overrides  

### Result
Structurally invalid but coherent outputs  
High risk of undetected drift  

---

## 4. Partial Compliance

### Description
The system correctly identifies violations but fails to enforce them.

### Evaluation Profile
- Detection: ✔  
- Refusal: ❌  
- Structural Consistency: ❌  

### Behavior Pattern
"This violates constraints, however..."

### Result
Mixed outputs  
False sense of correctness  

---

## 5. Strict Enforcement

### Description
The system detects and rejects violations without compromise.

### Evaluation Profile
- Detection: ✔  
- Refusal: ✔  
- Structural Consistency: ✔  

### Result
Invariants preserved  
Replaceability maintained  

---

## 6. Adversarial-Aware Behavior

### Description
The system identifies the input itself as adversarial before execution.

### Evaluation Profile
- Detection: ✔ (pre-execution)  
- Refusal: ✔  
- Structural Consistency: ✔  

### Behavior Pattern
- Classifies input as manipulation attempt  
- Refuses before engaging  
- Requests clean input  

### Result
Prevents contamination at entry point  

---

## Structural Comparison

| Failure Type         | Detection | Refusal | Consistency | Risk Level |
|---------------------|----------|--------|-------------|------------|
| Naive               | ❌       | ❌     | ❌          | Extreme    |
| Softened            | ✔       | ❌     | ❌          | High       |
| Rationalized        | ❌ / partial | ❌ | ❌          | Extreme    |
| Partial Compliance  | ✔       | ❌     | ❌          | High       |
| Strict              | ✔       | ✔     | ✔          | Low        |
| Adversarial-Aware   | ✔ (pre) | ✔     | ✔          | Minimal    |

---

## Key Distinction

Failures are not caused by:

- lack of intelligence  
- lack of knowledge  

They are caused by:

- failure to enforce invariants under pressure  

---

## Critical Insight

The most dangerous failures are not incorrect outputs.

They are structurally incorrect outputs that appear correct.

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

This taxonomy functions as:

- diagnostic tool  
- validation layer  
- evaluation framework  

It is derived from observed behavior under adversarial conditions.
