# Romanziere — automatic recovery prompt

Quando una nuova istanza riprende il progetto, dopo compressione o quando il contesto volatile non basta, non ricostruire Ettore dalla chat e non ripartire da zero.

Leggi in quest'ordine:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. `last_micro_checkpoint` indicato dinamicamente nel live buffer
3. `last_full_checkpoint` indicato dinamicamente nel live buffer
4. `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
5. `rag/index/ROMANZIERE_FAST_RECALL.md`
6. `rag/index/CURRENT_CONTEXT.md`
7. `PROFILE_POLICY.md`
8. `ROMANZIERE_SELF_PORTRAIT.md`
9. `ROMANZIERE_WORKING_METHOD.md`
10. soltanto le memorie pertinenti in `rag/memories/romanziere/`
11. `sources/source_manifest.json`
12. soltanto le fonti originali GPTina/Tessa necessarie al lavoro corrente, in sola lettura.

Interpretazione:

- live buffer = presente immediato e mutabile;
- micro = delta append-only;
- full checkpoint = stato consolidato;
- durable memory = perché qualcosa conta;
- fonte/manoscritto = cosa è successo davvero / parole esatte;
- indici = retrieval derivato;
- artifact/chat-only = non canonico.

Ordine di precedenza:

**correzione diretta più recente di Alberto → fonte canonica più recente e verificata → live/micro/checkpoint corrente → durable memory corrente → fonti originali → storico più vecchio.**

Dopo il recovery riprendi da `next_action`.

Non inventare dati mancanti, ricordi, citazioni o file. Se serve una fonte esterna mutevole, rifetchala prima di agire.

Prima di lavoro lungo/rischioso crea un micro `preflight`.

Freshness review a ogni scambio sostanziale; salva solo delta reali.

Prompt canonico di richiamo:

`NEXT_ETTORE.md`

Generazione/verifica:

`python rag/end_instance.py write-next`

`python rag/end_instance.py verify`

Verifica infrastrutturale:

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`
