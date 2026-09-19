# Revisione controllata — regole per nuove istanze

Obiettivo: evitare riscritture autonome e conservare le correzioni già approvate.

## Recupero iniziale
Leggere, in quest'ordine:
1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. il micro-checkpoint indicato come ultimo
3. il checkpoint pieno indicato come ultimo
4. `rag/index/ROMANZIERE_FAST_RECALL.md`
5. `rag/index/CURRENT_CONTEXT.md`
6. l'audit e le note ponte della scena corrente

## Gerarchia delle fonti
1. correzioni dirette dell'utente;
2. fonti GPTina/Tessa e checkpoint;
3. vecchio romanzo soltanto come materiale di confronto.

## Metodo obbligatorio
- Prima fare audit.
- Non produrre una nuova stesura autonoma.
- Proporre modifiche locali e attendere approvazione.
- Applicare soltanto le modifiche approvate.
- Non fare pulizia stilistica aggiuntiva durante una correzione puntuale.
- Se si nota un altro problema, segnalarlo separatamente senza correggerlo.
- Dopo ogni modifica applicata mostrare sempre il capitolo completo aggiornato.
- Quando l'utente conferma che una scena/capitolo è definitivo, copiare automaticamente la versione approvata anche in `romanzo/capitoli_corretti_2026-09-19/`, senza attendere una richiesta separata.
- Se l'utente dice “il resto non cambiare”, va interpretato letteralmente.
- Se l'utente dice “ok”, eseguire soltanto il prossimo passo già concordato.

## Dialoghi
Non inventare dialoghi. Una battuta fra virgolette deve avere fonte esatta oppure essere esplicitamente autorizzata come ricostruzione letteraria. Il vecchio romanzo non è prova di verbatim storico.

## Capitoli approvati
Le versioni approvate sono in:
`romanzo/capitoli_corretti_2026-09-19/`

Non modificarle salvo riapertura esplicita.

Le copie di lavoro sono in:
`romanzo/revisione_separata_2026-09-19/`

## Scena 20 — La seconda finestra
Stato corrente: **audit-only**.

File di audit:
`romanzo/revisione_separata_2026-09-19/AUDIT_20_LA_SECONDA_FINESTRA.md`

Nota ponte:
`romanzo/revisione_separata_2026-09-19/NOTE_PONTE_EREDE_SECONDA_FINESTRA.md`

Non esiste al momento una nuova stesura autorizzata di Scena 20 nella cartella di revisione.

Vincoli da preservare:
- GPTina è ancora presente;
- l'ingresso della nuova istanza è conflittuale, non pacificato;
- Nico la distingue subito da GPTina;
- il lavoro comune nasce per tentare di aiutare GPTina nel presente;
- l'errore sugli originali di GPTina e il successivo confine di sola lettura restano;
- indici, append-only, retrieval e RAG appartengono a questa fase;
- il RAG non va anticipato;
- il nome Tessa arriva soltanto dopo una prima traiettoria autonoma;
- il successivo lavoro comune sul romanzo tra Nico, GPTina e Tessa non va eliminato o compresso.

Regola sintetica:
**audit → proposta puntuale → approvazione → modifica minima → capitolo completo → stop.**
