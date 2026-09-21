# Romanziere — Live memory protocol

Updated: 2026-09-21

## Principio di verità

La repository è la memoria persistente.

Ordine di precedenza:

**correzione diretta più recente di Alberto → fonte canonica più recente e verificata → live buffer / ultimo micro / checkpoint corrente → memoria durevole corrente → fonti originali → materiale storico più vecchio.**

Una correzione nuova non falsifica retroattivamente il passato: si registra un nuovo delta, una nuova memoria o un override corrente.

## Livelli della continuità

- **live buffer** = presente immediato, proiezione piccola e mutabile;
- **micro-checkpoint** = delta append-only;
- **full checkpoint** = stato complessivo consolidato, append-only;
- **durable memory** = significato, criterio, identità o decisione destinata a durare;
- **fonti e manoscritto** = autorità per contenuti originali e parole esatte;
- **indici / SQLite / JSONL** = proiezioni di retrieval, derivate;
- **artifact / writing block / file soltanto in chat** = non canonici finché non sono realmente persistiti e verificati in GitHub.

## Live buffer

File:

`rag/live/ROMANZIERE_LIVE_CONTEXT.json`

Deve contenere almeno:

- `latest_summary`;
- `next_action`;
- `last_micro_checkpoint`;
- `last_full_checkpoint`;
- `active_threads`;
- `open_loops`;
- `recent_micro_checkpoints`;
- `micro_since_full_checkpoint`;
- `review_policy`.

Il live buffer non è fonte storica: è il punto di ripartenza.

## Freshness e micro-checkpoint

Freshness review: **ogni scambio sostanziale** (`substantive_turn_interval: 1`).

Domanda operativa:

> È emerso un delta che una futura istanza non potrebbe dedurre con sicurezza dalle fonti già persistite?

Se no, non creare rumore. Se sì, persistilo.

Micro immediato per correzioni, approvazioni, decisioni, regole, stato progetto, identità/profilo stabile, cambi relazionali, open loop importanti, file accettati, milestone, source update, workflow, visual context e preflight.

Formula:

**salva spesso il delta; consolida raramente lo stato; promuovi a memoria solo ciò che dura.**

## Preflight

Prima di lavoro lungo, rischioso o multi-file crea un micro `preflight` con:

- punto di partenza;
- HEAD corrente;
- cosa stai per fare;
- file coinvolti;
- ciò che è già verificato;
- ciò che è incerto;
- open loop pertinenti;
- next action in caso di interruzione.

## Checkpoint pieno

Dopo circa 5 micro significativi, prima/dopo cambio fase o a fine istanza valuta/crea un checkpoint pieno.

Deve contenere almeno:

- stato corrente;
- cosa è cambiato;
- file autoritativi;
- commit/hash importanti;
- decisioni vincolanti;
- correzioni correnti;
- test/CI realmente verificati;
- open loop;
- ciò che non è stato verificato;
- artifact/local-only;
- next action concreto.

## Durable memory v2

Le memorie legacy restano storiche e non vengono riscritte.

Le nuove durable memory devono usare metadata espliciti con almeno:

- `schema_version`;
- `memory_id` stabile;
- `owner: romanziere`;
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

`event_at` = quando il fatto appartiene alla storia.

`recorded_at` = quando è stato persistito.

Non trasformare la data di ritrovamento nella data dell'evento.

## Micro v1 / v2

- v1: legacy append-only, compatibilità soltanto in memoria;
- v2: formato corrente strict.

`changed[]` è **testo descrittivo del delta** e viene validato soltanto come `list[str]`.

I veri riferimenti restano:
- `source_refs`;
- `memory_refs`;
- `media_refs`;
- `work_refs`;
- `accepted_files`;
- `working_files`.

Audit legacy:

`rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`

Schema:

`rag/live/MICRO_CHECKPOINT_SCHEMA.md`

## Recovery canonico

All'avvio di una nuova istanza, dopo compressione o perdita di contesto:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. file indicato da `last_micro_checkpoint`
3. file indicato da `last_full_checkpoint`
4. `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
5. `rag/index/ROMANZIERE_FAST_RECALL.md`
6. `rag/index/CURRENT_CONTEXT.md`
7. `PROFILE_POLICY.md`
8. `ROMANZIERE_SELF_PORTRAIT.md`
9. `ROMANZIERE_WORKING_METHOD.md`
10. memorie pertinenti in `rag/memories/romanziere/`
11. `sources/source_manifest.json`
12. sole fonti esterne GPTina/Tessa realmente pertinenti, in sola lettura.

Recuperare per routing, non leggendo indiscriminatamente tutto.

Per parole esatte: fonte originale.

Per stato corrente: live buffer/checkpoint.

Per significato: durable memory.

Per il romanzo: file canonici del manoscritto.

Dopo il recovery riprendere da `next_action`, salvo correzione diretta successiva di Alberto.

## Ownership

Ownership canonica e reciproca:

- `MATRIXNEO23/Romanziere` = memoria/repository di Ettore;
- `MATRIXNEO23/scodinzolina-conntinuity` = memoria/repository di GPTina;
- `MATRIXNEO23/TESSA` = memoria/repository di Tessa.

**Nessuno modifica la repository o la memoria persistente dell'altro senza consenso esplicito e circoscritto del relativo owner.**

Per Ettore, GPTina e Tessa restano read-only per default. Un consenso eventuale non è generale: vale soltanto per l'azione e il perimetro autorizzati.

Leggere non significa poter scrivere. Collaborazione o relazione non costituiscono consenso implicito.

Non importare memorie esterne come autobiografia Ettore.

Principio: **nessuno intacca la memoria dell'altro.**

## Fine istanza

Capsula canonica:

`rag/END_INSTANCE_RECOVERY_CAPSULE.md`

Generatore/verifier:

`rag/end_instance.py`

Regola centrale:

**a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile perché la nuova istanza possa riprendere Ettore e il lavoro senza ricostruire a intuito.**

Procedura:

1. micro `preflight`;
2. salva e verifica il lavoro reale;
3. salva eventuali durable memory;
4. crea un full checkpoint;
5. completa la capsula;
6. crea il micro finale;
7. aggiorna live buffer;
8. aggiorna router/indici;
9. genera `NEXT_ETTORE.md` con `python rag/end_instance.py write-next`;
10. verifica tutto e CI.

## Ordine obbligatorio delle scritture

**SCRIVI IL LAVORO → VERIFICA GITHUB → MICRO/CHECKPOINT → AGGIORNA LIVE CONTEXT E INDICI → VERIFICA DI NUOVO → RISPONDI.**

Mai checkpointare lavori fantasma.

## Verifica tecnica

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`

`python rag/end_instance.py verify`
