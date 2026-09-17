#!/usr/bin/env python3
"""Check D1-HAR-001 schedule coverage and calculated allocated wire quantities."""

from __future__ import annotations

import csv
import json
from pathlib import Path

here = Path(__file__).resolve().parent
rows = list(csv.DictReader((here / "harness_schedule.csv").open(encoding="utf-8", newline="")))
errors: list[str] = []

required_ids = {
    "HAR-FLT-001",
    "HAR-FLT-002", "HAR-FLT-003", "HAR-FLT-004", "HAR-FLT-005", "HAR-FLT-006",
    "HAR-FLT-007", "HAR-FLT-008", "HAR-FLT-009",
    "HAR-FLT-010", "HAR-FLT-011", "HAR-GSE-001",
}
ids = [row["harness_id"] for row in rows]
if set(ids) != required_ids:
    errors.append(f"schedule IDs differ: missing={sorted(required_ids-set(ids))}; extra={sorted(set(ids)-required_ids)}")
if len(ids) != len(set(ids)):
    errors.append("duplicate harness IDs")

for row in rows:
    for field in ("endpoint_a", "endpoint_b", "connector_a", "connector_b", "wire_or_cable", "status"):
        if not row[field].strip():
            errors.append(f"{row['harness_id']} blank {field}")
    if int(row["quantity"]) != 1:
        errors.append(f"{row['harness_id']} unexpected quantity")
    if int(row["circuits"]) < 1 or int(row["cut_length_allocation_mm"]) < 1:
        errors.append(f"{row['harness_id']} invalid circuits/length")

# Counts come directly from the controlled per-harness definitions.
flight_24_mm = 4 * 150 + 5 * 2 * 180
flight_26_mm = 2 * 150 + 3 * 2 * 180 + 5 * 2 * 180 + 5 * 120
service_26_mm = 10 * 1000

result = {
    "document": "D1-HAR-VERIFY-001",
    "evidence": "CALCULATED schedule consistency; not fabrication or test evidence",
    "schedule_rows": len(rows),
    "flight_harnesses": sum(row["harness_id"].startswith("HAR-FLT") for row in rows),
    "ground_harnesses": sum(row["harness_id"].startswith("HAR-GSE") for row in rows),
    "allocated_flight_24awg_m": flight_24_mm / 1000,
    "allocated_flight_26awg_m": flight_26_mm / 1000,
    "allocated_ground_26awg_m": service_26_mm / 1000,
    "errors": errors,
    "result": "PASS" if not errors else "FAIL",
    "limitations": [
        "Allocated lengths are project assumptions until CAD routing and released harness drawings replace them",
        "Camera contact finish and solar-panel RTD lead transition/attachment remain open",
        "No voltage-drop, thermal, RF-loss, workmanship, vibration, or thermal-vacuum result is established",
    ],
}
(here / "D1-HAR-001_schedule_verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
