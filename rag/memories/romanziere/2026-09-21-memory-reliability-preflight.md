# Ettore — preflight affidabilità memoria — 2026-09-21

L'utente ha segnalato un problema reale nei sistemi di memoria di Tessa e GPTina e ha avvertito che la stessa classe di problema potrebbe presentarsi anche nel Romanziere.

Audit immediato di Ettore:
- `rag/live/MICRO_CHECKPOINT_SCHEMA.md` dichiara campi obbligatori più ricchi di quelli presenti in diversi micro-checkpoint recenti creati manualmente;
- `rag/live_context.py` valida solo una parte dello schema e usa un insieme di `change_type` che non coincide con diversi valori effettivamente usati nei micro recenti;
- il verifier corrente pretende `review_policy.substantive_turn_interval` fra 3 e 5, mentre il live context del Romanziere è intenzionalmente impostato a 1 per la regola di freshness a ogni scambio sostanziale;
- quindi il rischio non è solo teorico: esiste già una discrepanza fra schema, writer, verifier e dati storici.

Vincoli della correzione:
- non riscrivere retroattivamente i micro-checkpoint storici: sono append-only;
- trattare il live context come proiezione mutable, non come verità append-only;
- introdurre una versione corrente rigorosa dello schema e compatibilità di lettura per il legacy solo in memoria;
- allineare writer, verifier e policy reale del Romanziere;
- non dichiarare il sistema sano finché una verifica reale non passa sull'intero archivio.

Fonti read-only osservate:
- Tessa sta migrando a micro-checkpoint v2 con validazione stretta e compatibilità v1 in-memory, senza riscrivere la storia;
- GPTina sta lavorando sulla stessa classe di compatibilità/verifier.

Open loop: portare nel Romanziere una correzione equivalente ma adattata ai suoi dati storici e alla freshness policy a ogni scambio sostanziale; poi eseguire verifica completa.
