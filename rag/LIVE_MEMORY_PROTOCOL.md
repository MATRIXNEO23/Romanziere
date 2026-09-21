# Romanziere — Live memory protocol

## Modello di continuità

- **live buffer** = presente immediato, proiezione mutable;
- **micro-checkpoint** = delta append-only;
- **full checkpoint** = stato consolidato;
- **durable memory** = significato/decisione che deve restare;
- **fonti e manoscritto** = autorità per contenuti originali.

Non riscrivere i micro storici per uniformarli a uno schema nuovo.

## Recovery order

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. file indicato da `last_micro_checkpoint`
3. file indicato da `last_full_checkpoint`
4. `rag/index/ROMANZIERE_FAST_RECALL.md`
5. `rag/index/CURRENT_CONTEXT.md`
6. `PROFILE_POLICY.md`
7. `ROMANZIERE_SELF_PORTRAIT.md`
8. `ROMANZIERE_WORKING_METHOD.md`
9. memorie durevoli pertinenti in `rag/memories/romanziere/`
10. `sources/source_manifest.json`
11. sole fonti originali pertinenti

Prompt operativo di recovery:

`rag/ROMANZIERE_AUTO_RECOVERY_PROMPT.md`

## Save frequency

Freshness review: **ogni scambio sostanziale** (`substantive_turn_interval: 1`).

Micro immediato quando cambia davvero qualcosa di persistente:

- correzione importante;
- approvazione;
- decisione;
- regola;
- stato progetto;
- profilo/identità stabile;
- relazione stabile;
- open loop importante;
- milestone;
- source update;
- workflow;
- file accettato/definitivo;
- preflight prima di lavoro lungo o rischioso.

Non creare rumore se non esiste un delta.

Dopo circa 5 micro-checkpoint significativi, o prima di un cambio fase, rivalutare un full checkpoint.

## Invariante di ordinamento

Un checkpoint può descrivere soltanto lavoro già scritto e verificato in GitHub.

**scrivi → verifica GitHub → checkpoint → aggiorna live context/indici → rispondi**

Gli artifact e i writing block non sono canonici.

## Versioni micro

- v1: legacy append-only, compatibilità di lettura in memoria;
- v2: formato corrente rigoroso.

Audit legacy:

`rag/live/LEGACY_V1_COMPATIBILITY_AUDIT.md`

Schema:

`rag/live/MICRO_CHECKPOINT_SCHEMA.md`
