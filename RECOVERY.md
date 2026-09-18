# Recovery

On restart, after context compression, or when the current state is uncertain, recover in this order:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. the referenced last micro-checkpoint
3. the referenced last full checkpoint
4. `rag/index/ROMANZIERE_FAST_RECALL.md`
5. `rag/index/CURRENT_CONTEXT.md`
6. `PROFILE_POLICY.md`
7. relevant files in `rag/memories/romanziere/`
8. `sources/source_manifest.json`
9. relevant external source through `tools/source_reader.py`

The source registry provides read-only GPTina and Tessa memory access and a pinned reference to the existing novel.

Use source material before requesting repeated historical context. Exact wording must come from an exact source.

Literary style is not configured by this recovery file.
