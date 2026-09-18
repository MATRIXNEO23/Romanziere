# Romanziere memory record schema

New durable memories use front matter with: schema_version, memory_id, owner, kind, event_at, recorded_at, status, supersedes, event_id, thread_ids, entity_refs, source_refs, media_refs, importance, confidence, tags, append_only.

Owner is `romanziere`. Kind is `romanziere_memory`.

`event_at` is when the event belongs in history. `recorded_at` is when this repository records it. Git commit time remains the authoritative record-time evidence.

Corrections create a new record and preserve the old one. Supported states: `current`, `superseded`, `invalidated`, `historical`.

External GPTina/Tessa material remains source evidence and is not converted into Romanziere-owned memory merely because it was read.

Preferred future partition: `rag/memories/romanziere/YYYY/MM/`.
