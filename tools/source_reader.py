#!/usr/bin/env python3
from __future__ import annotations
import argparse, fnmatch, json, urllib.parse, urllib.request
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/"sources"/"source_manifest.json"

def get_json(url):
    req=urllib.request.Request(url,headers={"Accept":"application/vnd.github+json","User-Agent":"Romanziere-readonly-source"})
    with urllib.request.urlopen(req,timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def get_text(url):
    req=urllib.request.Request(url,headers={"User-Agent":"Romanziere-readonly-source"})
    with urllib.request.urlopen(req,timeout=30) as r:
        return r.read().decode("utf-8")

def source(name):
    data=json.loads(REG.read_text(encoding="utf-8"))
    for item in data["sources"]:
        if item["id"]==name:
            if item.get("mode")!="read_only":
                raise SystemExit("source is not read-only")
            return item
    raise SystemExit("unknown source")

def resolve(item):
    repo=item["repository"]; ref=item["ref"]
    q=urllib.parse.quote(ref,safe="")
    return get_json(f"https://api.github.com/repos/{repo}/commits/{q}")["sha"]

def allowed(item,path):
    return any(fnmatch.fnmatch(path,p) for p in item.get("patterns",[]))

def cat(item,path):
    if not allowed(item,path):
        raise SystemExit("path not allowed by source registry")
    sha=resolve(item)
    p=urllib.parse.quote(path,safe="/")
    return get_text(f"https://raw.githubusercontent.com/{item['repository']}/{sha}/{p}"),sha

def list_paths(item):
    sha=resolve(item)
    commit=get_json(f"https://api.github.com/repos/{item['repository']}/commits/{sha}")
    tree_sha=commit["commit"]["tree"]["sha"]
    tree=get_json(f"https://api.github.com/repos/{item['repository']}/git/trees/{tree_sha}?recursive=1")
    paths=[]
    for x in tree.get("tree",[]):
        if x.get("type")=="blob" and allowed(item,x["path"]):
            paths.append(x["path"])
    return sorted(set(paths)),sha

def main():
    ap=argparse.ArgumentParser(description="Read registered external sources without writing upstream.")
    sub=ap.add_subparsers(dest="cmd",required=True)
    lp=sub.add_parser("list"); lp.add_argument("source")
    cp=sub.add_parser("cat"); cp.add_argument("source"); cp.add_argument("path")
    args=ap.parse_args(); item=source(args.source)
    if args.cmd=="list":
        paths,sha=list_paths(item)
        print(json.dumps({"source":args.source,"commit":sha,"paths":paths},ensure_ascii=False,indent=2))
    else:
        text,sha=cat(item,args.path)
        print(f"<!-- source_commit: {sha} -->")
        print(text)

if __name__=="__main__":
    main()
