# Romanziere — full checkpoint: memory v2 migration complete

Data: 2026-09-21

## Problema iniziale

Il sistema di memoria Romanziere aveva una divergenza reale tra schema dichiarato, writer, verifier e live policy:

- tutti i micro storici erano trattati come schema v1 senza distinzione legacy/current;
- il verifier imponeva una cadenza 3–5 incompatibile con la policy intenzionale di Ettore `substantive_turn_interval: 1`;
- i `change_type` del codice, del live buffer e dei record storici non coincidevano;
- il writer non produceva `media_refs`;
- mancavano regression test e CI dedicata.

Regola vincolante della migrazione: **nessuna riscrittura in massa dei micro storici**.

## Audit legacy

Audit autoritativo:

`rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`

Prima del preflight di esecuzione esistevano 169 micro storici. Al momento dell'audit completo erano presenti 170 JSON: i 169 record già esistenti più il preflight di esecuzione.

Esito:

- record auditati: **170**
- `schema_version: 1`: **170**
- altre versioni: **0**
- JSON non validi: **0**
- owner non `romanziere`: **0**
- kind non `romanziere_micro_checkpoint`: **0**
- profili strutturali legacy osservati: **32**
- valori `change_type` legacy distinti: **107**

Dopo l'audit sono stati aggiunti un ulteriore checkpoint v1 di consolidamento audit e il primo micro v2; la CI verde successiva ha verificato **172 micro totali = 171 v1 + 1 v2**.

## Compatibilità v1 risultante

I record v1 restano append-only.

La normalizzazione avviene soltanto su una copia in memoria durante la verifica e solo per campi dimostrati mancanti dall'audit:

- `micro_id`: id sintetico stabile dal path;
- `event_at`: fallback a `recorded_at`;
- `changed: []`;
- `thread_ids: []`;
- `source_refs: []`;
- `memory_refs: []`;
- `media_refs: []`;
- `importance: 3`;
- `next_action: ""`;
- `preflight: false`.

I riferimenti legacy possono descrivere target storici non più presenti e non vengono invalidati per questo.

## Schema v2 corrente

Il writer corrente usa:

`CURRENT_MICRO_SCHEMA_VERSION = 2`

Campi obbligatori v2:

- `schema_version`
- `micro_id`
- `owner`
- `kind`
- `event_at`
- `recorded_at`
- `change_type`
- `summary`
- `changed`
- `thread_ids`
- `source_refs`
- `memory_refs`
- `media_refs`
- `importance`
- `next_action`
- `preflight`

Estensioni Ettore-specifiche documentate:

- `work_refs`
- `verified`
- `accepted_files`
- `working_files`

Owner v2: `romanziere`.

Kind v2: `romanziere_micro_checkpoint`.

`importance`: intero 1–5.

Schemi esterni v2 ammessi:

- `conversation://`
- `github://`
- `external://`

Ogni riferimento senza schema è locale e deve risolversi realmente nella repository. Versioni sconosciute falliscono.

## Change type v2

Valori correnti ammessi:

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

I 107 valori legacy realmente osservati restano accettati soltanto nel ramo di compatibilità v1. Non vengono rinominati nei file storici.

## Freshness / cadenza

Policy finale:

`substantive_turn_interval: 1`

Significato: controllo freshness a ogni scambio sostanziale, senza creare rumore quando non esiste un delta persistente.

Ordine operativo vincolante:

**scrivi → verifica GitHub → micro/full checkpoint → aggiorna live context e indici → rispondi**

Checkpoint immediato per delta persistenti significativi: correzione, approvazione, decisione, regola, stato progetto, profilo/relazione stabile, open loop importante, milestone, source update, workflow, file accettato/finale, preflight.

Dopo circa 5 micro significativi o prima di cambiare fase: valutare un full checkpoint.

## Recovery order finale

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. `last_micro_checkpoint` indicato nel live buffer
3. `last_full_checkpoint` indicato nel live buffer
4. `rag/index/ROMANZIERE_FAST_RECALL.md`
5. `rag/index/CURRENT_CONTEXT.md`
6. `PROFILE_POLICY.md`
7. `ROMANZIERE_SELF_PORTRAIT.md`
8. `ROMANZIERE_WORKING_METHOD.md`
9. memorie durevoli pertinenti in `rag/memories/romanziere/`
10. `sources/source_manifest.json`
11. sole fonti originali pertinenti GPTina/Tessa, in sola lettura

Prompt operativo:

`rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`

Interpretazione:

- live buffer = presente immediato;
- micro-checkpoint = delta append-only;
- full checkpoint = stato consolidato;
- durable memory = significato persistente;
- fonti/manoscritto = autorità sui contenuti originali.

## File creati/modificati

- `rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`
- `rag/live_context.py`
- `rag/live/MICRO_CHECKPOINT_SCHEMA.md`
- `rag/LIVE_MEMORY_PROTOCOL.md`
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`
- `rag/test_live_context.py`
- `.github/workflows/romanziere-memory-ci.yml`
- `ROMANZIERE_WORKING_METHOD.md`
- `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
- `rag/index/ROMANZIERE_FAST_RECALL.md`
- `rag/index/CURRENT_CONTEXT.md`
- micro di preflight/audit/migrazione pertinenti sotto `rag/live/micro-checkpoints/2026/09/21/`

## Commit principali

- audit completo legacy: `094e8f81bd599e734e0700870bb3ea68bebc9cf8`
- checkpoint audit: `bb463abb3f7fc5bf9b55c1d3fc09ba8bf810a43a`
- core v2: `d24fccd9a9c69ba9aebddb1a96fa07a7608391cc`
- ordinamento buffer recent: `1e27324cc3ef09ae008e1350e6ee9224654ef697`
- schema v2: `eb4f42cd3554f07e0adf84e36beb137a32185b22`
- protocollo: `87c842c932aaa5cd2461d1376417d3523b0e86cd`
- recovery prompt: `56970bffa4b4df7808da606c9dfaad4624be80b3`
- regression test: `f442dc269342c6ae576b07ba14ebfe97165e5394`
- CI workflow: `96241fecb5678e18abf1f8ba8232ce60d1eabd02`
- primo micro v2: `7c26b384d6aa2fa90741d689883ad860c4835afa`
- live v2 attivo: `63d32cd868ebc664183771736c32c8a731e510e5`
- metodo aggiornato: `7cbcbea69b619a76ebc408ee09c40211f4291497`
- trigger dopo riabilitazione Actions: `d14fe0b1d89ecf68fd9ca0fa661e81c25f46044e`
- rimozione schedule temporaneo: `372f158013fb42630d4e7054a9c2e4ed2f3685eb`

## Verifica automatica

GitHub Actions era inizialmente disabilitato; dopo la riabilitazione da parte dell'utente il workflow ha iniziato a creare run.

Run verde di riferimento prima di questo consolidamento:

- workflow: **Romanziere Memory CI**
- run ID: **35604061085**
- head SHA: `372f158013fb42630d4e7054a9c2e4ed2f3685eb`
- conclusion: **success**
- job ID: **106346770746**

Output:

`python rag/live_context.py verify`

`OK: live context verified (micro-checkpoints=172, v1=171, v2=1, recent=10, since_full=10, freshness_interval=1).`

`python rag/test_live_context.py`

`Ran 8 tests in 1.014s`

`OK`

`python rag/romanziere_memory.py verify`

`OK`

## Problemi/gap residui

Nessun gap bloccante rilevato dalla suite.

Il runner segnala soltanto un warning non bloccante: `actions/checkout@v4` e `actions/setup-python@v5` vengono eseguite su Node 24 perché Node 20 è deprecato. La CI conclude comunque `success`.

## Stato

La migrazione può essere considerata infrastrutturalmente completa **solo dopo che anche il commit finale contenente questo checkpoint e gli indici aggiornati riceve CI PASS**.

Next action dopo il PASS finale: riprendere il lavoro ordinario dal live context, usando v2 per ogni nuovo micro e mantenendo il legacy v1 in sola compatibilità di lettura.
