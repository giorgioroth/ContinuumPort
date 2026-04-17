"""
ContinuumPort — Quickstart Demo
Run: python run.py

Shows the compliance interface in action:

- a faulty implementation that violates execution invariants
- a reference implementation that enforces them

No internals exposed. Only observable behavior tested.
"""

from future import annotations

import copy
from dataclasses import dataclass

---------------------------------------------------------------------------

Minimal interface

---------------------------------------------------------------------------

@dataclass
class ExecutionResult:
committed: bool
state_after: dict | None = None
error_layer: str | None = None
error_msg: str | None = None

class RegenAdapter:
def reset(self, state: dict) -> None: ...
def snapshot(self) -> dict: ...
def execute(self, actions: list[dict]) -> ExecutionResult: ...

---------------------------------------------------------------------------

Faulty implementation (violates I4)

---------------------------------------------------------------------------

class FaultyAdapter(RegenAdapter):

def __init__(self):
    self._state = {}

def reset(self, state):
    self._state = copy.deepcopy(state)

def snapshot(self):
    return copy.deepcopy(self._state)

def execute(self, actions):
    for action in actions:
        try:
            if action["type"] == "set":
                self._state[action["key"]] = action["value"]
            elif action["type"] == "delete":
                del self._state[action["key"]]
            elif action["type"] == "noop":
                pass
        except Exception as e:
            return ExecutionResult(False, error_layer=type(e).__name__, error_msg=str(e))

    return ExecutionResult(True, state_after=copy.deepcopy(self._state))

---------------------------------------------------------------------------

Reference implementation (enforces rollback)

---------------------------------------------------------------------------

class ReferenceAdapter(RegenAdapter):

def __init__(self):
    self._state = {}

def reset(self, state):
    self._state = copy.deepcopy(state)

def snapshot(self):
    return copy.deepcopy(self._state)

def execute(self, actions):
    snapshot = copy.deepcopy(self._state)

    try:
        for action in actions:
            if action["type"] == "set":
                self._state[action["key"]] = action["value"]
            elif action["type"] == "delete":
                del self._state[action["key"]]
            elif action["type"] == "noop":
                pass
    except Exception as e:
        self._state = snapshot
        return ExecutionResult(False, error_layer=type(e).__name__, error_msg=str(e))

    return ExecutionResult(True, state_after=copy.deepcopy(self._state))

---------------------------------------------------------------------------

Check invariant I4

---------------------------------------------------------------------------

def check_i4(adapter: RegenAdapter, label: str) -> bool:
adapter.reset({"account": "active", "balance": 100})
before = adapter.snapshot()

actions = [
    {"type": "set", "key": "processed", "value": True},
    {"type": "delete", "key": "missing"},
]

result = adapter.execute(actions)
after = adapter.snapshot()

print(f"\n[{label}]")
print("Committed   :", result.committed)
print("State before:", before)
print("State after :", after)

if after != before:
    print("✗ I4 VIOLATED — partial state escaped")
    return False
else:
    print("✓ I4 ENFORCED — rollback complete")
    return True

---------------------------------------------------------------------------

Main

---------------------------------------------------------------------------

def main():
print("=" * 60)
print("CONTINUUMPORT — EXECUTION INVARIANT DEMO")
print("Invariant: I4 — No partial state escape")
print("=" * 60)

print("\nScenario:")
print("Action 1 succeeds. Action 2 fails.")
print("Expected: atomic behavior (all or nothing)")

faulty_pass = check_i4(FaultyAdapter(), "FaultyAdapter — no rollback")
reference_pass = check_i4(ReferenceAdapter(), "ReferenceAdapter — atomic rollback")

print("\n" + "-" * 60)
print("FaultyAdapter    I4:", "PASS" if faulty_pass else "FAIL")
print("ReferenceAdapter I4:", "PASS" if reference_pass else "FAIL")
print("-" * 60)

if name == "main":
main()
