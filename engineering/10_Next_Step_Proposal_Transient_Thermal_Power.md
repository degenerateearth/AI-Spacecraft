# D1-AN-THM-001 — Proposed preliminary transient thermal-power model

> **POST-EXECUTION CORRECTION — TMI-001:** The resulting code and numbers are
> retained only as HYPOTHETICAL PARAMETRIC SENSITIVITY — NOT COMPONENT-SPECIFIC.
> Critical thermal properties were assumptions, no physical hardware was tested,
> and the work did not advance THM-002 or EPS-007. See
> `review/incidents/Thermal_Model_Incident.md`.

Revision 0.2 · 2026-09-15 · **APPROVED AND EXECUTED**

## Decision record

The owner approved this bounded analysis task on 2026-09-15. Execution produced
the canonical artifacts listed below and the findings in
`engineering/11_Transient_Thermal_Power_Analysis.md`. Approval covered analysis
and documentation only; no purchase, external contact, fabrication, testing or
flight-release decision was authorized or performed.

## Why this step is next

The present scalar screen calculates equilibrium temperatures but omits thermal
inertia, conductance between parts and the duration of orbital sunlight and
eclipse. It therefore cannot assess battery charge-temperature protection,
heater energy, cold recovery, camera use or radio duty cycling. These are
coupled feasibility questions for the current 1U architecture.

This analysis can make meaningful progress with current public information and
free/open tools. Uncertain orbit, surface, contact and component properties can
be represented as bounded cases and sensitivity variables. Mission-specific
thermal test limits, as-built conductances and model correlation remain
KDD-01/KDD-02/KDD-05/KDD-06 and will not be invented.

## Proposed scope

1. Create a lumped-parameter network with identifiable nodes for the six solar
   panels, structure/rails, battery/EPS, avionics stack, radio/antenna hardware
   and camera bay.
2. Model orbital sunlight/eclipse transitions, solar input, albedo, Earth IR,
   radiation to space, internal mode dissipation and conductive links.
3. Couple battery/heater energy to the existing power model so heat and
   electrical energy use the same operational cases.
4. Run nominal 450, 475 and 500 km cases plus conservative public-information
   bounds for beta angle, optical properties, conductance, internal dissipation,
   initial temperature and degraded power.
5. Include cold startup/recovery, repeated low-generation orbits, hot imaging
   and downlink operations, and heater stuck-on/stuck-off fault cases.
6. Report temperature histories, limit excursions, heater energy, sensitivities
   and which assumptions dominate the result.

## Canonical deliverables

- `analysis/thermal_transient.py` — readable model and solver;
- `analysis/thermal_inputs.json` — values, units, ranges, provenance and evidence
  class for every input;
- `analysis/thermal_cases.csv` and `analysis/thermal_results.csv` — machine-
  readable cases and results;
- plots suitable for technical review;
- `engineering/11_Transient_Thermal_Power_Analysis.md` — equations, sources,
  configuration, results, limitations, numerical checks and design implications;
- updated requirements, open issues, readiness rows, status and configuration
  record if evidence changes.

The implementation will use the bundled Python runtime and free/open Python
libraries already available where practical. The model will retain a
standard-library execution path if a nonessential plotting library is absent.

## Evidence and acceptance criteria

The task is complete when:

- every numerical input has units, provenance and an evidence label;
- energy and sign conventions are documented and conservation residuals are
  checked;
- time-step convergence and at least one analytically checkable limiting case
  are demonstrated;
- results are reproducible from a clean invocation;
- uncertainty/sensitivity results show whether temperature conclusions are
  robust or assumption-driven;
- the model is compared with the current scalar screen and coupled power
  budget;
- no result is labeled `SIMULATED` beyond the configuration and cases actually
  executed; and
- unresolved values are preserved as assumptions, unknowns or known downstream
  dependencies.

This analysis can move THM-002 and EPS-007 forward but cannot close thermal
qualification, flight survival or twelve-month reliability. Those claims still
require released geometry/materials, as-built measurement, physical
thermal-vacuum/balance testing and independent review.

## Cost and boundary forecast

| Cost category | Increment authorized by this proposal |
|---|---:|
| AI expenditure | USD 0 beyond the existing ChatGPT Plus baseline |
| Software/tool expenditure | USD 0 planned |
| Spacecraft hardware expenditure | 0 |
| Ground-station expenditure | 0 |
| Testing/verification expenditure | 0 |
| Regulatory/licensing expenditure | 0 |
| Launch/integration expenditure | 0 |
| External professional/expert-review expenditure | 0 |

Expected boundary: public data are unlikely to establish actual joint
conductance, surface properties, internal EPS losses or flight-unit behavior.
The model should identify how accurately each must later be measured or supplied.
Encountering an input whose uncertainty prevents any useful conclusion will be
recorded as a consumer-AI/public-toolchain boundary rather than concealed.
