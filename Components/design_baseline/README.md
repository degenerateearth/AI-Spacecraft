# Degen-1 detailed-design selection register

Revision A · 2026-09-16

This directory records exact parts and custom assemblies selected after
D1-TRD-ARCH-001. A selection here is an input to detailed design. It becomes
`SUPPORTED` under D1-CMP-STD-001 only when every property actually used by the
released design is backed by primary evidence.

Current states:

| State | Meaning |
|---|---|
| SELECTED FOR DETAILED DESIGN | Exact part/topology chosen; further interface, circuit or analysis closure is required |
| SUPPORTED | Exact selection and all controlling mission properties are evidenced for the stated use |
| CUSTOM/TO BE VERIFIED | Degen-1 design has a defined identity and verification path; release artifacts are incomplete |
| REJECTED | Evaluated and unsuitable for the baseline, with reason retained |

| ID | Item | State | Record |
|---|---|---|---|
| D1-BAT-001 | 3S2P Panasonic BK120AAHU battery assembly | SELECTED FOR DETAILED DESIGN | [Battery record](D1-BAT-001.md) |
| D1-OBC-001 | BIRDS-derived PIC/serial-flash OBC | CUSTOM/TO BE VERIFIED | [OBC record](D1-OBC-001.md) |
| D1-EPS-001 | Power, charging, rails and launch inhibits | CUSTOM/TO BE VERIFIED | [EPS record](D1-EPS-001.md) |
| D1-BPB-001 | Backplane and fixed electrical interfaces | CUSTOM/TO BE VERIFIED | [Backplane record](D1-BPB-001.md) |
| D1-CAM-001 | SkyFox Labs piCAM/FM camera and custom carrier | SELECTED FOR DETAILED DESIGN | [Camera record](D1-CAM-001.md) |
| D1-COM-001 | Ebyte E22-400M22S UHF radio and custom carrier | CUSTOM/TO BE VERIFIED | [Radio record](D1-COM-001.md) |
| D1-SOL-001 | Five custom panels with ten AZUR SPACE 81442 SCAs | CUSTOM/TO BE VERIFIED | [Solar-panel record](D1-SOL-001.md) |
| D1-ADCS-001 | K&J D84 magnet, two custom HyMu 80 rods and retainers | CUSTOM/TO BE VERIFIED | [Passive ADCS record](D1-ADCS-001.md) |
| D1-ANT-001 | Custom 436.5 MHz canted-turnstile and four-channel release assembly | CUSTOM/TO BE VERIFIED | [Antenna/deployment record](D1-ANT-001.md) |
| D1-STR-001 | BIRDS-4-derived custom 1U rail frame | CUSTOM/TO BE VERIFIED | [Structure record](D1-STR-001.md) |

This register will replace the earlier mixed-vendor component proposal only
after all required functions have equivalent detailed records and the generated
Phase 1 register is revised. Until then, the earlier register remains the formal
list of open evidence exceptions and G1 remains open.
