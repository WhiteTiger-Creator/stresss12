#!/usr/bin/env python3
"""Badge-access containment rollup deployed during the Northgate incident.

This build is producing an unreliable containment queue. It is the artifact the
response team asked to have investigated and restored.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA_VERSION = "access-containment-v3"
CLASS_ORDER = ["privileged", "contractor", "staff", "visitor"]


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text())


def export_access(events: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    class_counts = {name: 0 for name in CLASS_ORDER}
    zones: set[str] = set()
    for event in events:
        badge_class = str(event.get("badge_class", ""))
        if badge_class in class_counts:
            class_counts[badge_class] += 1
        zones.add(str(event.get("zone", "")))

    contained = []
    for event in events:
        if event.get("badge_class") == "privileged":
            contained.append(
                {
                    "swipe_id": event["swipe_id"],
                    "entered_ms": event["granted_at"] if "granted_at" in event else 0,
                    "badge_class": event["badge_class"],
                    "zone": event["zone"],
                    "door": event["door"],
                }
            )

    contained.sort(key=lambda row: row["entered_ms"])

    summary = {
        "schema_version": SCHEMA_VERSION,
        "raw_swipe_count": len(events),
        "unique_swipe_ids": len({str(event["swipe_id"]) for event in events}),
        "total_swipes": len(events),
        "class_counts": class_counts,
        "zones": sorted(zones),
        "contained_count": len(contained),
        "revoked_excluded_count": 0,
    }

    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output_dir / "zone_matrix.json").write_text(json.dumps({}, indent=2) + "\n")
    with (output_dir / "contained.jsonl").open("w", encoding="utf-8") as handle:
        for row in contained:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/app/data/badge_events.json")
    parser.add_argument("--output-dir", default="/app/output")
    args = parser.parse_args()

    events = load_events(Path(args.input))
    export_access(events, Path(args.output_dir))
    print(f"Wrote containment rollup to {args.output_dir}")


if __name__ == "__main__":
    main()
