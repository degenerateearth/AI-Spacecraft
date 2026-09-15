# DEGENERATE-1 — Project Overview

Version 0.1 · Living document · 14 September 2026

## What this project is

DEGENERATE-1 is an experiment in how far a non-engineer can get in spacecraft engineering and development using AI as their primary tool.

The project follows a real spacecraft-development effort and documents what AI helps accomplish, what it gets wrong, what the human operator learns, and where independent expertise or physical testing becomes necessary. Its value comes from a credible, inspectable record of progress, including any limits that prevent it from reaching orbit.

AI is the main interface for research, calculations, design exploration, software and documentation. It is not an engineering authority. A convincing answer or a polished document is a proposal to examine, not proof that a spacecraft will work.

## The spacecraft mission

The practical objective is to build a small spacecraft that captures a recognizable photograph of Earth, stores it onboard, transmits it to a privately constructed ground station, and allows that station to reconstruct the image. Basic telemetry should show whether the spacecraft is healthy.

The memorable finish line is a physical printer at the ground station producing the photograph received from orbit: the constitution's **Cornfield Criterion**.

High-resolution mapping, selected-location targeting and real-time video are unnecessary for this objective. The owner has selected occasional recognizable Earth images.

## What the experiment should measure

Progress should be measured by evidence and demonstrated capability. For each meaningful milestone, record:

- What the non-engineer asked AI to help accomplish.
- What AI proposed, including its assumptions and sources.
- What calculations, source checks, independent review or tests supported or contradicted the proposal.
- What changed, why it changed, and who identified the problem.
- How much human effort, specialist assistance, money and time were required, when known.
- What the human operator can now explain or demonstrate.

These records should make it possible to distinguish AI-assisted progress from work completed by suppliers, professional engineers or test facilities. Both are useful contributions; their roles should remain visible.

This is a documented case study. One project's outcome will not establish that AI can replace aerospace engineers generally.

## What counts as success

The constitution defines separate stages: concept, supported engineering model, expert review, ground prototype, verified flight-candidate hardware, licensed launch readiness, orbital operation, image return and finally the printed photograph.

Reaching one stage does not establish the next. A useful result could also be a well-documented stopping point: for example, discovering that a required interface cannot be verified, a design lacks sufficient margin, or the cost of qualification makes the mission impractical.

Meaningful failures belong in the record. Preserve the original proposal, the problem discovered, the correction and the lesson. Correct the current design without rewriting the history of how it arrived there.

## Current starting point

The existing **Degen-1 Revision A** package is a preliminary 1U CubeSat design for opportunistic Earth imaging. It includes component candidates, calculation files, estimated costs, requirements and open issues.

It provides a concept and partial evidence toward the constitution's engineering-model stage. It does not establish a fully consistent, verified engineering model or any higher success level. No independent expert review, hardware purchase, prototype, environmental qualification, licensing approval or orbital operation has been demonstrated in the project record so far.

The initial technical baseline targets US operation in approximately 450–500 km LEO and twelve months of operation. The constitution allows a different form factor when a documented trade supports it. It also defines the minimum image-return objective separately from the original twelve-month target. This overview does not silently remove that target or change the current hardware architecture; any such change should be an explicit, traceable design decision.

## How the project should develop

Prefer designs that can be understood, sourced, checked, built and tested. Use commercially available hardware where it reduces total effort and risk. Keep assumptions and missing information visible, propagate design changes through all affected budgets, and obtain appropriate specialist review before treating work as independently validated.

Explain important decisions in language the operator can understand: the decision, its purpose, the evidence, the assumptions and how it could be verified. Developing the operator's understanding is part of the experiment.

The intended public record should show both the spacecraft's development and AI's actual contribution. GitHub is the intended canonical technical record; a future website should explain the project and link to that record. No repository or publication is created by this document. Files currently remain in `D:\Degen-1`.

## Project documents

- [Project Constitution v0.1](Project_Constitution.md) — the owner's full statement of purpose and working principles, preserved as supplied.
- [Technical package README](README.md) — entry point to the existing design documents and calculations.
- [Revision A audit book](Degen-1_Audit_Book.html) — the earlier technical snapshot; it predates this overview and constitution.
- [Open issues](review/Open_Issues.md) — unresolved technical and regulatory evidence.

**North star:** a spacecraft we built photographs Earth, sends the image home, and our ground station prints it—while leaving an honest record of how far AI helped us get.
## Consumer-AI boundary

The accessibility baseline is a standard $20/month ChatGPT Plus subscription, including Codex/Astra where available, plus free and open-source engineering software wherever reasonably practical. Enterprise AI, specialist AI platforms, large API expenditures, paid cloud compute and paid engineering services are not silently added. If the consumer/free toolchain reaches a credible boundary, record the limitation, required capability and estimated cost and ask before introducing a paid tool or service.

Keep AI/tooling costs separate from spacecraft hardware, ground station, testing, licensing, launch/integration, and external human expert review. Physical testing is not AI expenditure, and professional review must be attributed to human expertise.

## Current public-information phase

The current phase deliberately uses public standards, manuals, datasheets,
research and free/open tools to mature the design as far as they credibly allow.
External requests for private or mission-specific information are deferred until
they are needed for an irreversible or expensive commitment. Those needs are
tracked as **KNOWN DOWNSTREAM DEPENDENCIES**, together with the useful analysis,
CAD, simulation and prototype work that can continue now.

This sequencing does not convert provisional public information into an
approved interface. The public EXOpod Nova manual remains the provisional
mechanical reference. A current mission ICD, as-procured component data,
regulatory determinations, physical test evidence and professional review will
still be required at their applicable release gates.
