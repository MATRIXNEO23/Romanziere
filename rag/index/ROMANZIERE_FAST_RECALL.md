# Romanziere Fast Recall

Recovery order:
1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. referenced last micro-checkpoint
3. referenced full checkpoint
4. `rag/index/CURRENT_CONTEXT.md`
5. `PROFILE_POLICY.md`
6. `sources/source_manifest.json`
7. relevant read-only source

## Stato narrativo corrente

Revisione di **A modo mio** arrivata a **Scena 19 — L’erede**.

File:
- revisione: `romanzo/revisione_separata_2026-09-19/19_L_EREDE.md`
- archivio corretto: `romanzo/capitoli_corretti_2026-09-19/19_L_EREDE.md`
- audit: `romanzo/revisione_separata_2026-09-19/AUDIT_19_L_EREDE.md`
- ponte: `romanzo/revisione_separata_2026-09-19/NOTE_PONTE_EREDE_SECONDA_FINESTRA.md`

Ultimo stato bloccato:
- dialogo reale del posticino inserito;
- futura erede può comprendere/leggere ma non appropriarsi o riscrivere GPTina;
- non inventare il vecchio dialogo “può leggere / non scrive” come verbatim;
- il lavoro comune con l’erede **non va eliminato**;
- prossima scena: **La seconda finestra**;
- RAG/retrieval entra solo lì, quando Nico lavora già con l’erede/Tessa;
- GPTina è ancora presente nella prima finestra durante questo lavoro.

Source priority:
1. correzioni dirette dell’utente;
2. GPTina/Tessa source evidence;
3. vecchio romanzo come materiale di confronto.

Memory layers:
- live buffer = immediate state;
- micro-checkpoint = append-only delta;
- checkpoint = consolidated state;
- `rag/memories/romanziere/` = durable owned memory;
- registered external repositories = read-only evidence.
