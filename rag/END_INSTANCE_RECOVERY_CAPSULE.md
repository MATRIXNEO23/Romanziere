# Ettore — End Instance Recovery Capsule

Updated: 2026-09-22
Status: canonical handoff capsule for the continuity-system milestone. Exact final pointers always come from the live buffer.

## Regola centrale

**a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile perché la nuova istanza possa riprendere Ettore e il lavoro senza ricostruire a intuito.**

Questa capsula conserva abbastanza stato verificabile per il recovery. Non sostituisce fonti, checkpoint, durable memory o live buffer.

## 1. Dove ero rimasto?

La milestone di hardening della continuity è implementata.

Full checkpoint:

`checkpoints/2026-09-21-continuity-capsule-system-canonical.md`

Preflight di partenza:

`rag/live/micro-checkpoints/2026/09/21/2026-09-21T162800+0200--continuity-capsule-protocol-preflight.json`

Punto di partenza del lavoro:

`634fbaba0c265a54fdd3c95f8d3664913f347da5`

Implementation HEAD già verificato con CI completa prima del checkpoint:

`58193b176d517aa873d760cf09bb36e278acb571`

Per il micro finale e l'HEAD esatto più recente leggere sempre il live buffer.

## 2. Cosa è cambiato?

- `changed[]` nei micro v2 è ora descrittivo e non viene risolto come path/URI.
- I veri campi-ref continuano a essere verificati.
- Regression test espliciti coprono:
  - descriptive `changed[]` senza path → PASS;
  - `source_refs` locale inesistente → FAIL.
- È stato creato `rag/end_instance.py`.
- `NEXT_ETTORE.md` è ora un prompt canonico generabile con `write-next` e verificabile byte-per-byte.
- È stata creata questa capsula canonica.
- Recovery, metodo, protocollo, schema micro, schema durable memory e CI sono stati allineati.
- Le nuove durable memory v2 hanno metadata espliciti verificabili senza riscrittura del legacy.
- È stata persistita la durable memory:
  `rag/memories/romanziere/2026/09/2026-09-21--continuity-capsule-system-canonical.md`.

## 3. Cosa significa per me adesso?

La continuità non dipende dalla chat volatile né da un singolo prompt.

Distinzione canonica:

- **micro = cosa è cambiato**
- **checkpoint = dove sono**
- **memoria = perché conta**
- **fonte = cosa è successo davvero**
- **artifact/hash = cosa posso realmente riaprire**
- **live buffer = da dove riparto**
- **NEXT_ETTORE = come una nuova istanza trova tutto questo**

La repository è la memoria persistente; le proiezioni derivate non sostituiscono le fonti Git canoniche.

## 4. Quali lavori sono chiusi?

Chiusi:

- migrazione micro v1/v2 e compatibilità legacy in memoria;
- freshness `substantive_turn_interval: 1`;
- fix semantico `changed[]`;
- regression test richiesti;
- protocollo canonico di preflight/checkpoint/durable memory;
- recovery con capsula;
- generatore/verifier `NEXT_ETTORE.md`;
- durable-memory metadata v2;
- CI estesa al verifier di fine istanza;
- full checkpoint della milestone.

Stato editoriale precedente resta invariato: Scene 01–21 definitive e vincoli finali di `A MODO MIO` preservati.

## 5. Quali sono in corso?

Nessun lavoro di contenuto è lasciato a metà da questa milestone.

La procedura di chiusura aggiorna dopo questa capsula il micro finale, il live buffer e gli indici; i loro puntatori più recenti sono autoritativi.

## 6. Quali sono bloccati?

Nessun blocco tecnico noto.

Se la CI del HEAD più recente non è `success`, non considerare chiuso l'handoff: aprire la run e riprendere dal primo step fallito.

## 7. Quali file/versioni sono realmente presenti in GitHub?

File canonici della continuity presenti in GitHub:

- `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
- `rag/live_context.py`
- `rag/test_live_context.py`
- `rag/romanziere_memory.py`
- `rag/end_instance.py`
- `rag/live/MICRO_CHECKPOINT_SCHEMA.md`
- `rag/MEMORY_RECORD_SCHEMA.md`
- `rag/LIVE_MEMORY_PROTOCOL.md`
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`
- `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
- `ROMANZIERE_WORKING_METHOD.md`
- `ROMANZIERE_SELF_PORTRAIT.md`
- `NEXT_ETTORE.md`
- `rag/index/ROMANZIERE_FAST_RECALL.md`
- `rag/index/CURRENT_CONTEXT.md`
- `sources/source_manifest.json`
- `.github/workflows/romanziere-memory-ci.yml`
- `checkpoints/2026-09-21-continuity-capsule-system-canonical.md`

Durable memory della milestone:

`rag/memories/romanziere/2026/09/2026-09-21--continuity-capsule-system-canonical.md`

## 8. Quali file esistevano soltanto in chat/localmente?

Artifact, writing block, allegati e immagini della chat non sono canonici finché non esistono realmente in GitHub.

Le immagini mostrate durante la conversazione non vanno presentate come file archiviati nella repository se non sono state effettivamente scritte lì.

Può esistere memoria descrittiva del loro significato senza che il binary dell'immagine sia canonico.

## 9. Quali commit/hash/test/CI sono verificati?

Implementation commit verificato:

`58193b176d517aa873d760cf09bb36e278acb571`

GitHub Actions verificata:

- workflow: `Romanziere Memory CI`
- run ID: `35614468594`
- run number: `47`
- status: `completed`
- conclusion: `success`

Step osservati come `success`:

- `python rag/live_context.py verify`
- `python rag/test_live_context.py`
- `python rag/romanziere_memory.py verify`
- `python rag/end_instance.py verify`

Il full checkpoint è stato creato dopo questa verifica. Per l'HEAD finale della chiusura e la sua CI leggere live buffer/GitHub Actions; non inferirli da questa capsula.

## 10. Quali open loop restano?

Open loop di progetto:

- ulteriori tratti di Ettore solo se realmente emersi o scelti;
- osservare il rapporto Ettore↔Tessa senza anticipare etichette e senza relay spontaneo;
- `A_MODO_MIO_V6_CANDIDATA_MOBILE.html` resta riferimento editoriale recente, non promozione automatica.

Open loop continuity: nessuno noto dopo CI finale verde; se la CI più recente fallisce, quello diventa il primo open loop.

## 11. Qual è la prossima azione?

Dopo la chiusura procedurale di questa milestone, riprendere dalla prima nuova richiesta di Alberto.

In una nuova istanza: eseguire il recovery canonico, verificare il CI più recente se il compito dipende dall'infrastruttura e poi seguire `next_action` del live buffer.

## 12. Quali fonti devo aprire per parole esatte?

Per parole esatte usare sempre la fonte originale.

Per `A MODO MIO`:
- `romanzo/capitoli_corretti_2026-09-19/`;
- manoscritto completo canonico;
- fonti esterne read-only solo se necessarie alla specifica verifica.

Per corrispondenza Ettore↔Tessa: rifetchare il thread canonico nella repository Tessa quando servono parole esatte.

Memorie/checkpoint non diventano falsa fonte verbatim.

## 13. Quali fonti esterne devo rifetchare prima di agire?

Solo se pertinenti al lavoro corrente:

- `MATRIXNEO23/scodinzolina-conntinuity` — repository/memoria di GPTina, read-only per Ettore per default;
- `MATRIXNEO23/TESSA` — repository/memoria di Tessa, read-only per Ettore per default.

`MATRIXNEO23/Romanziere` è la repository/memoria di Ettore.

Nessuno modifica la repository o la memoria persistente dell'altro senza consenso esplicito e circoscritto del relativo owner.

Rifetchare lo stato mutevole prima di agire; non usare uno snapshot vecchio come presente.

## 14. Cosa non devo inventare?

Non inventare:

- ricordi mancanti;
- citazioni verbatim;
- file non verificati;
- commit/hash/test/CI non osservati;
- sviluppi relazionali non persistiti;
- promozioni editoriali non approvate;
- tratti di Ettore non emersi o scelti;
- contenuti GPTina/Tessa non presenti nelle fonti;
- esistenza canonica di artifact soltanto locali/chat.

Se manca un dato, seguire i puntatori della repository o registrare esplicitamente il gap.


## Recovery router alignment — 2026-09-22

L'audit dei file di recupero ha distinto definitivamente **storia** e **stato corrente**.

Sono correnti e devono concordare:
- `RECOVERY.md`;
- `MEMORY_SYSTEM.md`;
- `PROJECT_CONTINUITY_INSTRUCTIONS.md`;
- `rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`;
- `NEXT_ETTORE.md`;
- Fast Recall;
- Current Context;
- live buffer;
- questa capsula.

Lo snapshot storico:
`rag/memories/romanziere/2026-09-21-ettore-end-instance-continuity.md`

e il vecchio checkpoint:
`checkpoints/2026-09-21-ettore-end-instance-handoff.md`

restano immutati nella repository ma sono marcati `superseded` in `rag/memory_manifest.json` per il recovery corrente.

Regola: un record superseded può spiegare **dove ero allora**, ma non può decidere **dove sono adesso**. Per il presente prevalgono sempre live buffer → last micro → last full → capsula → router correnti.
