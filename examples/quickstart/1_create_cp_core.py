#!/usr/bin/env python3
"""
ContinuumPort Quickstart - Step 1: Create CP-Core Container

This demonstrates how to create a minimal CP-Core container from task state.
"""

import json
from datetime import datetime, timezone
from typing import List, Dict, Any


def create_cp_core_container(
    summary: str,
    constraints: List[str],
    task_state: str,
    context_data: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Creates a minimal CP-Core container.
    """
    container = {
        "cp_core_version": "1.0",
        "created_at": datetime.now(timezone.utc).isoformat(),
        
        # Core semantic state
        "summary": summary,
        "constraints": constraints,
        "task_state": task_state,
        
        # Optional context data
        "context": context_data or {},
        
        # Metadata
        "meta": {
            "container_type": "task_continuity",
            "generator": "quickstart_demo"
        }
    }
    return container


def validate_container(container: Dict[str, Any]) -> bool:
    """
    Basic validation that container has required fields.
    """
    required_fields = ["cp_core_version", "summary", "constraints", "task_state"]
    return all(field in container for field in required_fields)


def demo_crypto_bot_scenario():
    """
    Demonstrates creating a CP-Core container for the crypto trading bot scenario.
    """
    print("=" * 60)
    print("ContinuumPort Quickstart - Creating CP-Core Container")
    print("=" * 60)
    print()
    
    # Task state from scenario
    summary = "Building algorithmic trading bot for cryptocurrency markets"
    constraints = [
        "Real-time data required (sub-100ms latency)",
        "Risk management with position sizing (Kelly criterion)",
        "Paper trading validation before live deployment"
    ]
    task_state = "Completed backtesting phase. Starting paper trading implementation."
    
    context_data = {
        "technical_stack": ["Python", "ccxt", "pandas"],
        "target_exchanges": ["Binance", "Coinbase"],
        "risk_parameters": {
            "max_position_size": "5% of portfolio",
            "stop_loss": "2%"
        }
    }
    
    print("Creating container from task state...")
    container = create_cp_core_container(
        summary=summary,
        constraints=constraints,
        task_state=task_state,
        context_data=context_data
    )
    
    if validate_container(container):
        print("✓ Container created and validated")
    else:
        print("✗ Container validation failed")
        return
    
    print()
    print("-" * 60)
    print("CP-Core Container (JSON format):")
    print("-" * 60)
    print(json.dumps(container, indent=2))
    print()
    print("-" * 60)
    print("Observations:")
    print("✓ Task-relevant info only | ✗ No Identity | ✗ No Emotions")
    print("-" * 60)


if __name__ == "__main__":
    demo_crypto_bot_scenario()

```

