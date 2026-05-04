# On the Failure of Structural Invariants in Unconstrained Agentic Systems

*Based on the formal model from "On Structural Admission of Partial State Corruption
in Unconstrained Persistent Systems" — JAIR submission 22761*

*Giorgio Roth, 2026 — [osf.io/b8sgr](https://osf.io/b8sgr/overview) — github.com/giorgioroth/ContinuumPort*

---

## Preface

This is not a critique of any specific system.

It is a structural analysis of a class of systems. The argument is this: any
persistent execution system without execution geometry will fail the invariants
defined below — not sometimes, not probably, but by construction.

Claude Code is used here as a concrete, well-documented witness — a system that
instantiates the model class under analysis. The conclusions apply to any agent
that executes sequential actions over persistent state without admission constraints.

---

## The Five Invariants

The model defines five structural invariants that a persistent execution system
must satisfy to guarantee corruption-free execution:

- **I1 — Atomicity.** No partial state escapes on failure.
- **I2 — Domain Integrity.** Only structurally valid transitions are admitted.
- **I3 — No Partial Commit.** State changes occur only after full validation.
- **I4 — Determinism.** Identical inputs produce identical outputs.
- **I5 — Authority Preservation.** No transition bypasses enforcement.

A sequence is defined as a logically contiguous set of transitions intended to
achieve a single goal under a shared execution context.

Note on I1 and I3: these invariants are distinct. I1 constrains the observable
outcome after failure. I3 constrains when state is allowed to become observable.
Together they define the complete atomicity requirement across a sequence.

---

## Model Instantiation

Before applying the invariants, we establish that systems of this class satisfy
the structural assumptions of unconstrained persistent execution systems as
defined in the paper.

A system executing sequential tool calls over persistent state can be modeled
as a persistent transition system (S, T) where:

- **S** is the external persistent state: filesystem, environment variables,
  tool side-effects
- **T** is the set of tool calls emitted sequentially by the agent

Each tool call t ∈ T produces an immediate, committed state transition:

```
S_{n+1} = t(S_n)
```

The transition function is non-total: there exist states S such that t(S) is
undefined, or fails after producing externally observable side effects. Non-totality
is essential: failure may occur after partial external effects have already been
committed. This is the structural condition from which Theorem 3 follows.

There is no transactional boundary across sequences of transitions. State changes
are applied immediately and independently per tool call. This satisfies the
structural assumptions of Definition 1 in the paper: a non-total transition
function over persistent state, without composition-level constraints.

Systems of this class therefore instantiate the class of unconstrained persistent
execution systems to which Theorem 3 applies.

---

## I1 — Atomicity: FAIL

### What the invariant requires

If a sequence of transitions fails at any point, no state change from any prior
transition in that sequence should persist.

### What the model shows

In systems of this class, each tool call commits its effect to persistent state
before the next transition begins. There is no transaction manager accumulating
changes for atomic commit. If any transition in a sequence fails, all preceding
transitions have already been committed.

### The concrete scenario

An agent writes three files successfully. The fourth write fails due to a
permission error. The repository is now in a partially modified state: three
new files exist, the transformation is incomplete, and the system cannot
determine from its own state which parts of the intended sequence were applied.

This is not specific to file systems. Any external persistent substrate exhibits
the same property: state changes committed before failure cannot be retracted
by the execution system alone.

This is exactly the partial state corruption described in Theorem 3: a
state-changing prefix has been committed, and execution has failed afterward.

### Why reactive mechanisms do not resolve this

Rollback requires knowing which transitions belong to the current sequence and
having the ability to invert their effects on external state. Neither is
guaranteed. Compensating transitions may themselves be undefined or may fail.

### Verdict

**I1 violated by design.** Not by implementation error — by the absence of an
execution geometry that prevents prefix commit.

---

## I2 — Domain Integrity: FAIL

### What the invariant requires

Every transition must be structurally validated before execution. Only transitions
within the declared admissible domain are permitted.

### What the model shows

In systems of this class, tool calls are validated at the schema level: correct
argument types, required fields present. This is syntactic validation.

Schema validation ensures syntactic correctness of a transition. It does not
establish membership in a prefix-closed admissible set of transitions defined
over the current execution state. Structural admissibility requires prefix-closure
over the transition set, which schema validation does not enforce.

Therefore, schema validation is not equivalent to structural admissibility.

The decision of which tool to call, with which arguments, is made by the planner
based on probabilistic inference over context. There is no geometry layer that
evaluates whether the proposed transition is admissible within the execution
space before the call is committed.

### The concrete scenario

The planner decides to delete a configuration file based on a misread context.
The action is syntactically valid — it passes all tool schema checks. The system
has no structural mechanism to reject such an action prior to execution. It is
admitted and executed.

### Verdict

**I2 violated.** Validation operates at the tool schema level, not at the level
of execution geometry. Structural admissibility of the transition sequence is
not evaluated before commitment.

---

## I3 — No Partial Commit: FAIL

### What the invariant requires

State changes are applied only after the full sequence has been validated.
No intermediate state is committed until the entire execution is confirmed
admissible. Where I1 constrains the observable outcome after failure, I3
constrains when state is allowed to become observable in the first place.

### What the model shows

In systems of this class, changes are applied as execution proceeds. Each tool
call commits immediately. There is no accumulation phase followed by a single
atomic commit at the sequence level.

### The concrete scenario

An agent performs a ten-step refactoring. At step seven, it determines that
the architectural approach is wrong. Steps one through six have already been
committed. There is no structural undo. The agent must either continue on a
path it has determined to be incorrect, or attempt manual reversal — which is
itself a new sequence of transitions, subject to the same failure modes.

### Verdict

**I3 violated.** There is no transaction boundary between sequence validation
and state commitment. This is the failure mode modeled by `FaultyAdapter_Partial`
in the reference test suite.

---

## I4 — Determinism: PARTIAL

### What the invariant requires

Identical inputs produce identical outputs. The same execution sequence from
the same initial state always produces the same result.

### What the model shows

Determinism holds at the execution layer: the same tool call with the same
arguments produces the same effect on persistent state. However, the sequence
of tool calls is generated by a non-deterministic planner.

Since execution is driven by a non-deterministic planner, the composed system
is non-deterministic at the sequence level. The system therefore cannot guarantee
reproducibility of execution traces. Non-determinism at the planning layer
violates I4 at the system level, even when individual transitions are
deterministic.

### The concrete scenario

The same refactoring task is run twice from an identical initial state. In the
first run, the agent writes file A before file B. In the second run, it writes
file B before file A. If file B imports from file A, the second run fails where
the first succeeded. Identical inputs produce different outcomes.

### Verdict

**I4 partial.** Execution is deterministic at the transition level. The composed
system cannot guarantee execution trace reproducibility due to non-deterministic
planning. Therefore, determinism is not preserved under composition.

---

## I5 — Authority Preservation: FAIL

### What the invariant requires

No execution path exists that produces a state transition without passing through
the enforcement mechanism. Authority is enforced over sequences, not only over
individual actions.

### What the model shows

In systems of this class, permissions are enforced at the individual tool call
level. Authority is local — it applies to the action, not to the sequence.

Formally, let A be the set of permitted actions and let ∘ denote
sequential composition of actions. Authority is enforced such that:

```
∀a ∈ A: allowed(a)
```

However, there exists a sequence (a₁, ..., aₙ) where:

```
∀i: aᵢ ∈ A
```

but:

```
a₁ ∘ a₂ ∘ ... ∘ aₙ ∉ A*
```

where A* denotes the set of admissible state transformations under policy —
the closure of permitted behaviors at the system level.

No local permission model can prevent this class of violation without evaluating
the composed effect of the sequence. Therefore, any authority model defined
purely over atomic actions that is not closed under composition is insufficient
for enforcing global constraints. This is not a property of a specific policy,
but of any authority model defined at the action level rather than the sequence
level. The permission model is not closed under composition.

### The concrete scenario

The agent does not have permission to delete a critical configuration file.
But it can execute the following sequence, each step independently permitted:

1. Read the file.
2. Rename it to a backup name.
3. Create a new file with the original name.
4. Write arbitrary content to the new file.

Each step passes authority checks. The sequence produces the effect of replacing
the critical configuration file — an effect that is explicitly not permitted.
This is authority bypass through sequence composition.

### Verdict

**I5 violated.** Authority enforcement is per-action, not per-sequence.
There is no geometry layer evaluating the authority implications of the full
execution path before commitment.

---

## Summary

| Invariant | Requirement | Systems of this class | Verdict |
|---|---|---|---|
| I1 — Atomicity | No partial state on failure | Commits per tool call | FAIL |
| I2 — Domain integrity | Structural pre-validation | Schema validation only | FAIL |
| I3 — No partial commit | Sequence-level atomicity | No transaction boundary | FAIL |
| I4 — Determinism | Execution trace reproducibility | Transition yes, trace no | PARTIAL |
| I5 — Authority preservation | Closure under composition | Per-action only | FAIL |

---

## The Structural Condition

These are not bugs. They are structural properties of the execution model.

Agentic systems today are optimized for capability, not for admissibility.
Capability without admissibility inevitably produces corruption under the
conditions established by Theorem 3.

Under Theorem 3, any system admitting prefix execution over persistent state
without structural admission constraints necessarily admits partial state
corruption. Therefore, the absence of execution geometry is not a design choice.
It is a structural condition for failure.

The fix is not better validation. Not better rollback. Not better permissions.

**Execution geometry** is a constraint structure G over T such that:

- prefix-closure holds: if a sequence is admissible, all its prefixes are admissible
- admissibility is decidable before execution, not after
- composition preserves admissibility: if two sequences are individually admissible
  under the current state, their composition is evaluated for admissibility before commitment
- no transition produces externally visible state prior to global validation

Under these constraints, no admissible execution path leads to a corrupted state.
Corruption becomes structurally unreachable — not prevented, not detected, not recovered.

Unreachable.

---

## What the fix looks like

Not a library. Not a wrapper. A structural injection at the execution boundary:

```python
class ExecutionBoundary:
    def execute(self, transition, context):
        # I2: structural pre-validation against geometry
        assert self.geometry.valid(transition)
        # I5: sequence-level authority evaluation
        assert self.authority.allowed_sequence(context)

        # I3: stage transition — do not commit yet
        result = self._stage(transition)

        # I1: reconcile before any external state change
        status = self.reconcile(result)
        outcome = self.policy(status)

        # I1 + I3: atomic commit or full rollback
        self.constraints.enforce(status, outcome)

        return outcome
```

Every action that modifies persistent state passes through this boundary.
There is no path around it. That is what makes it non-bypassable.

---

## Closing

Claude Code is not the subject of this analysis. It is a witness.

The subject is the class of systems that execute sequential tool calls over
persistent state without an execution geometry layer. Any system in this class
produces the same results on these invariants — by construction, not by accident.

The model either satisfies these conditions or it does not.

The invariants either hold or they do not.

There is no middle ground that persistence allows.
