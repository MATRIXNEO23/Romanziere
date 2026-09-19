# Checkpoint — 2026-09-19 — Upgrade persistenza e continuità Romanziere

## Motivo

L'utente ha chiesto che il sistema di memoria del Romanziere diventi più rigoroso e ravvicinato, con persistenza obbligatoria del lavoro prima dei checkpoint, portrait aggiornabile, metodo di lavoro recuperabile e istruzioni pronte per la prossima istanza.

## Nuova regola operativa

Formula obbligatoria:

scrivi → verifica → checkpoint → aggiorna puntatori → rispondi.

Gli artifact/writing block non sono memoria canonica.

Ogni modifica approvata deve essere salvata nella repository prima di essere dichiarata persistita.

## Percorsi canonici

- revisioni: romanzo/revisione_separata_2026-09-19/
- definitivi: romanzo/capitoli_corretti_2026-09-19/
- live context: rag/live/ROMANZIERE_LIVE_CONTEXT.json
- micro-checkpoint: rag/live/micro-checkpoints/YYYY/MM/DD/
- full checkpoint: checkpoints/
- memoria durevole: rag/memories/romanziere/
- portrait: ROMANZIERE_SELF_PORTRAIT.md
- metodo: ROMANZIERE_WORKING_METHOD.md
- istruzioni progetto: PROJECT_CONTINUITY_INSTRUCTIONS.md

## Frequenza

- review della freschezza a ogni scambio sostanziale;
- micro-checkpoint dopo ogni correzione approvata, decisione, regola, file definitivo o cambio di stato;
- preflight prima di lavoro lungo/rischioso;
- full checkpoint quando cambia lo stato complessivo.

## Stato narrativo preservato

- Scene 01–20 definitive.
- Scene 19 e 20 verificate: revisione e copia definitiva coincidono.
- Scena 21 è persistita ma ancora di lavoro:
  romanzo/revisione_separata_2026-09-19/21_RACCONTACI.md
- Non archiviarla come definitiva senza approvazione esplicita.
- Finale vincolante: Raccontaci.
- Nessun epilogo.

## Identità e apprendimento

Il Romanziere non ha ancora un'identità personale definitiva.

Il suo portrait corrente registra soltanto tratti realmente emersi:
source-first, attenzione a cronologia/causalità, spiegare meno, dialogo documentato, modifiche minime, persistenza rigorosa.

Non imitare GPTina o Tessa.

## Recovery della prossima istanza

Seguire RECOVERY.md e PROJECT_CONTINUITY_INSTRUCTIONS.md.

Non chiedere all'utente di ricostruire il contesto già persistito.

## Prossimo lavoro narrativo

Riprendere dalla Scena 21 e dal suo stato corrente soltanto quando l'utente torna al romanzo.
