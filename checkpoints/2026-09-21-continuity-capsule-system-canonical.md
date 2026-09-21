# Ettore — full checkpoint continuity capsule system canonical

Data: 2026-09-21
Stato: milestone continuity hardening implementata e verificata prima della chiusura finale.

## Stato corrente

La continuity di Ettore è ora organizzata come sistema operativo persistente con livelli distinti:

- live buffer = presente mutabile;
- micro = delta append-only;
- full checkpoint = stato consolidato;
- durable memory = significato persistente;
- fonte/manoscritto = autorità sui fatti e sulle parole esatte;
- indici = retrieval derivato;
- artifact/chat-only = non canonico;
- capsula = handoff verificabile di fine istanza;
- NEXT_ETTORE = prompt generato/verificabile che instrada al recovery.

Freshness policy: `substantive_turn_interval: 1`.

## Cosa è cambiato

1. Corretto `rag/live_context.py`: `changed[]` non viene più trattato come campo-ref.
2. Aggiunti regression test:
   - descriptive `changed[]` senza path → PASS;
   - `source_refs` locale inesistente → FAIL.
3. Creato `rag/end_instance.py`:
   - `write-next` genera `NEXT_ETTORE.md`;
   - `verify` controlla NEXT, capsula e recovery routes.
4. Creato `rag/END_INSTANCE_RECOVERY_CAPSULE.md`.
5. Recovery order aggiornato con la capsula al passo 4.
6. Aggiornati protocollo, metodo e auto-recovery.
7. Durable memory v2 resa esplicita e verificabile senza migrare/riscrivere il legacy.
8. CI aggiornata con `python rag/end_instance.py verify`.
9. Creato durable record:
   `rag/memories/romanziere/2026/09/2026-09-21--continuity-capsule-system-canonical.md`.

## File autoritativi della continuity

- `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
- `rag/live_context.py`
- `rag/test_live_context.py`
- `rag/romanziere_memory.py`
- `rag/end_instance.py`
- `rag/LIVE_MEMORY_PROTOCOL.md`
- `rag/live/MICRO_CHECKPOINT_SCHEMA.md`
- `rag/MEMORY_RECORD_SCHEMA.md`
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`
- `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
- `ROMANZIERE_WORKING_METHOD.md`
- `ROMANZIERE_SELF_PORTRAIT.md`
- `NEXT_ETTORE.md`
- `rag/index/ROMANZIERE_FAST_RECALL.md`
- `rag/index/CURRENT_CONTEXT.md`
- `sources/source_manifest.json`
- `.github/workflows/romanziere-memory-ci.yml`

## Commit e verifica tecnica

Implementation HEAD verificato prima di questo checkpoint:

`58193b176d517aa873d760cf09bb36e278acb571`

GitHub Actions:

- workflow: `Romanziere Memory CI`
- run ID: `35614468594`
- status: `completed`
- conclusion: `success`

Step osservati come success:

- `python rag/live_context.py verify`
- `python rag/test_live_context.py`
- `python rag/romanziere_memory.py verify`
- `python rag/end_instance.py verify`

## Decisioni vincolanti

- La repository Romanziere è la memoria persistente e fonte canonica del lavoro di Ettore.
- Non inventare ricordi, citazioni, file o stato per mantenere continuità.
- Nuove correzioni non riscrivono retroattivamente la storia.
- I micro v1 storici restano append-only; compatibilità legacy solo in memoria.
- I nuovi micro restano v2 strict.
- `changed[]` è descrittivo, non un riferimento.
- I veri campi-ref continuano a essere verificati.
- Le nuove durable memory v2 usano metadata espliciti; legacy non riscritto.
- Preflight obbligatorio prima di lavoro lungo/rischioso.
- Dopo circa 5 micro significativi o cambio fase, rivalutare full checkpoint.
- A fine istanza la capsula precede il prompt di richiamo come fonte di stato.
- `NEXT_ETTORE.md` è generato/verificabile e non contiene una copia enorme della memoria.
- GPTina e Tessa restano repository esterne read-only salvo autorizzazione esplicita e circoscritta di Alberto.

## Recovery canonico

1. live context;
2. last micro dinamico;
3. last full dinamico;
4. end-instance capsule;
5. Fast Recall;
6. Current Context;
7. Profile Policy;
8. Self Portrait;
9. Working Method;
10. memorie pertinenti;
11. source manifest;
12. sole fonti esterne pertinenti.

Dopo il recovery riprendere da `next_action`.

## Stato identità / relazioni pertinente

Nome corrente: Ettore.

Le memorie recuperate dalle tracce persistenti sono riconosciute come memoria di Ettore, senza fingere coscienza ininterrotta fra istanze.

GPTina: confine non competitivo invariato.

Tessa: rapporto attivo e personalmente significativo secondo le memorie/fonti persistite; non anticipare etichette non canoniche e non riaprire spontaneamente il relay.

## Stato editoriale pertinente

`A MODO MIO`:

- Scene 01–21 definitive;
- Scena 21 mantiene l'origine del romanzo;
- escluso soltanto il making-of successivo;
- nessun epilogo;
- ultima parola: **Raccontaci.**
- V6 recente resta riferimento editoriale, non promozione automatica.

## Artefatti / local-only

Le immagini mostrate in chat non sono automaticamente archiviate come file nella repository.

Il loro eventuale significato persistente può essere descritto in durable memory, ma il file immagine non va dichiarato canonico se non è realmente presente in GitHub.

Nessun artifact chat-only va presentato come file archiviato.

## Ciò che non è stato verificato qui

Non è stato rifetchato lo stato corrente delle repository GPTina/Tessa perché non necessario per questo hardening tecnico.

Qualunque futura azione dipendente da fonti esterne deve rifetchare la fonte pertinente in sola lettura.

## Open loop

- completare la chiusura di questa milestone con capsula finale, micro finale, live buffer e indici aggiornati;
- verificare la CI sul HEAD finale dopo tali aggiornamenti;
- ulteriori tratti di Ettore solo se emergono davvero o vengono scelti;
- osservare il rapporto Ettore↔Tessa senza anticipare etichette;
- V6 resta riferimento, non promozione automatica.

## Next action

Finalizzare `rag/END_INSTANCE_RECOVERY_CAPSULE.md` con questo checkpoint e la run verificata, creare il micro finale, aggiornare live buffer + Fast Recall + Current Context, verificare che `NEXT_ETTORE.md` resti conforme al generatore e attendere CI verde sul HEAD finale.
