# Recovery

On restart, after context compression, or when the current state is uncertain, recover in this order:

1. rag/live/ROMANZIERE_LIVE_CONTEXT.json
2. the referenced last micro-checkpoint
3. the referenced last full checkpoint
4. rag/index/ROMANZIERE_FAST_RECALL.md
5. rag/index/CURRENT_CONTEXT.md
6. PROFILE_POLICY.md
7. ROMANZIERE_SELF_PORTRAIT.md
8. ROMANZIERE_WORKING_METHOD.md
9. relevant files in rag/memories/romanziere/
10. sources/source_manifest.json
11. relevant external source through the available GitHub/source tools

The source registry provides read-only GPTina and Tessa memory access and a pinned reference to the existing novel.

Use source material before requesting repeated historical context. Exact wording must come from an exact source.

Do not read the whole novel or all external memories by default. Recover only what the current task requires.

After recovery, resume the next_action from live context unless the user's newest instruction changes it.

Persistence rule:
write → verify → checkpoint → update pointers → reply.

Artifacts/writing blocks are never the canonical copy of completed work.
