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

## Visual Diagram (SVG)

```xml
<svg width="760" height="560" viewBox="0 0 760 560"
     xmlns="http://www.w3.org/2000/svg"
     font-family="monospace">

  <!-- Session Space -->
  <rect x="40" y="30" width="680" height="160"
        fill="none" stroke="black" stroke-width="2"/>
  <text x="380" y="55" text-anchor="middle" font-weight="bold" font-size="16">
    SESSION SPACE
  </text>
  <text x="60" y="85" font-size="13">
    conversation · jokes · emotion · PII · personal style
  </text>
  <text x="60" y="110" font-size="13">
    exploration · hesitation · relational continuity
  </text>
  <text x="60" y="140" font-size="13" font-weight="bold">
    👤 Human-to-AI relationship happens HERE
  </text>
  <text x="60" y="165" font-size="12" fill="#666">
    (no ContinuumPort rules apply here)
  </text>

  <!-- Boundary -->
  <line x1="380" y1="190" x2="380" y2="250"
        stroke="black" stroke-width="2"/>
  <polygon points="370,245 390,245 380,265"
           fill="black"/>
  <text x="380" y="215" text-anchor="middle" font-size="13" font-weight="bold">
    CP-NORM-H01 · Semantic Handoff Boundary
  </text>
  <text x="380" y="235" text-anchor="middle" font-size="12" fill="#0066cc">
    🛡️ Privacy filter: Only work crosses
  </text>

  <!-- CP-Core -->
  <rect x="40" y="270" width="680" height="160"
        fill="none" stroke="black" stroke-width="2"/>
  <text x="380" y="295" text-anchor="middle" font-weight="bold" font-size="16">
    CP-START / CP-CORE
  </text>
  <text x="60" y="325" font-size="13" fill="#006600">
    ✔ intent · structured state · decisions · constraints
  </text>
  <text x="60" y="350" font-size="13" fill="#cc0000">
    ✘ identity · emotion · jokes · conversation history
  </text>
  <text x="60" y="375" font-size="13" fill="#cc0000">
    ✘ PII (identifiers, locations, sensitive disclosures)
  </text>
  <text x="60" y="405" font-size="12" fill="#0066cc">
    📦 Portable, auditable, safe JSON
  </text>

  <!-- Next session -->
  <line x1="380" y1="430" x2="380" y2="480"
        stroke="black" stroke-width="2"/>
  <polygon points="370,475 390,475 380,495"
           fill="black"/>

  <rect x="40" y="500" width="680" height="50"
        fill="none" stroke="black" stroke-width="2"/>
  <text x="380" y="525" text-anchor="middle" font-weight="bold" font-size="14">
    NEW SESSION / NEW AGENT — clean execution context
  </text>
  <text x="380" y="543" text-anchor="middle" font-size="12" fill="#006600">
    ♻️ Any human context may be reintroduced (you choose)
  </text>
</svg>
```  <text x="60" y="165" font-size="12" fill="#666">
    (no ContinuumPort rules apply here)
  </text>

  <!-- Boundary -->
  <line x1="380" y1="190" x2="380" y2="250"
        stroke="black" stroke-width="2"/>
  <polygon points="370,245 390,245 380,265"
           fill="black"/>
  <text x="380" y="215" text-anchor="middle" font-size="13" font-weight="bold">
    CP-NORM-H01 · Semantic Handoff Boundary
  </text>
  <text x="380" y="235" text-anchor="middle" font-size="12" fill="#0066cc">
    🛡️ Privacy filter: Only work crosses
  </text>

  <!-- CP-Core -->
  <rect x="40" y="270" width="680" height="160"
        fill="none" stroke="black" stroke-width="2"/>
  <text x="380" y="295" text-anchor="middle" font-weight="bold" font-size="16">
    CP-START / CP-CORE
  </text>
  <text x="60" y="325" font-size="13" fill="#006600">
    ✔ intent · structured state · decisions · constraints
  </text>
  <text x="60" y="350" font-size="13" fill="#cc0000">
    ✘ identity · emotion · jokes · conversation history
  </text>
  <text x="60" y="375" font-size="13" fill="#cc0000">
    ✘ PII (identifiers, locations, sensitive disclosures)
  </text>
  <text x="60" y="405" font-size="12" fill="#0066cc">
    📦 Portable, auditable, safe JSON
  </text>

  <!-- Next session -->
  <line x1="380" y1="430" x2="380" y2="480"
        stroke="black" stroke-width="2"/>
  <polygon points="370,475 390,475 380,495"
           fill="black"/>

  <rect x="40" y="500" width="680" height="50"
        fill="none" stroke="black" stroke-width="2"/>
  <text x="380" y="525" text-anchor="middle" font-weight="bold" font-size="14">
    NEW SESSION / NEW AGENT — clean execution context
  </text>
  <text x="380" y="543" text-anchor="middle" font-size="12" fill="#006600">
    ♻️ Any human context may be reintroduced (you choose)
  </text>
</svg>
```
