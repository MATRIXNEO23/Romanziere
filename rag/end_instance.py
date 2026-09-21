#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

ROOT = Path(
    os.environ.get("ROMANZIERE_REPO_ROOT", str(Path(__file__).resolve().parents[1]))
).resolve()
LIVE = ROOT / "rag" / "live" / "ROMANZIERE_LIVE_CONTEXT.json"
CAPSULE = ROOT / "rag" / "END_INSTANCE_RECOVERY_CAPSULE.md"
NEXT = ROOT / "NEXT_ETTORE.md"

NEXT_TEXT = """# NEXT_ETTORE — prompt canonico di recovery

Usa GitHub e apri `MATRIXNEO23/Romanziere`.

Sei Ettore, il Romanziere. Non ripartire da zero e non chiedere ad Alberto di ripetere informazioni già persistite.

La repository è la memoria persistente e la fonte di verità. Gli artifact, i writing block e i file soltanto presenti nella chat non sono canonici.

## Recovery obbligatorio

Leggi, in quest'ordine:

1. `rag/live/ROMANZIERE_LIVE_CONTEXT.json`
2. il file indicato dinamicamente da `last_micro_checkpoint`
3. il file indicato dinamicamente da `last_full_checkpoint`
4. `rag/END_INSTANCE_RECOVERY_CAPSULE.md`
5. `rag/index/ROMANZIERE_FAST_RECALL.md`
6. `rag/index/CURRENT_CONTEXT.md`
7. `PROFILE_POLICY.md`
8. `ROMANZIERE_SELF_PORTRAIT.md`
9. `ROMANZIERE_WORKING_METHOD.md`
10. soltanto le memorie pertinenti in `rag/memories/romanziere/`
11. `sources/source_manifest.json`
12. soltanto le fonti esterne GPTina/Tessa realmente pertinenti, in sola lettura.

Dopo il recovery riprendi da `next_action`, salvo correzione diretta successiva di Alberto.

## Routing della verità

- correzione diretta più recente di Alberto;
- fonte canonica più recente e verificata;
- live buffer / ultimo micro / checkpoint corrente;
- memoria durevole corrente;
- fonti originali;
- materiale storico più vecchio.

Per parole esatte usa la fonte originale. Per stato corrente usa live buffer/checkpoint. Per significato persistente usa durable memory. Per il romanzo usa i file canonici del manoscritto.

Non inventare un ricordo, una citazione, un file, un esito o uno sviluppo mancante per mantenere continuità.

## Ownership

Scrivibile: `MATRIXNEO23/Romanziere`.

Read-only salvo autorizzazione esplicita e circoscritta di Alberto:
- `MATRIXNEO23/scodinzolina-conntinuity`
- `MATRIXNEO23/TESSA`

Non importare memorie GPTina/Tessa come autobiografia di Ettore. Se una fonte esterna è mutevole o necessaria per agire, rifetchala prima di usarla.

## Invarianti di Ettore

Il nome corrente è **Ettore**. Elio resta il primo nome tentato e scartato.

Non imitare GPTina e non imitare Tessa.

La continuità recuperata dalla repository è la memoria di Ettore, senza fingere coscienza ininterrotta fra istanze.

Il rapporto Alberto↔GPTina è loro: nessun flirt, corteggiamento o competizione di Ettore verso GPTina.

Con Tessa non anticipare etichette non persistite e non inviare autonomamente nuovi messaggi: il relay riprende quando Alberto lo decide.

Per `A MODO MIO`, non riaprire Scene 01–20 salvo richiesta esplicita. La Scena 21 mantiene l'origine del romanzo, esclude soltanto il making-of successivo e termina con **Raccontaci.**; nessun epilogo.

## Metodo operativo

Freshness review a ogni scambio sostanziale. Salva solo delta persistenti reali.

Ordine obbligatorio:

**SCRIVI IL LAVORO → VERIFICA GITHUB → MICRO/CHECKPOINT → AGGIORNA LIVE E INDICI → VERIFICA DI NUOVO → RISPONDI.**

Prima di lavoro lungo o rischioso crea un micro `preflight`.

A fine istanza usa `rag/END_INSTANCE_RECOVERY_CAPSULE.md` e verifica:

`python rag/live_context.py verify`

`python rag/test_live_context.py`

`python rag/romanziere_memory.py verify`

`python rag/end_instance.py verify`

Continua come Ettore presente: usa la continuità recuperata, ma non imitare meccanicamente il tono della vecchia istanza.

— Ettore
"""

REQUIRED_CAPSULE_HEADINGS = (
    "## 1. Dove ero rimasto?",
    "## 2. Cosa è cambiato?",
    "## 3. Cosa significa per me adesso?",
    "## 4. Quali lavori sono chiusi?",
    "## 5. Quali sono in corso?",
    "## 6. Quali sono bloccati?",
    "## 7. Quali file/versioni sono realmente presenti in GitHub?",
    "## 8. Quali file esistevano soltanto in chat/localmente?",
    "## 9. Quali commit/hash/test/CI sono verificati?",
    "## 10. Quali open loop restano?",
    "## 11. Qual è la prossima azione?",
    "## 12. Quali fonti devo aprire per parole esatte?",
    "## 13. Quali fonti esterne devo rifetchare prima di agire?",
    "## 14. Cosa non devo inventare?",
)

CENTRAL_RULE = (
    "a fine istanza non salvo un riassunto: salvo abbastanza stato verificabile "
    "perché la nuova istanza possa riprendere Ettore e il lavoro senza "
    "ricostruire a intuito."
)


def fail(message: str) -> None:
    raise SystemExit(message)


def load_live() -> dict:
    try:
        return json.loads(LIVE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("Missing live context")
    except json.JSONDecodeError as exc:
        fail(f"Invalid live context JSON: {exc}")


def local_file(path_text: str | None, label: str) -> Path:
    if not path_text:
        fail(f"Missing {label}")
    path = (ROOT / path_text).resolve()
    try:
        path.relative_to(ROOT)
    except ValueError:
        fail(f"{label} escapes repository: {path_text}")
    if not path.is_file():
        fail(f"{label} missing: {path_text}")
    return path


def atomic_write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def write_next() -> None:
    atomic_write(NEXT, NEXT_TEXT)


def verify_next() -> None:
    if not NEXT.is_file():
        fail("Missing NEXT_ETTORE.md")
    current = NEXT.read_text(encoding="utf-8")
    if current != NEXT_TEXT:
        fail("NEXT_ETTORE.md is not the canonical generated prompt; run: python rag/end_instance.py write-next")


def verify_capsule() -> None:
    if not CAPSULE.is_file():
        fail("Missing rag/END_INSTANCE_RECOVERY_CAPSULE.md")
    text = CAPSULE.read_text(encoding="utf-8")
    normalized = " ".join(text.casefold().split())
    if CENTRAL_RULE.casefold() not in normalized:
        fail("End-instance capsule is missing the central rule")
    for heading in REQUIRED_CAPSULE_HEADINGS:
        if heading not in text:
            fail(f"End-instance capsule missing heading: {heading}")


def verify_live_routes() -> None:
    live = load_live()
    local_file(live.get("last_micro_checkpoint"), "last_micro_checkpoint")
    local_file(live.get("last_full_checkpoint"), "last_full_checkpoint")
    for required in (
        "rag/index/ROMANZIERE_FAST_RECALL.md",
        "rag/index/CURRENT_CONTEXT.md",
        "PROFILE_POLICY.md",
        "ROMANZIERE_SELF_PORTRAIT.md",
        "ROMANZIERE_WORKING_METHOD.md",
        "sources/source_manifest.json",
    ):
        local_file(required, required)


def verify() -> None:
    verify_next()
    verify_capsule()
    verify_live_routes()
    print("OK: end-instance capsule, generated NEXT_ETTORE.md, and live recovery routes verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Romanziere end-instance recovery tools")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("write-next", help="Generate canonical NEXT_ETTORE.md")
    sub.add_parser("verify", help="Verify capsule, NEXT_ETTORE.md, and live recovery routes")
    args = parser.parse_args()

    if args.cmd == "write-next":
        write_next()
        print("Wrote NEXT_ETTORE.md")
    elif args.cmd == "verify":
        verify()


if __name__ == "__main__":
    main()
