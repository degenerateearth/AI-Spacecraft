# Thermal Model Incident

**Incident ID:** TMI-001  
**Date recorded:** 2026-09-15  
**Status:** Open corrective action  
**Evidence level:** DOCUMENTED incident; no physical test or expert review

## Incident statement

The numerical outputs of `D1-AN-THM-001` were presented prominently enough to
be read as results for the proposed ICEPS2 battery/EPS and spacecraft. They were
not. No physical part was purchased or tested, no thermal-vacuum or thermal-
balance data were used, and no manufacturer supplied the critical thermal
properties needed to make a component-specific prediction.

The model used a project-created 11-node geometry and numerous assumed heat
capacities, contact conductances, optical properties, view factors, heater
behavior, efficiencies, attitude histories and initial conditions. The B12
battery strap/isolation did not identify a manufacturer, part number, material
stack or geometry. The model therefore establishes only how that assumed
mathematical system behaves. It does not establish the temperature, heater duty,
energy margin, survival or suitability of ICEPS2 or any flight configuration.

## Trigger

The owner asked whether the reported values came from testing an actual physical
part with a vendor and part number against the vendor's stated documentation.
The answer was no. That challenge exposed a mismatch between the written caveats
and the prominence and specificity of the reported numerical results.

## Affected records

- `analysis/thermal_inputs.json`, `thermal_transient.py`, generated CSV/JSON/SVG
- `engineering/11_Transient_Thermal_Power_Analysis.md`
- `README.md`, `MILESTONES.md`, `review/Project_Status.yaml`
- R08, R10 and R22 status text
- EPS-002, EPS-007 and THM-002 readiness evidence
- O03 and O17

The original model and outputs are preserved because incorrect assumptions and
overstated interpretations are experimental evidence. They are reclassified as
**HYPOTHETICAL PARAMETRIC SENSITIVITY — NOT COMPONENT-SPECIFIC**.

## Root cause

1. The input file mixed a few documented component facts, such as mass and
   envelope, with unsupported thermal properties in one executable model.
2. The object name `battery_eps` and use of an ICEPS2 mass made an assumed node
   appear more specific than its evidence supported.
3. Readiness rows used `SIMULATED`, which described an activity but could be
   mistaken for validation of the selected hardware.
4. The report led with precise temperatures and energy values even though the
   parameters controlling those values were unknown.
5. There was no source-completeness gate preventing component-specific reporting
   when critical input properties were assumptions.

## Corrective disposition

- Withdraw every component-specific interpretation of the thermal numbers.
- Do not use the model to pass or fail R08, R10, R22, EPS-007 or the spacecraft.
- Give it no hardware-validation readiness credit.
- Preserve it only as a code-verification and sensitivity-study artifact.
- Require a named component/configuration and traceable values or bounded,
  justified ranges for critical properties before another component-specific
  thermal run: heat capacity/mass distribution, interfaces/contact conductance,
  surface finish/optical properties, internal dissipation by mode, heater and
  sensor topology/control, component temperature limits and attitude/orbit flux.
- When a critical value is unavailable, record an evidence gap and the blocked
  analysis. Do not substitute a generic value to obtain a result.
- Future plots and summaries must carry the evidence classification beside the
  number and state explicitly whether hardware was tested.

## Present engineering consequence

Thermal feasibility, battery charging temperature, heater energy and recovery
energy remain unknown for the proposed hardware. The current public ICEPS2
documentation supports some electrical and operating limits but does not supply
the internal thermal network or installed conductances required for this model.
The battery thermal interface is not yet a selected component or released
design. Component selection and a property-evidence audit must precede further
component-specific thermal work.

## Closure criteria

This incident may be closed only after all affected records use the corrected
classification, the component audit applies an explicit evidence gate, and an
independent reviewer confirms that the project cannot reasonably mistake the
hypothetical study for hardware evidence. Closure will not validate the thermal
design; it will only verify the record correction.
