# D1-QA-001 — Issued-package verification

2026-09-14. These are document and analytic-model checks, not hardware tests.

- PASS: Unique BOM IDs
- PASS: Six solar panels including aperture panel
- PASS: BOM mass reconciliation
- PASS: Base hardware cost reconciliation
- PASS: Mass with growth below project target
- PASS: Scalar recovery arithmetic reproduces its stated assumptions; it is not a thermal or hardware requirement pass
- PASS: Fixed-attitude nominal failure explicitly preserved
- PASS: Nominal energy growth reserve accounted
- PASS: Battery stress below permitted 20 percent DOD
- PASS: Downlink >=3dB assumed-threshold reserve
- PASS: Unique source IDs
- PASS: Markdown local links resolve
- PASS: HTML local links and section anchors resolve
- PASS: Recovery and RF screening positive across 450-500 km
- PASS: all source IDs used in narrative documents resolve.
- Drawing SVG rendered to PNG and visually inspected; coordinate-sign formatting corrected before issue.

The executed calculation script passed its internal assertions. BOM and source identifiers, totals and local links were independently checked. This does not close assumptions about thermal, radiation, orbit decay, supplier hardware, regulatory eligibility or physical tests.

2026-09-15 Thermal Model Incident correction: PASS for record consistency. The
model input, generated case rows, verification JSON, report, requirements,
readiness rows, status and mechanical/thermal narrative identify D1-AN-THM-001
as HYPOTHETICAL PARAMETRIC SENSITIVITY — NOT COMPONENT-SPECIFIC. THM-002 is NOT
STARTED and EPS-007 is BLOCKED. Numerical checks validate code behavior only.

2026-09-15 component-audit check: PASS. `Components/generate_component_cards.py`
regenerated 16 cards and one 16-row CSV, with exact B01–B16 ID order and assertions
against the controlled BOM quantities and low/base/high cost allowances. This is a
documentation consistency test, not component verification.

2026-09-15 external-readiness check: PASS. The generator produced 108 unique
matrix IDs, accepted only the six controlled status values, and reconciled the
summary to 3 complete, 21 provisionally addressed, 26 in progress, 28 not
started, 30 blocked and 0 not applicable. This verifies matrix consistency only;
it does not validate the University framework, close any row or constitute an
independent engineering review.

2026-09-15 Phase 1 component-evidence check: PASS for document consistency. The
generator produced 105 property rows for eight recommended COTS candidates and
two audited alternatives. All ten
gate rows are FAIL with disposition CANDIDATE / EVIDENCE INCOMPLETE; the Phase 1
baseline count is zero. The local archive manifest records fourteen manufacturer files,
byte counts, SHA-256 values, exact official URLs, revision/date and retrieval
date. Copyrighted PDFs and page captures are ignored by Git. This check validates record structure,
not component performance, obtainability, compatibility or flightworthiness.

2026-09-15 launch/deployer gate check: PASS. The public trade contains exactly
LD-01 through LD-03 and selects only LD-01 as the provisional mechanical
reference. The regenerated readiness matrix contains 108 unique IDs and
reconciles to 3 complete, 21 provisionally addressed, 27 in progress, 28 not
started, 29 blocked and 0 not applicable. The D1-LCH-001 dimensional screen
reconciles the CAD's nominal 100 x 100 x 113.5 mm envelope and 1.2762 kg growth
mass against the public EXOpod values. No tolerance, physical fit, available
slot, orbit, price, mission ICD or acceptance is claimed.

Orbit sensitivity is in `analysis/orbit_sensitivity.csv`: 400 and 550 km are trade points only. No cheaper available rideshare is asserted without a quote; neither point has a qualified orbital lifetime.

2026-09-15 first-engineering-gate check: PASS for sequencing consistency.
`review/First_Engineering_Gate.md`, the constitution, README, overview, milestone
register, status record, requirements and configuration log all identify Phase 1
component evidence closure as the controlling first engineering gate. M1 and M3
retain their preliminary evidence without further advancement. The gate remains
OPEN with 0 COTS and 0 custom components admitted.

2026-09-15 complete-operating-set check: PASS for list consistency.
`Components/generate_proposed_operating_set.py` produced 29 unique rows and 29
individual component cards: 19 flight and 10 ground. No row is marked `PHASE 1 BASELINE`. Eight custom/site
assemblies have project identifiers and development records; five functions say
`NO COMPLIANT PART IDENTIFIED`. This verifies coverage and labeling only, not
functional compatibility, component compliance or obtainability.

2026-09-16 detailed-baseline ADCS check: PASS for source custody and record
consistency. `D1-ADCS-001` selects the exact K&J `D84` magnet and defines two
custom 95 mm × 1 mm HyMu 80 rods from the published Quetzal-1 flight
architecture. The local archive manifest now contains 23 files; all 23 local
files match their recorded byte counts and SHA-256 hashes. The ADCS remains
`CUSTOM/TO BE VERIFIED`: no Degen-1 magnet moment, rod minor loop, integrated
magnetic survey, cage test or attitude simulation result exists.
