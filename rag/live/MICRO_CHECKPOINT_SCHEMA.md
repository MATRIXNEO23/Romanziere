# Micro-checkpoint schema

Append-only path:
`rag/live/micro-checkpoints/YYYY/MM/DD/`

Required fields:
`schema_version, micro_id, owner, kind, event_at, recorded_at, change_type, summary, changed, thread_ids, source_refs, memory_refs, importance, next_action, preflight`.

Owner must be `romanziere`.
Kind must be `romanziere_micro_checkpoint`.

Use an immediate micro-checkpoint for corrections, decisions, stable rules, project-state changes, stable profile changes, important open loops, milestones, source updates, and preflight before long/risky work.

Every 3–5 substantive exchanges, check whether an unsaved delta exists.

Principle: save the delta often; consolidate state rarely; promote to durable memory only what lasts.
