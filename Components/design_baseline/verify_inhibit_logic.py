#!/usr/bin/env python3
"""Verify the D1-FAB-001 Boolean inhibit architecture.

This proves only the stated logical series topology. It does not model MOSFET
leakage, parasitic power, wiring faults, timing, environment, or hardware.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path


DEVICES = (
    "QSERV_A",
    "QSERV_B",
    "QRBF_A",
    "QRBF_B",
    "QINH_1",
    "QINH_2",
    "QINH_3",
)


def path_on(commands: dict[str, bool], stuck_on: str | None = None) -> bool:
    states = {name: commands[name] or name == stuck_on for name in DEVICES}
    return all(states.values())


def commands(
    service_plug_inserted: bool,
    rbf_plug_inserted: bool,
    deployer_switches_actuated: tuple[bool, bool, bool],
) -> dict[str, bool]:
    # True commands a MOSFET on. Inserted RBF plugs open the jack's normally
    # closed switch contacts. Actuated SDS002RULC switches are also open.
    return {
        "QSERV_A": not service_plug_inserted,
        "QSERV_B": not service_plug_inserted,
        "QRBF_A": not rbf_plug_inserted,
        "QRBF_B": not rbf_plug_inserted,
        "QINH_1": not deployer_switches_actuated[0],
        "QINH_2": not deployer_switches_actuated[1],
        "QINH_3": not deployer_switches_actuated[2],
    }


checks: list[dict[str, object]] = []
errors: list[str] = []

# All eight physical deployer-switch combinations: the protected bus may turn
# on only when all switches are released and both RBF plugs are removed.
for sw in itertools.product((False, True), repeat=3):
    cmd = commands(False, False, sw)
    actual = path_on(cmd)
    expected = not any(sw)
    checks.append({"case": "switch_truth_table", "actuated": sw, "bus_on": actual})
    if actual != expected:
        errors.append(f"switch truth-table failure: {sw}")

# An inserted load RBF or battery-service plug must command the path off for
# every switch combination.
for service_inserted, rbf_inserted in ((True, False), (False, True), (True, True)):
    for sw in itertools.product((False, True), repeat=3):
        actual = path_on(commands(service_inserted, rbf_inserted, sw))
        checks.append(
            {
                "case": "plug_override",
                "service_inserted": service_inserted,
                "rbf_inserted": rbf_inserted,
                "actuated": sw,
                "bus_on": actual,
            }
        )
        if actual:
            errors.append(
                f"plug override failure: service={service_inserted}, "
                f"rbf={rbf_inserted}, switches={sw}"
            )

# Launch state: both plugs removed before flight and all three deployer switches
# actuated. No one device stuck on may energize the protected bus.
launch = commands(False, False, (True, True, True))
for device in DEVICES:
    actual = path_on(launch, stuck_on=device)
    checks.append({"case": "single_stuck_on_launch", "device": device, "bus_on": actual})
    if actual:
        errors.append(f"single stuck-on launch failure: {device}")

# Ground-safe states: either two-channel plug must remain effective after one
# of its two commanded-off MOSFET stages is stuck on.
for case_name, cmd, protected_devices in (
    ("load_rbf", commands(False, True, (False, False, False)), ("QRBF_A", "QRBF_B")),
    ("service_rbf", commands(True, False, (False, False, False)), ("QSERV_A", "QSERV_B")),
):
    for device in protected_devices:
        actual = path_on(cmd, stuck_on=device)
        checks.append({"case": f"single_stuck_on_{case_name}", "device": device, "bus_on": actual})
        if actual:
            errors.append(f"single stuck-on {case_name} failure: {device}")

result = {
    "document": "D1-FAB-LOGIC-VERIFY-001",
    "evidence": "CALCULATED Boolean topology only; not circuit simulation or test evidence",
    "device_count": len(DEVICES),
    "check_count": len(checks),
    "errors": errors,
    "result": "PASS" if not errors else "FAIL",
    "checks": checks,
    "limitations": [
        "Assumes seven series devices and independent gate-control traces are implemented as specified",
        "Does not model leakage, body-diode direction, parasitic power, contact bounce, wiring shorts, timing, radiation, thermal behavior, or common-cause failures",
        "Does not establish compliance with a mission-specific launch-provider ICD",
    ],
}

output_path = Path(__file__).with_name("D1-FAB-001_logic_verification.json")
output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
