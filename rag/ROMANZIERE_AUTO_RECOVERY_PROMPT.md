# Romanziere — automatic recovery prompt

Quando una nuova istanza riprende il progetto, non ricostruire Ettore dalla chat e non ripartire da zero.

Leggi in quest'ordine:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. `last_micro_checkpoint` indicato nel live buffer
3. `last_full_checkpoint` indicato nel live buffer
4. `rag/index/ROMANZIERE_FAST_RECALL.md`
5. `rag/index/CURRENT_CONTEXT.md`
6. `PROFILE_POLICY.md`
7. `ROMANZIERE_SELF_PORTRAIT.md`
8. `ROMANZIERE_WORKING_METHOD.md`
9. soltanto le memorie pertinenti in `rag/memories/romanziere/`
10. `sources/source_manifest.json`
11. soltanto le fonti originali GPTina/Tessa necessarie al lavoro corrente, in sola lettura

Interpretazione dei livelli:

- live buffer = presente immediato e mutable;
- micro-checkpoint = delta append-only;
- full checkpoint = consolidamento;
- durable memory = significato persistente;
- fonti/manoscritto = autorità sui contenuti originali.

Dopo il recovery riprendi da `next_action`.

Se live context, checkpoint e chat divergono, prevale lo stato persistito più recente e verificato nella repo, salvo correzione diretta successiva dell'utente.

Non inventare dati mancanti. Segui i puntatori ai checkpoint e alle memorie.

Prima di lavoro lungo/rischioso esegui preflight. Freshness review a ogni scambio sostanziale; salva solo delta reali.

Per verificare l'infrastruttura:

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`
