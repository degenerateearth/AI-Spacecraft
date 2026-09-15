# D1-CMP-STD-001 — Phase 1 component evidence standard

Revision A · 2026-09-15

## Purpose

Phase 1 prefers a component whose critical behavior can be checked from public
manufacturer evidence over a nominally better component that requires hidden
assumptions. This standard applies before a part is called a Phase 1 reference
component. It does not constitute procurement release, qualification or flight
approval.

## Phase 1 Component Evidence Requirement

Every physical component selected for the Phase 1 spacecraft baseline must
correspond to an identifiable, commercially obtainable part or an explicitly
documented custom-fabricated part.

Every selected COTS component must have publicly accessible, independently
verifiable manufacturer technical documentation sufficient to establish the
properties relevant to its use in DEGENERATE-1. A manufacturer datasheet, ICD,
user manual, mechanical drawing, qualification report or equivalent primary
document is acceptable only when its actual contents establish the needed
property. The existence of a document or product page is not evidence that an
unstated property is known.

At minimum, the evidence set must establish, as applicable: exact manufacturer
and part number/configuration; dimensions and mass; electrical interfaces;
supply voltage, current and power in all relevant modes; communications
interfaces and protocols; connector and pinout information; operating, storage
and thermal limits; mechanical interfaces; and deployment or operational
constraints. Mission life, environment and safety properties are required when
they are needed to analyze the assigned function.

Missing required data may not be replaced with generic values, a similar
product's values or AI-generated assumptions to pass this gate.

## Selection states

- **PHASE 1 BASELINE** — exact obtainable COTS configuration or released custom
  design; public primary evidence establishes every property needed for its
  assigned mission function. Configuration-controlled as-built and physical test
  evidence can remain later verification work, but no missing property may be
  silently assumed.
- **CANDIDATE / EVIDENCE INCOMPLETE** — a plausible part, but one or more required
  properties cannot be independently verified. It cannot enter the Phase 1
  baseline. It may remain in trade studies or envelope-only CAD when the evidence
  limitation is displayed with it.
- **UNSUITABLE** — current evidence or availability contradicts the mission, or a
  critical behavior cannot be established and a better documented alternative
  exists.
- **NO DOCUMENTED ALTERNATIVE** — critical property is absent and no better public
  option was found. The function requires a custom component or remains an open
  architecture function; do not simulate the gap.
- **CUSTOM DESIGN** — integration hardware that cannot honestly be represented as
  a purchased COTS subsystem. It needs a released design, constituent BOM and test.

## Minimum evidence gate

Every COTS selection needs:

1. manufacturer and exact public product/part identifier;
2. current manufacturer product or order/quote route and access date;
3. mechanical envelope, mass, mounting/interface drawing and keep-outs needed now;
4. input voltage range, current/power by relevant mode, startup/transient limits
   and output ratings where applicable;
5. named connector, pinout, signal levels and data/protocol information sufficient
   to design and test the interface;
6. operating and storage temperature limits distinguished from qualification;
7. public environmental, workmanship, radiation and heritage claims recorded
   exactly with their scope and revision;
8. software/firmware/API availability for commanded devices;
9. price or explicit `QUOTE REQUIRED`, lead time if published, configuration and
   export restrictions;
10. contradiction check among the current page, datasheet, option sheet, PCN and
    project record.

The gate is function-specific. A passive carrier may not require operating power;
a battery requires cell configuration, charge/discharge limits, protection and
life evidence; a camera requires optics, exposure/image behavior and data transfer;
an antenna requires RF and deployment behavior.

## Missing-property rule

Do not fill a missing critical property with a generic value. Record:

`PROPERTY UNKNOWN -> SOURCE(S) CHECKED -> ANALYSIS BLOCKED -> REQUIRED EVIDENCE`

An assumption may support a clearly labeled geometric envelope or sensitivity
study only when its result cannot be mistaken for component behavior. It may not
pass or fail a requirement, update a hardware readiness level, or become a
procurement specification without an explicit project decision and verification
method.

## Document custody

Each component source pack contains official URLs, document identifiers,
revision/date, retrieval date, evidence classification, project-authored fact
extraction and SHA-256 for any locally retained file. Archived copies are
preserved only where licensing permits. A downloaded file whose license does not
permit redistribution remains local and excluded from the public repository; the
repository keeps its official URL, identity and hash so another reviewer can
retrieve and compare the exact source.

## Evidence ceiling

Public documentation can support DOCUMENTED, CALCULATED and MODELED work. A
catalog claim of qualification or heritage is attributed to the manufacturer and
does not prove the ordered unit, integrated spacecraft, launch survival or one-year
operation. Those require configuration records, inspection, analysis, physical
test and independent review appropriate to the claim.
