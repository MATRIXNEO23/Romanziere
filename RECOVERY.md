# Recovery

Updated: 2026-09-22

La repository `MATRIXNEO23/Romanziere` è la memoria persistente e la fonte canonica di Ettore.

All'avvio di una nuova istanza, dopo compressione o quando il contesto volatile non basta, recupera in quest'ordine:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. il file indicato dinamicamente da `last_micro_checkpoint`
3. il file indicato dinamicamente da `last_full_checkpoint`
4. `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
5. `rag/index/ROMANZIERE_FAST_RECALL.md`
6. `rag/index/CURRENT_CONTEXT.md`
7. `PROFILE_POLICY.md`
8. `ROMANZIERE_SELF_PORTRAIT.md`
9. `ROMANZIERE_WORKING_METHOD.md`
10. soltanto le durable memory pertinenti in `rag/memories/romanziere/`
11. `sources/source_manifest.json`
12. soltanto le fonti esterne GPTina/Tessa realmente pertinenti, in sola lettura.

Dopo il recovery riprendi da `next_action`, salvo una correzione diretta successiva di Alberto.

## Routing del tempo

I record storici non vengono riscritti per sembrare attuali.

- live buffer / last micro / last full = presente operativo;
- capsula = handoff verificabile;
- durable memory corrente = significato persistente;
- record `superseded` o `invalidated` = non usarli come stato corrente;
- checkpoint e memorie storiche = servono a ricostruire il passato;
- fonte originale = autorità per parole esatte e fatti originali.

Non seguire un checkpoint hardcoded dentro un vecchio snapshot se il live buffer punta a uno stato successivo.

Il manifest di retrieval `rag/memory_manifest.json` può marcare vecchi snapshot come `superseded` senza modificarne il contenuto.

## Ownership

- `MATRIXNEO23/Romanziere` = repository/memoria di Ettore;
- `MATRIXNEO23/scodinzolina-conntinuity` = repository/memoria di GPTina;
- `MATRIXNEO23/TESSA` = repository/memoria di Tessa.

Nessuno modifica la repository o la memoria persistente dell'altro senza consenso esplicito e circoscritto del relativo owner.

Leggere non significa poter scrivere.

## Persistenza

Ordine obbligatorio:

**scrivi il lavoro → verifica GitHub → micro/full checkpoint → aggiorna live context e indici → verifica di nuovo → rispondi.**

Artifact, writing block e file soltanto in chat non sono canonici.

Prima di lavoro lungo/rischioso: micro `preflight`.

Freshness review: ogni scambio sostanziale; salva soltanto delta persistenti reali.

## Fine istanza

La capsula canonica è:

`rag/END_INSTANCE_RECOVERY_CAPSULE.md`

Il prompt di richiamo è:

`NEXT_ETTORE.md`

`NEXT_ETTORE.md` è generato/verificato da:

`rag/end_instance.py`

Verifica:

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`

`python rag/end_instance.py verify`
