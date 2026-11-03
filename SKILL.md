---
name: genpark-personal-agent-cutaneous-transcutaneous-oxygen-tcpo2-skill
version: 1.0.0
description: Calculates Transcutaneous Oxygen Pressure (tcPO2 in mmHg) and Regional Perfusion Index (RPI) to assess microvascular ischemic tissue viability and wound healing potential.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - dermatology
  - vascular
  - tcpo2
  - microcirculation
  - wound-healing
  - zero-dependency
---

# Cutaneous Transcutaneous Oxygen (tcPO2) Skill

## Mathematical Formulation

Regional Perfusion Index (RPI):

$$\text{RPI} = \frac{tcPO_{2,\text{limb}}}{tcPO_{2,\text{chest}}}$$

Normobaric hyperoxia ($100\% \, O_2$) response ratio:

$$\text{HRR} = \frac{tcPO_{2}(100\% \, O_2)}{tcPO_{2}(\text{room air})}$$

## Clinical Viability Stratification (WIfI Criteria)
- **Normal Microcirculation**: $tcPO_2 \ge 50\text{ mmHg}$ ($> 95\%$ spontaneous ulcer healing)
- **Compensated Ischemia**: $30 \le tcPO_2 < 50\text{ mmHg}$ (delayed healing; close surveillance)
- **Severe Tissue Ischemia**: $20 \le tcPO_2 < 30\text{ mmHg}$ (healing unlikely without revascularization)
- **Critical Limb-Threatening Ischemia (CLTI)**: $tcPO_2 < 20\text{ mmHg}$ (imminent necrosis; urgent arterial revascularization required)
