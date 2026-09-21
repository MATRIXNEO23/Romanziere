---
schema_version: 2
memory_id: "romanziere-2026-09-21-continuity-capsule-system-canonical"
owner: romanziere
kind: romanziere_memory
event_at: "2026-09-21T16:28:00+02:00"
recorded_at: "2026-09-21T16:42:00+02:00"
status: current
supersedes: []
event_id: "event-romanziere-continuity-capsule-system-canonical"
thread_ids: [continuity-memory, memory-reliability, workflow]
entity_refs: [Ettore, Alberto]
source_refs: [conversation://current]
media_refs: []
importance: 5
confidence: verified
tags: [continuity, recovery, checkpoint, end-instance, next-ettore]
append_only: true
---

# Continuità canonica, capsula di fine istanza e NEXT_ETTORE

Alberto ha richiesto che la continuity di Ettore sia un sistema operativo persistente, non soltanto una raccolta di note.

Ettore riconosce come vincolante la distinzione:

- **micro = cosa è cambiato**;
- **checkpoint = dove sono**;
- **memoria = perché conta**;
- **fonte = cosa è successo davvero**;
- **artifact/hash = cosa posso realmente riaprire**;
- **live buffer = da dove riparto**;
- **NEXT_ETTORE = come una nuova istanza trova tutto questo**.

La repository `MATRIXNEO23/Romanziere` resta la memoria persistente e la fonte canonica del lavoro di Ettore.

La freshness policy resta `substantive_turn_interval: 1`: a ogni scambio sostanziale Ettore valuta se esiste un delta che una futura istanza non potrebbe dedurre con sicurezza. Se non esiste, non crea rumore; se esiste, lo persiste.

Per lavoro lungo o rischioso il preflight è obbligatorio.

A fine istanza la capsula canonica è:

`rag/END_INSTANCE_RECOVERY_CAPSULE.md`

Regola scelta:

**a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile perché la nuova istanza possa riprendere Ettore e il lavoro senza ricostruire a intuito.**

`NEXT_ETTORE.md` è un entrypoint generato e verificabile, non il contenitore unico della memoria.

Il recovery deve seguire i puntatori dinamici del live buffer e recuperare soltanto le memorie/fonti pertinenti.

I micro v1 storici restano append-only; tutti i nuovi micro sono v2 strict. In v2 `changed[]` è descrittivo e non è un campo-ref.

GPTina e Tessa restano repository esterne read-only salvo autorizzazione esplicita e circoscritta di Alberto.
