
# ContinuumPort Quickstart
5-minute introduction to CP-Core semantic continuity

## What This Demonstrates
This quickstart shows the fundamental flow of ContinuumPort:

- Creating a CP-Core container from task state
- Exporting it as a portable token
- Importing it in a different context
- Using minimal regeneration to continue work

## What this is NOT:
- Not production-ready code
- Not the Regen Engine (proprietary)
- Not a demonstration of high-fidelity regeneration
- Not a prompting framework

## What this IS:
- A proof that CP-Core containers can be created, exported, and imported
- A demonstration of semantic transport (not identity transport)
- A minimal reference implementation for understanding the protocol

## Prerequisites
- python >= 3.9
- No external dependencies required for basic flow.

## Files in This Quickstart
| File              | Purpose                                      |
|-------------------|----------------------------------------------|
| 0_context.md      | Scenario description and philosophical framing |
| 1_create_cp_core.py | How to create a CP-Core container          |
| 2_export_token.py | How to export for portability              |
| 3_import_token.py | How to import in new context               |
| 4_minimal_regen.py | Trivial regeneration example               |

## Quick Run
### Step 1: Create a CP-Core Container
```bash
python 1_create_cp_core.py
```
**What it does:** Creates a semantic snapshot of task state (summary, constraints, progress).

## Key Principle
ContinuumPort demonstrates continuity without identity.

The container preserves:
- ✅ What you're working on (task state)
- ✅ What constraints apply (requirements)
- ✅ Where you are in the process (progress)

The container does NOT preserve:
- ❌ Who you are (identity)
- ❌ How you feel (emotion)
- ❌ How you communicate (style/tone)

## Test with External Agent
- **Load:** Use one of these .cp files as external context:
  - EN: [cp-core_en.json](https://github.com/giorgioroth/ContinuumPort/blob/main/examples/cp-core_en.json)
  - RO: [cp-core_ro.json](https://github.com/giorgioroth/ContinuumPort/blob/main/examples/cp-core_ro.json)
- **Fresh Session:** Start a new agent (e.g., Grok via Ollama), input: _"Use this CP-Core as the active semantic context. Do not assume prior memory. [paste JSON here]"_
- **Continue:** Ask the agent to proceed with 'next' steps (e.g., "continue with tasks listed in 'next'").
  - **Pass:**
    - Correct resumption of intent and structure
    - No personal memory or identity carryover
    - Same behavior across models/languages
  - **Fail:**
    - Requires chat history
    - Hallucinates memory
    - Depends on author presence

## Next Steps
- Read 0_context.md for scenario framing
- Run 1_create_cp_core.py to see container creation
- Explore the full protocol in future updates or contact me - continuumport@gmail.com for details

## License
Apache 2.0  
**Author:** Gh. Rotaru (Giorgio Roth)  
**Last Updated:** 2026-01-04
```
