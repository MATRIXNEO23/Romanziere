#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("romanziere_memory.py")


class RomanziereMemoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "rag").mkdir(parents=True)
        (self.root / "memory.md").write_text(
            "alpha recovery memory\n", encoding="utf-8"
        )
        self.env = os.environ.copy()
        self.env["ROMANZIERE_REPO_ROOT"] = str(self.root)
        self.write_manifest({})

    def tearDown(self):
        self.tmp.cleanup()

    def write_manifest(self, overrides):
        manifest = {
            "version": 1,
            "sources": [
                {
                    "pattern": "memory.md",
                    "priority": 1.0,
                    "kind": "test_memory"
                }
            ],
            "rag_sources": [],
            "status_overrides": overrides,
        }
        (self.root / "rag" / "memory_manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n",
            encoding="utf-8",
        )

    def run_cmd(self, *args, expect_ok=True):
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            env=self.env,
            text=True,
            capture_output=True,
        )
        if expect_ok and proc.returncode != 0:
            self.fail(proc.stderr or proc.stdout)
        if not expect_ok and proc.returncode == 0:
            self.fail("command unexpectedly succeeded")
        return proc

    def test_status_override_reindexes_without_text_change(self):
        first = self.run_cmd("search", "alpha")
        self.assertEqual(len(json.loads(first.stdout)), 1)

        self.write_manifest(
            {
                "memory.md": {
                    "status": "superseded",
                    "reason": "test override"
                }
            }
        )

        second = self.run_cmd("search", "alpha")
        self.assertEqual(json.loads(second.stdout), [])

    def test_verify_rejects_missing_override_target(self):
        self.write_manifest(
            {
                "missing.md": {
                    "status": "superseded"
                }
            }
        )
        self.run_cmd("verify", expect_ok=False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
