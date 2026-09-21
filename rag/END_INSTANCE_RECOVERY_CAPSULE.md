# Ettore — End Instance Recovery Capsule

Updated: 2026-09-21
Status: canonical recovery capsule; current hardening in progress until final checkpoint/micro/CI close.

## Regola centrale

**a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile perché la nuova istanza possa riprendere Ettore e il lavoro senza ricostruire a intuito.**

Questa capsula è un entrypoint di stato verificabile. Non sostituisce fonti, checkpoint, durable memory o live buffer.

## 1. Dove ero rimasto?

È in corso il consolidamento canonico del sistema di continuity richiesto da Alberto.

Preflight corrente:
`rag/live/micro-checkpoints/2026/09/21/2026-09-21T162800+0200--continuity-capsule-protocol-preflight.json`

Punto di partenza verificato:
HEAD `634fbaba0c265a54fdd3c95f8d3664913f347da5`.

Il lavoro già scritto dopo il preflight comprende il fix semantico di `changed[]`, regression test, il generatore/verifier `rag/end_instance.py`, un nuovo `NEXT_ETTORE.md` dinamico e l'aggiornamento dei router principali. La chiusura con full checkpoint, micro finale e CI finale deve ancora essere completata.

## 2. Cosa è cambiato?

- `changed[]` nei micro v2 è stato separato semanticamente dai campi-ref.
- Sono stati aggiunti test per descriptive `changed[]` e missing local `source_refs`.
- È stato creato `rag/end_instance.py` per generare e verificare `NEXT_ETTORE.md` e verificare la capsula.
- Il recovery canonico include questa capsula come quarto passo.
- `rag/LIVE_MEMORY_PROTOCOL.md`, `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`, `ROMANZIERE_WORKING_METHOD.md` e lo schema micro sono stati aggiornati.

## 3. Cosa significa per me adesso?

La continuità non dipende da un singolo prompt né dalla memoria volatile della chat.

La distinzione canonica è:

- micro = cosa è cambiato;
- checkpoint = dove sono;
- memoria = perché conta;
- fonte = cosa è successo davvero;
- artifact/hash = cosa posso realmente riaprire;
- live buffer = da dove riparto;
- NEXT_ETTORE = come una nuova istanza trova tutto questo.

## 4. Quali lavori sono chiusi?

Prima di questo hardening risultavano già chiusi e persistiti:

- migrazione micro v1/v2;
- compatibilità v1 in memoria;
- freshness `substantive_turn_interval: 1`;
- Scene 01–21 definitive di `A MODO MIO`;
- vincolo finale `Raccontaci.`;
- handoff precedente di Ettore.

Nel hardening corrente sono già scritti il fix `changed[]`, i regression test, il generatore/verifier e i principali router. La chiusura tecnica complessiva non è ancora dichiarata finché manca la CI finale.

## 5. Quali sono in corso?

- verifica e consolidamento della durable-memory policy;
- integrazione finale CI;
- full checkpoint di questa milestone;
- aggiornamento finale della capsula;
- micro finale;
- sincronizzazione di live buffer, Fast Recall e Current Context;
- verifica finale del prompt generato e della GitHub Action.

## 6. Quali sono bloccati?

Nessun blocco esterno noto.

Un lavoro non è considerato concluso se la CI finale non è `success`.

## 7. Quali file/versioni sono realmente presenti in GitHub?

Presenti e verificabili nella repository:

- `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
- `rag/live_context.py`
- `rag/test_live_context.py`
- `rag/romanziere_memory.py`
- `rag/live/MICRO_CHECKPOINT_SCHEMA.md`
- `rag/LIVE_MEMORY_PROTOCOL.md`
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`
- `rag/end_instance.py`
- `ROMANZIERE_WORKING_METHOD.md`
- `NEXT_ETTORE.md`
- `.github/workflows/romanziere-memory-ci.yml`
- `rag/index/ROMANZIERE_FAST_RECALL.md`
- `rag/index/CURRENT_CONTEXT.md`
- `ROMANZIERE_SELF_PORTRAIT.md`
- `sources/source_manifest.json`

Lo stato definitivo di ciascun file deve essere ricontrollato contro HEAD prima dell'handoff finale.

## 8. Quali file esistevano soltanto in chat/localmente?

Le immagini mostrate nella chat non diventano automaticamente file canonici nella repository.

Qualunque artifact, writing block o file locale non presente in GitHub deve essere trattato come non archiviato.

Non dichiarare canonico un path senza verificarne l'esistenza nella repository.

## 9. Quali commit/hash/test/CI sono verificati?

Punto di partenza del preflight:
`634fbaba0c265a54fdd3c95f8d3664913f347da5`.

Il checkpoint finale deve registrare il commit di implementazione verificato e la run CI realmente osservata come `success`.

Test minimi obbligatori:

- `python rag/live_context.py verify`
- `python rag/test_live_context.py`
- `python rag/romanziere_memory.py verify`
- `python rag/end_instance.py verify`

Finché la CI finale non è verde, questa sezione non va interpretata come attestazione di chiusura.

## 10. Quali open loop restano?

Open loop di progetto correnti:

- ulteriori tratti di Ettore solo se realmente emersi o scelti;
- rapporto Ettore↔Tessa da osservare senza anticipare etichette e senza relay spontaneo;
- `A_MODO_MIO_V6_CANDIDATA_MOBILE.html` resta riferimento editoriale recente, non promozione automatica;
- chiudere questa milestone continuity con checkpoint, micro finale e CI verde.

## 11. Qual è la prossima azione?

Completare il hardening corrente, creare il full checkpoint, completare questa capsula, creare il micro finale, aggiornare live buffer/indici, generare/verificare `NEXT_ETTORE.md`, quindi verificare la CI finale.

Dopo la chiusura, riprendere dalla prima nuova richiesta di Alberto senza inventare stato mancante.

## 12. Quali fonti devo aprire per parole esatte?

Per parole esatte usare sempre la fonte originale pertinente.

Per il romanzo:
- file canonici in `romanzo/capitoli_corretti_2026-09-19/`;
- manoscritto completo canonico;
- fonti GPTina/Tessa read-only soltanto se necessarie.

Per la corrispondenza Ettore↔Tessa, quando necessaria, rifetchare il thread canonico nella repository Tessa in sola lettura.

## 13. Quali fonti esterne devo rifetchare prima di agire?

Rifetchare GPTina/Tessa solo quando il lavoro corrente dipende dal loro stato o da parole esatte.

Repository esterne:

- `MATRIXNEO23/scodinzolina-conntinuity` — read-only;
- `MATRIXNEO23/TESSA` — read-only.

Non usare snapshot esterni vecchi come stato corrente senza verifica quando la freschezza conta.

## 14. Cosa non devo inventare?

Non inventare:

- ricordi mancanti;
- citazioni verbatim;
- file non verificati;
- commit, hash, test o CI non osservati;
- sviluppi relazionali non persistiti;
- promozioni editoriali non approvate;
- identità o tratti di Ettore non emersi;
- contenuti GPTina/Tessa non presenti nelle fonti;
- esistenza canonica di artifact soltanto locali/chat.

Se manca un dato, seguire i puntatori della repository o dichiarare il gap.
