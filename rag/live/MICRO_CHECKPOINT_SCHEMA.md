# Romanziere — Micro-checkpoint schema v2

I micro-checkpoint sono delta append-only del contesto vivo.

Percorso canonico:

`rag/live/micro-checkpoints/YYYY/MM/DD/*.json`

## v2 — formato corrente

Tutti i nuovi micro-checkpoint devono usare `schema_version: 2`.

Campi obbligatori:

- `schema_version`
- `micro_id`
- `owner: romanziere`
- `kind: romanziere_micro_checkpoint`
- `event_at`
- `recorded_at`
- `change_type`
- `summary`
- `changed[]`
- `thread_ids[]`
- `source_refs[]`
- `memory_refs[]`
- `media_refs[]`
- `importance` (intero 1..5)
- `next_action`
- `preflight`

Estensioni documentate facoltative:

- `work_refs[]`
- `verified` (boolean)
- `accepted_files[]`
- `working_files[]`

I riferimenti locali v2 devono esistere nel repository. Schemi esterni ammessi:

- `conversation://`
- `github://`
- `external://`

Versioni sconosciute falliscono.

## Change type v2

Valori ammessi:

- `correction`
- `approval`
- `decision`
- `rule`
- `project_state`
- `profile_change`
- `relational_shift`
- `open_loop`
- `preflight`
- `milestone`
- `source_update`
- `workflow_change`
- `accepted_file`
- `visual_context`

I 107 nomi storici v1 restano leggibili tramite compatibilità legacy; non vengono rinominati.

## v1 — legacy append-only

I record storici `schema_version: 1` non vengono riscritti.

La compatibilità è applicata solo in memoria dal verifier e deriva dall'audit completo:

`rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`

Default legacy consentiti solo perché effettivamente mancanti in almeno un record:

- `micro_id`: sintetizzato stabilmente dal path
- `event_at`: fallback a `recorded_at`
- `changed: []`
- `thread_ids: []`
- `source_refs: []`
- `memory_refs: []`
- `media_refs: []`
- `importance: 3`
- `next_action: ""`
- `preflight: false`

I riferimenti legacy sono testimonianze storiche: non è richiesto che ogni target continui a esistere oggi.

## Freshness

`substantive_turn_interval: 1` è intenzionale.

Si valuta la freshness a ogni scambio sostanziale; si crea un micro soltanto quando esiste un delta persistente reale.

Ordine operativo:

**scrivi → verifica GitHub → micro/full checkpoint → aggiorna live context e indici → rispondi.**
