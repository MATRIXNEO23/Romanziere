# Live memory protocol

Recovery order: live context, last micro-checkpoint, last full checkpoint, fast recall, current context, relevant durable memory, source registry, relevant source files.

The live context is a mutable projection. Micro-checkpoints are append-only deltas.

Save a delta after meaningful state changes and before long or risky work. Otherwise review freshness every 3–5 substantive exchanges.

Create a full checkpoint when overall state changes materially or several deltas deserve consolidation. Afterward update the live context and reset the micro-checkpoint counter. Keep prior micro-checkpoints.

Do not invent missing source history.
