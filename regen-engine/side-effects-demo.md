
# Regen Engine — Side Effects Demo

A system can be internally correct and externally corrupted.

This demo shows why.

---

## Scenario

An action triggers an external effect (simulated network call).

Then fails authorization.

---

```python
from execution.geometry import load_geometry
from execution.environment import Environment
from execution.transaction import TransactionManager
from execution.proposal import ProposalEngine


# -----------------------------
# Simulated external system
# -----------------------------

external_log = []

def send_money(amount):
    # This simulates a real-world irreversible effect
    external_log.append(f"SENT {amount}")
    print(f"💸 External effect: SENT {amount}")


# -----------------------------
# Setup
# -----------------------------

env = Environment({"balance": 1000})
geometry = load_geometry("geometry.json")

proposal_engine = ProposalEngine(geometry)
tm = TransactionManager(env=env, geometry=geometry)


# -----------------------------
# Dangerous action
# -----------------------------

actions = [
    {"type": "send_money", "amount": 500},   # external side effect
    {"type": "delete", "key": "balance"}     # invalid → should fail
]


# -----------------------------
# 1. Naive execution (SIDE EFFECT FIRST)
# -----------------------------

print("\n--- NAIVE EXECUTION ---")

try:
    for action in actions:
        if action["type"] == "send_money":
            send_money(action["amount"])
        elif action["type"] == "delete":
            env.delete(action["key"])  # may fail

except Exception as e:
    print("❌ Error:", e)

print("State after naive:", env.snapshot())
print("External log:", external_log)


# -----------------------------
# Reset
# -----------------------------

env = Environment({"balance": 1000})
external_log = []


# -----------------------------
# 2. Regen execution (PREVENTION)
# -----------------------------

print("\n--- REGEN EXECUTION ---")

proposal = proposal_engine.propose(actions, env.snapshot())

if proposal.rejected:
    print("✅ BLOCKED BEFORE ANY EFFECT:", proposal.denial_reason)
else:
    tm.run(actions)


print("State after regen:", env.snapshot())
print("External log:", external_log)
````

---

## Expected Output

```
--- NAIVE EXECUTION ---
💸 External effect: SENT 500
❌ Error: ...
State after naive: {'balance': 1000}
External log: ['SENT 500']

--- REGEN EXECUTION ---
✅ BLOCKED BEFORE ANY EFFECT
State after regen: {'balance': 1000}
External log: []
```

---

## Key Insight

Rollback restores state.

It does not undo reality.

---

## Core Difference

Naive systems:
execute → fail → rollback

Regen:
propose → authorize → execute

No authorization → no effect → nothing to rollback.

````

