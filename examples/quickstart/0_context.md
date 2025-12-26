
# Quickstart Scenario: The Algorithmic Trader

To understand ContinuumPort, let's use a practical scenario.

### The Situation
You are building a complex **Cryptocurrency Trading Bot**. You've spent 4 hours with an AI agent (Model A) defining the risk parameters, the technical stack (Python/ccxt), and the position sizing logic (Kelly Criterion).

### The Problem
You need to switch to a different model (Model B) or start a clean session because the current context is cluttered with debug logs and irrelevant conversation.

### The Traditional Way
You copy-paste your last 5 messages or try to write a "summary" yourself. Usually, you lose the specific constraints or the AI starts acting differently because it's trying to mimic your "tone" instead of focusing on the "code".

### The ContinuumPort Way
You generate a **CP-Core Container**. 

This container captures:
1. **Summary**: "Building a crypto trading bot."
2. **Constraints**: "Sub-100ms latency, Kelly Criterion, Paper trading first."
3. **State**: "Backtesting done. Moving to paper trading implementation."

When Model B receives this container, it doesn't try to "be your friend" or "remember your jokes". It simply **reconstructs the technical state** and continues the work.

**Continuity of work. Zero persistence of self.**

```
