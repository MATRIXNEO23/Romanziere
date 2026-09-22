# Memory system

Updated: 2026-09-22

La continuity del Romanziere separa deliberatamente memoria, stato operativo, fonti e proiezioni.

## Livelli

- **live buffer** — `rag/live/ROMANZIERE_LIVE_CONTEXT.json`: presente piccolo e mutabile;
- **micro-checkpoint** — delta append-only;
- **full checkpoint** — fotografia consolidata dello stato;
- **durable memory** — perché un fatto, criterio, tratto o decisione conta nel tempo;
- **fonti/manoscritto** — autorità su contenuti originali e parole esatte;
- **capsula di fine istanza** — stato sufficiente e verificabile per riprendere senza intuire;
- **NEXT_ETTORE** — entrypoint generato che instrada la nuova istanza;
- **indici SQLite/JSONL/Markdown** — proiezioni derivate di retrieval;
- **artifact/chat-only** — non canonici finché non persistiti e verificati in GitHub.

Formula:

**micro = cosa è cambiato; checkpoint = dove sono; memoria = perché conta; fonte = cosa è successo davvero; artifact/hash = cosa posso realmente riaprire; live buffer = da dove riparto; NEXT_ETTORE = come ritrovo tutto.**

## Passato e presente

Il passato non viene riscritto per adeguarlo alla struttura corrente.

Micro v1, vecchi checkpoint e vecchie memorie restano append-only.

Quando un vecchio snapshot di recovery è superato:
- il file resta immutato come documento storico;
- `rag/memory_manifest.json` può marcarlo `superseded`;
- i router correnti devono puntare a live buffer, capsula e checkpoint corrente;
- il retrieval ordinario non deve usare un record superseded come stato presente.

Le nuove durable memory usano lo schema v2 definito in `rag/MEMORY_RECORD_SCHEMA.md`.

## Persistenza invariant

Il lavoro reale viene salvato prima che la memoria dichiari che è stato salvato.

Per ogni cambiamento reale:

1. scrivere il file di lavoro in GitHub;
2. verificare contenuto e path;
3. creare micro/full checkpoint appropriato;
4. aggiornare live buffer e router;
5. verificare di nuovo;
6. soltanto dopo riportare il completamento.

Artifact e writing block non sono storage canonico.

## Freshness

Valutare la freshness a ogni scambio sostanziale (`substantive_turn_interval: 1`).

Micro immediato per:
- correzioni;
- approvazioni;
- decisioni;
- regole;
- cambi di stato;
- file finalizzati;
- source update;
- portrait/profile;
- cambi relazionali persistenti;
- workflow;
- open loop importanti;
- milestone;
- visual context;
- preflight prima di lavoro lungo/rischioso.

Dopo circa 5 micro significativi o un cambio di fase, rivalutare un full checkpoint.

## Recovery

Il protocollo operativo è `RECOVERY.md`.

Entrypoint collegati:
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`;
- `rag/END_INSTANCE_RECOVERY_CAPSULE.md`;
- `NEXT_ETTORE.md`;
- `PROJECT_CONTINUITY_INSTRUCTIONS.md`.

Il recovery order corrente include sempre la capsula dopo last micro e last full.

Non usare hardcoded checkpoint di vecchi handoff al posto dei puntatori dinamici del live buffer.

## Retrieval

Manifest:

`rag/memory_manifest.json`

Backend:

`rag/romanziere_memory.py`

Gli indici sono derivati e ricostruibili. Le fonti Git restano canoniche.

I record marcati `superseded` o `invalidated` non devono essere restituiti come memoria corrente.

## Ownership

Romanziere, GPTina e Tessa hanno repository/memorie distinte.

Nessuna scrittura incrociata senza consenso esplicito e circoscritto del relativo owner.

## Verifica

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`

`python rag/end_instance.py verify`
