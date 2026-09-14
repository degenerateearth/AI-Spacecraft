# CAD source review and dimensional traceability

CAD-001, 2026-09-14. Units mm; right-handed project axes, origin at nominal rail
envelope center, Z along rails, camera looking +X. Rotations in the model are
provisional packaging orientations, not supplier mounting approvals.

## Repository review before geometry

Reviewed the complete tracked-file inventory and all engineering documents 01–08,
Project_Constitution v0.2, Project_Overview, README, MILESTONES, BOM and program/cost
ledgers, requirements MD/CSV, FMEA, Open_Issues, Configuration_Log, Package_Verification,
Project_Status, AI_Toolchain_and_Boundaries, Source_Register and sources.json.
Reviewed analysis inputs, generator, results and sensitivity tables, and original
SCAD/SVG allocation drawings. The HTML audit book is an earlier generated duplicate;
its mechanical content was cross-checked, not adopted over authoritative Markdown.
PNG is a presentation of the SVG, not an independent dimensional authority.
Conversation logs supply owner history; .git objects and hashes are configuration
records, not geometry evidence. No supplier CAD, fabrication drawing, released
mounting ICD or AGENTS.md was present in the repository inventory.

Physical influences from other disciplines: six fixed photovoltaic faces are
required by the recovery energy concept; camera must retain +X panel power;
integrated battery must not be added twice; no active attitude hardware is selected;
radio thermal path and independent switch/RBF hardware must eventually fit; RF
variant and launch ICD remain conditional. Cost alternatives are not selected
hardware and are not included. Ground equipment is outside the spacecraft model.

## Dimension-to-geometry chain

| Mission / requirement | Decision / component | Dimension or constraint | Evidence and source | CAD representation |
|---|---|---|---|---|
| LEO mission / R03,R21 | Purchased ISISPACE frame B01 | 100 x 100 x 113.5 nominal | PROJECT DECISION: D1-ANA-001 mass/volume; final ICD UNKNOWN | NominalRailEnvelope reference |
| R03,R21 | Four rails B01 | 8 square, centers X/Y +/-46, full rail length | ASSUMPTION inherited from D1_Envelope.scad; not actual supplier geometry | Four named Rail objects |
| Image return / R02,R03 | Lower camera bay | Z -49:-22 (27 high) | PROJECT DECISION D1-ANA-001, D1-PAY-001 | CameraBay reference |
| R02,R27,R28 | CS-101 B15 | 42 x 25 x 45 vendor dimensions; X=45,Y=42,Z=25; center 25,0,-35.5 | DOCUMENTED vendor-derived S23 extraction in D1-PAY-001; selected axis assignment/placement provisional | CS101CameraEnvelope |
| R15 | D1-IF B10 | 88 x 88 x 6, Z -21:-15 | ASSUMPTION XY, PROJECT DECISION Z from SCAD/budget | D1IFAdapterEnvelope |
| R03,R09 | ICEPS2 Type A B02 | 96 x 92 x 26.5 excluding CSKB; Z -12:14.5 | DATASHEET DERIVED S03 p9; Z project allocation; orientation CAD-A02 | ICEPS2TypeAWithBattery |
| R03,R15 | DMC-3 B08 + two top modules | collective Z 20:36, 88 x 88 allocation | PROJECT DECISION/ASSUMPTION from budget/SCAD; real carrier outline UNKNOWN | AvionicsBay + DMC3CarrierEnvelope |
| R03,R14 | A3200 B06 | 65 x 40 x 7.1 | DATASHEET DERIVED S08 p12 physical table; placement CAD-A03 | NanoMindA3200Envelope |
| R03,R16 | AX100-U B07 | 65 x 40 x 6.5 | DATASHEET DERIVED S10 p4; placement CAD-A03 | NanoComAX100UEnvelope |
| R03,R30 | Service access allocation | Z 36:44, 8 high | PROJECT DECISION D1-ANA-001; XY CAD-A01 | UpperServiceClearance reference |
| R03,R12,R16 | Stowed AntS B09 | 98 x 98 x 7 includes supplied cover; Z 44:51 | SOURCE VERIFIED S05 product table; Z project decision | AntSUHFTurnstileStowed |
| R07,R27 | Six solar faces B03–05,B14 | Five 2.3 W and +X 1.8 W targets; two series cells/face | PROJECT DECISION D1-SYS-001; geometry CAD-A04 | Six individual panel envelopes; no invented cells |
| R03,R07 | +Z panel | Z 51:54 | PROJECT DECISION D1-ANA-001; XY CAD-A04 | SolarPlusZAntSMounted |
| R04,R05 | Mass/COM | 1330 g ceiling, +/-10 mm target | PROJECT DECISION requirements; 1063.5 g BOM sum CALCULATED | MassLedger; no certified COM |
| R03,R11,R13,R21,R24 | Mounts, restraints, vents, switches, harness | Supplier-controlled; numerical geometry absent | UNKNOWN D1-ICD-001, D1-ENV-001, D1-AIV-001 | UnresolvedInterfaces records |

Each geometric object's native properties also carry evidence, source, requirement,
BOM and role. Spreadsheet rows repeat provenance per scalar parameter.
SOURCE VERIFIED means a catalog statement was checked, not delivered hardware measured.
MODELED is independent of source confidence; no CAD artifact is SIMULATED, TESTED
or EXPERT-REVIEWED by virtue of its existence.

## Manufacturer checks

Revisited existing registered sources, without contacting vendors or downloading
gated manuals. Values do not establish as-ordered configuration or tolerances.

- [S03 ICEPS2 v1.2](https://www.isispace.nl/wp-content/uploads/2025/01/ISIS-ICEPS2-DSH-0001-ICEPS2_Datasheet-01_02.pdf), physical table p9: Type A 96 x 92 x 26.5, excludes CSKB; 184 g nominal with 179–189 g range. PDF also describes higher-capacity battery options than the 22.5 Wh planning baseline; configuration reconciliation remains open, not a CAD-driven power change.
- [S08 A3200 v1.17](https://gomspace.com/wp-content/uploads/2025/09/NanoMind_A3200.pdf), p12 physical table: 65 x 40 x 7.1 and 24 g including shield.
- [S10 AX100 v3.7](https://gomspace.com/wp-content/uploads/2025/09/gs-ds-nanocom-ax100.pdf), p4: 65 x 40 x 6.5 and 24.5 g; p22 illustrates two modules on DMC-3. This does not fix mating heights or harness clearance in this spacecraft.
- [S05 AntS](https://isispace.nl/product/vhf-uhf-antenna-for-1u-3u/), product table: stowed 98 x 98 x 7 including cover, mass <90 g. Preserve conservative BOM 90 g and separate top-panel allowance; cover substitution unverified.
- [S23 CS-101](https://crystalspace.eu/products/cs-101-kikas/) current text offers gated brief; original 42 x 25 x 45 and 50 g are retained from project documentation but were not independently recovered in the current page text. No form submitted.
- [S13 DMC-3](https://gomspace.com/UserFiles/Subsystems/datasheet/gs-ds-nanodock-dmc-3-112.pdf) direct retrieval failed again. Outline, supports and mating dimensions remain provisional.
- [S06 frame](https://www.cubesatshop.com/product/1-unit-cubesat-structure/) and [S02 EPS](https://www.isispace.nl/product/compact-electrical-power-system/) listings were inspected; no controlled, selected-configuration frame CAD has been incorporated.

No numerical hole pattern was extracted from a rendered mechanical drawing;
only the identified published envelope tables are used at this fidelity.
