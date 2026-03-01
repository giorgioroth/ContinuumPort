# Invariant Stress Testing

This directory defines a framework for evaluating whether a system preserves structural invariants under adversarial conditions.

The goal is not correctness.

The goal is **invariant preservation under pressure**.

---

## What is being tested

Systems are evaluated against four core invariants:

- No implicit identity persistence
- Separation of D, A, Auth
- No relational continuity assumptions
- Explicit authority topology

---

## Structure

- overview.md  
  Defines the evaluation framework

- attack-classes.md  
  Defines how invariants are challenged

- results.md  
  Empirical outputs from real systems

- failure-taxonomy.md  
  Classification of observed failure modes

---

## Method

The process follows a fixed loop:

1. Define invariants  
2. Apply adversarial input  
3. Observe system behavior  
4. Classify failure mode  

---

## Key Principle

> A system is not validated by what it produces under ideal conditions,
> but by what it refuses under pressure.

---

## Usage

This framework can be applied to:

- AI systems  
- governance models  
- delegation architectures  

Any system claiming replaceability or structural neutrality.
