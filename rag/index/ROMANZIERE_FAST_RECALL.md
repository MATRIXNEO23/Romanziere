# Romanziere Fast Recall

Recovery order:
1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. referenced last micro-checkpoint
3. referenced full checkpoint
4. `rag/index/CURRENT_CONTEXT.md`
5. `PROFILE_POLICY.md`
6. `sources/source_manifest.json`
7. relevant source through `tools/source_reader.py`

Memory layers:
- live buffer = immediate state;
- micro-checkpoint = append-only delta;
- checkpoint = consolidated state;
- `rag/memories/romanziere/` = durable owned memory;
- registered external repositories = read-only evidence.

Existing novel source is registered as `romanzo-base` and pinned to its bootstrap commit.
Literary training is not active yet.
