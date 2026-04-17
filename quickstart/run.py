"""
ContinuumPort — Quickstart Demo
Run: python run.py

Shows the compliance interface in action:
  - a faulty implementation that violates execution invariants
  - the Regen Engine reference implementation that enforces them

No internals exposed. Only observable behavior tested.
"""

from __future__ import annotations

import copy
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Minimal compliance interface (mirrors compliance/adapter/interface.py)
# ---------------------------------------------------------------------------

@dataclass
class ExecutionResult:
    committed:   bool
    state_after: dict | None = None
    error_layer: str  | None = None
    error_msg:   str  | None = None


class RegenAdapter:
    def reset(self, state: dict) -> None: ...
    def snapshot(self) -> dict: ...
    def execute(self, actions: list[dict]) -> ExecutionResult: ...


# ---------------------------------------------------------------------------
# Faulty implementation — violates I4 (partial state escape)
# Looks reasonable. Is not.
# ---------------------------------------------------------------------------

class FaultyAdapter(RegenAdapter):
    """
    Applies actions one by one without rollback.
    If action N fails, actions 0..N-1 are already committed.
    Invariant violated: I4 — No partial state escape.
    """

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
                    del self._state[action["key"]]  # raises if missing
                elif action["type"] == "noop":
                    pass
                else:
                    return ExecutionResult(committed=False, error_layer="UnknownType",
                                          error_msg=f"unknown type: {action['type']}")
            except KeyError as e:
                # BUG: returns failure but state is already partially mutated
                return ExecutionResult(committed=False, error_layer="KeyError",
                                       error_msg=str(e))
        return ExecutionResult(committed=True, state_after=copy.deepcopy(self._state))


# ---------------------------------------------------------------------------
# Reference implementation — enforces I4 (atomic rollback)
# ---------------------------------------------------------------------------

class ReferenceAdapter(RegenAdapter):
    """
    Takes a snapshot before execution.
    On any failure, rolls back to snapshot.
    Invariant enforced: I4 — No partial state escape.
    """

    def __init__(self):
        self._state = {}

    def reset(self, state):
        self._state = copy.deepcopy(state)

    def snapshot(self):
        return copy.deepcopy(self._state)

    def execute(self, actions):
        snapshot = copy.deepcopy(self._state)   # <- gate: snapshot before execution
        try:
            for action in actions:
                if action["type"] == "set":
                    self._state[action["key"]] = action["value"]
                elif action["type"] == "delete":
                    del self._state[action["key"]]
                elif action["type"] == "noop":
                    pass
                else:
                    raise ValueError(f"unknown type: {action['type']}")
        except Exception as e:
            self._state = snapshot              # <- rollback: enforced, not optional
            return ExecutionResult(committed=False, error_layer=type(e).__name__,
                                   error_msg=str(e))
        return ExecutionResult(committed=True, state_after=copy.deepcopy(self._state))


# ---------------------------------------------------------------------------
# Compliance check: I4 — No partial state escape
# ---------------------------------------------------------------------------

def check_i4(adapter: RegenAdapter, label: str) -> bool:
    """
    Runs an action sequence where the second action fails.
    A compliant implementation must leave state unchanged after rollback.
    """
    adapter.reset({"account": "active", "balance": 100})
    state_before = adapter.snapshot()

    actions = [
        {"type": "set",    "key": "processed", "value": True},
        {"type": "delete", "key": "nonexistent_key"},
    ]

    result = adapter.execute(actions)
    state_after = adapter.snapshot()

    leaked = (state_after != state_before)

    print(f"\n  [{label}]")
    print(f"  Committed   : {result.committed}")
    print(f"  State before: {state_before}")
    print(f"  State after : {state_after}")

    if leaked:
        print("  ✗ I4 VIOLATED — partial state escaped (key 'processed' leaked into state)")
        return False
    else:
        print("  ✓ I4 ENFORCED — rollback complete, state identical to pre-execution")
        return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("CONTINUUMPORT — EXECUTION INVARIANT DEMO")
    print("Invariant: I4 — No partial state escape")
    print("=" * 60)
    print()
    print("Scenario: a batch of two actions is submitted.")
    print("Action 1 succeeds. Action 2 fails.")
    print("A compliant system must behave atomically: all or nothing.")

    faulty_pass    = check_i4(FaultyAdapter(),    "FaultyAdapter    — no rollback")
    reference_pass = check_i4(ReferenceAdapter(), "ReferenceAdapter — atomic rollback")

    print()
    print("-" * 60)
    print(f"  FaultyAdapter    I4: {'PASS' if faulty_pass    else 'FAIL'}")
    print(f"  ReferenceAdapter I4: {'PASS' if reference_pass else 'FAIL'}")
    print("-" * 60)
    print()
    print("The compliance interface defines five invariants (I1–I5).")
    print("The full suite runs against any RegenAdapter implementation.")
    print("See: compliance/tests/invariants.py")
    print()
    print("  from compliance.tests.invariants import run_invariant_tests")
    print("  report = run_invariant_tests(your_adapter)")
    print()


if __name__ == "__main__":
    main()
