# -*- coding: utf-8 -*-
"""Uso: python3 _mk.py <nome_dataset>  -- le TSV do stdin, 1 issue por linha:
key<TAB>summary<TAB>status_name<TAB>status_cat<TAB>duedate<TAB>resolutiondate<TAB>updated
Use a string vazia para null. Grava <nome_dataset>.json no formato do artifact."""
import sys, json, os
PN={"G0120":"EG0120 - DAER","EG0232":"EG0232 - EMBASA","EG0235":"EG0235 - SEMOBI",
"EG0239":"EG0239 - CARPINA/ COMPESA","EG0240":"EG0240 - GOITÁ/ COMPESA","EG0241":"EG0241 - XARÉU/ COMPESA",
"EG0256":"EG0256 - SOPS_RS - EIA RIMA","EG0273":"EG0273 - DNIT AP","EG0274":"EG0274 - DNIT",
"EG0275":"EG0275 - CODEVASF","EG0285":"EG0285 - EMBASA - BARREIRAS","EG0286":"EG0286 - DNIT/AC ",
"G0280":"EG0280 - DMAE"}
d=os.path.dirname(os.path.abspath(__file__))
try:  # fonte autoritativa de nomes de projeto; mapa acima e apenas fallback
    for _p in json.load(open(os.path.join(d,os.pardir,"_projects_min.json"),encoding="utf-8")):
        PN[_p["key"]]=_p["name"]
except Exception as _e:
    print("aviso: _projects_min.json indisponivel (%s); usando mapa fixo"%_e, file=sys.stderr)
name=sys.argv[1]; out=[]
for ln in sys.stdin.read().split("\n"):
    if not ln.strip(): continue
    p=ln.split("\t")
    if len(p)!=7: sys.exit("linha invalida (%d campos): %r"%(len(p),ln))
    k,sm,st,cat,due,res,upd=p
    pj=k.rsplit("-",1)[0]
    out.append({"key":k,"fields":{"summary":sm,"status":{"name":st,"statusCategory":{"key":cat}},
      "project":{"key":pj,"name":PN.get(pj,pj)},"duedate":due or None,
      "resolutiondate":res or None,"updated":upd or None}})
json.dump(out,open(os.path.join(d,name+".json"),"w",encoding="utf-8"),ensure_ascii=False)
print(name,len(out))
