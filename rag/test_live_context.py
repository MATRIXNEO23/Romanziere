#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("live_context.py")


class LiveContextTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "rag" / "live" / "micro-checkpoints").mkdir(parents=True)
        (self.root / "checkpoints").mkdir(parents=True)
        (self.root / "checkpoints" / "base.md").write_text("# base\n", encoding="utf-8")
        live = {
            "schema_version": 1,
            "owner": "romanziere",
            "kind": "romanziere_live_context",
            "updated_at": "2026-09-21T00:00:00+02:00",
            "latest_summary": "",
            "next_action": "",
            "last_micro_checkpoint": None,
            "last_full_checkpoint": "checkpoints/base.md",
            "active_threads": [],
            "open_loops": [],
            "recent_micro_checkpoints": [],
            "micro_since_full_checkpoint": 0,
            "review_policy": {
                "substantive_turn_interval": 1,
                "immediate_triggers": [],
                "preflight_before_long_or_risky_work": True,
                "work_must_be_persisted_before_checkpoint": True,
                "artifact_is_never_canonical": True,
                "full_checkpoint_review_after_significant_micro_checkpoints": 5,
            },
        }
        self.live_path = self.root / "rag" / "live" / "ROMANZIERE_LIVE_CONTEXT.json"
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        self.env = os.environ.copy()
        self.env["ROMANZIERE_REPO_ROOT"] = str(self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def run_cmd(self, *args, expect_ok=True):
        p = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            env=self.env,
            text=True,
            capture_output=True,
        )
        if expect_ok and p.returncode != 0:
            self.fail(f"command failed: {p.stderr or p.stdout}")
        if not expect_ok and p.returncode == 0:
            self.fail("command unexpectedly succeeded")
        return p

    def make_valid_v2(self, **overrides):
        rec = {
            "schema_version": 2,
            "micro_id": "romanziere-micro-test",
            "owner": "romanziere",
            "kind": "romanziere_micro_checkpoint",
            "event_at": "2026-09-21T00:00:00+02:00",
            "recorded_at": "2026-09-21T00:00:00+02:00",
            "change_type": "decision",
            "summary": "test delta",
            "changed": [],
            "thread_ids": ["test"],
            "source_refs": ["conversation://test"],
            "memory_refs": [],
            "media_refs": [],
            "importance": 3,
            "next_action": "",
            "preflight": False,
        }
        rec.update(overrides)
        return rec

    def write_micro(self, name, rec):
        p = self.root / "rag" / "live" / "micro-checkpoints" / "2026" / "09" / "21" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
        return p

    def test_save_delta_creates_complete_v2_and_updates_live(self):
        (self.root / "work.txt").write_text("x", encoding="utf-8")
        p = self.run_cmd(
            "save-delta",
            "--summary", "decision test",
            "--change-type", "decision",
            "--changed", "work.txt",
            "--thread", "test",
            "--next", "continue",
        )
        self.assertIn("Created rag/live/micro-checkpoints/", p.stdout)
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        micro = json.loads((self.root / live["last_micro_checkpoint"]).read_text(encoding="utf-8"))
        required = {
            "schema_version","micro_id","owner","kind","event_at","recorded_at",
            "change_type","summary","changed","thread_ids","source_refs",
            "memory_refs","media_refs","importance","next_action","preflight"
        }
        self.assertEqual(micro["schema_version"], 2)
        self.assertTrue(required.issubset(micro))
        self.assertEqual(live["recent_micro_checkpoints"][-1], live["last_micro_checkpoint"])

    def test_recent_micro_checkpoints_limited_and_last_is_newest(self):
        for i in range(14):
            self.run_cmd(
                "save-delta",
                "--summary", f"delta {i}",
                "--change-type", "decision",
            )
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        self.assertEqual(len(live["recent_micro_checkpoints"]), 12)
        self.assertEqual(live["recent_micro_checkpoints"][-1], live["last_micro_checkpoint"])

    def test_mark_checkpoint_updates_full_and_resets_counter(self):
        target = self.root / "checkpoints" / "new.md"
        target.write_text("# new\n", encoding="utf-8")
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        live["micro_since_full_checkpoint"] = 9
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        self.run_cmd("mark-checkpoint", "checkpoints/new.md")
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        self.assertEqual(live["last_full_checkpoint"], "checkpoints/new.md")
        self.assertEqual(live["micro_since_full_checkpoint"], 0)

    def test_legacy_profile_from_audit_is_accepted_without_rewrite(self):
        legacy = {
            "schema_version": 1,
            "owner": "romanziere",
            "kind": "romanziere_micro_checkpoint",
            "recorded_at": "2026-09-21T00:00:00+02:00",
            "change_type": "identity-reflection",
            "summary": "legacy observed shape",
            "next_action": "continue",
            "memory_file": "rag/memories/romanziere/example.md",
        }
        p = self.write_micro("legacy.json", legacy)
        before = p.read_bytes()
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        self.run_cmd("verify")
        self.assertEqual(before, p.read_bytes())

    def test_incomplete_v2_is_rejected(self):
        rec = self.make_valid_v2()
        rec.pop("media_refs")
        p = self.write_micro("bad-v2.json", rec)
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        self.run_cmd("verify", expect_ok=False)

    def test_invalid_v2_change_type_is_rejected(self):
        rec = self.make_valid_v2(change_type="factual-correction")
        p = self.write_micro("bad-change.json", rec)
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        self.run_cmd("verify", expect_ok=False)

    def test_freshness_interval_one_passes(self):
        p = self.write_micro("ok.json", self.make_valid_v2())
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        result = self.run_cmd("verify")
        self.assertIn("freshness_interval=1", result.stdout)

    def test_descriptive_changed_without_path_passes(self):
        description = "corretta la semantica del finale"
        self.assertFalse((self.root / description).exists())
        rec = self.make_valid_v2(changed=[description])
        p = self.write_micro("descriptive-changed.json", rec)
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        result = self.run_cmd("verify")
        self.assertIn("freshness_interval=1", result.stdout)

    def test_missing_local_source_ref_in_v2_fails(self):
        missing_ref = "path/che/non/esiste.md"
        self.assertFalse((self.root / missing_ref).exists())
        rec = self.make_valid_v2(source_refs=[missing_ref])
        p = self.write_micro("missing-source-ref.json", rec)
        live = json.loads(self.live_path.read_text(encoding="utf-8"))
        rel = p.relative_to(self.root).as_posix()
        live["last_micro_checkpoint"] = rel
        live["recent_micro_checkpoints"] = [rel]
        self.live_path.write_text(json.dumps(live, indent=2) + "\n", encoding="utf-8")
        result = self.run_cmd("verify", expect_ok=False)
        self.assertIn(
            "source_refs missing local ref: path/che/non/esiste.md",
            result.stderr or result.stdout,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
