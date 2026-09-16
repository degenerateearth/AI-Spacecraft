#!/usr/bin/env python3
"""Verify detailed-baseline register and local source-custody consistency."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-local-archive",
        action="store_true",
        help="fail if copyrighted local-only source files are absent",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    readme = (HERE / "README.md").read_text(encoding="utf-8")
    register_rows = re.findall(
        r"^\| (D1-[A-Z-]+-\d{3}) \|.*?\|.*?\| \[[^]]+\]\(([^)]+)\) \|$",
        readme,
        flags=re.MULTILINE,
    )
    register_ids = [item_id for item_id, _ in register_rows]
    if len(register_ids) != len(set(register_ids)):
        errors.append("duplicate detailed-baseline ID in README")
    for item_id, target in register_rows:
        path = HERE / target
        if not path.is_file():
            errors.append(f"missing record for {item_id}: {target}")
        elif not path.read_text(encoding="utf-8").startswith(f"# {item_id}"):
            errors.append(f"record heading does not match {item_id}: {target}")

    matrix = (HERE / "COMPLETENESS_MATRIX.md").read_text(encoding="utf-8")
    matrix_ids = set(re.findall(r"\| (D1-[A-Z-]+-\d{3}) \|", matrix))
    absent_from_matrix = sorted(set(register_ids) - matrix_ids)
    if absent_from_matrix:
        errors.append("README IDs absent from completeness matrix: " + ", ".join(absent_from_matrix))

    status_text = (ROOT / "review" / "Project_Status.yaml").read_text(encoding="utf-8")
    count_match = re.search(r"^\s*detailed_component_records:\s*(\d+)\s*$", status_text, re.MULTILINE)
    if not count_match:
        errors.append("Project_Status.yaml lacks detailed_component_records")
        status_count = None
    else:
        status_count = int(count_match.group(1))
        if status_count != len(register_rows):
            errors.append(
                f"status count {status_count} does not match README record count {len(register_rows)}"
            )

    source_register = (ROOT / "review" / "Source_Register.md").read_text(encoding="utf-8")
    source_ids = re.findall(r"^\*\*S(\d+)\s+—", source_register, re.MULTILINE)
    duplicate_sources = sorted({value for value in source_ids if source_ids.count(value) > 1})
    if duplicate_sources:
        errors.append("duplicate Source_Register IDs: " + ", ".join(duplicate_sources))

    manifest_path = ROOT / "SOURCES" / "components" / "LOCAL_ARCHIVE_MANIFEST.csv"
    with manifest_path.open(newline="", encoding="utf-8-sig") as stream:
        manifest = list(csv.DictReader(stream))
    required_columns = {
        "local_path",
        "bytes",
        "sha256",
        "official_url",
        "document_identity",
        "retrieval_date",
        "evidence_class",
        "redistribution",
    }
    missing_columns = sorted(required_columns - set(manifest[0] if manifest else []))
    if missing_columns:
        errors.append("manifest missing columns: " + ", ".join(missing_columns))

    missing_local: list[str] = []
    verified_local = 0
    for row in manifest:
        path = ROOT / row["local_path"]
        if not path.is_file():
            missing_local.append(row["local_path"])
            continue
        verified_local += 1
        if path.stat().st_size != int(row["bytes"]):
            errors.append(f"archive byte-count mismatch: {row['local_path']}")
        if sha256(path).lower() != row["sha256"].lower():
            errors.append(f"archive SHA-256 mismatch: {row['local_path']}")
    if missing_local:
        message = f"{len(missing_local)} local-only archive files absent"
        if args.require_local_archive:
            errors.append(message)
        else:
            warnings.append(message)

    result = {
        "document": "D1-DD-VERIFY-001",
        "record_count": len(register_rows),
        "status_record_count": status_count,
        "matrix_id_count": len(matrix_ids),
        "source_id_count": len(source_ids),
        "archive_manifest_rows": len(manifest),
        "archive_files_verified": verified_local,
        "archive_files_missing": len(missing_local),
        "warnings": warnings,
        "errors": errors,
        "result": "PASS" if not errors else "FAIL",
    }
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
