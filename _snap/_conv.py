# -*- coding: utf-8 -*-
"""Converte saida bruta do searchJiraIssuesUsingJql para o formato minimo do snapshot.

Uso:
    python3 _conv.py <nome_dataset> <arquivo_raw1> [<arquivo_raw2> ...]

Cada <arquivo_raw> pode conter:
  {"issues":{"nodes":[...]}} | {"issues":[...]} | {"nodes":[...]} | [...]
Multiplos arquivos = paginas concatenadas (dedup por key).
Grava <nome_dataset>.json em _snap/ no formato consumido pelo artifact:
  [{"key":..., "fields":{"summary","status":{"name","statusCategory":{"key"}},
                         "project":{"key","name"},"duedate","resolutiondate","updated"}}]
Nao preserva accountIds, e-mails, avatares, iconUrls nem ADF.
"""
import json, os, sys

D = os.path.dirname(os.path.abspath(__file__))

PN = {}
try:
    for _p in json.load(open(os.path.join(D, os.pardir, "_projects_min.json"), encoding="utf-8")):
        PN[_p["key"]] = _p["name"]
except Exception as e:
    print("aviso: _projects_min.json indisponivel (%s)" % e, file=sys.stderr)


def nodes(obj):
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        iss = obj.get("issues")
        if isinstance(iss, dict) and isinstance(iss.get("nodes"), list):
            return iss["nodes"]
        if isinstance(iss, list):
            return iss
        if isinstance(obj.get("nodes"), list):
            return obj["nodes"]
    return []


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    name, files = sys.argv[1], sys.argv[2:]
    out, seen = [], set()
    for fp in files:
        raw = open(fp, encoding="utf-8").read().strip()
        if not raw:
            continue
        obj = json.loads(raw)
        for i in nodes(obj):
            k = i.get("key")
            if not k or k in seen:
                continue
            seen.add(k)
            f = i.get("fields") or {}
            st = f.get("status") or {}
            cat = (st.get("statusCategory") or {}).get("key") or ""
            pj = f.get("project") or {}
            pkey = pj.get("key") or k.rsplit("-", 1)[0]
            out.append({
                "key": k,
                "fields": {
                    "summary": f.get("summary") or "",
                    "status": {"name": st.get("name") or "?", "statusCategory": {"key": cat}},
                    "project": {"key": pkey, "name": PN.get(pkey) or pj.get("name") or pkey},
                    "duedate": f.get("duedate") or None,
                    "resolutiondate": f.get("resolutiondate") or None,
                    "updated": f.get("updated") or None,
                },
            })
    json.dump(out, open(os.path.join(D, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
    print("%s -> %d issues" % (name, len(out)))


if __name__ == "__main__":
    main()
