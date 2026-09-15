# D1-EXP-001 — Consumer-AI/toolchain record

Revision 0.1 · 2026-09-14

This file records the resource constraint for the DEGENERATE-1 experiment. It
is deliberately separate from spacecraft engineering costs.

## Baseline

The intended AI resource is a standard $20/month ChatGPT Plus subscription,
including Codex/Astra where available. The project should use the capabilities
available in that subscription rather than quietly adding enterprise access,
specialist AI platforms, large API spending, paid cloud compute, or paid
engineering services and then attributing their work to AI.

Free/open-source engineering tools are preferred wherever reasonably practical.
The project should evaluate FreeCAD and other appropriate open analysis,
simulation, CAD, documentation and programming tools before paid substitutes.

## Boundary procedure

When the current toolchain is insufficient, record:

1. the concrete limitation;
2. why the existing consumer/free tool cannot close it credibly;
3. the capability required;
4. an estimated cost and any non-cost implications;
5. whether external human expertise or physical testing is needed; and
6. the decision and approval before introducing a paid tool or service.

Until that decision, mark the task `BOUNDARY ENCOUNTERED` or `UNKNOWN`.
Do not hide the limitation by switching tools without recording the change.

## Current record

No enterprise AI, specialist AI platform, paid cloud compute, paid engineering
software, or external expert review is recorded for the current package. The
current technical package contains scalar calculations and a preliminary
standard-library Python transient thermal-power model, but not full FEA,
orbit-decay, radiation-transport or verified flight-software evidence. The
thermal model exposed failed central cases and sensitivity to unmeasured
interfaces; physical correlation remains downstream. These gaps are engineering
boundaries/open items, not proof that the consumer-AI approach can or cannot
close them.

On 2026-09-15, TMI-001 reclassified that calculation as **HYPOTHETICAL
PARAMETRIC SENSITIVITY — NOT COMPONENT-SPECIFIC**. The consumer toolchain could
write and numerically check a model, but public evidence did not supply the
critical installed thermal properties needed to interpret its numbers as
hardware behavior. This is an experimental boundary. Missing properties must be
recorded; generic substitutions may not be used to create an apparently complete
component prediction.

## Attribution rule

AI-assisted work may produce proposals, code, calculations and documents.
Manufacturer data, open-source software, physical tests, supplier work and
professional review must be attributed to their actual source. Reality remains
the final verification mechanism.

## Public-information phase and downstream dependencies

The present phase uses public standards, manuals, datasheets, research and
free/open tools. Direct requests for non-public information from vendors,
integrators, launch providers or regulators are deferred until the design is
approaching an irreversible or expensive commitment. A deferred dependency is
recorded as `KNOWN DOWNSTREAM DEPENDENCY`; it is not treated as a reason to stop
public-information work that remains technically meaningful.

For each dependency, the project records the missing evidence, current-phase
work, trigger for external engagement and the eventual closure evidence. If no
credible public-information work remains, the separate boundary procedure above
applies. This distinction prevents both premature outreach and false claims that
public material supplies flight-release evidence.
