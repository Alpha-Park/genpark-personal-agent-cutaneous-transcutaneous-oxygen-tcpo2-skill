"""
MCP Server for Cutaneous Transcutaneous Oxygen (tcPO2) Skill.
Provides standard Model Context Protocol JSON-RPC tool endpoints.
"""

import sys
import json
from client import TranscutaneousOxygenClient


def main():
    client = TranscutaneousOxygenClient()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except Exception:
            continue

        method = req.get("method")
        msg_id = req.get("id")

        if method == "tools/list":
            res = {
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "tools": [
                        {
                            "name": "evaluate_tcpo2",
                            "description": "Calculates Transcutaneous Oxygen Pressure (tcPO2 in mmHg) and Regional Perfusion Index (RPI) to assess microvascular ischemic tissue viability and wound healing potential.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "limb_tcpo2_mmhg": {
                                        "type": "number",
                                        "description": "Steady-state limb tcPO2 in mmHg."
                                    },
                                    "chest_reference_tcpo2_mmhg": {
                                        "type": "number",
                                        "description": "Chest reference tcPO2 in mmHg (default: 65.0)."
                                    },
                                    "o2_inhalation_tcpo2_mmhg": {
                                        "type": "number",
                                        "description": "tcPO2 during 100% O2 mask breathing in mmHg (optional)."
                                    },
                                    "sensor_temperature_c": {
                                        "type": "number",
                                        "description": "Electrode temperature in degrees C (default: 44.0)."
                                    },
                                    "anatomical_site": {
                                        "type": "string",
                                        "description": "Examined anatomical site (e.g. dorsum of foot, medial malleolus)."
                                    }
                                },
                                "required": [
                                    "limb_tcpo2_mmhg"
                                ]
                            }
                        }
                    ]
                }
            }
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

        elif method == "tools/call":
            params = req.get("params", {})
            name = params.get("name")
            args = params.get("arguments", {})

            if name == "evaluate_tcpo2":
                try:
                    out = client.evaluate_tcpo2(**args)
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "result": {
                            "content": [{"type": "text", "text": json.dumps(out, indent=2)}]
                        }
                    }
                except Exception as e:
                    res = {
                        "jsonrpc": "2.0",
                        "id": msg_id,
                        "isError": True,
                        "error": {"code": -32000, "message": str(e)}
                    }
                sys.stdout.write(json.dumps(res) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
