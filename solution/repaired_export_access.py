#!/usr/bin/env python3
"""Badge-access containment rollup, restored per the Northgate review decisions."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

SCHEMA_VERSION = "access-containment-v3"
CLASS_ORDER = ["privileged", "contractor", "staff", "visitor"]
CLASS_RANK = {name: len(CLASS_ORDER) - idx for idx, name in enumerate(CLASS_ORDER)}
PRIORITY_ORDER = ["critical", "high", "standard"]
PRIORITY_RANK = {name: len(PRIORITY_ORDER) - idx for idx, name in enumerate(PRIORITY_ORDER)}
CONTROLS_PATH = Path("/app/data/zone_controls.json")
STITCH_GAP_MS = 140
CARRY_CAP_MS = 780
ZONE_QUEUE_CAP = 2
ADMISSION_FLOOR = {"privileged": 150, "contractor": 190, "staff": 240, "visitor": 300}


def _norm_text(value: object) -> str:
    return " ".join(str(value).split())


def _norm_class(value: object) -> str:
    text = str(value).strip().lower()
    return text if text in CLASS_RANK else "visitor"


def _norm_zone(value: object) -> str:
    text = str(value).strip().lower()
    return text or "unknown"


def _norm_ms(value: object) -> int:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return 0


def _norm_revoked(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "1", "yes"}
    return bool(value)


def load_events(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_controls(path: Path = CONTROLS_PATH) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_events(rows: list[dict]) -> list[dict]:
    deduped: dict[str, dict] = {}
    for row in rows:
        swipe_id = str(row.get("swipe_id", "")).strip()
        if not swipe_id:
            continue
        candidate = {
            "swipe_id": swipe_id,
            "badge_id": str(row.get("badge_id", "")).strip(),
            "badge_class": _norm_class(row.get("badge_class", "")),
            "zone": _norm_zone(row.get("zone", "")),
            "door": _norm_text(row.get("door", "")),
            "event_ms": _norm_ms(row.get("event_ms", 0)),
            "exit_ms": _norm_ms(row.get("exit_ms", 0)),
            "revoked": _norm_revoked(row.get("revoked", False)),
        }
        existing = deduped.get(swipe_id)
        if existing is None:
            deduped[swipe_id] = candidate
            continue
        if candidate["event_ms"] > existing["event_ms"]:
            deduped[swipe_id] = candidate
            continue
        if candidate["event_ms"] < existing["event_ms"]:
            continue
        # PAC-3318 reverses this: on a duplicate tie the LOWER badge class wins.
        if CLASS_RANK[candidate["badge_class"]] < CLASS_RANK[existing["badge_class"]]:
            deduped[swipe_id] = candidate
            continue
        if CLASS_RANK[candidate["badge_class"]] > CLASS_RANK[existing["badge_class"]]:
            continue
        if len(candidate["door"]) > len(existing["door"]):
            deduped[swipe_id] = candidate
            continue
        if len(candidate["door"]) < len(existing["door"]):
            continue
        if candidate["zone"] > existing["zone"]:
            deduped[swipe_id] = candidate
    canonical = list(deduped.values())
    canonical.sort(key=lambda row: (row["zone"], row["event_ms"], row["swipe_id"]))
    return canonical


def _compact(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[list[int]] = []
    for start, end in sorted(spans):
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return [(s, e) for s, e in merged]


def _overlap(a_start: int, a_end: int, spans: list[tuple[int, int]]) -> list[tuple[int, int]]:
    out = []
    for start, end in spans:
        lo, hi = max(a_start, start), min(a_end, end)
        if hi > lo:
            out.append((lo, hi))
    return out


def controls_for(rows: list[dict], zone: str, layer: str, badge_class: str) -> list[tuple[int, int]]:
    """PAC-3326 scope: a class uses its OWN windows for this layer; only a class with
    no window of its own falls back to the `all` scope. Own entries do not also
    inherit `all`."""
    own = [
        (_norm_ms(r["start_ms"]), _norm_ms(r["end_ms"])) for r in rows
        if r.get("layer") == layer and _norm_zone(r.get("zone")) == zone
        and str(r.get("scope")) == badge_class and _norm_ms(r["end_ms"]) > _norm_ms(r["start_ms"])
    ]
    if own:
        return _compact(own)
    return _compact([
        (_norm_ms(r["start_ms"]), _norm_ms(r["end_ms"])) for r in rows
        if r.get("layer") == layer and _norm_zone(r.get("zone")) == zone
        and str(r.get("scope")) == "all" and _norm_ms(r["end_ms"]) > _norm_ms(r["start_ms"])
    ])


def build_sessions(canonical: list[dict], controls: list[dict]) -> dict[str, list[dict]]:
    by_zone: dict[str, list[dict]] = {}
    for row in canonical:
        # PAC-3322: revoked badges are excluded from session construction only.
        if row["revoked"]:
            continue
        by_zone.setdefault(row["zone"], []).append(row)

    result: dict[str, list[dict]] = {}
    for zone, rows in by_zone.items():
        rows.sort(key=lambda r: (r["event_ms"], r["swipe_id"]))
        sessions: list[dict] = []
        current: dict | None = None
        for row in rows:
            end_ms = max(row["exit_ms"], row["event_ms"])
            if current is None:
                current = {
                    "start_ms": row["event_ms"], "end_ms": end_ms,
                    "swipe_ids": [row["swipe_id"]], "top_class": row["badge_class"],
                }
                continue
            # PAC-3320 retuned the stitch gap; sessions merge across it.
            if row["event_ms"] <= current["end_ms"] + STITCH_GAP_MS:
                current["end_ms"] = max(current["end_ms"], end_ms)
                current["swipe_ids"].append(row["swipe_id"])
                if CLASS_RANK[row["badge_class"]] > CLASS_RANK[current["top_class"]]:
                    current["top_class"] = row["badge_class"]
                continue
            sessions.append(current)
            current = {
                "start_ms": row["event_ms"], "end_ms": end_ms,
                "swipe_ids": [row["swipe_id"]], "top_class": row["badge_class"],
            }
        if current is not None:
            sessions.append(current)

        prev_carry_out = 0
        prev_end: int | None = None
        built: list[dict] = []
        for session in sessions:
            dwell = max(session["end_ms"] - session["start_ms"], 0)
            lock_spans = _compact(_overlap(
                session["start_ms"], session["end_ms"],
                controls_for(controls, zone, "lockdown", session["top_class"])))
            maint_spans = _compact(_overlap(
                session["start_ms"], session["end_ms"],
                controls_for(controls, zone, "maintenance", session["top_class"])))
            lockdown_overlap = sum(e - s for s, e in lock_spans)
            maintenance_overlap = sum(e - s for s, e in maint_spans)
            # PAC-3328: lockdown wins any instant both layers cover.
            shared = 0
            for ls, le in lock_spans:
                for ms, me in maint_spans:
                    shared += max(0, min(le, me) - max(ls, ms))
            maintenance_used = max(maintenance_overlap - shared, 0)
            adjusted_dwell = max(
                dwell - (-(-lockdown_overlap // 2)) - (maintenance_used // 3), 0
            )
            idle_gap = 0 if prev_end is None else max(session["start_ms"] - prev_end, 0)
            carry_in = max(prev_carry_out - (-(-idle_gap // 4)), 0)
            ledger_dwell = adjusted_dwell + (carry_in // 5)
            carry_out = min(
                carry_in + adjusted_dwell + len(session["swipe_ids"]) * 6, CARRY_CAP_MS
            )
            built.append({
                "start_ms": session["start_ms"], "end_ms": session["end_ms"],
                "dwell_ms": dwell,
                "lockdown_overlap_ms": lockdown_overlap,
                "maintenance_overlap_ms": maintenance_overlap,
                "adjusted_dwell_ms": adjusted_dwell,
                "idle_gap_ms": idle_gap, "carry_in_ms": carry_in,
                "carry_out_ms": carry_out, "ledger_dwell_ms": ledger_dwell,
                "swipe_count": len(session["swipe_ids"]),
                "swipe_ids": sorted(session["swipe_ids"]),
                "top_class": session["top_class"],
            })
            prev_carry_out = carry_out
            prev_end = session["end_ms"]
        result[zone] = built
    return {zone: result[zone] for zone in sorted(result)}


def build_queue(sessions: dict[str, list[dict]]) -> list[dict]:
    queue: list[dict] = []
    for zone, rows in sessions.items():
        for row in rows:
            if row["ledger_dwell_ms"] < ADMISSION_FLOOR[row["top_class"]]:
                continue
            if row["ledger_dwell_ms"] >= 420 or (
                row["top_class"] == "privileged" and row["lockdown_overlap_ms"] > 0
            ):
                priority = "critical"
            elif row["ledger_dwell_ms"] >= 300 or row["swipe_count"] >= 3:
                priority = "high"
            else:
                priority = "standard"
            payload = (
                f"{zone}|{row['start_ms']}|{row['end_ms']}|{','.join(row['swipe_ids'])}"
                f"|{row['top_class']}|{row['ledger_dwell_ms']}"
            )
            queue.append({
                "ticket_id": f"{zone}:{row['start_ms']}-{row['end_ms']}",
                "zone": zone, "start_ms": row["start_ms"], "end_ms": row["end_ms"],
                "top_class": row["top_class"], "priority": priority,
                "dwell_ms": row["dwell_ms"], "adjusted_dwell_ms": row["adjusted_dwell_ms"],
                "ledger_dwell_ms": row["ledger_dwell_ms"],
                "lockdown_overlap_ms": row["lockdown_overlap_ms"],
                "maintenance_overlap_ms": row["maintenance_overlap_ms"],
                "carry_in_ms": row["carry_in_ms"], "carry_out_ms": row["carry_out_ms"],
                "swipe_count": row["swipe_count"], "swipe_ids": row["swipe_ids"],
                "session_digest": hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12],
            })
    queue.sort(key=lambda r: (
        -PRIORITY_RANK[r["priority"]], -r["ledger_dwell_ms"], -r["dwell_ms"],
        -r["swipe_count"], r["zone"], r["start_ms"],
    ))
    # PAC-3330: responder capacity cap, applied AFTER the ordering chain above.
    kept: dict[str, int] = {}
    capped: list[dict] = []
    for row in queue:
        taken = kept.get(row["zone"], 0)
        if taken >= ZONE_QUEUE_CAP:
            continue
        kept[row["zone"]] = taken + 1
        capped.append(row)
    return capped


def export_access(events: list[dict], output_dir: Path, controls: list[dict]) -> dict:
    output_dir.mkdir(parents=True, exist_ok=True)
    canonical = canonical_events(events)
    sessions = build_sessions(canonical, controls)
    queue = build_queue(sessions)

    class_counts = {name: 0 for name in CLASS_ORDER}
    for row in canonical:
        class_counts[row["badge_class"]] += 1

    all_rows = [r for rows in sessions.values() for r in rows]
    matrix = {
        zone: {
            "session_count": len(rows),
            "total_dwell_ms": sum(r["dwell_ms"] for r in rows),
            "total_ledger_dwell_ms": sum(r["ledger_dwell_ms"] for r in rows),
            "max_carry_out_ms": max((r["carry_out_ms"] for r in rows), default=0),
            "queued_count": sum(1 for r in queue if r["zone"] == zone),
        }
        for zone, rows in sessions.items()
    }

    canonical_payload = "\n".join(
        f"{r['swipe_id']}|{r['badge_id']}|{r['badge_class']}|{r['zone']}|{r['event_ms']}"
        f"|{r['exit_ms']}|{1 if r['revoked'] else 0}" for r in canonical
    )
    control_payload = "\n".join(
        f"{r['layer']}|{r['scope']}|{_norm_zone(r['zone'])}|{_norm_ms(r['start_ms'])}|{_norm_ms(r['end_ms'])}"
        for r in sorted(controls, key=lambda r: (
            str(r["layer"]), str(r["scope"]), _norm_zone(r["zone"]), _norm_ms(r["start_ms"])))
    )
    queue_payload = "\n".join(
        f"{r['ticket_id']}|{r['priority']}|{r['ledger_dwell_ms']}|{r['session_digest']}" for r in queue
    )

    summary = {
        "schema_version": SCHEMA_VERSION,
        "raw_swipe_count": len(events),
        "unique_swipe_ids": len({str(e.get("swipe_id", "")).strip() for e in events if str(e.get("swipe_id", "")).strip()}),
        "canonical_swipe_count": len(canonical),
        "class_counts": class_counts,
        "zones": sorted(sessions),
        "zone_count": len(sessions),
        "revoked_excluded_count": sum(1 for r in canonical if r["revoked"]),
        "session_count": len(all_rows),
        "total_dwell_ms": sum(r["dwell_ms"] for r in all_rows),
        "total_adjusted_dwell_ms": sum(r["adjusted_dwell_ms"] for r in all_rows),
        "total_ledger_dwell_ms": sum(r["ledger_dwell_ms"] for r in all_rows),
        "total_lockdown_overlap_ms": sum(r["lockdown_overlap_ms"] for r in all_rows),
        "total_maintenance_overlap_ms": sum(r["maintenance_overlap_ms"] for r in all_rows),
        "max_ledger_dwell_ms": max((r["ledger_dwell_ms"] for r in all_rows), default=0),
        "max_carry_out_ms": max((r["carry_out_ms"] for r in all_rows), default=0),
        "longest_session_ms": max((r["dwell_ms"] for r in all_rows), default=0),
        "contained_count": len(queue),
        "priority_counts": {
            name: sum(1 for r in queue if r["priority"] == name) for name in PRIORITY_ORDER
        },
        "canonical_swipe_checksum": hashlib.sha256(canonical_payload.encode("utf-8")).hexdigest(),
        "zone_control_checksum": hashlib.sha256(control_payload.encode("utf-8")).hexdigest(),
        "containment_checksum": hashlib.sha256(queue_payload.encode("utf-8")).hexdigest(),
    }

    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (output_dir / "zone_matrix.json").write_text(json.dumps(matrix, indent=2) + "\n", encoding="utf-8")
    with (output_dir / "contained.jsonl").open("w", encoding="utf-8") as handle:
        for row in queue:
            handle.write(json.dumps(row, separators=(",", ":")) + "\n")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/app/data/badge_events.json")
    parser.add_argument("--output-dir", default="/app/output")
    args = parser.parse_args()

    events = load_events(Path(args.input))
    export_access(events, Path(args.output_dir), load_controls())
    print(f"Wrote containment rollup to {args.output_dir}")


if __name__ == "__main__":
    main()
