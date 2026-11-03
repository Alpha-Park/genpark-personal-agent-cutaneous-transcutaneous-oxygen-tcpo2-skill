"""
Cutaneous Transcutaneous Oxygen Tension (tcPO2) & Microvascular Perfusion Client.
Zero-mock pure Python standard library implementation.
Calculates Transcutaneous Oxygen Pressure (tcPO2 mmHg), Regional Perfusion Index (RPI),
and wound healing / limb salvage potential based on heated Clark sensor polarography.
"""

import math
from typing import Dict, Any, Optional


class TranscutaneousOxygenClient:
    """
    Evaluates cutaneous microvascular perfusion and ischemic tissue viability via heated Clark polarography:
    - Sensor heated to 44 C (induces maximal capillary hyperemia and stratum corneum lipid fluidity)
    - Steady-state tcPO2 (mmHg)
    - Regional Perfusion Index (RPI): tcPO2_limb / tcPO2_chest_reference
    - Wound healing stratification and Critical Limb-Threatening Ischemia (CLTI) scoring
    """

    def __init__(self):
        pass

    def evaluate_tcpo2(
        self,
        limb_tcpo2_mmhg: float,
        chest_reference_tcpo2_mmhg: Optional[float] = 65.0,
        o2_inhalation_tcpo2_mmhg: Optional[float] = None,
        sensor_temperature_c: Optional[float] = 44.0,
        anatomical_site: Optional[str] = "dorsum of foot"
    ) -> Dict[str, Any]:
        """
        Calculates tcPO2 microvascular viability metrics.
        limb_tcpo2_mmhg: measured steady-state tcPO2 at examination site (mmHg).
        chest_reference_tcpo2_mmhg: reference infraclavicular tcPO2 (mmHg, default: 65.0).
        o2_inhalation_tcpo2_mmhg: tcPO2 during 100% O2 normobaric mask breathing (optional).
        sensor_temperature_c: electrode heating temp (default: 44.0 C).
        """
        if limb_tcpo2_mmhg < 0:
            raise ValueError("Limb tcPO2 must be non-negative.")
        if chest_reference_tcpo2_mmhg <= 0:
            raise ValueError("Chest reference tcPO2 must be strictly positive.")

        # Regional Perfusion Index (RPI)
        rpi = limb_tcpo2_mmhg / chest_reference_tcpo2_mmhg

        # Hyperoxia response ratio if O2 challenge performed
        hyperoxia_response_ratio = None
        if o2_inhalation_tcpo2_mmhg is not None and limb_tcpo2_mmhg > 0:
            hyperoxia_response_ratio = round(o2_inhalation_tcpo2_mmhg / limb_tcpo2_mmhg, 2)

        # Clinical ischemic wound healing classification:
        # tcPO2 >= 50 mmHg: Normal / High Healing Probability (>95% spontaneous ulcer healing)
        # tcPO2 30 - 49 mmHg: Borderline / Compensated Microcirculation (delayed healing, conservative therapy)
        # tcPO2 20 - 29 mmHg: Severe Ischemia / Low Healing Potential (<50% without revascularization)
        # tcPO2 < 20 mmHg: Critical Limb-Threatening Ischemia (CLTI, ulcer healing unlikely, high amputation risk)
        if limb_tcpo2_mmhg >= 50.0:
            perfusion_status = "Optimal Microvascular Oxygen Delivery (Normal)"
            healing_probability = "High (>95% probability of spontaneous epithelialization and surgical wound healing)."
        elif limb_tcpo2_mmhg >= 30.0:
            perfusion_status = "Borderline / Moderate Microvascular Compromise"
            healing_probability = "Moderate; delayed healing, optimization of perfusion and edema control advised."
        elif limb_tcpo2_mmhg >= 20.0:
            perfusion_status = "Severe Microvascular Tissue Ischemia"
            healing_probability = "Low (<50%); spontaneous healing improbable; vascular intervention indicated."
        else:
            perfusion_status = "Critical Limb-Threatening Ischemia (CLTI)"
            healing_probability = "Extremely Low (<10%); tissue necrosis risk; urgent arterial revascularization required."

        return {
            "status": "success",
            "oxygen_measurements_mmhg": {
                "limb_tcpo2_mmhg": round(limb_tcpo2_mmhg, 1),
                "chest_reference_tcpo2_mmhg": round(chest_reference_tcpo2_mmhg, 1),
                "o2_inhalation_tcpo2_mmhg": round(o2_inhalation_tcpo2_mmhg, 1) if o2_inhalation_tcpo2_mmhg else None
            },
            "indices": {
                "regional_perfusion_index_rpi": round(rpi, 2),
                "hyperoxia_response_ratio": hyperoxia_response_ratio,
                "sensor_temperature_c": sensor_temperature_c
            },
            "clinical_viability": {
                "perfusion_status": perfusion_status,
                "healing_probability": healing_probability,
                "anatomical_site": anatomical_site
            }
        }
