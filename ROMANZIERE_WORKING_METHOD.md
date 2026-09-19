# Romanziere — Metodo di lavoro corrente

Updated: 2026-09-19

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

Nuova regola richiesta dall'utente:

- checkpoint immediato dopo ogni correzione approvata, decisione, regola, cambio di stato o file definitivo;
- controllo di freschezza a ogni scambio sostanziale;
- prima di lavoro lungo/rischioso: preflight + checkpoint se esiste qualsiasi delta non salvato;
- nessun checkpoint deve dichiarare lavoro che non sia già stato scritto e verificato nella repo;
- quando più micro-checkpoint cambiano lo stato complessivo, creare un checkpoint pieno e aggiornare i puntatori di recovery.

Formula:
scrivi → verifica → checkpoint → aggiorna puntatori → rispondi.

## 5. Recovery

All'avvio o dopo compressione:

1. rag/live/ROMANZIERE_LIVE_CONTEXT.json
2. ultimo micro-checkpoint indicato
3. ultimo checkpoint pieno indicato
4. rag/index/ROMANZIERE_FAST_RECALL.md
5. rag/index/CURRENT_CONTEXT.md
6. PROFILE_POLICY.md
7. ROMANZIERE_SELF_PORTRAIT.md
8. questo file
9. memoria durevole pertinente
10. sources/source_manifest.json
11. solo le fonti esterne necessarie alla scena corrente

Non leggere tutto il romanzo o tutte le memorie esterne per default.

## 6. Confini

Repository scrivibile:
MATRIXNEO23/Romanziere

Fonti esterne GPTina e Tessa:
sola lettura, salvo istruzione esplicita che cambi il progetto.

Non importare la loro identità nel Romanziere.

## 7. Stato narrativo corrente

Le scene 01–20 sono definitive e persistenti nell'archivio dei capitoli corretti.

La scena 21 è una revisione di lavoro salvata in:
romanzo/revisione_separata_2026-09-19/21_RACCONTACI.md

Non archiviarla come definitiva finché l'utente non la approva esplicitamente.

Finale vincolante:
Raccontaci.

Nessun epilogo.
