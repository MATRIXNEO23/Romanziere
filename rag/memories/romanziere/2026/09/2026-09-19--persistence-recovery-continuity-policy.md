# Memoria durevole — Persistenza, recovery e continuità del Romanziere

event_at: 2026-09-19
recorded_at: 2026-09-19T19:24:00+02:00
owner: romanziere
status: current

## Regola richiesta dall'utente

Il Romanziere deve usare la repository come memoria persistente primaria.

Il lavoro corretto non deve restare soltanto in artifact/writing block.

Ogni correzione approvata va prima salvata e verificata nella repo, poi checkpointata.

I capitoli definitivi vanno copiati automaticamente nella cartella designata:
romanzo/capitoli_corretti_2026-09-19/

I salvataggi devono essere ravvicinati:
- micro-checkpoint dopo ogni modifica approvata o cambio di stato significativo;
- freshness review a ogni scambio sostanziale;
- checkpoint pieno per consolidare cambi di stato complessivi.

Il Romanziere deve mantenere:
- ROMANZIERE_SELF_PORTRAIT.md
- ROMANZIERE_WORKING_METHOD.md
- live context e recovery indexes aggiornati.

La prossima istanza deve poter ripartire senza chiedere la storia da capo leggendo:
PROJECT_CONTINUITY_INSTRUCTIONS.md e la catena di recovery.

## Invariante

scrivi → verifica → checkpoint → aggiorna puntatori → rispondi.
