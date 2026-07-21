#!/usr/bin/env python3
"""Northgate badge-access containment audit CLI: diagnose and repair."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

WORKFLOW_PATH = Path("/app/workflow/export_access.py")
FROZEN_PATH = Path("/app/workflow/.export_access.original")
DOSSIER_PATH = Path("/app/incident/access_review_dossier.md")
SPEC_PATH = Path("/app/docs/report_spec.json")
EVENTS_PATH = Path("/app/data/badge_events.json")

REPAIRED_SOURCE = '#!/usr/bin/env python3\n"""Badge-access containment rollup, restored per the Northgate review decisions."""\n\nfrom __future__ import annotations\n\nimport argparse\nimport hashlib\nimport json\nfrom pathlib import Path\n\nSCHEMA_VERSION = "access-containment-v3"\nCLASS_ORDER = ["privileged", "contractor", "staff", "visitor"]\nCLASS_RANK = {name: len(CLASS_ORDER) - idx for idx, name in enumerate(CLASS_ORDER)}\nPRIORITY_ORDER = ["critical", "high", "standard"]\nPRIORITY_RANK = {name: len(PRIORITY_ORDER) - idx for idx, name in enumerate(PRIORITY_ORDER)}\nCONTROLS_PATH = Path("/app/data/zone_controls.json")\nSTITCH_GAP_MS = 140\nCARRY_CAP_MS = 780\nZONE_QUEUE_CAP = 2\nADMISSION_FLOOR = {"privileged": 150, "contractor": 190, "staff": 240, "visitor": 300}\n\n\ndef _norm_text(value: object) -> str:\n    return " ".join(str(value).split())\n\n\ndef _norm_class(value: object) -> str:\n    text = str(value).strip().lower()\n    return text if text in CLASS_RANK else "visitor"\n\n\ndef _norm_zone(value: object) -> str:\n    text = str(value).strip().lower()\n    return text or "unknown"\n\n\ndef _norm_ms(value: object) -> int:\n    try:\n        return int(str(value).strip())\n    except (TypeError, ValueError):\n        return 0\n\n\ndef _norm_revoked(value: object) -> bool:\n    if isinstance(value, bool):\n        return value\n    if isinstance(value, str):\n        return value.strip().lower() in {"true", "1", "yes"}\n    return bool(value)\n\n\ndef load_events(path: Path) -> list[dict]:\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\ndef load_controls(path: Path = CONTROLS_PATH) -> list[dict]:\n    if not path.exists():\n        return []\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\ndef canonical_events(rows: list[dict]) -> list[dict]:\n    deduped: dict[str, dict] = {}\n    for row in rows:\n        swipe_id = str(row.get("swipe_id", "")).strip()\n        if not swipe_id:\n            continue\n        candidate = {\n            "swipe_id": swipe_id,\n            "badge_id": str(row.get("badge_id", "")).strip(),\n            "badge_class": _norm_class(row.get("badge_class", "")),\n            "zone": _norm_zone(row.get("zone", "")),\n            "door": _norm_text(row.get("door", "")),\n            "event_ms": _norm_ms(row.get("event_ms", 0)),\n            "exit_ms": _norm_ms(row.get("exit_ms", 0)),\n            "revoked": _norm_revoked(row.get("revoked", False)),\n        }\n        existing = deduped.get(swipe_id)\n        if existing is None:\n            deduped[swipe_id] = candidate\n            continue\n        if candidate["event_ms"] > existing["event_ms"]:\n            deduped[swipe_id] = candidate\n            continue\n        if candidate["event_ms"] < existing["event_ms"]:\n            continue\n        # PAC-3318 reverses this: on a duplicate tie the LOWER badge class wins.\n        if CLASS_RANK[candidate["badge_class"]] < CLASS_RANK[existing["badge_class"]]:\n            deduped[swipe_id] = candidate\n            continue\n        if CLASS_RANK[candidate["badge_class"]] > CLASS_RANK[existing["badge_class"]]:\n            continue\n        if len(candidate["door"]) > len(existing["door"]):\n            deduped[swipe_id] = candidate\n            continue\n        if len(candidate["door"]) < len(existing["door"]):\n            continue\n        if candidate["zone"] > existing["zone"]:\n            deduped[swipe_id] = candidate\n    canonical = list(deduped.values())\n    canonical.sort(key=lambda row: (row["zone"], row["event_ms"], row["swipe_id"]))\n    return canonical\n\n\ndef _compact(spans: list[tuple[int, int]]) -> list[tuple[int, int]]:\n    merged: list[list[int]] = []\n    for start, end in sorted(spans):\n        if not merged or start > merged[-1][1]:\n            merged.append([start, end])\n        else:\n            merged[-1][1] = max(merged[-1][1], end)\n    return [(s, e) for s, e in merged]\n\n\ndef _overlap(a_start: int, a_end: int, spans: list[tuple[int, int]]) -> list[tuple[int, int]]:\n    out = []\n    for start, end in spans:\n        lo, hi = max(a_start, start), min(a_end, end)\n        if hi > lo:\n            out.append((lo, hi))\n    return out\n\n\ndef controls_for(rows: list[dict], zone: str, layer: str, badge_class: str) -> list[tuple[int, int]]:\n    """PAC-3326 scope: a class uses its OWN windows for this layer; only a class with\n    no window of its own falls back to the `all` scope. Own entries do not also\n    inherit `all`."""\n    own = [\n        (_norm_ms(r["start_ms"]), _norm_ms(r["end_ms"])) for r in rows\n        if r.get("layer") == layer and _norm_zone(r.get("zone")) == zone\n        and str(r.get("scope")) == badge_class and _norm_ms(r["end_ms"]) > _norm_ms(r["start_ms"])\n    ]\n    if own:\n        return _compact(own)\n    return _compact([\n        (_norm_ms(r["start_ms"]), _norm_ms(r["end_ms"])) for r in rows\n        if r.get("layer") == layer and _norm_zone(r.get("zone")) == zone\n        and str(r.get("scope")) == "all" and _norm_ms(r["end_ms"]) > _norm_ms(r["start_ms"])\n    ])\n\n\ndef build_sessions(canonical: list[dict], controls: list[dict]) -> dict[str, list[dict]]:\n    by_zone: dict[str, list[dict]] = {}\n    for row in canonical:\n        # PAC-3322: revoked badges are excluded from session construction only.\n        if row["revoked"]:\n            continue\n        by_zone.setdefault(row["zone"], []).append(row)\n\n    result: dict[str, list[dict]] = {}\n    for zone, rows in by_zone.items():\n        rows.sort(key=lambda r: (r["event_ms"], r["swipe_id"]))\n        sessions: list[dict] = []\n        current: dict | None = None\n        for row in rows:\n            end_ms = max(row["exit_ms"], row["event_ms"])\n            if current is None:\n                current = {\n                    "start_ms": row["event_ms"], "end_ms": end_ms,\n                    "swipe_ids": [row["swipe_id"]], "top_class": row["badge_class"],\n                }\n                continue\n            # PAC-3320 retuned the stitch gap; sessions merge across it.\n            if row["event_ms"] <= current["end_ms"] + STITCH_GAP_MS:\n                current["end_ms"] = max(current["end_ms"], end_ms)\n                current["swipe_ids"].append(row["swipe_id"])\n                if CLASS_RANK[row["badge_class"]] > CLASS_RANK[current["top_class"]]:\n                    current["top_class"] = row["badge_class"]\n                continue\n            sessions.append(current)\n            current = {\n                "start_ms": row["event_ms"], "end_ms": end_ms,\n                "swipe_ids": [row["swipe_id"]], "top_class": row["badge_class"],\n            }\n        if current is not None:\n            sessions.append(current)\n\n        prev_carry_out = 0\n        prev_end: int | None = None\n        built: list[dict] = []\n        for session in sessions:\n            dwell = max(session["end_ms"] - session["start_ms"], 0)\n            lock_spans = _compact(_overlap(\n                session["start_ms"], session["end_ms"],\n                controls_for(controls, zone, "lockdown", session["top_class"])))\n            maint_spans = _compact(_overlap(\n                session["start_ms"], session["end_ms"],\n                controls_for(controls, zone, "maintenance", session["top_class"])))\n            lockdown_overlap = sum(e - s for s, e in lock_spans)\n            maintenance_overlap = sum(e - s for s, e in maint_spans)\n            # PAC-3328: lockdown wins any instant both layers cover.\n            shared = 0\n            for ls, le in lock_spans:\n                for ms, me in maint_spans:\n                    shared += max(0, min(le, me) - max(ls, ms))\n            maintenance_used = max(maintenance_overlap - shared, 0)\n            adjusted_dwell = max(\n                dwell - (-(-lockdown_overlap // 2)) - (maintenance_used // 3), 0\n            )\n            idle_gap = 0 if prev_end is None else max(session["start_ms"] - prev_end, 0)\n            carry_in = max(prev_carry_out - (-(-idle_gap // 4)), 0)\n            ledger_dwell = adjusted_dwell + (carry_in // 5)\n            carry_out = min(\n                carry_in + adjusted_dwell + len(session["swipe_ids"]) * 6, CARRY_CAP_MS\n            )\n            built.append({\n                "start_ms": session["start_ms"], "end_ms": session["end_ms"],\n                "dwell_ms": dwell,\n                "lockdown_overlap_ms": lockdown_overlap,\n                "maintenance_overlap_ms": maintenance_overlap,\n                "adjusted_dwell_ms": adjusted_dwell,\n                "idle_gap_ms": idle_gap, "carry_in_ms": carry_in,\n                "carry_out_ms": carry_out, "ledger_dwell_ms": ledger_dwell,\n                "swipe_count": len(session["swipe_ids"]),\n                "swipe_ids": sorted(session["swipe_ids"]),\n                "top_class": session["top_class"],\n            })\n            prev_carry_out = carry_out\n            prev_end = session["end_ms"]\n        result[zone] = built\n    return {zone: result[zone] for zone in sorted(result)}\n\n\ndef build_queue(sessions: dict[str, list[dict]]) -> list[dict]:\n    queue: list[dict] = []\n    for zone, rows in sessions.items():\n        for row in rows:\n            if row["ledger_dwell_ms"] < ADMISSION_FLOOR[row["top_class"]]:\n                continue\n            if row["ledger_dwell_ms"] >= 420 or (\n                row["top_class"] == "privileged" and row["lockdown_overlap_ms"] > 0\n            ):\n                priority = "critical"\n            elif row["ledger_dwell_ms"] >= 300 or row["swipe_count"] >= 3:\n                priority = "high"\n            else:\n                priority = "standard"\n            payload = (\n                f"{zone}|{row[\'start_ms\']}|{row[\'end_ms\']}|{\',\'.join(row[\'swipe_ids\'])}"\n                f"|{row[\'top_class\']}|{row[\'ledger_dwell_ms\']}"\n            )\n            queue.append({\n                "ticket_id": f"{zone}:{row[\'start_ms\']}-{row[\'end_ms\']}",\n                "zone": zone, "start_ms": row["start_ms"], "end_ms": row["end_ms"],\n                "top_class": row["top_class"], "priority": priority,\n                "dwell_ms": row["dwell_ms"], "adjusted_dwell_ms": row["adjusted_dwell_ms"],\n                "ledger_dwell_ms": row["ledger_dwell_ms"],\n                "lockdown_overlap_ms": row["lockdown_overlap_ms"],\n                "maintenance_overlap_ms": row["maintenance_overlap_ms"],\n                "carry_in_ms": row["carry_in_ms"], "carry_out_ms": row["carry_out_ms"],\n                "swipe_count": row["swipe_count"], "swipe_ids": row["swipe_ids"],\n                "session_digest": hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12],\n            })\n    queue.sort(key=lambda r: (\n        -PRIORITY_RANK[r["priority"]], -r["ledger_dwell_ms"], -r["dwell_ms"],\n        -r["swipe_count"], r["zone"], r["start_ms"],\n    ))\n    # PAC-3330: responder capacity cap, applied AFTER the ordering chain above.\n    kept: dict[str, int] = {}\n    capped: list[dict] = []\n    for row in queue:\n        taken = kept.get(row["zone"], 0)\n        if taken >= ZONE_QUEUE_CAP:\n            continue\n        kept[row["zone"]] = taken + 1\n        capped.append(row)\n    return capped\n\n\ndef export_access(events: list[dict], output_dir: Path, controls: list[dict]) -> dict:\n    output_dir.mkdir(parents=True, exist_ok=True)\n    canonical = canonical_events(events)\n    sessions = build_sessions(canonical, controls)\n    queue = build_queue(sessions)\n\n    class_counts = {name: 0 for name in CLASS_ORDER}\n    for row in canonical:\n        class_counts[row["badge_class"]] += 1\n\n    all_rows = [r for rows in sessions.values() for r in rows]\n    matrix = {\n        zone: {\n            "session_count": len(rows),\n            "total_dwell_ms": sum(r["dwell_ms"] for r in rows),\n            "total_ledger_dwell_ms": sum(r["ledger_dwell_ms"] for r in rows),\n            "max_carry_out_ms": max((r["carry_out_ms"] for r in rows), default=0),\n            "queued_count": sum(1 for r in queue if r["zone"] == zone),\n        }\n        for zone, rows in sessions.items()\n    }\n\n    canonical_payload = "\\n".join(\n        f"{r[\'swipe_id\']}|{r[\'badge_id\']}|{r[\'badge_class\']}|{r[\'zone\']}|{r[\'event_ms\']}"\n        f"|{r[\'exit_ms\']}|{1 if r[\'revoked\'] else 0}" for r in canonical\n    )\n    control_payload = "\\n".join(\n        f"{r[\'layer\']}|{r[\'scope\']}|{_norm_zone(r[\'zone\'])}|{_norm_ms(r[\'start_ms\'])}|{_norm_ms(r[\'end_ms\'])}"\n        for r in sorted(controls, key=lambda r: (\n            str(r["layer"]), str(r["scope"]), _norm_zone(r["zone"]), _norm_ms(r["start_ms"])))\n    )\n    queue_payload = "\\n".join(\n        f"{r[\'ticket_id\']}|{r[\'priority\']}|{r[\'ledger_dwell_ms\']}|{r[\'session_digest\']}" for r in queue\n    )\n\n    summary = {\n        "schema_version": SCHEMA_VERSION,\n        "raw_swipe_count": len(events),\n        "unique_swipe_ids": len({str(e.get("swipe_id", "")).strip() for e in events if str(e.get("swipe_id", "")).strip()}),\n        "canonical_swipe_count": len(canonical),\n        "class_counts": class_counts,\n        "zones": sorted(sessions),\n        "zone_count": len(sessions),\n        "revoked_excluded_count": sum(1 for r in canonical if r["revoked"]),\n        "session_count": len(all_rows),\n        "total_dwell_ms": sum(r["dwell_ms"] for r in all_rows),\n        "total_adjusted_dwell_ms": sum(r["adjusted_dwell_ms"] for r in all_rows),\n        "total_ledger_dwell_ms": sum(r["ledger_dwell_ms"] for r in all_rows),\n        "total_lockdown_overlap_ms": sum(r["lockdown_overlap_ms"] for r in all_rows),\n        "total_maintenance_overlap_ms": sum(r["maintenance_overlap_ms"] for r in all_rows),\n        "max_ledger_dwell_ms": max((r["ledger_dwell_ms"] for r in all_rows), default=0),\n        "max_carry_out_ms": max((r["carry_out_ms"] for r in all_rows), default=0),\n        "longest_session_ms": max((r["dwell_ms"] for r in all_rows), default=0),\n        "contained_count": len(queue),\n        "priority_counts": {\n            name: sum(1 for r in queue if r["priority"] == name) for name in PRIORITY_ORDER\n        },\n        "canonical_swipe_checksum": hashlib.sha256(canonical_payload.encode("utf-8")).hexdigest(),\n        "zone_control_checksum": hashlib.sha256(control_payload.encode("utf-8")).hexdigest(),\n        "containment_checksum": hashlib.sha256(queue_payload.encode("utf-8")).hexdigest(),\n    }\n\n    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\\n", encoding="utf-8")\n    (output_dir / "zone_matrix.json").write_text(json.dumps(matrix, indent=2) + "\\n", encoding="utf-8")\n    with (output_dir / "contained.jsonl").open("w", encoding="utf-8") as handle:\n        for row in queue:\n            handle.write(json.dumps(row, separators=(",", ":")) + "\\n")\n    return summary\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser()\n    parser.add_argument("--input", default="/app/data/badge_events.json")\n    parser.add_argument("--output-dir", default="/app/output")\n    args = parser.parse_args()\n\n    events = load_events(Path(args.input))\n    export_access(events, Path(args.output_dir), load_controls())\n    print(f"Wrote containment rollup to {args.output_dir}")\n\n\nif __name__ == "__main__":\n    main()\n'


def load_spec() -> dict:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


def load_events(path: Path = EVENTS_PATH) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8"))


def input_stats(events: list[dict]) -> dict:
    ids = [str(e.get("swipe_id", "")).strip() for e in events]
    present = [i for i in ids if i]
    return {
        "raw_swipe_count": len(events),
        "unique_swipe_ids": len(set(present)),
        "duplicate_swipe_ids": len(present) - len(set(present)),
        "revoked_row_count": sum(
            1 for e in events
            if (e.get("revoked") is True)
            or (isinstance(e.get("revoked"), str) and e["revoked"].strip().lower() in {"true", "1", "yes"})
        ),
    }


def frozen_audit() -> dict:
    raw = FROZEN_PATH.read_bytes()
    return {
        "frozen_sha256": hashlib.sha256(raw).hexdigest(),
        "frozen_byte_count": len(raw),
    }


def _line_has_all(line: str, terms: list[str]) -> bool:
    low = line.lower()
    return all(t.lower() in low for t in terms)


def find_dossier_quote(text: str, terms: list[str]) -> str:
    """First line of the dossier containing every term, returned VERBATIM."""
    for line in text.splitlines():
        if line.strip() and _line_has_all(line, terms):
            return line.strip()
    raise SystemExit(f"no dossier line matches {terms}")


def find_pipeline_evidence(source: str, terms: list[str]) -> str:
    """First line of the FROZEN workflow containing every term, VERBATIM."""
    for line in source.splitlines():
        if line.strip() and _line_has_all(line, terms):
            return line.strip()
    raise SystemExit(f"no pipeline line matches {terms}")


def build_issues(dossier: str, frozen: str, spec: dict) -> list[dict]:
    issues = []
    for entry in spec["known_defects"]:
        issues.append({
            "defect_id": entry["defect_id"],
            "stage": entry["stage"],
            "dossier_quote": find_dossier_quote(dossier, entry["dossier_terms"]),
            "pipeline_evidence": find_pipeline_evidence(frozen, entry["pipeline_terms"]),
            "repair_action": entry["repair_action"],
        })
    issues.sort(key=lambda row: row["defect_id"])
    return issues


def build_diagnosis(dossier: str, frozen: str, spec: dict, events: list[dict]) -> dict:
    issues = build_issues(dossier, frozen, spec)
    payload = "\n".join(
        f"{i['defect_id']}|{i['stage']}|{i['repair_action']}" for i in issues
    )
    return {
        "schema_version": spec["diagnosis_report"]["schema_version"],
        "input_stats": input_stats(events),
        "defect_count": len(issues),
        "defects": issues,
        "diagnosis_checksum": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
    }


def patch_workflow() -> None:
    """Write the repaired pipeline to disk BEFORE it is loaded or run."""
    WORKFLOW_PATH.write_text(REPAIRED_SOURCE, encoding="utf-8")


def cmd_diagnose(dossier_path: Path, report_path: Path) -> None:
    spec = load_spec()
    report = build_diagnosis(
        dossier_path.read_text(encoding="utf-8"),
        FROZEN_PATH.read_text(encoding="utf-8"),
        spec,
        load_events(),
    )
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote diagnosis to {report_path}")


def cmd_repair(output_dir: Path) -> None:
    spec = load_spec()
    before = frozen_audit()
    dossier = DOSSIER_PATH.read_text(encoding="utf-8")
    frozen = FROZEN_PATH.read_text(encoding="utf-8")
    events = load_events()

    patch_workflow()
    output_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        [sys.executable, str(WORKFLOW_PATH), "--output-dir", str(output_dir)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode != 0:
        raise SystemExit(f"repaired workflow failed: {result.stderr}")

    diagnosis = build_diagnosis(dossier, frozen, spec, events)
    (output_dir / "diagnosis.json").write_text(
        json.dumps(diagnosis, indent=2) + "\n", encoding="utf-8")

    repaired_bytes = WORKFLOW_PATH.read_bytes()
    removed = [t for t in spec["workflow_repair"]["forbidden_tokens"]
               if t not in repaired_bytes.decode("utf-8")]
    audit = {
        "schema_version": spec["repair_audit"]["schema_version"],
        "pre_repair_sha256": before["frozen_sha256"],
        "pre_repair_byte_count": before["frozen_byte_count"],
        "post_repair_sha256": hashlib.sha256(repaired_bytes).hexdigest(),
        "post_repair_byte_count": len(repaired_bytes),
        "defects_repaired": [i["defect_id"] for i in diagnosis["defects"]],
        "forbidden_tokens_removed": sorted(removed),
        "artifacts": sorted(p.name for p in output_dir.iterdir() if p.is_file()),
    }
    audit["artifacts"] = sorted(set(audit["artifacts"]) | {"repair_audit.json"})
    (output_dir / "repair_audit.json").write_text(
        json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(f"Repaired workflow and wrote artifacts to {output_dir}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Northgate badge-access containment audit")
    sub = parser.add_subparsers(dest="command", required=True)

    diag = sub.add_parser("diagnose")
    diag.add_argument("--dossier", default=str(DOSSIER_PATH))
    diag.add_argument("--report", default="/app/output/diagnosis.json")

    rep = sub.add_parser("repair")
    rep.add_argument("--output-dir", default="/app/output")

    args = parser.parse_args()
    if args.command == "diagnose":
        cmd_diagnose(Path(args.dossier), Path(args.report))
    else:
        cmd_repair(Path(args.output_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
