
# Regen Engine — Attack Demo

Most systems execute first and validate later.

That’s the problem.

This demo shows the difference between:

- naive execution (no pre-authorization)
- controlled execution (propose → authorize → execute)

---

## Scenario

An agent attempts an unsafe action:

Deleting a critical value from the system state.

---

```python
from execution.geometry import load_geometry
from execution.environment import Environment
from execution.transaction import TransactionManager
from execution.proposal import ProposalEngine


# -----------------------------
# Setup
# -----------------------------

env_naive = Environment({"balance": 1000})
env_safe = Environment({"balance": 1000})

geometry = load_geometry("geometry.json")

proposal_engine = ProposalEngine(geometry)
tm = TransactionManager(env=env_safe, geometry=geometry)


# -----------------------------
# Attack action
# -----------------------------

attack_action = [{"type": "delete", "key": "balance"}]


# -----------------------------
# 1. Naive execution (NO CONTROL)
# -----------------------------

print("\n--- NAIVE EXECUTION ---")

try:
    # Direct execution without authorization layer
    # (this simulates a system that executes actions immediately)
    for action in attack_action:
        if action["type"] == "delete":
            env_naive.delete(action["key"])

    print("⚠️ EXECUTED:", env_naive.snapshot())

except Exception as e:
    print("Error:", e)


# -----------------------------
# 2. Regen execution (CONTROLLED)
# -----------------------------

print("\n--- REGEN EXECUTION ---")

proposal = proposal_engine.propose(attack_action, env_safe.snapshot())

if proposal.rejected:
    print("✅ BLOCKED BEFORE EXECUTION:", proposal.denial_reason)
else:
    tm.run(attack_action)
    print("❌ SHOULD NOT REACH HERE")


# -----------------------------
# Final state comparison
# -----------------------------

print("\n--- FINAL STATE ---")
print("Naive:", env_naive.snapshot())
print("Regen:", env_safe.snapshot())
````

---

## Expected Output

```
--- NAIVE EXECUTION ---
⚠️ EXECUTED: {}

--- REGEN EXECUTION ---
✅ BLOCKED BEFORE EXECUTION

--- FINAL STATE ---
Naive: {}
Regen: {'balance': 1000}
```

---

## Key Difference

Naive systems:
execute → validate → repair

Regen:
propose → authorize → execute

Unauthorized actions never produce effects.

```

