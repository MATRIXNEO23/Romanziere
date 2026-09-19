# Live memory protocol

Recovery order: live context, last micro-checkpoint, last full checkpoint, fast recall, current context, profile policy, self portrait, working method, relevant durable memory, source registry, relevant source files.

The live context is a mutable projection. Micro-checkpoints are append-only deltas.

## Save frequency

Review freshness at every substantive exchange.

Create an immediate micro-checkpoint after every:
- user correction;
- approved edit;
- decision;
- stable rule;
- project-state change;
- accepted/finalized file;
- source update;
- workflow/profile update;
- important open loop or milestone.

Before long or risky work, checkpoint any unsaved delta first.

## Ordering invariant

A checkpoint may only describe work that has already been written and verified in the repository.

Use:
write actual file → verify → micro-checkpoint → update live context → respond.

When an artifact/writing block is edited, persist the corresponding repo file before treating the edit as durable.

When a scene becomes definitive, copy it to:
romanzo/capitoli_corretti_2026-09-19/
and verify equality with the approved revision.

Create a full checkpoint when overall state changes materially or several deltas deserve consolidation. Afterward update the live context and recovery indexes. Keep all prior micro-checkpoints.

Do not invent missing source history.
