# DEGENERATE-1 Milestones

This register defines when the GitHub repository should receive a milestone
update. A milestone closes only when its listed evidence exists in the
repository. Documentation quality alone does not advance physical credibility.

| ID | Milestone | Exit evidence | Status |
|---|---|---|---|
| M0 | Project foundation | Constitution, preliminary audit package, cost/status tracking, conversation log, and GitHub baseline | Complete |
| G1 | **First engineering gate — Phase 1 component evidence closure** | Exact documented component or released custom design for every F01–F16 function; all mission-relevant properties and interfaces closed under D1-CMP-STD-001 | **In progress — 29-line operating set proposed; 0 COTS components and 0 custom components admitted** |
| M1 | Mission and requirements baseline | Mission success criteria, traceable requirements, orbit assumption, imaging concept, and open-issue review | Preliminary work preserved; further advancement waits on G1 |
| M1A | Public launch/deployer planning gate | Three-path trade, provisional mechanical reference, source archive, CAD screen, conflicts and explicit contract/ICD gaps | Complete — planning evidence only |
| M1B | Public-information readiness reassessment | Phase rule, known downstream dependency register, matrix classification and next-step decision | Complete — governance/planning evidence only |
| M2 | COTS architecture selection | Supplier-verifiable BOM, interface closure, mass/power/data/link budgets with margin, and procurement decision record | Executed through G1; 0 components admitted; 105 property rows audited across 8 recommended candidates and 2 alternatives |
| M3 | Analysis baseline | Reproducible structural, thermal, power, communications, orbit/debris, and radiation analyses with limitations recorded | Paused as controlling work pending G1; hypothetical sensitivity code remains preserved |
| M4 | Engineering model | As-built configuration, firmware/software revision, bench procedures, and functional test results | Proposed |
| M5 | Environmental verification | Launch-provider-compatible vibration, thermal-vacuum, deployment, battery, and end-to-end communications evidence | Proposed |
| M6 | Regulatory and launch readiness | Licensing/coordination records, debris assessment, launch-provider acceptance, and closed critical hazards | Proposed |
| M7 | Mission result | Recognizable Earth image captured in orbit, downlinked, reconstructed, and printed with the evidence archived | Proposed |

G1 is the first engineering gate even though preliminary M1–M3 work already
exists. That earlier work remains evidence and history, but it does not authorize
continued fidelity or milestone advancement. Component evidence closure now
controls the work sequence.

## Update rule

At each milestone:

1. Update `review/Project_Status.yaml`, the cost ledger, requirements, risks,
   open issues, and configuration log.
2. Add test, analysis, expert-review, or regulatory evidence without overstating
   its maturity.
3. Commit the milestone as a coherent review point and create an annotated Git
   tag using `milestone-MN-short-name`.
4. Push the commit and tag to GitHub.
5. Preserve failures, corrections, abandoned approaches, and toolchain
   boundaries when they affected the result.

The baseline tag is `milestone-M0-project-foundation`.
