# Open-source upstream register

Revision A · 2026-09-16  
Purpose: preserve the exact public revisions inspected during D1-TRD-ARCH-001.
Upstream source is not copied into this repository by this register.

| Project | Upstream revision inspected | Use in Degen-1 | License/evidence note |
|---|---|---|---|
| BIRDS General Documentation | `76cf923be9dc7e923e7397b5426c5b1e3d3f41c6` | Platform ICD and textbook | Official BIRDSOpenSource repository; public educational record |
| BIRDS-4 OBC | `490f74487d65ebfb0037bbdd9f3e7aab6aefc3a5` | OBC schematic, BOM and firmware reference | Official BIRDSOpenSource repository |
| BIRDS-5 parts list | `c5ab9884684190afe6abd231336a7d1674d9b1cf` | Later 1U/2U parts and mission reference | Official BIRDSOpenSource repository |
| PyCubed hardware | `d1adfd0c207dd5951ab175af53b3b7c1c72a5212` | Integrated-board implementation comparison | Official PyCubed repository; inspect repository license before reuse |
| OreSat C3 hardware | `4d1c366bc0e01940caa8e8377f3c605080e73074` | OBC/radio/fabrication reference | CERN-OHL-S-2.0; v6 is not the flown v5 |
| OreSat batteries | `c0f0cba9235978170217d468419ccbf441f74e52` | Battery safety/topology reference | Current commit says schematic complete and layout in progress |
| OreSat solar hardware | `af8f6f3def958309f3864055bd1944e20f51357d` | Solar-panel and MPPT reference | CERN-OHL-S-2.0; GaAs design described as flown |
| OreSat backplane | `6af10722e5b004508c614fc10ffa8e688bffbbb3` | Backplane/RF-routing reference | CERN-OHL-S-2.0; includes 1U v2 design history |
| VST104-Sierra | `766662d9bf6e61cfed37e8672254448ef8bdc7b0` | Low-power OBC fallback/reference | Repository license must accompany any reused source |
| OpenLST firmware/tools | `b996935a516967936859634887fdf7b4d48dcc7c` | UHF protocol, firmware and ground-tool reference | GPLv3; 2018 public release |
| OpenLST hardware | `c977b8c4f6b4cf8d0b82d946cea9dd22c405342f` | UHF schematic/layout/BOM reference | CC BY-SA 4.0; rev 2.1 Gerbers present; RFFM6403 discontinued |

## Rules for reuse

1. Pin an upstream revision before incorporating files.
2. Preserve the upstream license, copyright and source-location notices.
3. Record each local modification in a Degen-1 change log.
4. Do not claim the upstream project's flight heritage for a changed Degen-1 board.
5. Recheck each exact manufacturer part number for lifecycle and documentation
   before admitting it to the Degen-1 baseline.
