# ContinuumPort Examples

This directory contains validated CP-Core containers demonstrating semantic continuity across models and sessions.

---

## Validation Methodology

All examples were tested in clean sessions (no prior conversation history) across multiple models:
- Grok (xAI)
- Claude (Anthropic)
- Gemini (Google)
- ChatGPT (OpenAI)

Each model reconstructed working state from CP-Core structure alone, without identity, memory, or emotional persistence.

---

## Files

### Minimal Structure

**`minimal_cp_core.json`**  
Smallest valid CP-Core container demonstrating required fields.

### Cross-Language Validation

**`cp-core_en.json`** — English container  
**`cp-core_ro.json`** — Romanian container (semantically equivalent)

Both versions were successfully regenerated across all tested models without semantic decay. This validates language-agnostic semantic continuity through structure alone.

### Task-Oriented Example

**`example_task.json`**  
Technical reporting container for a complex industrial task (Bifacial PV Efficiency Report).

Demonstrates:
- Structured task resumption across sessions
- Constraint enforcement (RAW mode)
- Non-anthropomorphic compliance
- Multi-stage work continuity

### Empirical Demonstration

**`demonstration_grok_2026-01-01.cp`**  
Complete, unedited transcript of a conversation with Grok (xAI) on January 1, 2026.

This conversation demonstrates all ContinuumPort principles in practice:
- Ephemeral inference without persistent memory
- Objective analysis maintained after author identity reveal
- Semantic continuity through structured containers
- Non-anthropomorphic interaction throughout

Full analysis available in project documentation.

**`language-flexibility.md`**  
Technical documentation on cross-language validation methodology.

### Reference Implementation

**`quickstart/`**  
Python-based reference implementation and validation tools.

---

## Observations

Semantic continuity was preserved through structure alone across all tested models.

Models resumed work at correct stages without requiring:
- Author context
- Session history
- Conversational presence
- Identity or emotional state

No anthropomorphic drift was observed in any validation session.

---

## Supplementary Materials

Video demonstrations and blog posts discussing these examples exist as educational materials but are not part of normative validation.

Primary evidence consists of:
- The CP-Core containers themselves
- Transcripts of clean-session regeneration
- Cross-model consistency verification

---

**Note:** These examples demonstrate the protocol in practice. They are not normative specifications—see the main repository documentation for normative content.
