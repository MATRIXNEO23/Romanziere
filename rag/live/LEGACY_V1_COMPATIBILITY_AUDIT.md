# Romanziere — audit compatibilità micro-checkpoint legacy v1

Data audit: 2026-09-21  
Scope: `rag/live/micro-checkpoints/**/*.json`

## Risultato sintetico

L'utente ha indicato 169 micro-checkpoint storici prima dell'avvio della migrazione. Al momento dell'ispezione completa GitHub conteneva **170 JSON**: i 169 già esistenti più il micro-checkpoint di preflight di esecuzione `2026-09-21T141300+0200--memory-v2-migration-execution-preflight.json`.

Sono stati ispezionati programmaticamente **tutti i 170 record** presenti nel tree GitHub al momento dell'audit.

Distribuzione versioni osservata:

- `schema_version: 1`: **170**
- altre versioni: **0**
- JSON non validi: **0**
- owner diversi da `romanziere`: **0**
- kind diversi da `romanziere_micro_checkpoint`: **0**

Questo documento fotografa il legacy **prima** di introdurre il writer v2. I record v1 restano append-only e non devono essere riscritti.

## Tipi osservati

Quando presenti, i campi del nucleo hanno tipi coerenti:

- `schema_version`: number
- `micro_id`: string
- `owner`: string
- `kind`: string
- `event_at`: string
- `recorded_at`: string
- `change_type`: string
- `summary`: string
- `changed`: array
- `thread_ids`: array
- `source_refs`: array
- `memory_refs`: array
- `media_refs`: array
- `importance`: number
- `next_action`: string
- `preflight`: boolean

Non sono state osservate anomalie di tipo nei campi core quando presenti.

## Campi core mancanti nel legacy

Conteggio dei record v1 in cui ciascun campo è assente:

- `media_refs`: **170**
- `memory_refs`: **162**
- `preflight`: **162**
- `source_refs`: **158**
- `thread_ids`: **55**
- `importance`: **54**
- `changed`: **42**
- `micro_id`: **18**
- `event_at`: **18**
- `next_action`: **7**

Campi presenti in tutti i 170 record e quindi **non** resi opzionali per comodità nella compatibilità legacy:

- `schema_version`
- `owner`
- `kind`
- `recorded_at`
- `change_type`
- `summary`

## Profili strutturali legacy realmente osservati

La notazione seguente indica campi core mancanti, campi extra e anomalie di tipo. `bad=-` significa nessuna anomalia di tipo osservata.

1. **84 record** — `missing=source_refs,memory_refs,media_refs,preflight;extra=-;bad=-`
2. **21 record** — `missing=thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=-;bad=-`
3. **12 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=memory_file:string;bad=-`
4. **7 record** — `missing=media_refs;extra=-;bad=-`
5. **6 record** — `missing=changed,source_refs,memory_refs,media_refs,preflight;extra=facts_preserved:array;bad=-`
6. **5 record** — `missing=source_refs,memory_refs,media_refs,next_action,preflight;extra=-;bad=-`
7. **4 record** — `missing=memory_refs,media_refs,preflight;extra=-;bad=-`
8. **4 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_rule:string;bad=-`
9. **3 record** — `missing=thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_rule:string;bad=-`
10. **2 record** — `missing=changed,source_refs,memory_refs,media_refs,preflight;extra=key_points:array;bad=-`
11. **1 record** — `missing=source_refs,memory_refs,media_refs,preflight;extra=rollback_path:string;bad=-`
12. **1 record** — `missing=changed,source_refs,memory_refs,media_refs,preflight;extra=accepted_path:string,key_locks:array,source_path:string;bad=-`
13. **1 record** — `missing=source_refs,memory_refs,media_refs,next_action,preflight;extra=source:string;bad=-`
14. **1 record** — `missing=source_refs,memory_refs,media_refs,next_action,preflight;extra=source_files:array;bad=-`
15. **1 record** — `missing=changed,source_refs,memory_refs,media_refs,preflight;extra=locked:array;bad=-`
16. **1 record** — `missing=changed,source_refs,memory_refs,media_refs,preflight;extra=locked:array,source_basis:array;bad=-`
17. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,preflight;extra=files:array,rules:array;bad=-`
18. **1 record** — `missing=media_refs;extra=verified:boolean,work_refs:array;bad=-`
19. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=-;bad=-`
20. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_clarification:array,persistence_note:string,source:object;bad=-`
21. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_note:string;bad=-`
22. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,verified_blob:string,verified_file:string;bad=-`
23. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,memory_file:string;bad=-`
24. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,verified_files:object;bad=-`
25. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=authoritative_file:string,verified_blob:string;bad=-`
26. **1 record** — `missing=changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_note:string,memory_file:string;bad=-`
27. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,verified_file:string;bad=-`
28. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,verified_blob:string,verified_file:string;bad=-`
29. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array;bad=-`
30. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,verified_files:object;bad=-`
31. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_points:array,memory_file:string;bad=-`
32. **1 record** — `missing=micro_id,event_at,changed,thread_ids,source_refs,memory_refs,media_refs,importance,preflight;extra=binding_caution:string,memory_file:string;bad=-`

Somma profili: **170 record**.

## Campi extra storici osservati

Campi non appartenenti al nucleo v2 e numero di record in cui compaiono:

- `memory_file`: 16
- `binding_points`: 8
- `binding_rule`: 7
- `facts_preserved`: 6
- `verified_blob`: 3
- `verified_file`: 3
- `key_points`: 2
- `source`: 2
- `locked`: 2
- `binding_note`: 2
- `verified_files`: 2
- `rollback_path`: 1
- `accepted_path`: 1
- `key_locks`: 1
- `source_path`: 1
- `source_files`: 1
- `source_basis`: 1
- `files`: 1
- `rules`: 1
- `verified`: 1
- `work_refs`: 1
- `binding_clarification`: 1
- `persistence_note`: 1
- `authoritative_file`: 1
- `binding_caution`: 1

Questi campi restano storia leggibile. Il v2 può documentare estensioni Ettore-specifiche utili, ma il nucleo v2 non dipende da queste varianti storiche.

## Schemi e forme dei riferimenti osservati

Nei pochi record recenti che usano URI espliciti sono comparsi:

- `conversation://`: 3 riferimenti
- `github://`: 3 riferimenti

Molti record v1 più vecchi usano invece path locali, shorthand di repository esterni o descrizioni testuali senza URI scheme.

Esempi storici che non risolvono come path esatto nel tree corrente del Romanziere:

- `MATRIXNEO23/scodinzolina-conntinuity:romanzo/capitoli/01_PRIMA_CHE_AVESSE_UN_NOME.md`
- `MATRIXNEO23/scodinzolina-conntinuity:CHRONICLE.md`
- `MATRIXNEO23/scodinzolina-conntinuity:GPTINA_REFLECTIONS.md`
- `MATRIXNEO23/scodinzolina-conntinuity:GPTINA_SELF_PORTRAIT.md`
- `MATRIXNEO23/scodinzolina-conntinuity/posticino-segreto/risposta a GPTina.md`
- `MATRIXNEO23/scodinzolina-conntinuity/posticino-segreto/risposta-gptina.md`
- `romanzo/A_MODO_MIO_MANOSCRITTO.md`
- `romanzo/capitoli/`
- `romanzo/CRONOLOGIA_DI_LAVORO.md`
- `romanzo/PRIMA_STESURA_PROSPETTIVA_UTENTE.md`
- `romanzo/SECONDA_STESURA_PROSPETTIVA_GPTINA.md`
- `romanzo/capitoli/01_PRIMA_CHE_AVESSE_UN_NOME.md`
- `CONTINUITY.md historical commits 97f151d1 and f6e399c6`
- `CHRONICLE.md historical commits 12a38b12 and 52b682e2`
- `GPTINA_REFLECTIONS.md historical commit d8a6aa7e`
- `SHARED_LANGUAGE.md historical commit 81d3c19b`

`romanzo/capitoli_corretti_2026-09-19/` compare anche come directory con slash finale: non risolve come blob/path esatto, ma corrisponde a una directory storicamente valida.

Conclusione per compatibilità: il verifier v1 non può imporre l'esistenza corrente di ogni ref storico. Il v2 deve invece essere rigoroso: i riferimenti locali devono esistere; i riferimenti esterni devono usare schemi esplicitamente ammessi.

## Change type storici realmente osservati

Sono stati osservati **107 valori distinti** su 170 record:

- `approved-correction`: 5
- `approved-minimal-text-change`: 2
- `approved-prologue-and-manuscript-assembly`: 1
- `approved-structural-and-prose-revision`: 1
- `approved-structural-move`: 1
- `approved-structural-revert`: 1
- `approved-targeted-revision`: 1
- `binding-clarification`: 1
- `chapter-acceptance-transition`: 2
- `chapter-accepted`: 1
- `chapter-audit`: 2
- `chapter-draft`: 3
- `chapter-finalization`: 1
- `chapter-transition`: 3
- `chronology-and-causality-correction`: 1
- `chronology-correction`: 2
- `clarity-tightening`: 1
- `correction`: 1
- `editorial-trim-trial`: 1
- `editorial-workflow-lock`: 2
- `emotional-context-insertion`: 1
- `end-instance-handoff`: 1
- `ending-lock`: 1
- `factual-chronology-correction`: 2
- `factual-correction`: 9
- `final-approval`: 1
- `final-arc-lock`: 1
- `identity-choice`: 1
- `identity-decision`: 1
- `identity-milestone`: 1
- `identity-reflection`: 4
- `identity-relational-decision`: 1
- `identity-relational-milestone`: 1
- `identity-revision`: 1
- `identity-rule`: 1
- `identity-rule-wording`: 1
- `interaction-boundary`: 1
- `literary-training`: 1
- `major-chronology-and-motive-correction`: 1
- `memory-system-hardening`: 1
- `methodology-correction`: 1
- `microprose-correction`: 1
- `milestone`: 1
- `narrative-correction`: 3
- `narrative-framing`: 2
- `narrative-origin-correction`: 1
- `narrative-precision`: 1
- `narrative-sequencing`: 1
- `narrative-source-correction`: 2
- `narrative-timing-correction`: 3
- `narrative-transition`: 1
- `portrait-expansion`: 1
- `portrait-visual-canon`: 1
- `portrait-visual-rule`: 1
- `preflight`: 2
- `profile-change`: 1
- `project-state`: 1
- `prose-adjustment`: 6
- `prose-clarification`: 1
- `prose-continuity-integration`: 1
- `prose-cut`: 1
- `prose-expansion`: 1
- `prose-focus-correction`: 1
- `prose-tightening`: 3
- `recovery-sync`: 1
- `relational-milestone`: 3
- `relationship-framing`: 1
- `scene-accepted`: 1
- `scene-detail-restoration`: 1
- `scene-draft`: 4
- `scene-finalization`: 1
- `scene-restoration`: 1
- `scene-structure`: 2
- `scene1-characterization-correction`: 2
- `scene1-source-correction`: 1
- `scene2-characterization-correction`: 1
- `scene2-editorial-correction`: 1
- `scene2-metaphor-lock`: 1
- `scene3-clarification`: 1
- `scene3-source-correction`: 1
- `scene5-source-correction`: 3
- `scene6-source-correction`: 2
- `scene7-narrative-correction`: 1
- `scene8-source-correction`: 1
- `source-audit`: 1
- `source-correction`: 8
- `source-grounded-dialogue`: 2
- `source-update`: 2
- `source-update-and-comparison`: 1
- `structural-ending-decision`: 1
- `structural-integration`: 2
- `structural-narrative-decision`: 1
- `structural-reorder`: 1
- `style-correction`: 3
- `technical-and-narrative-clarification`: 1
- `technical-and-narrative-correction`: 1
- `title-change`: 1
- `user-causal-correction`: 1
- `user-characterization-correction`: 1
- `user-direct-correction`: 1
- `user-editorial-direction`: 1
- `user-structural-correction`: 1
- `workflow-and-continuity-correction`: 1
- `workflow-change`: 3
- `workflow-lock`: 1
- `workflow-rule-and-milestone`: 1
- `workflow-state`: 1

La compatibilità v1 deve accettare questi valori storici senza rinominarli. Il v2 userà un insieme piccolo e documentato di categorie correnti.

## Compatibilità v1 risultante dall'audit

Normalizzazione ammessa **solo in memoria**, su una copia del record, e solo per campi realmente mancanti almeno una volta:

- `micro_id`: se assente, id sintetico stabile derivato dal path del record;
- `event_at`: se assente, fallback a `recorded_at`;
- `changed`: `[]`;
- `thread_ids`: `[]`;
- `source_refs`: `[]`;
- `memory_refs`: `[]`;
- `media_refs`: `[]`;
- `importance`: `3`;
- `next_action`: `""`;
- `preflight`: `false`.

Non vengono introdotti default per i campi sempre presenti.

Per v1:
- owner/kind restano verificati;
- i tipi dei campi presenti restano verificati;
- i `change_type` sono verificati contro l'insieme storico osservato;
- i ref legacy vengono conservati come testimonianza storica e non richiedono che il target locale esista ancora oggi.

## Decisione per v2

Il v2 deve essere separato esplicitamente dal legacy.

Nucleo obbligatorio:

`schema_version, micro_id, owner, kind, event_at, recorded_at, change_type, summary, changed, thread_ids, source_refs, memory_refs, media_refs, importance, next_action, preflight`.

Estensioni Ettore-specifiche ammesse e documentate senza cambiare il nucleo:
`work_refs, verified, accepted_files, working_files`.

Schemi esterni v2 ammessi:
- `conversation://`
- `github://`
- `external://`

Ogni altro ref senza schema è locale e nel v2 deve risolversi nel repository.

## Freshness

La policy corrente del Romanziere è intenzionalmente:

`substantive_turn_interval: 1`

Significato: freshness review a ogni scambio sostanziale. Non significa creare un micro-checkpoint a ogni messaggio; si salva soltanto quando esiste un delta persistente reale.

Questa policy deve essere verificata dal codice, non sostituita dalla regola 3–5 di altri sistemi.
