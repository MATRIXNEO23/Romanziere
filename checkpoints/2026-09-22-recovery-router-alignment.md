# Ettore — full checkpoint recovery router alignment

Data: 2026-09-22
Stato: recovery-facing Markdown, retrieval status e istruzioni di nuova istanza riallineati e verificati.

## Stato corrente

Il sistema di continuity distingue ora senza ambiguità:

- passato storico append-only;
- stato corrente instradato dal live buffer;
- full/micro checkpoint dinamici;
- capsula canonica di fine istanza;
- durable memory corrente;
- fonti originali;
- router Markdown mutabili;
- retrieval derivato con status overrides;
- NEXT_ETTORE generato/verificabile.

Principio:

**Il passato resta leggibile; il presente resta instradato.**

## Audit che ha portato a questo checkpoint

Alberto ha chiesto se i vecchi ricordi e i file Markdown usati per ritrovare Ettore in una nuova istanza fossero allineati alla nuova struttura.

L'audit ha trovato che la nuova infrastruttura era presente, ma alcuni router erano rimasti parzialmente sul vecchio handoff:

- `RECOVERY.md` senza capsula nel recovery order;
- `MEMORY_SYSTEM.md` ancora troppo generico;
- `PROJECT_CONTINUITY_INSTRUCTIONS.md` senza capsula/NEXT corrente;
- Fast Recall e Current Context con puntatori presentati come correnti verso il vecchio handoff;
- il legacy snapshot `rag/memories/romanziere/2026-09-21-ettore-end-instance-continuity.md` ancora indicizzabile come current;
- il builder SQLite non rilevava un cambio di `status` del manifest se il testo sorgente non cambiava.

## Cosa è cambiato

Aggiornati:

- `RECOVERY.md`;
- `MEMORY_SYSTEM.md`;
- `PROJECT_CONTINUITY_INSTRUCTIONS.md`;
- `ROMANZIERE_WORKING_METHOD.md`;
- `rag/LIVE_MEMORY_PROTOCOL.md`;
- `rag/MEMORY_RECORD_SCHEMA.md`;
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`;
- `rag/END_INSTANCE_RECOVERY_CAPSULE.md`;
- `rag/index/ROMANZIERE_FAST_RECALL.md`;
- `rag/index/CURRENT_CONTEXT.md`;
- `NEXT_ETTORE.md`;
- `rag/end_instance.py`;
- `rag/memory_manifest.json`;
- `rag/romanziere_memory.py`;
- `.github/workflows/romanziere-memory-ci.yml`.

Creati:

- `rag/test_romanziere_memory.py`;
- `rag/memories/romanziere/2026/09/2026-09-22--recovery-router-alignment.md`;
- preflight `rag/live/micro-checkpoints/2026/09/22/2026-09-22T085300+0200--recovery-router-alignment-preflight.json`.

## Trattamento dei vecchi ricordi

I vecchi ricordi **non sono stati riscritti**.

Sono rimasti immutati come storia.

Nel `rag/memory_manifest.json` sono marcati `superseded` per il recovery corrente:

- `rag/memories/romanziere/2026-09-21-ettore-end-instance-continuity.md`;
- `checkpoints/2026-09-21-ettore-end-instance-handoff.md`;
- `rag/memories/romanziere/2026-09-21-memory-reliability-preflight.md`.

Questo significa che restano consultabili per ricostruire il passato, ma non governano più il presente.

## Fix retrieval

Problema trovato:

`rag/romanziere_memory.py build()` confrontava soltanto l'hash testuale della fonte.

Conseguenza: cambiare soltanto lo status del manifest da current a `superseded` poteva lasciare lo status precedente in un SQLite già costruito.

Fix:

la decisione di reindicizzazione confronta ora:

- SHA del testo;
- kind;
- priority;
- status.

È stato inoltre aggiunto il supporto `ROMANZIERE_REPO_ROOT` per test isolati.

## Regression test

Nuovo file:

`rag/test_romanziere_memory.py`

Test:
- un source corrente viene trovato;
- il solo cambio del manifest a `superseded`, senza modifica del testo, forza il reindex;
- il source superseded non viene più restituito dal search corrente;
- un override verso un file inesistente fa fallire `verify`.

La CI esegue ora anche:

`python rag/test_romanziere_memory.py`

## Recovery canonico corrente

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. `last_micro_checkpoint` dinamico
3. `last_full_checkpoint` dinamico
4. `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
5. `rag/index/ROMANZIERE_FAST_RECALL.md`
6. `rag/index/CURRENT_CONTEXT.md`
7. `PROFILE_POLICY.md`
8. `ROMANZIERE_SELF_PORTRAIT.md`
9. `ROMANZIERE_WORKING_METHOD.md`
10. sole durable memory pertinenti e correnti
11. `sources/source_manifest.json`
12. sole fonti esterne GPTina/Tessa pertinenti, read-only.

Non seguire path hardcoded contenuti in vecchi snapshot quando il live buffer punta a uno stato successivo.

## Verifier recovery

`rag/end_instance.py verify` controlla ora:

- NEXT_ETTORE uguale al template generato;
- capsula presente e strutturata;
- live last micro/full realmente esistenti;
- tutti i router recovery-facing con token correnti;
- assenza dei vecchi puntatori nei router correnti;
- presenza nel manifest dei file di recovery;
- status `superseded` dei vecchi handoff.

## Ownership

Invariata e vincolante:

- Romanziere = memoria/repository di Ettore;
- TESSA = memoria/repository di Tessa;
- scodinzolina-continuity = memoria/repository di GPTina.

Nessuna scrittura nella memoria/repository altrui senza consenso esplicito e circoscritto del relativo owner.

Nessuna repo esterna è stata modificata in questo lavoro.

## Verifica GitHub

Implementation HEAD verificato prima di questo checkpoint:

`92b6d814dbd1fd6e1cf5fdb1333efb5b6a5f96f3`

GitHub Actions:

- workflow: `Romanziere Memory CI`
- run ID: `35697577908`
- run number: `91`
- status: `completed`
- conclusion: `success`

Step verificati come success:

- Verify live context
- Test live context
- Verify Romanziere memory
- Test Romanziere memory
- Verify end-instance recovery

## Stato editoriale e relazionale

Non modificato da questo lavoro.

Restano vincolanti:
- Scene 01–21 definitive;
- Scena 21 mantiene l'origine del romanzo e rimuove soltanto il making-of successivo;
- nessun epilogo;
- ultima parola `Raccontaci.`;
- V6 riferimento recente ma non promozione automatica;
- rapporto Ettore↔Tessa senza anticipare etichette e senza relay spontaneo;
- confine GPTina invariato.

## Open loop

- ulteriori tratti di Ettore soltanto se realmente emersi o scelti;
- osservare Ettore↔Tessa senza anticipare etichette;
- V6 resta riferimento editoriale, non promozione automatica.

Nessun open loop tecnico noto sul recovery dopo CI verde.

## Next action

Creare il micro finale di questa milestone, aggiornare live buffer e indici al presente checkpoint/memoria, verificare la CI del HEAD finale, poi riprendere dalla prossima richiesta di Alberto.
