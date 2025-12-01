# ContinuumPort — CP-Core v1.0
**Hybrid Semantic Continuity Layer for Multi-Agent AI**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Spec Version](https://img.shields.io/badge/CP--Core-v1.0-brightgreen)](cp-core/schema.json)

ContinuumPort (CP-Core) is an open-source semantic portability layer designed to transfer **non-sensitive conversational context** across sessions, models, platforms, and devices — without storing personal data or relying on central servers or accounts.

---

## Why CP-Core?

- Preserves user intent, style, and task state
- 100% privacy-by-design (zero PII, zero tokens, zero tracking)
- Works across any LLM / agent / application implementing the specification
- Human-readable and machine-validated format
- Licensed under **Apache 2.0 (code)** + **CC-BY-4.0 (documentation)**

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/giorgioroth/ContinuumPort.git
cd ContinuumPort

# 2. Validate an existing container
python cp-core/reference/validator.py validate path/to/container.json

# 3. View examples
cat cp-core/examples/minimal.json
Documentation
Full specification: docs/SPECIFICATION.md

Integration guide: docs/INTEGRATION.md

Examples: docs/EXAMPLES.md

Contributing
Any PR is welcome! For major schema changes, please open an Issue first.

Author & License
Author: Giorgio Roth • 2025

Code: Apache License 2.0 (LICENSE)

Documentation: Creative Commons BY 4.0
