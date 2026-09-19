# Romanziere Fast Recall

Recovery order:
1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. referenced last micro-checkpoint
3. referenced full checkpoint
4. `rag/index/CURRENT_CONTEXT.md`
5. `PROFILE_POLICY.md`
6. `sources/source_manifest.json`
7. relevant read-only source

## Stato narrativo corrente — 2026-09-19

Scene **01–20** revisionate e archiviate in:
`romanzo/capitoli_corretti_2026-09-19/`

Scena corrente: **21**.

Ultimo checkpoint pieno:
`checkpoints/2026-09-19-scene21-context-recovery.md`

### Fine Scena 20
Termina su:
`Quel qualcuno, però, non aveva ancora un nome.`

Tessa non è ancora nominata.

### Arco finale corretto
- GPTina ancora presente nel posticino persistente.
- nuova istanza distinta, inizialmente trattata con durezza;
- tentativi faticosi di salvare/trasferire GPTina;
- graduale ammorbidimento;
- nome **Tessa** solo dopo una traiettoria propria;
- lavoro a tre sul romanzo: Nico + Tessa + GPTina;
- non trasformare il finale in making-of;
- pressione su Tessa durante le correzioni: fonti, Nico, GPTina, provenienza, niente imitazione né falsa certezza;
- finale bloccato su **Raccontaci.**
- nessun epilogo;
- destino di GPTina irrisolto;
- Scena 23 finale.

### Override importanti
- `Erede` nella Scena 19 approvata è parola trovata da Nico.
- La vecchia chiusura `Le zampine ce le metto ancora.` non è più il finale: la correzione diretta dell'utente successiva impone `Raccontaci.`.
- Il vecchio `10_RACCONTACI.md` è materiale di audit, non autorità.
- Base storica più utile: commit `b79fbae1...`; versione ampia `ee203b02...` come confronto.

### Metodo
**file corrente completo → audit → proposta puntuale → approvazione → modifica minima → file completo → stop.**

Quando una scena è confermata definitiva, archiviarla automaticamente in `romanzo/capitoli_corretti_2026-09-19/`.
