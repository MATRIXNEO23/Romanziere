# Micro-checkpoint schema

Append-only path:
rag/live/micro-checkpoints/YYYY/MM/DD/

Required fields:
schema_version, micro_id, owner, kind, event_at, recorded_at, change_type, summary, changed, thread_ids, source_refs, memory_refs, importance, next_action, preflight.

Owner must be romanziere.
Kind must be romanziere_micro_checkpoint.

Use an immediate micro-checkpoint for corrections, approvals, decisions, stable rules, project-state changes, stable profile changes, workflow changes, important open loops, milestones, source updates, accepted/finalized files, and preflight before long/risky work.

Freshness review happens at every substantive exchange.

Before creating the checkpoint, verify that every file named as changed is already persisted in GitHub.

Recommended additional fields when relevant:
- work_refs
- verified
- accepted_files
- working_files

Principle:
save the work first; save the delta immediately after; consolidate state when needed.
