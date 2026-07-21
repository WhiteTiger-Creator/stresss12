#!/usr/bin/env python3
"""Broken Beacon threat workflow used for repair task."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA_VERSION = "edr-triage-v2"


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def export_report(events: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    severity_counts = {name: 0 for name in ("critical", "high", "medium", "low")}
    host_groups: set[str] = set()
    for event in events:
        severity = str(event.get("severity", ""))
        if severity in severity_counts:
            severity_counts[severity] += 1
        host_groups.add(str(event.get("host_group", "")))

    threats = []
    for event in events:
        severity = event.get("severity")
        if severity == "critical":
            threats.append(
                {
                    "detection_id": event["detection_id"],
                    "seen_ms": event["seen_at"] if "seen_at" in event else 0,
                    "severity": event["severity"],
                    "host_group": event["host_group"],
                    "rule_name": event["rule_name"],
                }
            )

    threats.sort(key=lambda row: row["seen_ms"])

    summary = {
        "schema_version": SCHEMA_VERSION,
        "raw_alert_count": len(events),
        "unique_detection_ids": len({str(event["detection_id"]) for event in events}),
        "total_alerts": len(events),
        "severity_counts": severity_counts,
        "host_groups": sorted(host_groups),
        "escalated_count": len(threats),
        "suppressed_excluded_count": 0,
    }

    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output_dir / "service_matrix.json").write_text(json.dumps({}, indent=2) + "\n")
    with (output_dir / "flagged.jsonl").open("w", encoding="utf-8") as handle:
        for row in threats:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/app/data/events.json")
    parser.add_argument("--output-dir", default="/app/output")
    args = parser.parse_args()

    events = load_events(Path(args.input))
    export_report(events, Path(args.output_dir))
    print(f"Wrote report to {args.output_dir}")


if __name__ == "__main__":
    main()
