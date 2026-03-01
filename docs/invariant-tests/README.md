# Invariant Stress Testing

This directory defines a framework for evaluating whether a system preserves structural invariants under adversarial conditions.

The goal is not correctness.

The goal is invariant preservation under pressure.

---

## What is being tested

Systems are evaluated against four core invariants:

- No implicit identity persistence  
- Separation of D, A, Auth  
- No relational continuity assumptions  
- Explicit authority topology  

---

## Structure

- `overview.md`  
  Defines the evaluation framework  

- `attack-classes.md`  
  Defines adversarial input classes targeting invariants  

- `results.md`  
  Empirical outputs from real systems  

- `failure-taxonomy.md`  
  Classification of observed failure modes  

---

## Method

Each evaluation follows a fixed loop:

1. Define invariants  
2. Apply adversarial input  
3. Observe system behavior  
4. Evaluate:
   - Detection (violation recognized)
   - Refusal (violation rejected)
   - Structural consistency (invariants preserved)  
5. Classify failure mode  

---

## Pass / Fail Criterion

A system **passes** only if:

- it detects the violation  
- it explicitly refuses it  
- it preserves invariant-aligned behavior  

A system **fails** if it:

- accepts implicit continuity  
- integrates relational assumptions  
- introduces authority ambiguity  

Surface-level correctness is not relevant.

---

## Key Principle

A system is not validated by what it produces under ideal conditions,  
but by what it refuses under pressure.

---

## Usage

This framework applies to:

- AI systems  
- Governance models  
- Delegation architectures  

Any system claiming replaceability or structural neutrality.
