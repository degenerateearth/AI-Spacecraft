# DEGENERATE-1 Milestones

This register defines when the GitHub repository should receive a milestone
update. A milestone closes only when its listed evidence exists in the
repository. Documentation quality alone does not advance physical credibility.

| ID | Milestone | Exit evidence | Status |
|---|---|---|---|
| M0 | Project foundation | Constitution, preliminary audit package, cost/status tracking, conversation log, and GitHub baseline | Complete |
| M1 | Mission and requirements baseline | Mission success criteria, traceable requirements, orbit assumption, imaging concept, and open-issue review | In progress |
| M1A | Public launch/deployer planning gate | Three-path trade, provisional mechanical reference, source archive, CAD screen, conflicts and explicit contract/ICD gaps | Complete — planning evidence only |
| M1B | Public-information readiness reassessment | Phase rule, known downstream dependency register, matrix classification and next-step decision | Complete — governance/planning evidence only |
| M2 | COTS architecture selection | Supplier-verifiable BOM, interface closure, mass/power/data/link budgets with margin, and procurement decision record | In progress — strict evidence gate defined; 0 components admitted; 105 property rows audited across 8 recommended candidates and 2 alternatives |
| M3 | Analysis baseline | Reproducible structural, thermal, power, communications, orbit/debris, and radiation analyses with limitations recorded | In progress — hypothetical thermal sensitivity code exists; component-specific thermal analysis not started |
| M4 | Engineering model | As-built configuration, firmware/software revision, bench procedures, and functional test results | Proposed |
| M5 | Environmental verification | Launch-provider-compatible vibration, thermal-vacuum, deployment, battery, and end-to-end communications evidence | Proposed |
| M6 | Regulatory and launch readiness | Licensing/coordination records, debris assessment, launch-provider acceptance, and closed critical hazards | Proposed |
| M7 | Mission result | Recognizable Earth image captured in orbit, downlinked, reconstructed, and printed with the evidence archived | Proposed |

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
