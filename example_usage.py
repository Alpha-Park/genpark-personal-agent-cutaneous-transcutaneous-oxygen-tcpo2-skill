"""
Example usage of Cutaneous Transcutaneous Oxygen (tcPO2) Skill.
Demonstrates normal microvascular oxygen delivery vs critical limb-threatening ischemia (CLTI).
"""

import json
from client import TranscutaneousOxygenClient


def main():
    print("=== Testing Cutaneous tcPO2 Skill ===")
    client = TranscutaneousOxygenClient()

    # 1. Healthy young subject (Dorsal foot tcPO2 = 62.0 mmHg, chest ref = 66.0 mmHg -> RPI = 0.94 -> Normal)
    res_normal = client.evaluate_tcpo2(
        limb_tcpo2_mmhg=62.0,
        chest_reference_tcpo2_mmhg=66.0,
        o2_inhalation_tcpo2_mmhg=185.0,
        anatomical_site="dorsum of foot"
    )
    print("\n[Case 1: Normal Microvascular Oxygenation]")
    print(json.dumps(res_normal, indent=2))

    # 2. Diabetic patient with critical peripheral arterial disease (Foot tcPO2 = 14.0 mmHg, chest ref = 62.0 mmHg -> RPI = 0.23 -> CLTI)
    res_clti = client.evaluate_tcpo2(
        limb_tcpo2_mmhg=14.0,
        chest_reference_tcpo2_mmhg=62.0,
        o2_inhalation_tcpo2_mmhg=22.0,
        anatomical_site="first metatarsal head"
    )
    print("\n[Case 2: Critical Limb-Threatening Ischemia (CLTI)]")
    print(json.dumps(res_clti, indent=2))

    # Assertions
    assert res_normal["oxygen_measurements_mmhg"]["limb_tcpo2_mmhg"] >= 50.0
    assert "Normal" in res_normal["clinical_viability"]["perfusion_status"]
    assert res_clti["oxygen_measurements_mmhg"]["limb_tcpo2_mmhg"] < 20.0
    assert "Critical" in res_clti["clinical_viability"]["perfusion_status"]
    print("\n[SUCCESS] Cutaneous tcPO2 tests passed!")


if __name__ == "__main__":
    main()
