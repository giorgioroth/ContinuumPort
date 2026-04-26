# The Case

Your agent executed two actions.

Action 1 succeeded.  
Action 2 failed.

**What is your system's state now?**

Not what you think. What you can prove.

---

## Without structural execution control

```
[FaultyAdapter — no rollback]

State before: {'account': 'active', 'balance': 100}

Execution:
  Action 1: processed = True   → OK
  Action 2: transfer funds     → FAILED

State after:  {'account': 'active', 'balance': 100, 'processed': True}

✗ VIOLATION — partial state escaped
```

The system reported failure.  
The state mutated anyway.

You now have no valid snapshot:

- You cannot assert what committed
- You cannot safely retry
- You cannot safely continue

This is not a corner case.  
**This is the default failure mode of non-atomic systems.**

---

## With Regen Engine

```
[ContinuumPort — atomic rollback]

State before: {'account': 'active', 'balance': 100}

Execution:
  Action 1: processed = True   → OK
  Action 2: transfer funds     → FAILED

State after:  {'account': 'active', 'balance': 100}

✓ ENFORCED — state invariance under failure
```

Failure occurred.  
No state transition survived.

Not by retry logic.  
Not by compensating actions.  
Not by post-hoc cleanup.

**By construction.**

---

## Run it yourself

```bash
git clone https://github.com/giorgioroth/ContinuumPort
cd ContinuumPort/quickstart
python run.py
```

No dependencies. Deterministic output in seconds.

---

## What this means for your system

When execution fails mid-task:

- Can you reconstruct the exact state?
- Can you prove absence of partial commits?
- Can you retry without semantic drift?

If any answer is no — your system is already operating on **undefined state space**.

---

## The guarantee

```
execute(α) ⟺ authorize(G, α)
```

A transition exists iff it is permitted by the declared execution geometry.

- Not detected after execution
- Not corrected after failure
- **Not reachable**

---

## If you've already seen the failure

Then you already know:

Partial state is not a bug.  
**It is a structural leak.**

→ access@continuumport.com  
→ [ContinuumPort](https://github.com/giorgioroth/ContinuumPort)  
→ [Formal model/DOI](https://doi.org/10.17605/OSF.IO/AZEC2)

---

*Gh. Rotaru (Giorgio Roth) — 2026*
