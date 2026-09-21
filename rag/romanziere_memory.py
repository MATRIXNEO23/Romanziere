#!/usr/bin/env python3
import argparse, json, re, sqlite3, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RAG=ROOT/"rag"
DB=RAG/"index"/"romanziere_memory.sqlite3"
MANIFEST=RAG/"memory_manifest.json"
TOKEN=re.compile(r"[0-9A-Za-zÀ-ÖØ-öø-ÿ_]+",re.UNICODE)


DURABLE_V2_REQUIRED={
    "schema_version","memory_id","owner","kind","event_at","recorded_at",
    "status","supersedes","event_id","thread_ids","source_refs","media_refs",
    "importance","confidence",
}

def frontmatter_fields(text):
    if not text.startswith("---\n"):
        return None
    end=text.find("\n---\n",4)
    if end<0:
        return None
    fields={}
    for line in text[4:end].splitlines():
        if not line or line[:1].isspace() or ":" not in line:
            continue
        key,value=line.split(":",1)
        fields[key.strip()]=value.strip().strip('"').strip("'")
    return fields

def verify_durable_memories():
    base=ROOT/"rag"/"memories"/"romanziere"
    checked=0
    legacy=0
    if not base.exists():
        return checked,legacy
    for p in sorted(base.rglob("*.md")):
        text=p.read_text(encoding="utf-8")
        fields=frontmatter_fields(text)
        if not fields or fields.get("schema_version")!="2":
            legacy+=1
            continue
        missing=sorted(DURABLE_V2_REQUIRED-set(fields))
        if missing:
            raise SystemExit(f"{p.relative_to(ROOT)} missing durable v2 metadata: {missing}")
        if fields.get("owner")!="romanziere":
            raise SystemExit(f"{p.relative_to(ROOT)} durable owner must be romanziere")
        try:
            importance=int(fields.get("importance",""))
        except ValueError:
            raise SystemExit(f"{p.relative_to(ROOT)} durable importance must be integer 1..5")
        if not 1<=importance<=5:
            raise SystemExit(f"{p.relative_to(ROOT)} durable importance must be integer 1..5")
        checked+=1
    return checked,legacy

def manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8"))

def iter_sources():
    m=manifest()
    for group in ("sources","rag_sources"):
        for spec in m.get(group,[]):
            pat=spec["pattern"]
            paths=[ROOT/pat] if not any(x in pat for x in "*?[") else ROOT.glob(pat)
            for p in paths:
                if p.is_file():
                    yield p,spec

def digest(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def chunk(text,n=1400):
    parts=[x.strip() for x in re.split(r"\n\s*\n",text) if x.strip()]
    out=[]; buf=""
    for p in parts:
        if buf and len(buf)+len(p)+2>n:
            out.append(buf); buf=p
        else:
            buf=(buf+"\n\n"+p).strip()
    if buf: out.append(buf)
    return out

def connect():
    DB.parent.mkdir(parents=True,exist_ok=True)
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    c.executescript("""
    CREATE TABLE IF NOT EXISTS source_state(source TEXT PRIMARY KEY, sha TEXT, kind TEXT, priority REAL, status TEXT);
    CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(source UNINDEXED, kind UNINDEXED, priority UNINDEXED, status UNINDEXED, text, tokenize='unicode61 remove_diacritics 2');
    """)
    return c

def build():
    m=manifest(); overrides=m.get("status_overrides",{})
    desired={}
    for p,spec in iter_sources():
        try: text=p.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        rp=p.relative_to(ROOT).as_posix()
        desired[rp]=(text,spec,overrides.get(rp,{}).get("status","current"))
    c=connect()
    current={r["source"]:r["sha"] for r in c.execute("SELECT source,sha FROM source_state")}
    changed=[s for s,v in desired.items() if current.get(s)!=digest(v[0])]
    removed=set(current)-set(desired)
    with c:
        for s in set(changed)|removed:
            c.execute("DELETE FROM chunks WHERE source=?",(s,))
            c.execute("DELETE FROM source_state WHERE source=?",(s,))
        for s in changed:
            text,spec,status=desired[s]
            kind=spec.get("kind","source"); pri=float(spec.get("priority",1.0))
            c.execute("INSERT INTO source_state VALUES(?,?,?,?,?)",(s,digest(text),kind,pri,status))
            for x in chunk(text):
                c.execute("INSERT INTO chunks VALUES(?,?,?,?,?)",(s,kind,pri,status,x))
    stats={"sources":c.execute("SELECT count(*) FROM source_state").fetchone()[0],"chunks":c.execute("SELECT count(*) FROM chunks").fetchone()[0],"changed":len(changed),"removed":len(removed)}
    c.close(); return stats

def search(q,k=6):
    build()
    terms=[m.group(0).casefold() for m in TOKEN.finditer(q)]
    if not terms: return []
    expr=" OR ".join('"'+t+'"' for t in terms)
    c=connect()
    rows=c.execute("SELECT source,kind,priority,status,text,bm25(chunks) rank FROM chunks WHERE chunks MATCH ? ORDER BY rank LIMIT ?",(expr,max(40,k*10))).fetchall()
    out=[]
    for r in rows:
        d=dict(r)
        if d["status"] in ("superseded","invalidated"): continue
        out.append(d)
        if len(out)>=k: break
    c.close(); return out

def exact(q):
    q=q.casefold(); out=[]
    for p,spec in iter_sources():
        try: text=p.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        if q in text.casefold(): out.append({"source":p.relative_to(ROOT).as_posix(),"kind":spec.get("kind","source")})
    return out

def verify():
    c=sqlite3.connect(":memory:"); c.execute("CREATE VIRTUAL TABLE f USING fts5(t)"); c.close()
    for bad in ("rag/memories/gptina","rag/memories/tessa"):
        p=ROOT/bad
        if p.exists() and any(x.is_file() for x in p.rglob("*")): raise SystemExit("foreign memory in owned tree")
    current,legacy=verify_durable_memories()
    print(f"OK: durable_v2={current}, legacy_unmigrated={legacy}")

def main():
    ap=argparse.ArgumentParser(); sp=ap.add_subparsers(dest="cmd",required=True)
    sp.add_parser("build"); q=sp.add_parser("search"); q.add_argument("query"); q.add_argument("--top-k",type=int,default=6)
    e=sp.add_parser("find-exact"); e.add_argument("text"); sp.add_parser("verify")
    a=ap.parse_args()
    if a.cmd=="build": print(build())
    elif a.cmd=="search": print(json.dumps(search(a.query,a.top_k),ensure_ascii=False,indent=2))
    elif a.cmd=="find-exact": print(json.dumps(exact(a.text),ensure_ascii=False,indent=2))
    else: verify()

if __name__=="__main__": main()
