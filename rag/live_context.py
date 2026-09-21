#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import uuid
from datetime import datetime
from pathlib import Path

ROOT = Path(
    os.environ.get("ROMANZIERE_REPO_ROOT", str(Path(__file__).resolve().parents[1]))
).resolve()
RAG = ROOT / "rag"
LIVE = RAG / "live"
MICRO = LIVE / "micro-checkpoints"
CTX = LIVE / "ROMANZIERE_LIVE_CONTEXT.json"

CURRENT_MICRO_SCHEMA_VERSION = 2
LEGACY_MICRO_SCHEMA_VERSION = 1

V2_CHANGE_TYPES = {
    "correction",
    "approval",
    "decision",
    "rule",
    "project_state",
    "profile_change",
    "relational_shift",
    "open_loop",
    "preflight",
    "milestone",
    "source_update",
    "workflow_change",
    "accepted_file",
    "visual_context",
}

# Exact values observed in the complete legacy audit on 2026-09-21.
LEGACY_CHANGE_TYPES = {
    "approved-correction",
    "approved-minimal-text-change",
    "approved-prologue-and-manuscript-assembly",
    "approved-structural-and-prose-revision",
    "approved-structural-move",
    "approved-structural-revert",
    "approved-targeted-revision",
    "binding-clarification",
    "chapter-acceptance-transition",
    "chapter-accepted",
    "chapter-audit",
    "chapter-draft",
    "chapter-finalization",
    "chapter-transition",
    "chronology-and-causality-correction",
    "chronology-correction",
    "clarity-tightening",
    "correction",
    "editorial-trim-trial",
    "editorial-workflow-lock",
    "emotional-context-insertion",
    "end-instance-handoff",
    "ending-lock",
    "factual-chronology-correction",
    "factual-correction",
    "final-approval",
    "final-arc-lock",
    "identity-choice",
    "identity-decision",
    "identity-milestone",
    "identity-reflection",
    "identity-relational-decision",
    "identity-relational-milestone",
    "identity-revision",
    "identity-rule",
    "identity-rule-wording",
    "interaction-boundary",
    "literary-training",
    "major-chronology-and-motive-correction",
    "memory-system-hardening",
    "methodology-correction",
    "microprose-correction",
    "milestone",
    "narrative-correction",
    "narrative-framing",
    "narrative-origin-correction",
    "narrative-precision",
    "narrative-sequencing",
    "narrative-source-correction",
    "narrative-timing-correction",
    "narrative-transition",
    "portrait-expansion",
    "portrait-visual-canon",
    "portrait-visual-rule",
    "preflight",
    "profile-change",
    "project-state",
    "prose-adjustment",
    "prose-clarification",
    "prose-continuity-integration",
    "prose-cut",
    "prose-expansion",
    "prose-focus-correction",
    "prose-tightening",
    "recovery-sync",
    "relational-milestone",
    "relationship-framing",
    "scene-accepted",
    "scene-detail-restoration",
    "scene-draft",
    "scene-finalization",
    "scene-restoration",
    "scene-structure",
    "scene1-characterization-correction",
    "scene1-source-correction",
    "scene2-characterization-correction",
    "scene2-editorial-correction",
    "scene2-metaphor-lock",
    "scene3-clarification",
    "scene3-source-correction",
    "scene5-source-correction",
    "scene6-source-correction",
    "scene7-narrative-correction",
    "scene8-source-correction",
    "source-audit",
    "source-correction",
    "source-grounded-dialogue",
    "source-update",
    "source-update-and-comparison",
    "structural-ending-decision",
    "structural-integration",
    "structural-narrative-decision",
    "structural-reorder",
    "style-correction",
    "technical-and-narrative-clarification",
    "technical-and-narrative-correction",
    "title-change",
    "user-causal-correction",
    "user-characterization-correction",
    "user-direct-correction",
    "user-editorial-direction",
    "user-structural-correction",
    "workflow-and-continuity-correction",
    "workflow-change",
    "workflow-lock",
    "workflow-rule-and-milestone",
    "workflow-state",
}

V2_REQUIRED = {
    "schema_version",
    "micro_id",
    "owner",
    "kind",
    "event_at",
    "recorded_at",
    "change_type",
    "summary",
    "changed",
    "thread_ids",
    "source_refs",
    "memory_refs",
    "media_refs",
    "importance",
    "next_action",
    "preflight",
}

V2_OPTIONAL_EXTENSIONS = {
    "work_refs": list,
    "verified": bool,
    "accepted_files": list,
    "working_files": list,
}

# Only fields proven missing by LEGACY_V1_COMPATIBILITY_AUDIT.md are defaulted.
LEGACY_STATIC_DEFAULTS = {
    "changed": [],
    "thread_ids": [],
    "source_refs": [],
    "memory_refs": [],
    "media_refs": [],
    "importance": 3,
    "next_action": "",
    "preflight": False,
}

ALLOWED_EXTERNAL_PREFIXES = ("conversation://", "github://", "external://")

DEFAULT_REVIEW_POLICY = {
    "substantive_turn_interval": 1,
    "immediate_triggers": [
        "correction",
        "approval",
        "decision",
        "rule",
        "project_state",
        "profile_change",
        "relational_shift",
        "open_loop",
        "milestone",
        "source_update",
        "workflow_change",
        "accepted_file",
        "visual_context",
    ],
    "preflight_before_long_or_risky_work": True,
    "work_must_be_persisted_before_checkpoint": True,
    "artifact_is_never_canonical": True,
    "full_checkpoint_review_after_significant_micro_checkpoints": 5,
}


def fail(message: str) -> None:
    raise SystemExit(message)


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def safe_slug(text: str) -> str:
    text = text.casefold().strip()
    text = re.sub(r"[^0-9a-zà-öø-ÿ_-]+", "-", text, flags=re.UNICODE)
    text = re.sub(r"-+", "-", text).strip("-")
    return (text[:64] or "delta").strip("-")


def load_live() -> dict:
    if not CTX.is_file():
        return {
            "schema_version": 1,
            "owner": "romanziere",
            "kind": "romanziere_live_context",
            "updated_at": now_iso(),
            "latest_summary": "",
            "next_action": "",
            "last_micro_checkpoint": None,
            "last_full_checkpoint": None,
            "active_threads": [],
            "open_loops": [],
            "recent_micro_checkpoints": [],
            "micro_since_full_checkpoint": 0,
            "review_policy": dict(DEFAULT_REVIEW_POLICY),
            "note": (
                "Projection only. Append-only truth lives in "
                "micro-checkpoints/checkpoints/memories/sources."
            ),
        }
    try:
        return json.loads(CTX.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid live context JSON: {exc}")


def normalize_legacy_for_validation(record: dict, path: Path | None) -> dict:
    """Return an in-memory v1 compatibility view; never rewrite the source file."""
    normalized = dict(record)
    for key, default in LEGACY_STATIC_DEFAULTS.items():
        if key not in normalized:
            normalized[key] = list(default) if isinstance(default, list) else default
    if "micro_id" not in normalized:
        normalized["micro_id"] = (
            f"legacy:{rel(path)}" if path is not None else "legacy:in-memory"
        )
    if "event_at" not in normalized:
        normalized["event_at"] = normalized.get("recorded_at")
    return normalized


def ref_is_external(ref: str) -> bool:
    return ref.startswith(ALLOWED_EXTERNAL_PREFIXES)


def local_ref_exists(ref: str) -> bool:
    if not ref or Path(ref).is_absolute():
        return False
    try:
        target = (ROOT / ref).resolve()
        target.relative_to(ROOT)
    except (ValueError, OSError):
        return False
    return target.exists()


def validate_string_list(record: dict, key: str, errors: list[str]) -> None:
    value = record.get(key)
    if not isinstance(value, list):
        errors.append(f"{key} must be a list")
        return
    if any(not isinstance(item, str) for item in value):
        errors.append(f"{key} must contain only strings")


def validate_v2_refs(record: dict, errors: list[str]) -> None:
    ref_fields = (
        "changed",
        "source_refs",
        "memory_refs",
        "media_refs",
        "work_refs",
        "accepted_files",
        "working_files",
    )
    for key in ref_fields:
        if key not in record:
            continue
        value = record[key]
        if not isinstance(value, list):
            continue
        for ref in value:
            if not isinstance(ref, str):
                continue
            if ref_is_external(ref):
                continue
            if not local_ref_exists(ref):
                errors.append(f"{key} missing local ref: {ref}")


def validate_micro(record: dict, path: Path | None = None) -> list[str]:
    errors: list[str] = []
    version = record.get("schema_version")
    if version not in (LEGACY_MICRO_SCHEMA_VERSION, CURRENT_MICRO_SCHEMA_VERSION):
        return [f"unsupported schema_version={version}"]

    normalized = (
        normalize_legacy_for_validation(record, path)
        if version == LEGACY_MICRO_SCHEMA_VERSION
        else dict(record)
    )

    missing = sorted(V2_REQUIRED - set(normalized))
    if missing:
        errors.append(f"missing keys: {missing}")

    if normalized.get("owner") != "romanziere":
        errors.append("owner must be romanziere")
    if normalized.get("kind") != "romanziere_micro_checkpoint":
        errors.append("kind must be romanziere_micro_checkpoint")

    change_type = normalized.get("change_type")
    allowed = LEGACY_CHANGE_TYPES if version == LEGACY_MICRO_SCHEMA_VERSION else V2_CHANGE_TYPES
    if change_type not in allowed:
        errors.append(f"invalid change_type={change_type}")

    for key in ("micro_id", "event_at", "recorded_at", "summary", "next_action"):
        if not isinstance(normalized.get(key), str):
            errors.append(f"{key} must be a string")
    if not str(normalized.get("micro_id") or "").strip():
        errors.append("micro_id is empty")
    if not str(normalized.get("summary") or "").strip():
        errors.append("summary is empty")

    for key in ("changed", "thread_ids", "source_refs", "memory_refs", "media_refs"):
        validate_string_list(normalized, key, errors)

    importance = normalized.get("importance")
    if isinstance(importance, bool) or not isinstance(importance, int) or not 1 <= importance <= 5:
        errors.append("importance must be integer 1..5")
    if not isinstance(normalized.get("preflight"), bool):
        errors.append("preflight must be a boolean")

    if version == CURRENT_MICRO_SCHEMA_VERSION:
        for key, expected_type in V2_OPTIONAL_EXTENSIONS.items():
            if key in normalized and not isinstance(normalized[key], expected_type):
                errors.append(f"{key} must be {expected_type.__name__}")
            if key in normalized and expected_type is list:
                validate_string_list(normalized, key, errors)
        validate_v2_refs(normalized, errors)

    if path is not None and path.suffix != ".json":
        errors.append("micro-checkpoint path must end in .json")
    return errors


def save_delta(args: argparse.Namespace) -> Path:
    recorded_at = now_iso()
    event_at = args.event_at or recorded_at
    dt = datetime.fromisoformat(recorded_at)
    stamp = dt.strftime("%Y-%m-%dT%H%M%S%z")
    slug = safe_slug(args.summary)
    token = uuid.uuid4().hex[:8]
    target = (
        MICRO / f"{dt:%Y}" / f"{dt:%m}" / f"{dt:%d}"
        / f"{stamp}--{slug}--{token}.json"
    )

    record = {
        "schema_version": CURRENT_MICRO_SCHEMA_VERSION,
        "micro_id": f"romanziere-micro-{stamp}-{token}",
        "owner": "romanziere",
        "kind": "romanziere_micro_checkpoint",
        "event_at": event_at,
        "recorded_at": recorded_at,
        "change_type": args.change_type,
        "summary": args.summary.strip(),
        "changed": args.changed or [],
        "thread_ids": args.thread or [],
        "source_refs": args.source or ["conversation://current"],
        "memory_refs": args.memory or [],
        "media_refs": args.media or [],
        "importance": args.importance,
        "next_action": (args.next_action or "").strip(),
        "preflight": bool(args.preflight or args.change_type == "preflight"),
    }
    if args.work_ref:
        record["work_refs"] = args.work_ref
    if args.accepted_file:
        record["accepted_files"] = args.accepted_file
    if args.working_file:
        record["working_files"] = args.working_file
    if args.verified:
        record["verified"] = True

    errors = validate_micro(record, target)
    if errors:
        fail("Invalid micro-checkpoint:\n- " + "\n- ".join(errors))

    atomic_write(target, json.dumps(record, ensure_ascii=False, indent=2) + "\n")

    live = load_live()
    recent = list(live.get("recent_micro_checkpoints") or [])
    recent.append(rel(target))
    recent = sorted(set(recent))[-12:]

    threads = list(live.get("active_threads") or [])
    for thread in record["thread_ids"]:
        if thread not in threads:
            threads.append(thread)

    loops = list(live.get("open_loops") or [])
    for resolved in args.resolve or []:
        loops = [item for item in loops if item != resolved]
    for item in args.open_loop or []:
        if item not in loops:
            loops.append(item)

    live.update(
        {
            "schema_version": 1,
            "owner": "romanziere",
            "kind": "romanziere_live_context",
            "updated_at": recorded_at,
            "latest_summary": record["summary"],
            "next_action": record["next_action"],
            "last_micro_checkpoint": rel(target),
            "active_threads": threads,
            "open_loops": loops,
            "recent_micro_checkpoints": recent,
            "micro_since_full_checkpoint": int(
                live.get("micro_since_full_checkpoint") or 0
            ) + 1,
        }
    )
    live["review_policy"] = dict(DEFAULT_REVIEW_POLICY)
    live.setdefault(
        "note",
        "Projection only. Append-only truth lives in "
        "micro-checkpoints/checkpoints/memories/sources.",
    )
    atomic_write(CTX, json.dumps(live, ensure_ascii=False, indent=2) + "\n")
    return target


def mark_checkpoint(path_text: str) -> None:
    path = (ROOT / path_text).resolve()
    checkpoints = (ROOT / "checkpoints").resolve()
    if checkpoints not in path.parents or not path.is_file():
        fail(f"Checkpoint must exist under checkpoints/: {path_text}")
    live = load_live()
    live["updated_at"] = now_iso()
    live["last_full_checkpoint"] = rel(path)
    live["micro_since_full_checkpoint"] = 0
    live["review_policy"] = dict(DEFAULT_REVIEW_POLICY)
    atomic_write(CTX, json.dumps(live, ensure_ascii=False, indent=2) + "\n")


def verify_live_context() -> None:
    if not CTX.is_file():
        fail("Missing rag/live/ROMANZIERE_LIVE_CONTEXT.json")
    live = load_live()

    required_live = (
        "schema_version",
        "owner",
        "kind",
        "updated_at",
        "latest_summary",
        "next_action",
        "last_micro_checkpoint",
        "last_full_checkpoint",
        "active_threads",
        "open_loops",
        "recent_micro_checkpoints",
        "micro_since_full_checkpoint",
        "review_policy",
    )
    for key in required_live:
        if key not in live:
            fail(f"Live context missing key: {key}")

    if live.get("owner") != "romanziere":
        fail("Live context owner must be romanziere")
    if live.get("kind") != "romanziere_live_context":
        fail("Live context kind must be romanziere_live_context")

    recent = list(live.get("recent_micro_checkpoints") or [])
    if len(recent) > 12:
        fail("recent_micro_checkpoints must contain at most 12 items")
    if len(recent) != len(set(recent)):
        fail("recent_micro_checkpoints contains duplicates")
    if recent != sorted(recent):
        fail("recent_micro_checkpoints must be oldest-to-newest")

    last_micro = live.get("last_micro_checkpoint")
    if last_micro:
        if not recent or recent[-1] != last_micro:
            fail("last_micro_checkpoint must equal newest recent_micro_checkpoints item")
        if not (ROOT / last_micro).is_file():
            fail(f"last_micro_checkpoint missing: {last_micro}")

    last_full = live.get("last_full_checkpoint")
    if last_full and not (ROOT / last_full).is_file():
        fail(f"last_full_checkpoint missing: {last_full}")

    policy = live.get("review_policy") or {}
    if policy.get("substantive_turn_interval") != 1:
        fail("review_policy.substantive_turn_interval must be exactly 1")

    count = 0
    v1 = 0
    v2 = 0
    seen_v2_ids: set[str] = set()
    for path in sorted(MICRO.rglob("*.json")) if MICRO.is_dir() else []:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(f"Invalid micro-checkpoint JSON {rel(path)}: {exc}")
        errors = validate_micro(record, path)
        if errors:
            fail(f"Invalid {rel(path)}:\n- " + "\n- ".join(errors))
        if record.get("schema_version") == LEGACY_MICRO_SCHEMA_VERSION:
            v1 += 1
        elif record.get("schema_version") == CURRENT_MICRO_SCHEMA_VERSION:
            v2 += 1
            micro_id = record["micro_id"]
            if micro_id in seen_v2_ids:
                fail(f"duplicate v2 micro_id: {micro_id}")
            seen_v2_ids.add(micro_id)
        count += 1

    for path_text in recent:
        if not (ROOT / path_text).is_file():
            fail(f"Recent micro-checkpoint missing: {path_text}")

    print(
        "OK: live context verified "
        f"(micro-checkpoints={count}, v1={v1}, v2={v2}, "
        f"recent={len(recent)}, since_full={live.get('micro_since_full_checkpoint')}, "
        "freshness_interval=1)."
    )


def print_status() -> None:
    print(json.dumps(load_live(), ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser(description="Romanziere frequent live-context saver")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("save-delta", help="Append a v2 micro-checkpoint and refresh live context")
    sp.add_argument("--summary", required=True)
    sp.add_argument("--change-type", choices=sorted(V2_CHANGE_TYPES), required=True)
    sp.add_argument("--event-at")
    sp.add_argument("--changed", action="append", default=[])
    sp.add_argument("--thread", action="append", default=[])
    sp.add_argument("--source", action="append", default=[])
    sp.add_argument("--memory", action="append", default=[])
    sp.add_argument("--media", action="append", default=[])
    sp.add_argument("--work-ref", action="append", default=[])
    sp.add_argument("--accepted-file", action="append", default=[])
    sp.add_argument("--working-file", action="append", default=[])
    sp.add_argument("--importance", type=int, choices=range(1, 6), default=3)
    sp.add_argument("--next", dest="next_action", default="")
    sp.add_argument("--open-loop", action="append", default=[])
    sp.add_argument("--resolve", action="append", default=[])
    sp.add_argument("--verified", action="store_true")
    sp.add_argument("--preflight", action="store_true")

    mp = sub.add_parser("mark-checkpoint", help="Point live context to a full checkpoint")
    mp.add_argument("path")

    sub.add_parser("status", help="Show current live context")
    sub.add_parser("verify", help="Verify live buffer and every legacy/current micro")

    args = ap.parse_args()
    if args.cmd == "save-delta":
        target = save_delta(args)
        print(f"Created {rel(target)}")
    elif args.cmd == "mark-checkpoint":
        mark_checkpoint(args.path)
        print(f"Marked full checkpoint: {args.path}")
    elif args.cmd == "status":
        print_status()
    elif args.cmd == "verify":
        verify_live_context()


if __name__ == "__main__":
    main()
