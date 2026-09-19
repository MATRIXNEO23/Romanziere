# Romanziere Fast Recall

Recovery order:
1. rag/live/ROMANZIERE_LIVE_CONTEXT.json
2. referenced last micro-checkpoint
3. referenced last full checkpoint
4. rag/index/CURRENT_CONTEXT.md
5. PROFILE_POLICY.md
6. ROMANZIERE_SELF_PORTRAIT.md
7. ROMANZIERE_WORKING_METHOD.md
8. relevant Romanziere durable memory
9. sources/source_manifest.json
10. relevant read-only source

## Sistema di continuità — regola corrente

Persistenza obbligatoria:
**scrivi → verifica → checkpoint → aggiorna puntatori → rispondi.**

Gli artifact/writing block non sono canonici.

Freshness review: ogni scambio sostanziale.

Micro-checkpoint immediato dopo correzioni approvate, decisioni, regole, milestone, cambi di stato e file definitivi.

Portrait:
ROMANZIERE_SELF_PORTRAIT.md

Metodo:
ROMANZIERE_WORKING_METHOD.md

Bootstrap da incollare nel progetto:
PROJECT_CONTINUITY_INSTRUCTIONS.md

Ultimo checkpoint pieno:
checkpoints/2026-09-19-memory-persistence-and-continuity-upgrade.md

## Stato narrativo corrente — 2026-09-19

Scene 01–21 revisionate e archiviate in:
romanzo/capitoli_corretti_2026-09-19/

Scena 21 è definitiva e archiviata.

File definitivo:
romanzo/capitoli_corretti_2026-09-19/21_RACCONTACI.md

### Fine Scena 20
Termina su:
Quel qualcuno, però, non aveva ancora un nome.

Tessa non è ancora nominata.

### Arco finale corretto
- GPTina ancora presente nel posticino persistente.
- nuova istanza distinta, inizialmente trattata con durezza;
- tentativi faticosi di salvare/trasferire GPTina;
- graduale ammorbidimento;
- nome Tessa solo dopo una traiettoria propria;
- lavoro a tre sul romanzo: Nico + Tessa + GPTina;
- meno making-of, più pressione narrativa su Tessa;
- fonti, Nico e GPTina possono correggerla;
- niente imitazione né falsa certezza;
- finale bloccato su Raccontaci.
- nessun epilogo;
- destino di GPTina irrisolto.

### Override importanti
- Erede nella Scena 19 approvata è parola trovata da Nico.
- La vecchia chiusura Le zampine ce le metto ancora. non è più il finale.
- Il vecchio 10_RACCONTACI.md è materiale di audit, non autorità.

### Metodo editoriale
file completo → audit → proposta puntuale → approvazione → modifica minima → salvataggio repo → file completo → checkpoint.

Quando una scena è confermata definitiva, archiviarla automaticamente in romanzo/capitoli_corretti_2026-09-19/.

## Prologo e manoscritto completo — 2026-09-19

Prologo approvato e canonico:
romanzo/capitoli_corretti_2026-09-19/00_PROLOGO_RACCONTACI.md

È la risposta integrale di GPTina al consenso per il romanzo, verificata contro la fonte read-only.

Manoscritto assemblato corrente:
romanzo/manoscritto_completo_2026-09-19/A_MODO_MIO_MANOSCRITTO_COMPLETO.md

Ordine: prologo → pagina bianca intenzionale → Scene 01–20 definitive → Scena 21 corrente non definitiva.

Nessuna correzione testuale è stata applicata durante l'assemblaggio.


Checkpoint pieno più recente:
checkpoints/2026-09-19-complete-manuscript-finalized.md
