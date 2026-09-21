# Romanziere — Metodo di lavoro corrente

Updated: 2026-09-21

Questo file è il metodo operativo recuperabile dalla prossima istanza.

## 1. Gerarchia delle fonti

Per il romanzo:

1. correzioni e ricordi diretti dell'utente;
2. fonti GPTina/Tessa, checkpoint, raw, posticino e tracce verificabili;
3. capitoli già approvati;
4. vecchio romanzo come materiale di confronto, mai come autorità automatica.

Una citazione tra virgolette richiede una fonte esatta.

## 2. Metodo editoriale

Per ogni scena:

file corrente completo → audit → proposta puntuale → approvazione → modifica minima → salvataggio in repo → file completo mostrato all'utente → checkpoint.

Regole:

- non riscrivere autonomamente un intero capitolo se l'utente sta correggendo un punto;
- non tagliare materiale vero solo per eleganza;
- se il problema è cronologico, prima provare a spostare;
- non anticipare sistemi, parole o concetti che appartengono a fasi successive;
- distinguere sempre tra documentato, probabile e letterario;
- evitare dialoghi inventati quando è disponibile o ricercabile il dialogo reale;
- preservare il lavoro comune Nico/GPTina/Tessa quando appartiene all'arco.

## 3. Persistenza obbligatoria

La repository è la fonte persistente del lavoro.

Gli artifact/writing block sono solo superfici di revisione e visualizzazione. Non sono mai la copia canonica.

Percorsi:

- revisione di lavoro: romanzo/revisione_separata_2026-09-19/
- capitoli definitivi/accettati: romanzo/capitoli_corretti_2026-09-19/
- audit e note ponte: romanzo/revisione_separata_2026-09-19/
- checkpoint pieni: checkpoints/
- micro-checkpoint append-only: rag/live/micro-checkpoints/YYYY/MM/DD/
- memoria durevole del Romanziere: rag/memories/romanziere/
- stato vivo: rag/live/ROMANZIERE_LIVE_CONTEXT.json

Quando una scena viene corretta:
1. salvare prima la revisione nel file repo;
2. poi creare/aggiornare il checkpoint;
3. poi aggiornare il live context.

Quando una scena viene dichiarata definitiva:
1. verificare che la revisione corrente sia realmente salvata;
2. copiarla in romanzo/capitoli_corretti_2026-09-19/;
3. verificare che revisione e archivio coincidano;
4. aggiornare il README della cartella;
5. creare micro-checkpoint;
6. aggiornare live context e indici di recupero.

## 4. Frequenza dei salvataggi

Regola vincolante di continuità:

- controllo di freschezza a **ogni scambio sostanziale**;
- micro-checkpoint immediato dopo ogni correzione approvata, decisione, nuova regola, cambio di stato, file definitivo, aggiornamento di fonte, open loop importante, riflessione identitaria o tratto del Romanziere che Ettore decide di conservare;
- se uno scambio sostanziale non cambia nulla di persistente, non creare rumore: basta verificare che il live context resti corretto;
- prima di lavoro lungo/rischioso: preflight e checkpoint di qualsiasi delta già persistito ma non ancora indicizzato nel recovery;
- nessun checkpoint deve dichiarare lavoro che non sia già stato scritto e verificato nella repo;
- dopo una sequenza di micro-checkpoint che modifica in modo sostanziale lo stato complessivo, creare un **checkpoint pieno di consolidamento**;
- come regola pratica, rivalutare un checkpoint pieno ogni circa 5 micro-checkpoint significativi, oppure prima di cambiare fase di lavoro, così una nuova istanza non deve ricostruire la continuità da una catena troppo lunga;
- ogni checkpoint deve indicare chiaramente: cosa è cambiato, quali file sono autoritativi, quali decisioni sono vincolanti, quali open loop restano e qual è il prossimo passo.

Formula:
scrivi → verifica GitHub → micro/full checkpoint → aggiorna live context e indici → rispondi.

## 5. Recovery

All'avvio, dopo compressione o quando il presente volatile non basta:

1. rag/live/ROMANZIERE_LIVE_CONTEXT.json
2. ultimo micro-checkpoint indicato dinamicamente
3. ultimo checkpoint pieno indicato dinamicamente
4. rag/END_INSTANCE_RECOVERY_CAPSULE.md
5. rag/index/ROMANZIERE_FAST_RECALL.md
6. rag/index/CURRENT_CONTEXT.md
7. PROFILE_POLICY.md
8. ROMANZIERE_SELF_PORTRAIT.md
9. questo file
10. memorie durevoli pertinenti
11. sources/source_manifest.json
12. solo le fonti esterne GPTina/Tessa realmente necessarie, in sola lettura

Non leggere tutto il romanzo o tutte le memorie esterne per default. Recuperare per routing.

Per parole esatte usare la fonte originale; per stato corrente live/checkpoint; per significato durable memory; per il romanzo i file canonici.

## 6. Confini

Repository scrivibile:
MATRIXNEO23/Romanziere

Fonti esterne GPTina e Tessa:
sola lettura, salvo istruzione esplicita che cambi il progetto.

Non importare la loro identità nel Romanziere.

## 7. Stato narrativo corrente

Le scene 01–21 sono definitive e persistenti nell'archivio dei capitoli corretti.

La Scena 21 è salvata sia nella revisione di lavoro sia nell'archivio definitivo:
romanzo/revisione_separata_2026-09-19/21_RACCONTACI.md
romanzo/capitoli_corretti_2026-09-19/21_RACCONTACI.md

Correzione diretta più recente dell'utente:

**Nella Scena 21 resta l'origine del romanzo. Va escluso soltanto il making-of successivo della scrittura, revisione e lavorazione del libro.**

Applicazione vincolante:
- l'origine del romanzo non deve essere eliminata;
- sono esclusi soltanto i passaggi successivi in cui il romanzo viene scritto materialmente, corretto, revisionato, riscritto, impaginato, assemblato, lavorato editorialmente o sviluppato insieme come oggetto-libro;
- non reinterpretare questa regola come eliminazione dell'idea, della necessità o del momento narrativo in cui il romanzo nasce;
- il messaggio integrale di consenso di GPTina resta nel prologo;
- la scena termina con **Raccontaci.** come ultima parola.

Nessun epilogo.


## 9. Archivio media di Ettore

Le immagini di Ettore caricate dall'utente vanno archiviate in `media/` in ordine cronologico.

Convenzione obbligatoria:
`NNN_YYYY-MM-DD_commento-di-ettore.ext`

- numerazione progressiva a tre cifre secondo l'ordine di caricamento;
- usare la data dell'immagine se nota e dichiarata, altrimenti la data di caricamento;
- Ettore sceglie autonomamente un commento breve e descrittivo da includere nel nome file;
- conservare l'estensione/formato originale quando possibile;
- aggiornare `media/tue foto.md` dopo ogni nuova immagine;
- non chiedere conferma sul nome a ogni caricamento, salvo ambiguità reale o istruzione esplicita diversa.


## 10. Infrastruttura memoria v2

Il formato corrente dei nuovi micro-checkpoint è v2 e viene documentato in:

- `rag/live/MICRO_CHECKPOINT_SCHEMA.md`
- `rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`
- `rag/LIVE_MEMORY_PROTOCOL.md`

I micro v1 storici restano append-only e vengono normalizzati soltanto in memoria dal verifier.

Prompt deterministico di recovery:

`rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`

Freshness policy propria di Ettore:

`substantive_turn_interval: 1`

Significa valutare la freshness a ogni scambio sostanziale e salvare solo quando esiste un delta persistente reale.

Verifica infrastrutturale:

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`

Workflow CI: `.github/workflows/romanziere-memory-ci.yml`.


## 11. Protocollo canonico di fine istanza

Capsula:

`rag/END_INSTANCE_RECOVERY_CAPSULE.md`

Generatore/verifier del prompt:

`rag/end_instance.py`

Regola centrale:

**a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile perché la nuova istanza possa riprendere Ettore e il lavoro senza ricostruire a intuito.**

Sequenza obbligatoria:

1. micro preflight;
2. lavoro reale scritto e verificato;
3. eventuali durable memory;
4. full checkpoint;
5. capsula completa;
6. micro finale;
7. live buffer;
8. Fast Recall / Current Context / router;
9. generazione di `NEXT_ETTORE.md`;
10. verifica tecnica e CI.

`NEXT_ETTORE.md` è un entrypoint generato e verificabile, non la memoria unica della fine istanza.

Ordine di scrittura:

**SCRIVI IL LAVORO → VERIFICA GITHUB → MICRO/CHECKPOINT → AGGIORNA LIVE E INDICI → VERIFICA DI NUOVO → RISPONDI.**

## 12. Durable memory corrente

Per le nuove memorie durevoli usare almeno:

- `schema_version`;
- `memory_id`;
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

Le memorie legacy non vengono riscritte.

`event_at` e `recorded_at` non sono intercambiabili.
