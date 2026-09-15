#!/usr/bin/env python3
"""Generate the public-information launch and deployer trade table."""

from __future__ import annotations

import csv
from pathlib import Path


OUT = Path(__file__).with_name("Launch_Deployer_Trade.csv")
FIELDS = [
    "candidate_id", "service_path", "one_u_support", "public_orbit_evidence",
    "public_interface_evidence", "published_price", "quote_route",
    "mechanical_screen", "mission_screen", "safety_and_test_screen",
    "current_disposition", "evidence_level", "critical_unknowns",
]

ROWS = [
    {
        "candidate_id": "LD-01",
        "service_path": "EXOLAUNCH mission management with standard 1U EXOpod Nova slot; host mission TBD",
        "one_u_support": "YES — EXOpod Nova User Manual Rev. 1.2 Table 1",
        "public_orbit_evidence": "Mission-specific; EXOLAUNCH has integrated on multiple launch vehicles; no 450–500 km slot identified publicly",
        "public_interface_evidence": "S33 — June 2024 public manual gives dimensions, mass, COG, rails, deployment and fit checks",
        "published_price": "NOT PUBLISHED for 1U service",
        "quote_route": "Official Fly with EXOpod/contact route; no inquiry sent",
        "mechanical_screen": "PROVISIONAL PASS for nominal envelope and mass; tolerances, rail geometry, COG and physical fit open",
        "mission_screen": "BLOCKED pending exact orbit, epoch, dispersions and lifetime analysis",
        "safety_and_test_screen": "BLOCKED pending mission ICD, integration guide, battery/RF/inhibit rules and test levels",
        "current_disposition": "SELECTED PROVISIONAL MECHANICAL REFERENCE",
        "evidence_level": "DOCUMENTED; CALCULATED; MODELED",
        "critical_unknowns": "Price; slot; launch vehicle; orbit; schedule; customer ICD; acceptance data; regulatory scope",
    },
    {
        "candidate_id": "LD-02",
        "service_path": "ISISPACE/ISILaunch with 1U ISIPOD or subdivided QuadPack; host mission TBD",
        "one_u_support": "YES — current launch-equipment page and deployer brochure",
        "public_orbit_evidence": "Regular rideshares across several vehicles; mission-specific orbit; no 450–500 km slot identified publicly",
        "public_interface_evidence": "S36/S37 — service page plus brochure; no current controlled customer ICD located",
        "published_price": "NOT PUBLISHED; quote after mission details",
        "quote_route": "Official Book your launch/contact route; no inquiry sent",
        "mechanical_screen": "PROVISIONAL PASS for 1.2762 kg growth mass versus brochure 1.75 kg 1U limit; full geometry open",
        "mission_screen": "BLOCKED pending exact orbit, epoch, dispersions and lifetime analysis",
        "safety_and_test_screen": "BLOCKED pending customer ICD, acceptance plan, battery/RF/inhibit rules and test levels",
        "current_disposition": "COMMERCIAL ALTERNATE",
        "evidence_level": "DOCUMENTED; CALCULATED",
        "critical_unknowns": "Current 1U ICD; price; slot; orbit; schedule; included services; acceptance data",
    },
    {
        "candidate_id": "LD-03",
        "service_path": "Voyager/Nanoracks NRCSD deployment from ISS",
        "one_u_support": "YES — NRCSD IDD and NASA SmallSat State of the Art",
        "public_orbit_evidence": "Approximately 400–420 km, 51.6 degrees, typically 1–3 months after berthing per S40",
        "public_interface_evidence": "S38 — NR-NRCSD-S0003 Rev. - provides dimensional, inhibit, battery, safety and test requirements",
        "published_price": "NOT PUBLISHED",
        "quote_route": "Current service availability and commercial route require confirmation; no inquiry sent",
        "mechanical_screen": "PROVISIONAL PASS for nominal rail length and mass; switch/RBF access and full dimensional compliance open",
        "mission_screen": "HIGH RISK/BLOCKED — published altitude is below preferred range and 365.25-day residence is not demonstrated",
        "safety_and_test_screen": "Crewed ISS path adds detailed battery, materials, hazard and acceptance reviews",
        "current_disposition": "LOWER-ORBIT FALLBACK; NOT REFERENCE",
        "evidence_level": "DOCUMENTED; CALCULATED",
        "critical_unknowns": "Current commercial availability; price; deployment date; lifetime; ICA; battery acceptance scope",
    },
]


assert len(ROWS) == 3
assert [r["candidate_id"] for r in ROWS] == ["LD-01", "LD-02", "LD-03"]
assert all(set(r) == set(FIELDS) for r in ROWS)

with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDS)
    writer.writeheader()
    writer.writerows(ROWS)

print(f"Wrote {len(ROWS)} candidates to {OUT}")
