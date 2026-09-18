#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, uuid
from datetime import datetime
from pathlib import Path

ROOT=Path(os.environ.get("ROMANZIERE_REPO_ROOT", str(Path(__file__).resolve().parents[1]))).resolve()
LIVE=ROOT/"rag"/"live"
MICRO=LIVE/"micro-checkpoints"
CTX=LIVE/"ROMANZIERE_LIVE_CONTEXT.json"
TYPES={"correction","decision","rule","project_state","profile_shift","open_loop","preflight","milestone","source_update"}

def now(): return datetime.now().astimezone().isoformat(timespec="seconds")
def rel(p): return p.resolve().relative_to(ROOT).as_posix()
def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    t=p.with_name(p.name+".tmp"); t.write_text(s,encoding="utf-8"); os.replace(t,p)

def load():
    if CTX.exists(): return json.loads(CTX.read_text(encoding="utf-8"))
    return {
      "schema_version":1,"owner":"romanziere","kind":"romanziere_live_context",
      "updated_at":now(),"latest_summary":"","next_action":"",
      "last_micro_checkpoint":None,"last_full_checkpoint":None,
      "active_threads":[],"open_loops":[],"recent_micro_checkpoints":[],
      "micro_since_full_checkpoint":0,
      "review_policy":{"substantive_turn_interval":4,"preflight_before_long_or_risky_work":True}
    }

def save(args):
    ts=now(); dt=datetime.fromisoformat(ts)
    slug=re.sub(r"[^0-9a-z_-]+","-",args.summary.casefold()).strip("-")[:60] or "delta"
    token=uuid.uuid4().hex[:8]
    p=MICRO/f"{dt:%Y}"/f"{dt:%m}"/f"{dt:%d}"/f"{dt:%Y-%m-%dT%H%M%S%z}--{slug}--{token}.json"
    rec={
      "schema_version":1,"micro_id":f"romanziere-micro-{token}",
      "owner":"romanziere","kind":"romanziere_micro_checkpoint",
      "event_at":args.event_at or ts,"recorded_at":ts,
      "change_type":args.change_type,"summary":args.summary,
      "changed":args.changed,"thread_ids":args.thread,
      "source_refs":args.source or ["conversation://current"],
      "memory_refs":args.memory,"importance":args.importance,
      "next_action":args.next_action,"preflight":args.preflight or args.change_type=="preflight"
    }
    write(p,json.dumps(rec,ensure_ascii=False,indent=2)+"\n")
    ctx=load(); recent=(ctx.get("recent_micro_checkpoints") or [])+[rel(p)]
    ctx.update({
      "updated_at":ts,"latest_summary":args.summary,"next_action":args.next_action,
      "last_micro_checkpoint":rel(p),"recent_micro_checkpoints":recent[-12:],
      "micro_since_full_checkpoint":int(ctx.get("micro_since_full_checkpoint",0))+1
    })
    for t in args.thread:
      if t not in ctx["active_threads"]: ctx["active_threads"].append(t)
    if args.next_action and args.next_action not in ctx["open_loops"]: ctx["open_loops"].append(args.next_action)
    write(CTX,json.dumps(ctx,ensure_ascii=False,indent=2)+"\n")
    print(rel(p))

def mark(path):
    p=ROOT/path
    if not p.is_file() or (ROOT/"checkpoints").resolve() not in p.resolve().parents: raise SystemExit("invalid checkpoint")
    ctx=load(); ctx["updated_at"]=now(); ctx["last_full_checkpoint"]=path; ctx["micro_since_full_checkpoint"]=0
    write(CTX,json.dumps(ctx,ensure_ascii=False,indent=2)+"\n")

def verify():
    ctx=load()
    if ctx.get("owner")!="romanziere" or ctx.get("kind")!="romanziere_live_context": raise SystemExit("invalid live context")
    if not 3 <= int(ctx.get("review_policy",{}).get("substantive_turn_interval",0)) <= 5: raise SystemExit("invalid review interval")
    lm=ctx.get("last_micro_checkpoint")
    if lm and not (ROOT/lm).is_file(): raise SystemExit("missing last micro")
    lf=ctx.get("last_full_checkpoint")
    if lf and not (ROOT/lf).is_file(): raise SystemExit("missing full checkpoint")
    count=0
    if MICRO.exists():
      for p in MICRO.rglob("*.json"):
        r=json.loads(p.read_text(encoding="utf-8"))
        if r.get("owner")!="romanziere" or r.get("kind")!="romanziere_micro_checkpoint" or r.get("change_type") not in TYPES: raise SystemExit(f"invalid {rel(p)}")
        count+=1
    print(f"OK live-context micro={count}")

def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd",required=True)
    s=sub.add_parser("save-delta"); s.add_argument("--summary",required=True); s.add_argument("--change-type",required=True,choices=sorted(TYPES)); s.add_argument("--event-at")
    s.add_argument("--changed",action="append",default=[]); s.add_argument("--thread",action="append",default=[]); s.add_argument("--source",action="append",default=[]); s.add_argument("--memory",action="append",default=[]); s.add_argument("--importance",type=int,default=3,choices=range(1,6)); s.add_argument("--next",dest="next_action",default=""); s.add_argument("--preflight",action="store_true")
    m=sub.add_parser("mark-checkpoint"); m.add_argument("path")
    sub.add_parser("status"); sub.add_parser("verify")
    a=ap.parse_args()
    if a.cmd=="save-delta": save(a)
    elif a.cmd=="mark-checkpoint": mark(a.path)
    elif a.cmd=="status": print(json.dumps(load(),ensure_ascii=False,indent=2))
    else: verify()

if __name__=="__main__": main()
