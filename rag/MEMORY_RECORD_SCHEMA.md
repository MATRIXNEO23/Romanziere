# Romanziere memory record schema

Updated: 2026-09-21

Le memorie storiche legacy restano append-only e non vengono riscritte.

Le nuove durable memory usano front matter schema v2 con almeno:

- `schema_version`;
- `memory_id` stabile;
- `owner`;
- `kind`;
- `event_at`;
- `recorded_at`;
- `status`;
- `supersedes`;
- `event_id`;
- `thread_ids`;
- `source_refs`;
- `media_refs`;
- `importance`;
- `confidence`.

Campi raccomandati già usati dal Romanziere:

- `entity_refs`;
- `tags`;
- `append_only`.

Owner corrente: `romanziere`.

Kind corrente: `romanziere_memory`.

`event_at` = quando il fatto appartiene alla storia.

`recorded_at` = quando la repository registra la memoria.

La data di ritrovamento non sostituisce la data dell'evento.

Correzioni e override producono un nuovo record; non si falsifica retroattivamente una memoria storica.

Stati supportati:

- `current`;
- `superseded`;
- `invalidated`;
- `historical`.

Le fonti GPTina/Tessa restano evidenza esterna read-only e non diventano autobiografia Ettore solo perché vengono lette.

Percorso preferito per nuove memorie:

`rag/memories/romanziere/YYYY/MM/`

Il verifier `rag/romanziere_memory.py verify` valida i metadata delle memorie che dichiarano `schema_version: 2`, mantenendo compatibilità con il corpus legacy non migrato.

Per record legacy che non hanno front matter v2, lo stato corrente può essere espresso senza riscrivere il file tramite `rag/memory_manifest.json -> status_overrides`.

Un override `superseded` significa: il record resta parte della storia ma non governa più il presente né il recovery corrente.
