# D1-RVW-001 — Open issues and release gates

Revision A. The package is ready for an aerospace engineer to audit its choices, assumptions and missing evidence. It is not a completed CDR or a manufacturing release. Critical and high items below block a claim of demonstrated launch survival and twelve-month capability.

| ID | Priority | Issue | Owner role | Closure artifact | Requirements |
|---|---|---|---|---|---|
| O01 | Critical | EXOpod Nova is only a provisional mechanical reference; launch mission, integrator contract, target orbit and mission ICD are not selected | Systems/mission | Written offer/contract and signed ICD; injection/collision/decay/demise analysis | R01,R03,R21,R25 |
| O02 | Critical | RF authorization and band unresolved; 437MHz conditional | Regulatory/RF | Approved service/frequency and ground authority; update hardware if needed | R17 |
| O03 | Critical | Thermal feasibility is unknown. D1-AN-THM-001 used unsupported thermal properties and is retained only as hypothetical sensitivity under TMI-001 | Thermal/EPS | Selected component property evidence, released thermal interfaces, component-specific model, correlation and verified controls | R08,R10,R22; review/incidents/Thermal_Model_Incident.md |
| O04 | Critical | EPS 3.3V tolerance incompatible with direct avionics connection | Electrical | Released adapter/protection or guaranteed supplier interface; environmental/radiation verification | R15,R23 |
| O05 | Critical | Three-inhibit independence and solar paths unproven | Safety/EPS | Supplier circuit review/fault tree and all-state test | R11,R13 |
| O06 | Critical | Radiation critical-part evidence missing | EEE | Orbit/dose/SEE assessment; lot/revision evidence or qualification | R01,R23 |
| O07 | High | Camera-aperture panel and 1U stack fit not established | Mechanical/payload | Vendor CAD, aperture cell layout and power guarantee; build fit | R03,R27 |
| O08 | High | DMC-3 has a current quote route, but the exact option configuration, delivered revision, price and supply commitment are unresolved | Procurement | Complete OSF 1012964 from a released pin map; later reconcile quote/delivered revision before purchase | R06,R15 |
| O09 | High | Camera electrical/power/shutter/Sun exposure/JPEG details gated | Payload | Current CS-101 brief and confirmed configuration plus tests | R02,R28,R29 |
| O10 | High | NOAA license/determination not obtained | Regulatory | Full-capability filing and required authority | R18 |
| O11 | High | One-year battery evidence and passivation behavior unknown | EPS | 6000-cycle/calendar evidence and source passivation verification | R09,R26 |
| O12 | High | Mode5 sensitivity/pattern/contacts not demonstrated | RF/ops | Actual threshold, radiation pattern and pass simulation | R16,R19 |
| O13 | High | No structural FEA/environment profiles/test reports | Mechanical/AIV | Accepted loads model, margins and final assembly tests | R21,R30 |
| O14 | High | No quantified image opportunity rate with uncontrolled attitude | Mission/payload | Attitude/orbit Monte Carlo and scene replay; accept opportunity risk | R02 |
| O15 | Medium | All selected flight prices are estimates | Procurement | Comparable quotes with tests/software/support separated | R06,R32 |
| O16 | High | Flight firmware and boot recovery only specified | Software | Implemented versioned code and fault-injection/rehearsal evidence | R14,R20 |

## Review disposition

PDR: candidate design, conditional budget closure. CDR: NOT PASSED. Fabrication release: NOT PASSED. Test readiness: NOT PASSED. Flight readiness: NOT PASSED.

Systems reviewer: __________ Date: __________
Electrical/safety reviewer: __________ Date: __________
Mechanical/thermal reviewer: __________ Date: __________
Radiation/reliability reviewer: __________ Date: __________
RF/regulatory reviewer: __________ Date: __________
Payload/operations reviewer: __________ Date: __________

The owner approved opportunistic Earth imagery, US operation and nominal 450–500 km with flexibility for a lower-cost rideshare. No arbitrary financial ceiling applies. In-scope engineering decisions may be refined without changing those requirements. Targeted imagery or guaranteed spatial resolution requires a new mission baseline.
| O17 | High | Thermal Model Incident: executable calculation was mistaken for component evidence because critical inputs were assumptions; full component-specific thermal, orbit-decay and radiation analysis remain unexercised | Experiment/toolchain | Enforce source-completeness gates; record each boundary and never replace missing critical properties with generic values | Constitution §§21–24; TMI-001 |
| O18 | Medium | Actual AI subscription/tooling spend has not been reconciled against account records | Experiment/accounting | Update Project_Cost_Ledger.csv and Project_Status.yaml with verified amounts and dates | Constitution §22 |

## CAD-001 accommodation findings

| ID | Priority | Issue / assumptions | Owner role | Closure artifact | Requirements |
|---|---|---|---|---|---|
| O19 | High | Rail/board/EPS/AntS bounding envelopes intersect; CAD-A01/A02 and CAD-C01 | Mechanical | Controlled frame and selected component corner profiles, mounting and tolerance stack | R03,R21,R30 |
| O20 | High | Provisional solar panel geometry intersects EPS/AntS/camera; CAD-A04 and CAD-C02–C05 | Mechanical/payload/EPS | Agreed panel footprint, stackup, aperture, cell string routing and camera bracket | R03,R07,R27 |
| O21 | High | DMC carrier and module placements, mating heights, connectors, harness and deployment sweep unknown; CAD-A03/CAD-C06/C07 | Mechanical/RF | Released carrier ICD, connector access/bend radii, antenna sweep and lens pupil/FOV checks | R03,R12,R16,R28,R30 |
| O22 | High | Assigned BOM mass is not CAD material mass; 295 g unmodeled/unlocated; COM not credible | Mechanical | As-ordered masses/COM, frame and mounting geometry, complete mass reconciliation | R04,R05 |

Dimension provenance, provisional values and documented-design -> CAD-conflict ->
proposed-correction records are in [CAD traceability](../drawings/freecad/TRACEABILITY.md)
and [CAD findings](../drawings/freecad/FINDINGS.md). No correction changes the architecture yet.

## External readiness audit findings — 2026-09-15

| ID | Priority | Issue | Owner role | Closure artifact | Readiness rows |
|---|---|---|---|---|---|
| O23 | Critical | No independent aerospace feasibility review has occurred; current evidence is AI-generated and self-audited | Chief engineer/independent review board | Reviewer qualifications, signed review record, findings and dispositions | GOV-007,GOV-010,MIS-008 |
| O24 | High | No named project organization, decision authority, WBS, resource-loaded schedule or committed funding plan | Owner/project manager | Accepted RACI/authority matrix, WBS, critical-path schedule and funding gate | GOV-003–005 |
| O25 | High | Requirements and T01–T18 are preliminary but not a closed bidirectional verification baseline with executable procedures | Systems/AIV | Approved requirements baseline, verification cross-reference and detailed procedures | SYS-003,SYS-004,AIV-003 |
| O26 | High | Ground site, station design, software, contact analysis and trained operators are absent | Ground/RF/operations | Site survey, released ground BOM/design, software, coverage analysis and rehearsal records | GRD-001–006,OPS-003 |
| O27 | Critical | Legal operator/entity and accountable regulatory contacts are undefined, blocking defensible FCC/NOAA/FAA paths | Owner/regulatory | Operator identity/ownership record, licensing strategy and responsible contacts | REG-001–007 |
| O28 | High | No complete materials/processes/outgassing list, detailed hazard reports or battery transport package exists | Materials/safety/QA | As-built materials/process list, hazard analyses and accepted battery/shipping evidence | MEC-008,MEC-009,LCH-003,REG-009 |
| O29 | High | Verification article strategy, facilities, fixtures, EGSE, calibration and quality system are not baselined | AIV/QA/project manager | Approved model philosophy, facility/equipment plan, quality/AIT plan and funded schedule | AIV-001–005 |

The complete 108-item audit and closure criteria are in
[Master CubeSat Readiness Checklist](Master_CubeSat_Readiness_Checklist.md).
These findings lower the honest project maturity assessment to Constitution
Level 0 with partial progress toward Level 1; they do not alter the spacecraft
architecture.

## Launch and deployer constraint-gate findings — 2026-09-15

| ID | Priority | Issue | Owner role | Closure artifact | Requirements |
|---|---|---|---|---|---|
| O30 | Critical | Public EXOpod Nova documentation does not supply a 1U price, available mission/orbit, customer electrical safety and battery rules, test levels, delivery schedule or signed acceptance criteria | Owner/systems/launch integration | Common mission data sheet; comparable written EXOLAUNCH/ISISPACE responses; selected offer and controlled mission ICD | R01,R03,R06,R11–R13,R21,R25 |
| O31 | High | CAD matches nominal Nova envelope numbers but lacks rail tolerances/profile/finish, switch and RBF access, credible COG/inertia and physical fit evidence | Mechanical/AIV | Controlled B01 CAD/certificates, tolerance analysis, complete mass properties and Nova/TestPod fit/ejection report | R03–R05,R21,R30 |

The three-path trade and conflict records LDC-01–LDC-06 are in
[D1-LCH-001](../engineering/09_Launch_and_Deployer_Baseline.md). The reference
selection changes planning evidence only. It does not close O01, O05, O13,
LCH-001, LCH-002 or AIV-006.

## Phase 1 component-evidence findings — 2026-09-15

| ID | Priority | Issue | Owner role | Closure artifact | Requirements |
|---|---|---|---|---|---|
| O32 | Critical | No physical component currently passes the complete Phase 1 mission-relevant public-evidence gate; several BOM lines are allowances rather than identified parts | Systems/procurement/subsystem leads | Property matrix with no required UNKNOWN/CONFLICT rows for each admitted part; exact configurations and archived/hash-controlled primary sources | R01,R03,R06–R10,R14–R23 |
| O33 | Critical | ICEPS2 current page and linked issue 1.2 datasheet disagree on Type A battery energy/configuration | EPS/safety | Reconciled exact Type A configuration and controlled evidence; revised energy/life analysis | R08–R10,R22 |
| O34 | High | CS-101 lacks public mission-critical data; piCAM/FM is better documented but still lacks enough evidence for baseline admission | Payload/radiation/EPS | Selected exact camera with complete property evidence, interface design and verification plan | R14–R18,R23 |
| O35 | High | DMC-3 availability was previously recorded incorrectly; current documents exist, but its order-option configuration is not selected | CDH/integration | Completed OSF 1012964 configuration and pin-by-pin interface review | R06,R07,R19,R21 |
