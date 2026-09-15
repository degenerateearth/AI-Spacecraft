# Configuration log

Rev A — 2026-09-14. Initial issued package for Degen-1. Owner scope: occasional recognizable Earth images, US-operated, nominal 450–500 km LEO, flexible rideshare if it lowers cost/complexity, lowest reasonable COTS build cost, distinct program cost categories and no arbitrary financial ceiling.

Working calculations were revised before this release to add the CS-101 camera, aperture-panel derating, updated stack allocations, Mode 5 radio framing and independent regulator interface. Only the issued imaging configuration is included in the deliverable package. No hardware has been acquired, modified or tested.

The package is a preliminary engineering design with formal open items. Subsequent revisions must log changed assumptions, affected requirements, budgets, vendor revisions and verification evidence. A hash manifest identifies this issue's exact files.
Rev B — 2026-09-14. Updated the constitution and supporting documentation to make the consumer-AI/free-software constraint explicit. Added the eight-category cost ledger, status schema, and AI toolchain boundary procedure. No spacecraft mission, design, or success-level claim was silently changed.

CAD-001 — 2026-09-14. Translated Revision A allocations into a FreeCAD 1.1.3
parametric envelope model. Retained documented Z locations and expanded EPS/AntS
from old sketch placeholders to published envelope dimensions. Assumptions and
23 bounding-envelope overlaps recorded; real material interference is not proven.
Added native/STEP exports, generation script, source traceability, mass ledger,
software verification and O19–O22. No flight hardware, FEA, thermal simulation,
expert review, design release or higher success level results from this work.

PA-001 — 2026-09-15. Audited exactly the existing B01–B16 BOM lines. Added one
component card per line, a sortable master audit, source/order-route check and a
reproducible generator that fails if BOM IDs, quantities or cost allowances drift.
Recorded current vendor facts separately from project requirements, assumptions
and unknowns. B01's public €3,450 listing exceeds its €3,000 base allowance; the
controlled BOM was not rebased. B08 availability remains unconfirmed. No new
component, purchase, supplier contact, test or procurement release resulted.

ERA-001 — 2026-09-15. Selected the University of Hawaiʻi *A Guide to CubeSat
Mission and Bus Design*, Edition 1, as an external development framework and
supplemented it with primary CubeSat, NASA, FCC, NOAA, FAA and future launch-ICD
sources. Audited the full repository against 108 applicable readiness items:
3 complete, 21 provisionally addressed, 26 in progress, 28 not started and 30
blocked. Added O23–O29. Corrected project status from Level 1 to Level 0 with
partial evidence toward Level 1 because internal design closure, hardware,
testing, regulatory approval and expert review do not exist. No architecture or
mission change resulted.

LDG-001 — 2026-09-15. Compared three public 1U launch/deployer paths and
selected a standard EXOpod Nova 1U slot as provisional mechanical reference.
Retained ISISPACE/ISILaunch as the commercial alternate and Voyager/NRCSD as a
lower-orbit fallback. Moved LCH-001 from BLOCKED to IN PROGRESS. Public sources
do not establish an available 450–500 km slot, firm 1U price, mission ICD or
one-year orbit residence. This planning decision changes no component, CAD
geometry, launch commitment, orbit, cost estimate, licensing status or
Constitution success level. Evidence: engineering/09, Launch_Deployer_Trade.csv,
S33–S40, O01/O30/O31 and R03–R05/R11.

PIR-001 — 2026-09-15. Defined the present public-information development phase
and separated work that can proceed now from final closure requiring vendor,
integrator, regulator, test-facility or expert evidence. Added the known
downstream dependency register and reassessed the 108-row readiness matrix.
Retained the public EXOpod Nova baseline as provisional. No external contact,
component, requirement waiver, flight release or success-level change resulted.

THM-001 — 2026-09-15. Executed the approved D1-AN-THM-001 preliminary
transient thermal-power model using standard-library Python and public/project
inputs. Modeled all 1.0635 kg in 11 nodes across 10 orbital, environment,
attitude, heater-fault and conductance cases. Central nominal, cold, hot and
fixed-camera recovery cases do not close battery temperature and stored energy;
a deliberately low-conductance nominal sensitivity closes, making the thermal
interface a controlling design variable. R08/R10/R22 now record simulated
failure; O03 remains critical; THM-002 and EPS-007 moved to IN PROGRESS. No
hardware, paid software, external contact, test, expert review, architecture
change or success-level increase resulted.
