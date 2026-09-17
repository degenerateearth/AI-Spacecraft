# D1-DD-CMP-001 - detailed-design component completeness matrix

Revision A - 2026-09-16  
Status: **ACTIVE CONTROL REGISTER - THEORETICAL DESIGN INCOMPLETE**

This register controls the BIRDS-derived detailed design selected by
D1-TRD-ARCH-001. The earlier `Proposed_Operating_Component_Set` and
`phase1_closure` register remain historical records of the rejected mixed-vendor
proposal.

`SELECTED` means that an exact COTS item or custom architecture has been chosen.
It does not mean the component is qualified or that its custom release package is
complete.

## Flight segment

| Function | Controlled item | Identity/state | Remaining design closure |
|---|---|---|---|
| 1U rails and load structure | D1-STR-001 | CUSTOM/TO BE VERIFIED; pinned BIRDS-4 22-instance frame geometry, 6061-T6 and controlled rail finish selected | release Degen-native parametric parts/drawings, tolerances, interfaces, fasteners, inspection plan and structural analyses |
| Five solar panels | D1-SOL-001 | CUSTOM; AZUR `81442` selected | PCB/mechanical variants, RTD, harness and panel acceptance release |
| Battery energy storage | D1-BAT-001 | CUSTOM; Panasonic `BK120AAHU` 3S2P selected | pack drawing/BOM, protection, cell curves, screening and exact mass |
| Power conversion/charging/distribution | D1-EPS-001 | CUSTOM; principal ICs selected | full schematic/BOM/layout/calculations and release tests |
| Launch inhibits, RBF and service access | D1-FAB-001 | OPEN; switch element selected in EPS record | exact RBF, access board, three-actuator geometry and fault tree |
| OBC and safe-state control | D1-OBC-001 | CUSTOM; architecture under revision | freeze current MCU, memory, clocks, supervisors and full board release |
| Passive backplane | D1-BPB-001 | CUSTOM; exact Hirose pair and logical map selected | geometry, slot tables, current/return analysis and fabrication release |
| UHF transceiver | D1-COM-001 | CUSTOM carrier; Ebyte `E22-400M22S` selected | carrier, RF network, waveform, protocol, link and EMC closure |
| UHF antenna and deployment | D1-ANT-001 | CUSTOM/TO BE VERIFIED; OreSat-derived 436.5 MHz canted turnstile and Quetzal-derived four-channel release selected | release RF/end-panel PCB, elements, pivots, line, complete BOM, harness interface, EM/structural analyses and RF/deployment verification |
| Earth camera | D1-CAM-001 | SkyFox `piCAM/FM` selected | connector suffix, current limit, STEP/configuration and carrier release |
| Passive attitude stabilization | D1-ADCS-001 | CUSTOM/TO BE VERIFIED; K&J `D84` plus two 95 mm × 1 mm HyMu 80 rods selected | release rod/retainer drawings; characterize magnet, rod loops and integrated residual dipole; cage test and probability/dynamics analysis |
| Harnesses | D1-HAR-001 | OPEN | exact wire, contacts, connectors, lengths, routing and assembly/inspection data |
| Mounting/bonding hardware | D1-MECH-HW-001 | OPEN | itemized fasteners, locking, torque, bonding and access sequence |
| Thermal materials/interfaces | D1-THM-001 | OPEN | exact surface finishes, interface materials, heater decision and thermal-node evidence |
| Flight software | D1-FSW-001 | OPEN | reproducible source/build, state machine, drivers, protocol, storage and fault tests |

## Ground segment

| Function | Controlled item | Identity/state | Remaining design closure |
|---|---|---|---|
| Matching UHF radio/modem | D1-GS-RAD-001 | OPEN; same E22 module is leading architecture | USB/SPI controller, enclosure, supply and public software release |
| Directional circular antenna | D1-GS-ANT-001 | OPEN | exact antenna with pattern/gain evidence and frequency coverage |
| Pointing | D1-GS-POINT-001 | OPEN | select manual sighting or exact az/el rotator/controller and tracking procedure |
| Feedline/filter/T-R path | D1-GS-RF-001 | OPEN | exact cable/connectors/filter/protection and loss/noise/power budget |
| Station computer | D1-GS-PC-001 | OPEN | minimum documented hardware/software interface and reproducible image |
| Pass prediction/control software | D1-GS-SW-001 | OPEN | open-source package versions, orbit input, Doppler schedule, command safeguards |
| Image reconstruction/archive | D1-GS-IMG-001 | OPEN | released decoder, integrity checks, storage and operator workflow |
| Image printing | D1-GS-PRN-001 | OPEN | exact printer/driver/paper interface or documented ordinary-PC print requirement |
| Site power, mast and protection | D1-GS-SITE-001 | SITE-DEPENDENT CUSTOM | conservative portable configuration plus site-specific safety path |

## Current result

Ten detailed component records exist. Exact selections now control the battery
cell, camera, UHF module, solar-cell assembly, stack connectors, principal EPS
parts, passive-ADCS magnet/material geometry, the principal antenna feed and
release parts, and the nominal 1U frame geometry/material. The design is not yet
buildable under D1-DES-STD-001 because structure drawings/tolerances/analysis,
released antenna fabrication data, ADCS retainers and measured
magnetic properties, harnesses, released avionics and the ground chain are
incomplete. No entry in this matrix is physical test evidence.
