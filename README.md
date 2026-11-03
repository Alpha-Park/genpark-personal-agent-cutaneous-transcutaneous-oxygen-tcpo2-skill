# Cutaneous Transcutaneous Oxygen (tcPO2) Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Transcutaneous Oxygen Pressure ($tcPO_2$ in mmHg) and Regional Perfusion Index (RPI) using heated Clark polarographic sensor physics to evaluate ischemic wound healing potential.

## Architecture

```mermaid
flowchart TD
    A[44C Heated Clark Electrode on Skin] --> B[Measure Steady-State tcPO2 mmHg]
    B --> C[Reference Chest Electrode & Calculate RPI]
    C --> D[Evaluate Optional 100% O2 Challenge Response]
    D --> E[Classify Normal > 50 vs CLTI < 20 mmHg]
```

## Quickstart

```python
from client import TranscutaneousOxygenClient

client = TranscutaneousOxygenClient()
result = client.evaluate_tcpo2(
    limb_tcpo2_mmhg=62.0,
    chest_reference_tcpo2_mmhg=66.0
)
print(result)
```

## License

Apache-2.0
