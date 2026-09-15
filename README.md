# DEGEN-1
## 1U CubeSat preliminary engineering design — Revision A

Issued 14 September 2026. Status: **AUDITABLE PRELIMINARY DESIGN / NOT RELEASED FOR FABRICATION OR FLIGHT**.

## First engineering step

The controlling first engineering gate is [Phase 1 component evidence
closure](review/First_Engineering_Gate.md). DEGENERATE-1 must establish an exact,
commercially obtainable or explicitly custom-designed component for every
required function before further simulation, higher-fidelity CAD, procurement or
performance claims can control the project. Existing calculations and CAD remain
preliminary records and do not supply missing component properties.

The [complete proposed operating component set](Components/Proposed_Operating_Component_Set.md)
now covers 19 flight and 10 ground hardware lines. It is a functionally complete
proposal and an explicit gap register, not a Phase 1 baseline: every COTS line is
still evidence incomplete, every custom line is unreleased, or no compliant exact
part has yet been identified.

The design targets one year of opportunistic imaging and housekeeping telemetry in LEO at low build cost using commercially marketed CubeSat subsystems. The owner selected occasional recognizable Earth images, US operation and nominal 450–500 km LEO, with no arbitrary spacecraft budget ceiling. Revision A proposed a CrystalSpace CS-101 camera; the evidence audit prefers SkyFox piCAM/FM, but neither is admitted to the Phase 1 baseline. Selected-location imaging or mapping would require a revised baseline.

The pre-gate candidate architecture uses an ISISPACE 1U chassis, six fixed solar panels, ICEPS2 Type A battery/EPS, AntS UHF antenna, and GomSpace A3200/AX100-U avionics on a DMC-3 carrier. One small custom adapter is required to resolve supply-voltage tolerance and inter-vendor routing. No propulsion, reaction wheels, GNSS receiver or deployable solar arrays are included. This paragraph records the proposed architecture and is not a released component baseline.

The original [component audit](Components/README.md) covers every existing B01–B16 BOM line. The stricter [Phase 1 functional audit](Components/Phase1_Functional_Audit.md), [105-row property matrix](Components/Phase1_Component_Property_Matrix.csv) and [evidence standard](review/Phase1_Component_Evidence_Standard.md) find that **no physical component has yet passed into the Phase 1 baseline**. Named products remain candidates until public primary evidence establishes every mission-relevant property. The audit identifies SkyFox `piCAM/FM` as a better documented camera candidate, corrects NanoDock DMC-3 availability, and records Pumpkin structure/panel alternatives without promoting them. None of these findings silently changes the controlled BOM.

**Planning results:** 1.064 kg current best estimate, 1.276 kg including 20% growth; EUR46,500 base flight-hardware allowance (EUR29,350–70,100 range). These are engineering estimates, not supplier quotations. Spacecraft build, including engineering/prototype hardware, assembly and nonrecurring engineering labor, is EUR152,500 base before contingency. Testing, ground station, licensing, launch and operations are separate categories. The cost report explains inclusions and uncertainty.

The original scalar power model closes nominal energy at +18.4% with a tumble-average assumption and reported +0.124 Wh/orbit for fixed-attitude recovery. The later 11-node calculation is reclassified as **HYPOTHETICAL PARAMETRIC SENSITIVITY — NOT COMPONENT-SPECIFIC** after the [Thermal Model Incident](review/incidents/Thermal_Model_Incident.md). Its precise numerical outputs depend on unsupported thermal properties and cannot pass or fail the spacecraft or an identified component. Thermal feasibility, orbit lifetime, radiation, inhibit independence and final mechanical/interface compliance remain open. No analysis in this package demonstrates launch survival or twelve-month operation.

### Audit reading order

1. [First engineering gate](review/First_Engineering_Gate.md), [Phase 1 evidence standard](review/Phase1_Component_Evidence_Standard.md), and [functional component audit](Components/Phase1_Functional_Audit.md)
2. [Mission and architecture](engineering/01_Mission_and_Architecture.md)
3. [System budgets and analysis rationale](engineering/02_Budgets_and_Analyses.md)
4. [Interfaces and adapter specification](engineering/03_Interfaces.md)
5. [Mechanical and environmental design](engineering/04_Mechanical_Thermal_Radiation.md)
6. [Flight software and mission operations](engineering/05_Software_and_Operations.md)
7. [Assembly, integration and verification](engineering/06_Integration_and_Verification.md)
8. [Cost and procurement trade](procurement/Cost_and_Procurement.md)
9. [Open issues and review gates](review/Open_Issues.md)
10. [Imaging payload](engineering/07_Imaging_Payload.md) and [US compliance plan](engineering/08_US_Compliance.md)
11. [Launch and deployer planning baseline](engineering/09_Launch_and_Deployer_Baseline.md)
12. [Preliminary transient thermal-power analysis](engineering/11_Transient_Thermal_Power_Analysis.md)
13. [Requirements traceability](review/Requirements.md), [FMEA](review/FMEA.md), [sources](review/Source_Register.md)
14. [Known downstream dependencies](review/Known_Downstream_Dependencies.md)

### Reproduction and configuration

Run `python analysis/recalculate.py` for the original scalar budgets. Run `python analysis/thermal_transient.py --self-test` for the 11-node transient thermal-power model; its canonical inputs are `analysis/thermal_inputs.json` and its CSV/JSON/SVG outputs are regenerated. Both scripts use Python's standard library. Assertions and numerical checks verify model consistency, not flight hardware. The HTML audit book is an earlier generated snapshot; the individual Markdown documents and model inputs are authoritative within this package.

The original SVG is an allocation sketch. [CAD-001 FreeCAD model](drawings/freecad/README.md) now provides editable parametric component envelopes and a STEP review export, with explicit assumptions and fit conflicts. It is not manufacturing CAD or supplier geometry. The electrical diagrams specify functional interfaces, not a released pin-to-pin harness. PCB fabrication files, vendor proprietary ICDs, supplier quotes, hardware test reports and flight software implementation remain incomplete.

All external facts carry source IDs resolved in the source register. **V** denotes vendor-stated information; **A** denotes an engineering assumption/allocation; **C** denotes a calculation; **OPEN** denotes missing evidence. Published product changes supersede older brochures. Engineering approval signatures remain blank; AI authorship is not an engineering release.

## Project purpose — added after Revision A

Read the [Project Overview](Project_Overview.md) for the AI-assisted engineering experiment and the owner's [Project Constitution v0.1](Project_Constitution.md) for its principles and success levels. The Revision A audit book remains the earlier technical snapshot; these documents do not imply a new engineering or flight-readiness release.
## Consumer-AI experiment constraint

The baseline engineering interface is a standard $20/month ChatGPT Plus subscription, including Codex/Astra where available, with free/open-source engineering tools wherever practical. Paid AI or software is not introduced silently. See [AI toolchain and boundaries](review/AI_Toolchain_and_Boundaries.md), [project status](review/Project_Status.yaml), and the separate [project cost ledger](procurement/Project_Cost_Ledger.csv).

Project gates and their required evidence are tracked in [MILESTONES.md](MILESTONES.md). GitHub updates are made at those review points.

Before planning major engineering work, consult the [Master CubeSat Readiness Checklist](review/Master_CubeSat_Readiness_Checklist.md). It audits this repository against an independent University of Hawaiʻi CubeSat development framework plus primary launch, NASA and US regulatory sources. The public-information-phase reassessment leaves the project at Constitution Level 0 with partial evidence toward Level 1. It distinguishes current work from final closure that depends on later vendor, regulator, integrator, test or expert evidence.

The [Launch and Deployer Constraint Gate](engineering/09_Launch_and_Deployer_Baseline.md) selects a standard 1U EXOpod Nova slot as a provisional mechanical reference. No launch, orbit, price, mission ICD or acceptance is selected. EXOLAUNCH and ISISPACE require written offers; ISS/NRCSD remains a lower-orbit fallback whose one-year residence is unproved.

The project is presently in a public-information development phase. Direct
contact for private or mission-specific evidence is tracked as a [known
downstream dependency](review/Known_Downstream_Dependencies.md), while public
analysis, CAD, simulation and test planning continue. This sequencing does not
waive public requirements or turn provisional inputs into release evidence.

Archived external-framework provenance and licensing are recorded in [SOURCES/README.md](SOURCES/README.md).
