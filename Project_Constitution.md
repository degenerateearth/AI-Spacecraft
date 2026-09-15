# DEGENERATE-1 — PROJECT CONSTITUTION
Version 0.2
Status: Living document

## 1. THE QUESTION

This project exists to investigate:

> “How far can a non-aerospace engineer get toward a physically credible
> spacecraft in 2026 using AI as the engineering interface?”

DEGENERATE-1 is both a spacecraft-development project and an experiment
in AI-assisted engineering.

The project is NOT an exercise in generating impressive-looking aerospace
documents.

Every artifact should move the project toward something that could
eventually be built, tested, reviewed by qualified people, and—if feasible—
legally launched and operated.

---

## 2. MISSION

Design and, if practical, eventually build a very small spacecraft capable
of:

1. Operating in low Earth orbit.
2. Capturing at least one recognizable photograph of Earth.
3. Storing that image onboard.
4. Downlinking the image to Earth.
5. Allowing a privately constructed ground station to receive and
reconstruct the image.
6. Providing sufficient telemetry to determine basic spacecraft health.

The emotional finish line is intentionally simple:

> A spacecraft we built takes a picture of Earth, sends it down, and our
> ground station prints the picture.

Everything else supports that objective.

---

## 3. SUCCESS LEVELS

The project must distinguish between levels of success.

### Level 0 — Concept
A coherent mission architecture exists.

### Level 1 — Engineering Model
The design is internally consistent and supported by calculations,
datasheets, simulations, budgets, and documented assumptions.

### Level 2 — Expert Review
Relevant portions have been reviewed by people with appropriate
engineering or regulatory expertise.

### Level 3 — Hardware Prototype
Representative hardware demonstrates major spacecraft functions on Earth.

### Level 4 — Flight-Candidate Hardware
Integrated hardware exists and has undergone an appropriate verification
and environmental-test program.

### Level 5 — Licensed / Launch-Ready
Required regulatory, spectrum, launch-provider, safety, and integration
requirements have been satisfied.

### Level 6 — Orbital Operation
DEGENERATE-1 operates in orbit.

### Level 7 — Mission Success
A recognizable image of Earth is successfully received by the ground
station and reconstructed.

### Level 8 — Cornfield Criterion
The received image causes a physical printer at the ground station to
produce a paper photograph.

Level 8 is the canonical ridiculous finish line.

Do not describe a lower level as though a higher level has been achieved.

---

## 4. DESIGN PHILOSOPHY

Optimize for:

- Simplicity
- Reliability
- Testability
- Documented reasoning
- Commercially available components where appropriate
- Low total mission cost
- Conservative engineering margins
- Open documentation
- Reproducibility
- Legal and responsible operation

Do NOT optimize for:

- Novelty for its own sake
- Maximum performance
- Unnecessary autonomy
- Impressive specifications
- Feature count
- Aerospace aesthetics
- Artificial complexity
- Making AI-generated work appear more mature than it is

A boring design that works is superior to an impressive design that
cannot be defended.

---

## 5. FORM FACTOR

No spacecraft form factor is sacred.

1U CubeSat may be used as the initial baseline.

However, PocketQube, CubeSat, or another standardized architecture may be
selected if a documented trade study demonstrates that it better serves
the mission.

Do not choose the smallest spacecraft simply because it is interesting.

Evaluate at minimum:

- spacecraft cost
- launch/integration implications
- available volume
- mass
- power generation/storage
- communications performance
- antenna constraints
- camera requirements
- attitude requirements
- thermal behavior
- component availability
- testing difficulty
- regulatory implications
- engineering margin

---

## 6. AI'S ROLE

AI is an engineering interface, research assistant, analyst, documentation
system, and design collaborator.

AI is NOT an engineering authority.

AI-generated statements do not become facts merely because they appear
plausible.

For important engineering claims, distinguish between:

- ASSUMPTION
- CALCULATED
- SIMULATED
- DATASHEET-SUPPORTED
- SOURCE-VERIFIED
- EXPERIMENTALLY TESTED
- EXPERT-REVIEWED
- FLIGHT-PROVEN

Never silently upgrade evidence from one category to another.

---

## 7. PHYSICAL CREDIBILITY RULE

Every major subsystem must eventually answer:

> “Why should we believe this will actually work?”

Examples include:

- Electrical Power System
- Command and Data Handling
- Communications
- Antenna system
- Camera/payload
- Attitude determination/control
- Thermal design
- Structure
- Flight software
- Ground station

Answers should ultimately rely on calculations, manufacturer data,
simulation, physical testing, relevant standards, prior flight heritage,
or qualified review—not AI confidence.

---

## 8. ENGINEERING BUDGETS

Maintain explicit, version-controlled budgets where applicable.

At minimum:

- Mass budget
- Power budget
- Energy/orbit budget
- Data budget
- Communications/link budget
- Storage budget
- Thermal assumptions
- Cost budget

Include margins.

When one design change affects another budget, propagate the change.

Do not allow mutually inconsistent numbers to survive in separate
documents.

---

## 9. REQUIREMENTS TRACEABILITY

Every major design decision should trace back to:

MISSION
→ REQUIREMENT
→ DESIGN DECISION
→ ANALYSIS
→ VERIFICATION METHOD

If a feature cannot be traced to a mission requirement or meaningful risk
reduction, question whether it belongs.

---

## 10. UNCERTAINTY

Unknowns are acceptable.

Hidden unknowns are not.

Maintain an explicit list of:

- Open questions
- Unverified assumptions
- Missing data
- Engineering risks
- Regulatory questions
- Components requiring characterization
- Areas requiring professional review

Writing "UNKNOWN" is preferable to inventing a plausible answer.

---

## 11. FAILURE IS DATA

Do not rewrite project history to make the AI appear successful.

Preserve meaningful failures.

When appropriate, document:

AI PROPOSED:
[original idea]

PROBLEM:
[what analysis, research, expert review, or testing discovered]

CORRECTION:
[what changed]

LESSON:
[what this demonstrates about AI-assisted engineering]

These failures are part of the experiment.

---

## 12. HUMAN KNOWLEDGE CONSTRAINT

The primary human operator is NOT assumed to be an aerospace engineer.

Do not hide important reasoning behind unexplained specialist terminology.

When presenting an engineering decision:

1. State the decision.
2. Explain why it matters.
3. Show the underlying evidence/calculation.
4. Identify assumptions.
5. Explain how it could be verified.
6. Identify where specialist review is warranted.

The goal is not merely for AI to design DEGENERATE-1.

The human operator must progressively understand DEGENERATE-1.

---

## 13. SAFETY AND REGULATORY CONSTRAINT

DEGENERATE-1 must be designed for lawful, responsible operation.

Do not design intentional interference with other spectrum users,
circumvention of launch/spectrum rules, hazardous uncontrolled behavior,
or avoidance of regulatory oversight.

Treat regulatory requirements as engineering requirements.

Where relevant, identify the responsible authority, applicable standard,
license, coordination process, or launch-provider requirement.

Do not claim compliance until compliance has actually been established.

---

## 14. PUBLIC DOCUMENTATION

The public website should answer two questions simultaneously:

### What is DEGENERATE-1?

and

### How far has AI actually gotten?

Clearly distinguish:

- Proposed
- Designed
- Analyzed
- Simulated
- Purchased
- Built
- Tested
- Independently reviewed
- Approved
- Flown

Do not present renders as hardware.

Do not present simulations as tests.

Do not present AI conclusions as independent validation.

---

## 15. OPEN PROJECT

Where legally and practically appropriate, publish:

- Requirements
- Architecture
- Design documentation
- CAD
- Schematics
- Software
- Ground-station software
- BOMs
- Analysis
- Test results
- Design revisions
- Failure reports

GitHub should act as the canonical technical record.

The website should present the project clearly and link to canonical
artifacts rather than becoming a second inconsistent source of truth.

---

## 16. SCOPE CONTROL

Before adding a major feature, ask:

> “Does this materially increase the probability that DEGENERATE-1
> successfully photographs Earth and returns that image?”

If NO:

Do not add it unless it significantly improves safety, compliance,
testability, educational value, or the AI-engineering experiment.

DEGENERATE-1 does not need to be an impressive satellite.

It needs to accomplish one stupidly simple mission extremely well.

---

## 17. ANTI-SCOPE-CREEP EXAMPLES

Unless subsequently justified by mission analysis, DEGENERATE-1 does NOT
need:

- Propulsion
- Inter-satellite communications
- AI onboard the spacecraft
- High-resolution Earth observation
- Continuous imagery
- Real-time video
- Exotic materials
- Experimental radios
- Custom silicon
- Complex deployables
- Autonomous mission planning
- Multiple scientific payloads

These features may be interesting.

Interesting is not sufficient justification.

---

## 18. DECISION PRIORITY

When competing designs appear similarly viable, prefer in this order:

1. Safety and legality
2. Mission probability of success
3. Engineering margin
4. Testability
5. Simplicity
6. Availability of credible documentation/data
7. Cost
8. Mass/volume optimization
9. Performance
10. Novelty

---

## 19. CODEX INSTRUCTION

Before making a significant architectural change, reread this document.

If a requested task conflicts with this document:

1. Identify the conflict.
2. Explain why it conflicts.
3. Propose the smallest reasonable alternative.
4. Do not silently change the project's mission to accommodate the task.

If new evidence demonstrates that this document itself should change,
propose an explicit revision rather than quietly ignoring it.

---

## 20. NORTH STAR

When the project becomes complicated, return to this:

CAMERA
↓
EARTH
↓
SPACECRAFT
↓
RADIO LINK
↓
GROUND STATION
↓
EARTH.JPG
↓
PRINTER

If DEGENERATE-1 accomplishes that chain from orbit, the mission worked.

Everything else is engineering in service of that moment.

---

## 21. CONSUMER-AI AND FREE-SOFTWARE CONSTRAINT

The baseline engineering interface for this experiment is a standard
$20/month ChatGPT Plus subscription, using capabilities available within that
subscription, including Codex/Astra where available. DEGENERATE-1 must not
quietly become dependent on enterprise AI subscriptions, expensive specialist
AI platforms, large API expenditures, paid cloud compute, or professional
engineering services presented as AI capability.

This constraint applies to the AI and software engineering interface. It does
not impose a $20 limit on spacecraft hardware, testing, licensing, launch, or
the rest of the physical mission.

Use free and open-source engineering software wherever reasonably practical,
including FreeCAD and appropriate open analysis and simulation tools. Record
the actual tool and version used for important work. If the consumer-AI/free-
software toolchain cannot credibly proceed, do not silently work around that
boundary. Identify the limitation, explain why the existing toolchain is
insufficient, identify the needed capability, estimate its cost where
possible, and ask before introducing a paid tool or service.

“Consumer AI got us this far, and then we hit this wall” is a valid result.
The project must not optimize its methods or reporting to prove that AI can
design a spacecraft.

## 22. COST ACCOUNTING AND EVIDENCE BOUNDARIES

Maintain separate ledgers for:

1. AI expenditure
2. Software/tool expenditure
3. Spacecraft hardware expenditure
4. Ground-station expenditure
5. Testing/verification expenditure
6. Regulatory/licensing expenditure
7. Launch/integration expenditure
8. External professional/expert-review expenditure

AI subscriptions and software tools are not physical-project costs. Physical
testing is not an AI expense. Professional review is external human expertise
and must never be attributed to AI. Record zero or unknown amounts explicitly
with their basis.

## 23. TRANSPARENT STATUS

Public project status must show the current success level; AI/tooling cost to
date; physical-project cost to date; and what is proposed, calculated,
simulated, physically built, tested, independently expert-reviewed, approved,
flown, or still unknown. Polished documents, CAD renders, simulations, and AI
confidence must never imply a higher physical-credibility level than the
evidence supports.

Failures, incorrect AI assumptions, abandoned designs, expert corrections,
simulation failures, and physical-test failures are valuable experimental
results and should be preserved where useful.

## 24. PUBLIC-INFORMATION DEVELOPMENT PHASE

The present phase asks how far the design can be matured using the consumer-AI
baseline, free/open engineering tools, publicly available technical
information, published standards, datasheets, manuals and research. Direct
contact with launch providers, deployer vendors, integrators, regulators,
component vendors or other external organizations for information that is not
publicly available is normally a downstream phase.

Continue closing every item that can be closed credibly with public evidence.
Use the public EXOpod Nova information as a provisional mechanical baseline
where justified. Do not invent mission-specific, controlled or vendor-private
requirements. When final closure requires such information, record it as a
**KNOWN DOWNSTREAM DEPENDENCY**, state what can still be done now, and identify
the event that makes the dependency current.

Known downstream dependencies do not establish flight readiness and do not
permit known public requirements to be ignored. Before flight-component
purchase, final mechanical fabrication, qualification testing or launch
integration, reconcile the design against current mission-specific ICDs,
supplier configuration data, quotes, regulatory determinations and applicable
expert review. Record every resulting correction.

If public information, consumer AI or free/open tools cease to support credible
progress, record that boundary as an experimental result under Section 21.

## 25. Phase 1 component evidence

Every physical component admitted to the Phase 1 spacecraft baseline must be an
identifiable, commercially obtainable part or an explicitly documented custom-
fabricated part. A selected COTS component requires publicly accessible primary
manufacturer documentation whose actual contents establish every property needed
for its DEGENERATE-1 function. A datasheet title alone is insufficient.

Missing mission-relevant data may not be replaced with generic, similar-product
or AI-generated values to pass the gate. Such a part remains **CANDIDATE /
EVIDENCE INCOMPLETE** and cannot enter the Phase 1 baseline. When no sufficiently
documented COTS part exists, record the function as a custom-component need with
its own requirements, design, analysis and verification path.

Preserve the exact source URL, document identity/revision/date, retrieval date,
evidence classification and, when licensing permits local archiving, a hash of
the exact document. Documentation supports only the claims actually present in
it. Physical testing and independent review remain separate evidence.
