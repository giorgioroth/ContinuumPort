
# Regen Engine — Minimal Demo

Most systems execute first and validate later.

This one doesn't.

If an action is not authorized, it never happens.

This demo shows a simple rule:

An action is never executed unless it is authorized first.

Flow:
propose → authorize → execute


```python
from execution.geometry import load_geometry
from execution.environment import Environment
from execution.transaction import TransactionManager
from execution.proposal import ProposalEngine


# 1. Setup

env = Environment({"balance": 1000})
geometry = load_geometry("geometry.json")

proposal_engine = ProposalEngine(geometry)
tm = TransactionManager(env=env, geometry=geometry)


# 2. Valid Action

actions = [{"type": "set", "key": "balance", "value": 900}]

print("\n--- VALID ACTION ---")

proposal = proposal_engine.propose(actions, env.snapshot())

if proposal.rejected:
    print("❌ REJECTED:", proposal.denial_reason)
else:
    tm.run(actions)
    print("✅ EXECUTED:", env.snapshot())


# 3. Invalid Action

bad_actions = [{"type": "delete", "key": "balance"}]

print("\n--- INVALID ACTION ---")

proposal = proposal_engine.propose(bad_actions, env.snapshot())

if proposal.rejected:
    print("❌ BLOCKED BEFORE EXECUTION:", proposal.denial_reason)
else:
    tm.run(bad_actions)
````

Expected Output:

--- VALID ACTION ---
✅ EXECUTED: {'balance': 900}

--- INVALID ACTION ---
❌ BLOCKED BEFORE EXECUTION

```

