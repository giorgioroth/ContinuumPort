# ContinuumPort — CP-Core v1.0
**Hybrid Semantic Continuity Layer for Multi-Agent AI**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Spec Version](https://img.shields.io/badge/CP--Core-v1.0-brightgreen)](cp-core/schema.json)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

**ContinuumPort: semantic continuity made simple — powered by Regen Engine**

---

## Overview
ContinuumPort (CP-Core) is an open-source semantic portability layer designed to transfer **non-sensitive conversational context** between sessions, models, platforms, and devices — without storing personal data and without relying on central servers.

---

## Key Features
- Maintains user intent, style, and task state
- 100% privacy-by-design (zero PII, zero tokens, zero tracking)
- Works across any LLM / agent / app implementing the spec
- Human-readable + machine-verifiable format
- Licensed under Apache 2.0 (code) + CC-BY-4.0 (documentation)

---

## Security & Engine Disclaimer

ContinuumPort provides the CP-Core specification, examples, and validation tools for semantic portability. The underlying **Regen Engine** is proprietary and **not included** in this repository. This repository does **not** expose any secret code or functionality of Regen Engine — it only demonstrates the structure and usage of CP-Core containers. Users can safely explore, test, and integrate CP-Core without access to Regen Engine internals.


## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/username/ContinuumPort-CP-Core.git
cd ContinuumPort-CP-Core

# 2. Validate an existing CP-Core container
python cp-core/reference/validator.py validate path/to/container.json

# 3. Explore examples
cat cp-core/examples/minimal.json
For full documentation and integration guides:

Specification: /docs/SPECIFICATION.md

Integration: /docs/INTEGRATION.md

Examples
The repository includes example CP-Core containers for testing and reference:

minimal.json – simplest valid container

full-example.json – fully populated example

extended-with-hints.json – includes memory hints and agent guidance

Contributing
Any PR is welcome!

For major schema changes, open an Issue first.

Keep contributions consistent with privacy-by-design principles.

Author & License
Author: Giorgio Roth • 2025
License: Apache License 2.0 (code) + Creative Commons BY 4.0 (documentation)
Documentation: Creative Commons BY 4.0
