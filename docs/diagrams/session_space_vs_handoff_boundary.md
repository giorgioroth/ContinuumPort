# Session Space vs Semantic Handoff Boundary

**This diagram is descriptive, not prescriptive. Normative authority resides exclusively in CP-NORM-H01.**

```
┌───────────────────────────────────────────────┐
│               SESSION SPACE                   │
│                                               │
│  - conversation                                │
│  - jokes / tone / emotions                     │
│  - personal context (PII, autobiographical)    │
│  - exploration, hesitation, retries            │
│  - relational continuity                       │
│                                               │
│  👤 Human-to-AI relationship happens HERE     │
│  (no ContinuumPort rules apply here)           │
│  (Personal context remains local. Work state crosses boundary.)  │
└───────────────────────┬───────────────────────┘
                        │
                        │  CP-NORM-H01
                        │  Semantic Handoff Boundary
                        │  (explicit / normative)
                        │  
                        │  🛡️ Privacy filter: Only work crosses
                        ▼
┌───────────────────────────────────────────────┐
│                CP-START / CP-CORE              │
│                                               │
│  ✔ intent                                     │
│  ✔ structured working state                   │
│  ✔ decisions                                  │
│  ✔ constraints                                │
│  ✔ next action                                │
│                                               │
│  ✘ identity                                   │
│  ✘ emotion                                    │
│  ✘ jokes                                      │
│  ✘ conversational history                     │
│  ✘ personal style                             │
│  ✘ PII (identifiers, locations, sensitive disclosures)            │
│                                               │
│  📦 Portable, auditable, safe JSON            │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│             NEW SESSION / NEW AGENT            │
│                                               │
│  - clean execution context                     │
│  - no inherited presence                      │
│  - work resumes from explicit state            │
│                                               │
│  ♻️ Any human context may be reintroduced     │
│     (you choose what comes back)              │
└───────────────────────────────────────────────┘
```

---

## Key Principles

**SESSION SPACE** = human, free-form, non-transferable  
**Handoff Boundary** = normative, explicit, enforced  
**CP-CORE** = portable semantic work state

---

## How to read this diagram

This diagram separates **human interaction** from **portable semantic work state**.
Only the **handoff boundary** is governed by ContinuumPort.

### 1. Session Space *(no ContinuumPort rules apply)*

* Free-form human ↔ AI interaction
* Personal context, jokes, tone, and emotions are allowed
* Exploration, hesitation, and conversational flow happen here
* **Nothing in this space is portable by default**

---

### 2. Semantic Handoff Boundary *(CP-NORM-H01)*

* Explicit, **normative** boundary
* Defines what **may** and **may not** cross between sessions
* Enforces privacy and safety **by design**, not by policy
* Prevents accidental transfer of personal or relational context

---

### 3. CP-Core / CP-START

* **Portable semantic work state only**
* Includes intent, structured working state, decisions, constraints
* Excludes:

  * identity
  * relational memory
  * emotions
  * jokes
  * personal style
  * PII
* Safe to store, share, audit, and execute across systems

---

### 4. New Session / New Agent

* Clean execution context
* No inherited presence or conversational history
* Work resumes strictly from explicit state
* **Human context may be reintroduced manually, at the user’s discretion**

