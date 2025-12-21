# ContinuumPort — CP-Core v1.0
**Hybrid Semantic Continuity Layer for Multi-Agent AI**

## Overview

ContinuumPort (CP-Core) is an open, specification-driven semantic portability layer that enables the transfer of **non-sensitive conversational context** across sessions, models, platforms, and devices.

It is designed to be:
- privacy-first (zero PII by design),
- model-agnostic,
- user-owned,
- independent of any central service.

ContinuumPort intentionally separates **open semantic state transport** (CP-Core) from **high-fidelity context regeneration** (Regen Engine), enabling both open interoperability and commercially viable performance.

---

## Licensing

ContinuumPort-Core (CP-Core specification and reference implementations)  
are released under the **MIT License**.

The proprietary **ContinuumPort-Regen Engine** is not included in this repository  
and is distributed under separate commercial licensing terms.

---

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Spec Version](https://img.shields.io/badge/CP--Core-v1.0-brightgreen)](cp-core/schema.json)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

**ContinuumPort: semantic continuity made simple.**  
*CP-Core is open. Regen Engine is proprietary.*

---

## Key Features

- Portable semantic context across models, agents, and sessions  
- Preservation of user intent, task state, and conversational direction  
- Privacy-by-design (no PII, no logs, no hidden retention)  
- Fully model-agnostic and implementation-independent  
- Human-readable, machine-verifiable open schema  
- MIT-licensed open standard (CP-Core)

---

## Non-Goals and Explicit Boundaries

ContinuumPort is intentionally limited to **semantic context transport**.  
It explicitly excludes the following:

- AI models, generation, training, or fine-tuning  
- Behavioral, emotional, or personality continuity  
- Identity construction or persistent self-representation  
- RLHF, engagement optimization, or compliance shaping  
- Autonomous decision-making or judgment  

ContinuumPort provides **context**, never behavior, emotion, or intent.

---

## Allowed vs. Prohibited Use

**Allowed**
- Context transfer across sessions and models  
- Long-term project and task continuity  
- Multi-agent interoperability  
- Schema standardization and validation  

**Prohibited**
- Emotional or psychological continuity  
- Behavioral tuning or personality shaping  
- Hidden data retention or opaque state  
- Treating CP-Core as an autonomous actor  

---

## FAQ

**Does CP-Core shape model behavior or personality?**  
No. It transfers semantic context only.

**Is CP-Core an identity or emotional memory system?**  
No. Identity, emotion, and attachment are explicitly out of scope.

---

## Security & Engine Disclaimer

This repository provides the **CP-Core specification**, validation tools, and usage examples only.

The **Regen Engine** is proprietary and not included.  
No internal, sensitive, or commercial Regen Engine code is present in this repository.

Developers can safely explore, test, and integrate CP-Core without access to proprietary components.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/giorgioroth/continuumport.git
cd continuumport

# 2. Validate a CP-Core container
python cp-core/reference/validator.py validate path/to/container.json

# 3. Explore examples
cat cp-core/examples/minimal.json
````

---

## Documentation

* Specification: `docs/SPECIFICATION.md`
* Integration Guide: `docs/INTEGRATION.md`

---

## Examples

The repository includes reference CP-Core containers:

* `minimal.json` — minimal valid container
* `full-example.json` — fully populated example
* `extended-with-hints.json` — includes memory hints and agent guidance

---

## Contributing

Contributions are welcome.

For major schema changes, please open an Issue first.
All contributions must respect privacy-by-design principles and explicit CP-Core boundaries.

---

## Early Adopters

First 20 spots opening soon for private and local AI builders.

Follow updates or reach out via
[@continuumport](https://x.com/continuumport)

---

## Author & License

**Author:** Gh. Rotaru (Giorgio Roth)
© 2025 — Released under the **MIT License**

```

