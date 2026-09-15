# D1-QA-001 — Issued-package verification

2026-09-14. These are document and analytic-model checks, not hardware tests.

- PASS: Unique BOM IDs
- PASS: Six solar panels including aperture panel
- PASS: BOM mass reconciliation
- PASS: Base hardware cost reconciliation
- PASS: Mass with growth below project target
- PASS: Recovery closes after camera-face derating
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

2026-09-15 component-audit check: PASS. `Components/generate_component_cards.py`
regenerated 16 cards and one 16-row CSV, with exact B01–B16 ID order and assertions
against the controlled BOM quantities and low/base/high cost allowances. This is a
documentation consistency test, not component verification.

Orbit sensitivity is in `analysis/orbit_sensitivity.csv`: 400 and 550 km are trade points only. No cheaper available rideshare is asserted without a quote; neither point has a qualified orbital lifetime.
