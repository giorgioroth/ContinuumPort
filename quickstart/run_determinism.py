"""
ContinuumPort — Determinism Demo
Run: python run_determinism.py

Shows how non-deterministic execution violates invariant I5.

Same input. Same initial state.
Different outputs → violation.

The failure demonstrated here does not use randomness.
It uses a realistic source of non-determinism: execution order
that depends on iteration over an unordered structure.

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
# Faulty implementation — violates I5 (non-determinism)
#
# The bug: the adapter accumulates an internal _pending set of keys
# modified across calls and flushes them in a different order each time,
# depending on how many prior executions have run.
#
# A subtler version of this pattern appears in real systems when
# execution depends on mutable internal bookkeeping that is not reset
# between cycles. The adapter looks stateless from the outside — it
# accepts reset() — but carries hidden ordering state that affects output.
#
# This is the realistic failure mode: not random.randint, but implicit
# state that survives between executions and changes ordering.
#
# Looks like an optimization. Is a violation.
# ---------------------------------------------------------------------------

class FaultyAdapter(RegenAdapter):
    """
    Carries hidden internal state that affects execution order.
    Output depends on execution history, not only on declared input.
    Invariant violated: I5 — Deterministic outcome.
    """

    def __init__(self):
        self._state = {}
        self._call_count = 0  # hidden: not reset by reset()

    def reset(self, state):
        self._state = copy.deepcopy(state)
        # BUG: _call_count is NOT reset — it persists across resets

    def snapshot(self):
        return copy.deepcopy(self._state)

    def execute(self, actions):
        self._call_count += 1
        # BUG: odd-numbered calls apply actions in declared order;
        #      even-numbered calls apply them in reverse order.
        #      From outside, reset() was called — caller expects clean state.
        ordered = list(actions)
        if self._call_count % 2 == 0:
            ordered = list(reversed(ordered))
        for action in ordered:
            if action["type"] == "set":
                self._state[action["key"]] = action["value"]
        return ExecutionResult(committed=True, state_after=copy.deepcopy(self._state))


# ---------------------------------------------------------------------------
# Reference implementation — enforces I5 (deterministic)
#
# Actions execute in declared order. First write wins when targeting
# the same key — or last write wins — but the rule is explicit and stable.
# ---------------------------------------------------------------------------

class ReferenceAdapter(RegenAdapter):
    """
    Executes actions in declared order.
    Same input sequence always produces the same output.
    Invariant enforced: I5 — Deterministic outcome.
    """

    def __init__(self):
        self._state = {}

    def reset(self, state):
        self._state = copy.deepcopy(state)

    def snapshot(self):
        return copy.deepcopy(self._state)

    def execute(self, actions):
        for action in actions:
            if action["type"] == "set":
                self._state[action["key"]] = action["value"]
            elif action["type"] == "delete":
                self._state.pop(action["key"], None)
            elif action["type"] == "noop":
                pass
            else:
                return ExecutionResult(committed=False, error_layer="UnknownType",
                                       error_msg=f"unknown type: {action['type']}")
        return ExecutionResult(committed=True, state_after=copy.deepcopy(self._state))


# ---------------------------------------------------------------------------
# Compliance check: I5 — Deterministic outcome
#
# Two action sequences that should produce the same result.
# A compliant system produces identical outputs for identical inputs.
# ---------------------------------------------------------------------------

def check_i5(adapter: RegenAdapter, label: str) -> bool:
    """
    Submits the same action sequence twice from the same initial state.
    A compliant implementation must produce identical outputs.
    """
    initial_state = {"x": 0}

    # Two actions targeting the same key with different values.
    # Declared order: "set x=1" then "set x=2" → final value must be 2.
    # A non-deterministic adapter may apply them in reverse on the second call.
    actions = [
        {"type": "set", "key": "x", "value": 1},
        {"type": "set", "key": "x", "value": 2},
    ]

    adapter.reset(copy.deepcopy(initial_state))
    adapter.execute(actions)
    first = adapter.snapshot()

    adapter.reset(copy.deepcopy(initial_state))
    adapter.execute(actions)
    second = adapter.snapshot()

    print(f"\n  [{label}]")
    print(f"  Run 1 result: {first}  (expected: x=2)")
    print(f"  Run 2 result: {second}  (expected: x=2)")

    if first != second:
        print(f"  ✗ I5 VIOLATED — same input, different outputs across executions")
        return False
    elif first != {"x": 2}:
        print(f"  ✗ I5 VIOLATED — stable but incorrect output (expected x=2, got x={first['x']})")
        return False
    else:
        print(f"  ✓ I5 ENFORCED — identical correct output across executions")
        return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("CONTINUUMPORT — DETERMINISM DEMO")
    print("Invariant: I5 — Deterministic outcome")
    print("=" * 60)
    print()
    print("Scenario: identical input is executed twice from identical state.")
    print("Declared order: set x=1, then set x=2. Expected result: x=2.")
    print("A compliant system must produce identical, correct outputs.")

    faulty    = check_i5(FaultyAdapter(),    "FaultyAdapter    — order-dependent execution")
    reference = check_i5(ReferenceAdapter(), "ReferenceAdapter — declared order enforced")

    print()
    print("-" * 60)
    print(f"  FaultyAdapter    I5: {'PASS' if faulty    else 'FAIL'}")
    print(f"  ReferenceAdapter I5: {'PASS' if reference else 'FAIL'}")
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
