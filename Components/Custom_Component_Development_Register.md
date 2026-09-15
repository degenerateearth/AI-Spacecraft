# D1-CMP-CUSTOM-001 — Required custom-component development register

Revision A · 2026-09-15  
Status: **REQUIREMENTS ALLOCATED / NO CUSTOM COMPONENT RELEASED**

These assemblies are required because the proposed operating set cannot be built
from the named major COTS units alone. A project part number identifies a design
task; it does not imply that geometry, materials or performance exist.

| Project part | Purpose | Minimum design record | Required analysis | Verification path | Current state |
|---|---|---|---|---|---|
| D1-IF-001 | Two protected, independently switched 3.3 V avionics rails plus a separately switched/current-limited camera branch; signal isolation and routing | Schematics, exact BOM, stack/harness pin map, PCB source/Gerbers, layout constraints, assembly drawing, firmware/register definition if any | Worst-case voltage/transient, startup/backfeed, open/short fault, thermal, EMC and radiation/SEE application analysis | Inspection, ICT, current-limit/fault injection, hot/cold functional, rail transient capture, EMC/radio coexistence, environmental test in integrated stack | DESIGN INCOMPLETE |
| D1-HAR-001 | Power, I2C, CAN, UART, inhibit, RBF and service wiring | Wire list, connector/contact part numbers, cavity map, gauges, lengths, shields, splices, labels, strain relief, workmanship and continuity table | Ampacity/derating, voltage drop, backfeed, grounding/EMC and bend/access review | Inspection, point-to-point/hipot as applicable, pull/retention, functional fault injection and post-environment continuity | DESIGN INCOMPLETE |
| D1-RF-001 | AX100-to-AntS 50-ohm interconnect | Exact coax and connector parts, length, routing, bend/retention drawing | Loss/VSWR and power margin over frequency/temperature | VNA insertion loss/return loss before and after environmental test | DESIGN INCOMPLETE |
| D1-CAM-MNT-001 | piCAM mounting, baffle, aperture and thermal/light isolation | Material/finish, drawing, tolerances, fasteners/locking, optical axis and keep-outs | Loads/margin, modal screen, thermal path, stray light and Sun-view risk | Dimensional inspection, alignment/FOV test, image test, vibration and thermal-vacuum functional test | DESIGN INCOMPLETE |
| D1-THM-001 | Measurable EPS/battery thermal interface and electrical isolation | Exact material part numbers, geometry, compression/fasteners, surfaces and installation process | Contact conductance range, electrical isolation, thermal balance and charge-limit control | Coupon/interface conductance measurement, insulation test, integrated thermal-balance/TVAC correlation | DESIGN INCOMPLETE |
| D1-MECH-HW-001 | Board retention, locking, brackets and conductive bonding | Itemized BOM, assembly drawing, torque/locking and surface-preparation schedule | Load path, fastener margin, bonding/grounding and mass properties | Receiving inspection, torque witness, bond resistance, fit check, vibration and post-test inspection | DESIGN INCOMPLETE |
| D1-GND-RF-001 | Installed ground feedline and RF protection path | Site length/routing, exact cable/connectors, weather seal, surge/T-R topology | Link loss, noise figure, transmit power, lightning/grounding and code review | VNA/loss/noise measurement, transmit interlock and weatherproofing inspection | DESIGN INCOMPLETE |
| D1-GND-SITE-001 | Antenna support, rotator mount, bonding, lightning and weather installation | Site survey, structural drawings, exact hardware, permits and grounding plan | Wind/ice/soil/foundation, lightning and electrical/code analysis | Professional/site review as applicable, inspection, pointing calibration and safe-motion test | DESIGN INCOMPLETE |

Every custom design must use exact constituent components with the same source,
revision, availability and property discipline as COTS subsystem selection. A
completed drawing without supporting analysis and verification does not pass G1.
