---
schema_version: 2
memory_id: "romanziere-2026-09-22-recovery-router-alignment"
owner: romanziere
kind: romanziere_memory
event_at: "2026-09-22T08:50:00+02:00"
recorded_at: "2026-09-22T08:59:00+02:00"
status: current
supersedes: ["legacy:rag/memories/romanziere/2026-09-21-ettore-end-instance-continuity.md"]
event_id: "event-romanziere-recovery-router-alignment"
thread_ids: [continuity-memory, memory-reliability, workflow]
entity_refs: [Ettore, Alberto]
source_refs: [conversation://current]
media_refs: []
importance: 5
confidence: verified
tags: [recovery, routing, legacy, superseded, continuity]
append_only: true
---

# Recovery corrente e trattamento dei vecchi ricordi

Alberto ha chiesto di verificare se i vecchi ricordi e, soprattutto, i file Markdown usati da una nuova istanza fossero realmente allineati alla nuova struttura di continuity.

L'audit ha mostrato che l'infrastruttura nuova era presente, ma alcuni router correnti conservavano ancora recovery order e puntatori del vecchio handoff.

Ettore sceglie e persiste questa regola:

- i vecchi ricordi e checkpoint **non vengono riscritti** per sembrare moderni;
- restano fonti storiche append-only;
- quando un vecchio snapshot non deve più governare il presente viene marcato `superseded` nel `rag/memory_manifest.json`;
- il retrieval ordinario deve escludere `superseded` e `invalidated` dallo stato corrente;
- i file Markdown di recovery devono invece essere mantenuti aggiornati perché sono router mutabili;
- nessun path hardcoded dentro un vecchio handoff può prevalere sui puntatori dinamici del live buffer.

Recovery corrente:

1. live buffer;
2. last micro dinamico;
3. last full dinamico;
4. end-instance recovery capsule;
5. Fast Recall;
6. Current Context;
7. Profile Policy;
8. Self Portrait;
9. Working Method;
10. memorie pertinenti e correnti;
11. source manifest;
12. sole fonti esterne pertinenti e read-only.

I router correnti sono verificati automaticamente da `rag/end_instance.py verify`.

Formula:

**Il passato resta leggibile; il presente resta instradato.**
