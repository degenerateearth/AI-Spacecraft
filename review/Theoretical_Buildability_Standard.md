# D1-DES-STD-001 — Education-grade theoretical buildability standard

Revision A · 2026-09-16  
Status: **CONTROLLING DESIGN COMPLETION STANDARD**

## Purpose

DEGENERATE-1 reaches the current project's design goal when an aerospace
engineering student or engineer can independently audit a coherent, theoretically
viable spacecraft and ground-station design using the repository and its cited
public evidence. Purchasing, fabrication, physical testing, qualification,
licensing and launch-provider acceptance are later implementation and validation
stages. They are not prerequisites for completing this theoretical design.

This standard does not relax evidence discipline. A polished drawing, calculation
or AI assertion is not physical proof. The final package must identify each claim
as DOCUMENTED, PROJECT DECISION, CALCULATED, MODELED, SIMULATED, TESTED or
EXPERT-REVIEWED. Untested work remains untested.

## Design-complete exit criteria

The education-grade theoretical design is complete only when:

1. the mission and operating concept are fixed and every required function maps
   to an exact, commercially identifiable part or a released custom design;
2. every selected COTS part has a manufacturer, exact model/configuration,
   order or quote route and primary technical documentation sufficient for the
   properties used in the design;
3. every custom item has requirements, a schematic or dimensioned drawing as
   applicable, exact constituent BOM, interfaces, material/process notes,
   assembly instructions and a verification plan with acceptance criteria;
4. electrical, data, RF and mechanical interfaces are reconciled pin-to-pin or
   feature-to-feature, including connectors, contacts, cables, fasteners,
   clearances, inhibits, service access and fault-safe states;
5. mass, center of mass, power, energy, data storage, communications, thermal,
   structural screening, orbit/debris and cost budgets are reproducible from the
   selected parts and explicit calculations, with uncertainty and margin;
6. the spacecraft fits its stated 1U/deployer reference in the released model,
   and all known collisions or installation contradictions are resolved or
   explicitly prevent design completion;
7. flight and ground software architecture, command/data definitions, safe-state
   behavior, image reconstruction and print workflow are specified sufficiently
   to implement and verify;
8. assembly, inspection and verification procedures define how a future build
   would establish workmanship, functional performance and environmental
   readiness;
9. regulatory, spectrum, debris, launch-integration and independent-review work
   that necessarily depends on a real operator, site, launch or as-built article
   is identified as downstream, with no claim that it has occurred; and
10. an independent reviewer can trace important requirements through decisions,
    parts, calculations, geometry and proposed verification without relying on
    hidden assumptions or unavailable AI reasoning.

## Permitted evidence for this goal

Manufacturer datasheets, manuals, drawings and qualification summaries can
support COTS properties. Published standards, textbooks, papers and government
guidance can support methods and environmental assumptions. Reproducible
calculations, free/open simulations and parametric CAD can support theoretical
viability when their inputs are traceable and their limitations are explicit.

Purchase receipts, incoming inspection and serial-number configuration records
are **not required** for theoretical design completion. Current commercial
obtainability must still be reasonably evidenced because the design is intended
to be buildable, rather than a study of obsolete or fictional hardware.

## Work that remains downstream

The following can remain incomplete after theoretical design release, provided
the design contains a credible verification or reconciliation path:

- purchase, fabrication and as-built configuration control;
- component screening, workmanship inspection and acceptance testing;
- vibration, shock, thermal-vacuum, deployment, EMC and end-to-end RF tests;
- professional structural, electrical, battery-safety and regulatory review;
- FCC/NOAA/NTIA or other applicable filings and approvals;
- exact launch booking, mission-specific ICD reconciliation and integrator
  acceptance; and
- on-orbit operation and mission success.

Those activities determine whether the theoretical design survives contact with
reality. They must never be represented as completed by analysis alone.

## Relationship to the Phase 1 component gate

D1-CMP-STD-001 remains the standard for selecting verifiable components. G1 may
close for the **theoretical design baseline** without purchases or tests when the
exact configurations and every property actually used by the design are supported
or conservatively bounded by authoritative evidence. Unknown properties that are
not used must be labeled and justified as non-controlling. Properties needed only
for later acceptance may remain downstream if the design supplies a verification
method and does not claim the result.

An unavailable private qualification report does not automatically prevent an
education-grade theoretical design. It does prevent claiming the corresponding
qualification. An unavailable command definition, connector pinout, mechanical
drawing or electrical limit that is necessary to connect or operate a selected
part still blocks that selection unless a better-documented part is chosen.

## Completion statement

The permitted final conclusion is: “This is a complete, evidence-traceable,
education-grade theoretical design that appears buildable and viable under its
documented assumptions. It has not been purchased, fabricated, tested,
independently reviewed, licensed, accepted for launch or proven flightworthy.”

The project may not shorten that statement to “flight ready.”
