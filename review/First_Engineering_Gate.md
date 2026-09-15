# D1-GATE-001 — First engineering gate: Phase 1 component evidence closure

Revision A · 2026-09-15  
Status: **IN PROGRESS — 0 COMPONENTS ADMITTED**

## Required outcome

The first engineering step for DEGENERATE-1 is to establish a complete,
internally coherent and publicly fact-checkable component set for every function
needed to capture, store and downlink a recognizable Earth image.

No further spacecraft performance simulation, higher-fidelity CAD, detailed
interface release or physical procurement may be treated as the controlling next
step until this gate closes. Work already completed remains in the record at its
stated evidence level. It may be used to identify required component properties,
but it cannot supply missing component data or promote a candidate.

## Exit criteria

This gate closes only when:

1. every required function F01–F16 has an assigned exact COTS configuration or a
   released custom-component definition;
2. every COTS selection passes D1-CMP-STD-001 with no mission-relevant property
   recorded as unknown, conflicting, similar-product-derived or assumed;
3. every custom component has requirements, constituent part numbers, released
   interfaces, analysis inputs and a verification path;
4. the selected set has a pin-to-pin electrical/data/RF interface matrix and a
   mechanically consistent mounting/keep-out definition derived from the selected
   documentation;
5. the mass, power, data and cost budgets are regenerated only from the selected
   configurations and explicitly identified project calculations;
6. exact source URLs, revisions/dates, retrieval dates, evidence classifications
   and archive hashes are recorded; and
7. contradictions are resolved or the affected component remains outside the
   baseline.

Commercial availability must be independently supportable. A storefront,
datasheet or option sheet that does not establish the exact required configuration
and properties does not close the gate.

## Present result

- Required functions audited: 16
- Recommended COTS candidates: 8
- Audited COTS alternatives: 2
- Property records: 105
- Complete proposed operating-set lines: 29 (19 flight, 10 ground)
- COTS candidates passing: 0
- Custom components released: 0
- Gate status: **OPEN**

The present record is a screened candidate architecture, not a Phase 1 component
baseline.

`Components/Proposed_Operating_Component_Set.md` now assigns every necessary
flight and ground physical function to a candidate, a project custom-part number,
or an explicit `NO COMPLIANT PART IDENTIFIED` state. Functional list completeness
does not close this gate.

## Immediate work order

Work function by function in dependency order:

1. F01/F02 structure, rails, switches and RBF architecture;
2. F03/F04 EPS and battery exact configuration;
3. F06/F07 OBC and carrier, including D1-IF pin-map requirements;
4. F08/F09 complete flight RF chain;
5. F10 camera and its protection/interface needs;
6. F05 exact face-by-face solar generation hardware;
7. F11–F15 released custom integration hardware;
8. F16 complete ground-station chain; and
9. cross-component interface and budget reconciliation.

When public evidence cannot close a property, record the boundary and the
specific analysis it blocks. Do not skip to simulation with an invented value.
Direct vendor contact and paid services remain downstream unless separately
authorized.
