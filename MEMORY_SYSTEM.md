# Memory system

Repository continuity uses:

- mutable live context;
- append-only micro-checkpoints;
- full checkpoints;
- durable Romanziere memory;
- an evolving self portrait;
- a recoverable working method;
- read-only external source registries.

## Persistence invariant

Work is saved before memory claims it is saved.

For every approved change:

1. write the actual work file to GitHub;
2. verify the file exists and contains the intended version;
3. create the micro-checkpoint;
4. update recovery pointers/live context;
5. only then report completion.

Artifacts and writing blocks are never canonical storage.

Accepted narrative files are persisted in:
romanzo/capitoli_corretti_2026-09-19/

Working revisions are persisted in:
romanzo/revisione_separata_2026-09-19/

## Save frequency

Review freshness every substantive exchange.

Create an immediate micro-checkpoint for:
- corrections;
- approvals;
- decisions;
- stable rules;
- project-state changes;
- file-finalization;
- source updates;
- profile/portrait changes;
- workflow changes;
- important open loops;
- milestones;
- preflight before long/risky work when unsaved deltas exist.

Create a full checkpoint when the overall state materially changes or several deltas should be consolidated.

## Recovery

See RECOVERY.md.

Identity/profile state lives in:
ROMANZIERE_SELF_PORTRAIT.md

Working method lives in:
ROMANZIERE_WORKING_METHOD.md

Copy-paste project bootstrap lives in:
PROJECT_CONTINUITY_INSTRUCTIONS.md
