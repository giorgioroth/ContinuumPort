#!/usr/bin/env python3
"""
ContinuumPort CP-Core Validator v1.0 (Draft)

Validates CP-Core containers against the official specification:
https://github.com/giorgioroth/ContinuumPort/blob/main/docs/SPECIFICATION.md

Usage:
    python tools/validator.py path/to/container.json
    python tools/validator.py examples/minimal_cp_core.json

Returns 0 if valid, 1 if invalid.
"""

import json
import sys
import re
from pathlib import Path

# PII detection patterns (basic but effective)
PII_PATTERNS = [
    re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'),  # IP
    re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),  # Email
    re.compile(r'\b\d{9,}\b'),  # Possible phone (9+ digits)
    re.compile(r'\b(?:street|strada|via|nr\.?)\s+\d+', re.I),  # Address hint
]

# Prohibited behavioral hint categories
PROHIBITED_HINT_CATEGORIES = {
    "tone", "style", "personality", "behavior", "emotion", "empathy",
    "friendly", "warm", "encouraging", "enthusiastic", "cautious"
}

def load_container(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON syntax: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ File not found: {path}")
        sys.exit(1)

def validate_structure(container: dict) -> bool:
    errors = []

    required = ["cp", "intent", "state", "timestamp"]
    for field in required:
        if field not in container:
            errors.append(f"Missing required field: '{field}'")

    if "cp" in container and container["cp"] != "1.0":
        errors.append(f"Unsupported version: {container['cp']} (only '1.0' allowed)")

    if "intent" in container and (not isinstance(container["intent"], str) or len(container["intent"]) > 2000):
        errors.append("'intent' must be string ≤ 2000 characters")

    if "state" in container and (not isinstance(container["state"], str) or len(container["state"]) > 5000):
        errors.append("'state' must be string ≤ 5000 characters")

    if "style" in container and (not isinstance(container["style"], str) or len(container["style"]) > 500):
        errors.append("'style' must be string ≤ 500 characters")

    if "hints" in container:
        if not isinstance(container["hints"], list):
            errors.append("'hints' must be an array")
        elif len(container["hints"]) > 20:
            errors.append("'hints' array too long (>20)")
        else:
            for i, hint in enumerate(container["hints"]):
                if not isinstance(hint, str) or len(hint) > 200:
                    errors.append(f"Hint #{i} invalid length or type")
                elif ":" not in hint:
                    errors.append(f"Hint #{i} missing ':' separator")

    if "timestamp" in container:
        if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", container["timestamp"]):
            errors.append("'timestamp' must be ISO 8601 UTC (e.g., 2025-12-27T12:00:00Z)")

    if errors:
        for e in errors:
            print(f"❌ Structural error: {e}")
        return False
    return True

def validate_semantics(container: dict) -> bool:
    errors = []

    # Check for PII in key fields
    text_fields = [container.get(f, "") for f in ["intent", "state", "style"] if f in container]
    if "hints" in container:
        text_fields.extend(container["hints"])

    for field in text_fields:
        if isinstance(field, str):
            for pattern in PII_PATTERNS:
                if pattern.search(field):
                    errors.append("Potential PII detected (email, IP, phone, address)")

    # Check for prohibited behavioral hints
    if "hints" in container:
        for hint in container["hints"]:
            if isinstance(hint, str):
                category = hint.split(":", 1)[0].lower().strip()
                if category in PROHIBITED_HINT_CATEGORIES:
                    errors.append(f"Prohibited behavioral hint category: '{category}'")

    if errors:
        for e in errors:
            print(f"❌ Semantic violation: {e}")
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python validator.py <path/to/container.json>")
        sys.exit(1)

    path = sys.argv[1]
    print(f"🔍 Validating CP-Core container: {path}")

    container = load_container(path)

    if validate_structure(container) and validate_semantics(container):
        print("✅ Valid CP-Core v1.0 container")
        print("   Conforms to privacy, security, and non-anthropomorphic boundaries.")
        sys.exit(0)
    else:
        print("❌ Invalid container")
        sys.exit(1)

if __name__ == "__main__":
    main()
