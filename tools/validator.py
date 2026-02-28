First complete implementation of CP-Core Task Continuity regime enforcement.

ContinuumPort CP-Core Validator v1.0

Reference implementation of CP-Core Task Continuity regime enforcement.

Validates CP-Core containers against the official specification:
https://github.com/giorgioroth/ContinuumPort/blob/main/docs/SPECIFICATION.md

This validator enforces structural regime membership (Task Continuity):
A CP-Core container is valid ⇔ A_local = 0 (D-only state preserved).

Any field, hint, or value that introduces agent-specific adaptive memory (A_local)
constitutes a regime violation.

Based on:
"Structural Modes of Continuity in Adaptive Systems" (Rotaru, 2025)

Usage:
python tools/validator.py path/to/container.json

Returns 0 if valid (D-only regime confirmed), 1 if invalid (regime violation detected).

#!/usr/bin/env python3
"""
ContinuumPort CP-Core Validator v1.0

Reference implementation of CP-Core regime enforcement.

Validates CP-Core containers against the official specification:
https://github.com/giorgioroth/ContinuumPort/blob/main/docs/SPECIFICATION.md

This validator enforces structural regime membership (Task Continuity):
    A CP-Core container is valid ⇔ A_local = 0 and D is preserved.

Any field, hint, or value that introduces agent-specific adaptive memory (A_local)
constitutes a regime violation.

Based on:
"Structural Modes of Continuity in Adaptive Systems" (Rotaru, 2025)

Usage:
    python tools/validator.py path/to/container.json

Returns 0 if valid (D-only regime confirmed), 1 if invalid (regime violation detected).
"""

import json
import sys
import re
from datetime import datetime

# ── Schema boundaries ──────────────────────────────────────────────────────────

# Fields that introduce agent-specific adaptive memory (A_local)
# Presence of any of these constitutes a regime violation.
ADAPTIVE_MEMORY_FIELDS = {
    "style", "persona", "memory", "preferences",
    "history", "profile", "identity", "personality"
}

# PII detection patterns — governance boundary enforcement
PII_PATTERNS = [
    (re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'), "IP address"),
    (re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'), "email"),
    (re.compile(r'\b(?:\+?\d[\d\s\-]{7,}\d)\b'), "phone number"),
    (re.compile(r'\b(?:street|strada|via|nr\.?)\s+\d+', re.I), "address"),
]

# Hint categories that proxy agent-conditioned behavior (A_local signal)
BEHAVIORAL_HINT_CATEGORIES = {
    "tone", "style", "personality", "behavior", "emotion", "empathy",
    "friendly", "warm", "encouraging", "enthusiastic", "cautious"
}


# ── Predicates ─────────────────────────────────────────────────────────────────

def is_behavioral_hint(category: str) -> bool:
    """
    Returns True if the hint category is a proxy for agent-conditioned behavior.
    This is A_local detection at the hint level — not an arbitrary content filter.
    """
    return category.lower().strip() in BEHAVIORAL_HINT_CATEGORIES


# ── Loaders ────────────────────────────────────────────────────────────────────

def load_container(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON syntax: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        sys.exit(1)


# ── Structural validation ──────────────────────────────────────────────────────

def validate_structure(container: dict) -> bool:
    """
    Validates container format and schema compliance.
    Detects adaptive memory fields (A_local) at the schema level.
    """
    errors = []

    # Required fields
    for field in ["cp", "intent", "state", "timestamp"]:
        if field not in container:
            errors.append(f"Missing required field: '{field}'")

    # Version
    if "cp" in container and container["cp"] != "1.0":
        errors.append(f"Unsupported version: '{container['cp']}' (only '1.0' supported)")

    # intent
    if "intent" in container:
        if not isinstance(container["intent"], str) or len(container["intent"]) > 2000:
            errors.append("'intent' must be a string ≤ 2000 characters")

    # state
    if "state" in container:
        if not isinstance(container["state"], str) or len(container["state"]) > 5000:
            errors.append("'state' must be a string ≤ 5000 characters")

    # hints
    if "hints" in container:
        if not isinstance(container["hints"], list):
            errors.append("'hints' must be an array")
        elif len(container["hints"]) > 20:
            errors.append("'hints' array exceeds maximum length (20)")
        else:
            for i, hint in enumerate(container["hints"]):
                if not isinstance(hint, str) or len(hint) > 200:
                    errors.append(f"hints[{i}]: invalid type or length (max 200 chars)")
                elif ":" not in hint:
                    errors.append(f"hints[{i}]: missing ':' separator (format: 'category: value')")

    # timestamp
    if "timestamp" in container:
        try:
            datetime.fromisoformat(container["timestamp"].replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            errors.append("'timestamp' must be a valid ISO 8601 UTC datetime (e.g., 2026-02-28T14:00:00Z)")

    # A_local leak detection at schema level
    errors.extend(detect_adaptive_memory_leak(container))

    if errors:
        for e in errors:
            print(f"❌ Structural error: {e}")
        return False
    return True


# ── A_local boundary enforcement ───────────────────────────────────────────────

def detect_adaptive_memory_leak(container: dict) -> list:
    """
    Detects fields that introduce agent-specific adaptive memory (A_local).

    This enforces the regime boundary at the schema level:
        Task Continuity ⟺ A_local = 0
        Any A_local > 0 collapses the regime categorically.
    """
    violations = []
    for key in container.keys():
        if key.lower() in ADAPTIVE_MEMORY_FIELDS:
            violations.append(
                f"Field '{key}' introduces A_local (agent-specific adaptive memory). "
                f"CP-Core enforces D-only regime. Remove this field."
            )
    return violations


# ── Regime validation ──────────────────────────────────────────────────────────

def validate_regime(container: dict) -> bool:
    """
    Validates regime membership: confirms the container belongs to Task Continuity.

    Checks:
    1. PII — governance boundary (data that should not persist)
    2. Behavioral hints — A_local signal at hint level
    """
    errors = []

    # Named fields for contextual reporting
    named_fields = {
        "intent": container.get("intent", ""),
        "state": container.get("state", ""),
    }

    if "hints" in container:
        for i, h in enumerate(container["hints"]):
            named_fields[f"hints[{i}]"] = h

    # PII detection
    for field_name, value in named_fields.items():
        if isinstance(value, str):
            for pattern, label in PII_PATTERNS:
                if pattern.search(value):
                    errors.append(
                        f"Potential PII ({label}) detected in '{field_name}'. "
                        f"CP-Core must not carry personally identifiable information."
                    )

    # Behavioral hints
    if "hints" in container:
        for i, hint in enumerate(container["hints"]):
            if isinstance(hint, str) and ":" in hint:
                category = hint.split(":", 1)[0]
                if is_behavioral_hint(category):
                    errors.append(
                        f"hints[{i}] category '{category.strip()}' introduces A_local "
                        f"(agent-conditioned behavior). Not allowed in D-only regime."
                    )

    if errors:
        for e in errors:
            print(f"❌ Regime violation: {e}")
        return False
    return True


# ── Entry point ────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) != 2:
        print("Usage: python validator.py <path/to/container.json>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"🔍 Validating CP-Core container: {path}")
    print("   Regime check: Task Continuity (A_local = 0, D preserved)")

    container = load_container(path)

    if not validate_structure(container):
        print("❌ Container rejected — structural or regime boundary violation.")
        sys.exit(1)

    if not validate_regime(container):
        print("❌ Container rejected — regime violation detected.")
        sys.exit(1)

    print("✅ Valid CP-Core v1.0 container")
    print("   Regime: Task Continuity confirmed (D-only, A_local = 0)")
    print("   Conforms to portability, privacy, and non-anthropomorphic boundaries.")
    sys.exit(0)


if __name__ == "__main__":
    main()
