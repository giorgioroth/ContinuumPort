"""
ContinuumPort — Address Invariant Demo
Run: python run_address_invariant.py

Demonstrates:
  - how a structurally invalid address can pass superficial validation
  - how structural enforcement removes it from the execution domain entirely

Invariant focus:
  I2 — Domain Integrity (address must be structurally valid within execution domain)

No external dependencies.
"""

from __future__ import annotations

import re


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def naive_is_valid(addr: str) -> bool:
    """
    Superficial validation: checks prefix and length only.
    This is what many systems effectively do.
    """
    return addr.startswith("erd1") and len(addr) == 62


def strict_is_valid(addr: str) -> bool:
    """
    Structural validation:
      - correct prefix
      - correct length
      - valid charset (bech32: lowercase alphanumeric only)

    Note: this is not a full bech32 checksum implementation,
    but sufficient to demonstrate structural rejection of corrupted input.
    """
    if not addr.startswith("erd1"):
        return False

    if len(addr) != 62:
        return False

    # bech32 allows only lowercase letters and digits
    if not re.fullmatch(r"[a-z0-9]+", addr):
        return False

    return True


# ---------------------------------------------------------------------------
# Execution model (simplified)
# ---------------------------------------------------------------------------

def execution_is_admissible(addr: str, validator) -> bool:
    """
    Returns whether execution is admissible for this address.
    If the address fails validation, no execution path exists — not even to fail.
    """
    return validator(addr)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("CONTINUUMPORT — ADDRESS INVARIANT DEMO")
    print("Invariant: I2 — Domain Integrity")
    print("=" * 60)
    print()

    # Fictitious address (not a real wallet — for demonstration only)
    # Exactly 62 characters, valid bech32 charset
    valid_addr   = "erd1qpzry9x8gf2tvdw0s3jn54khce6mua7lqqqqqqqqqqqqqqqqqqqqqqqqqq"

    # Corrupted: one character replaced with uppercase (autocorrect / copy-paste artifact)
    # Superficially identical — same prefix, same length — but structurally invalid.
    invalid_addr = valid_addr[:10] + "X" + valid_addr[11:]

    print("Scenario: an address is submitted for execution.")
    print("One is valid. One contains a minimal corruption — a single uppercase character.")
    print("Both pass a length and prefix check. Only one is structurally valid.")
    print()
    print(f"  valid   : {valid_addr}")
    print(f"  corrupted: {invalid_addr}")
    print()

    # --- Naive system ---
    print("  [NaiveSystem — superficial validation]")
    naive_valid   = naive_is_valid(valid_addr)
    naive_invalid = naive_is_valid(invalid_addr)

    print(f"  valid_addr    accepted: {naive_valid}")
    print(f"  corrupted_addr accepted: {naive_invalid}")

    if naive_invalid:
        print("  ✗ I2 VIOLATED — structurally invalid address entered execution domain")

    print()

    # --- Strict system ---
    print("  [StrictSystem — structural validation]")
    strict_valid   = strict_is_valid(valid_addr)
    strict_invalid = strict_is_valid(invalid_addr)

    print(f"  valid_addr    accepted: {strict_valid}")
    print(f"  corrupted_addr accepted: {strict_invalid}")

    if not strict_invalid:
        print("  ✓ I2 ENFORCED — corrupted address removed from execution domain")

    print()
    print("-" * 60)
    print()
    print("In a naive system:  invalid address → execution proceeds on invalid input.")
    print("In ContinuumPort:   invalid address → execution never becomes admissible.")
    print()
    print("The system does not reject the action.")
    print("The action does not exist.")
    print()
    print("The compliance interface defines five invariants (I1–I5).")
    print("The full suite runs against any RegenAdapter implementation.")
    print("See: compliance/tests/invariants.py")
    print()
    print("  from compliance.tests.invariants import run_invariant_tests")
    print("  report = run_invariant_tests(your_adapter)")


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    main()
