# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-29 ~17:54 UTC (14:54 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
# Artifact: pasta Artifacts NAO montada (device_request_folder_access recusado nesta
#   sessao). Snapshot gerado a partir do _artifact_src.html ja versionado no repo.
# 6 conjuntos do mes corrente reconsultados ao vivo; lookahead conferido por
#   key+updated (payload completo estoura o limite de tokens do MCP).
# Meses congelados (2026-04..2026-08) nao sao reconsultados por design.
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from _w import write

LIVE = json.load(open(os.path.expanduser('~/pr03tmp/live.json'), encoding='utf-8'))
K = "2026-09"

def norm(rows):
    return sorted([{"key":k,"summary":sm,"status":st,"cat":cat,"project":pj,"duedate":du,
                    "resolutiondate":rd,"updated":up} for k,sm,st,cat,pj,du,rd,up in rows],
                  key=lambda r: r["key"])

def cur(name):
    p = os.path.join(D, name + '.json')
    if not os.path.exists(p): return None
    return sorted([{"key":i["key"],"summary":i["fields"]["summary"],
                    "status":i["fields"]["status"]["name"],
                    "cat":i["fields"]["status"]["statusCategory"]["key"],
                    "project":i["fields"]["project"]["key"],
                    "duedate":i["fields"]["duedate"],
                    "resolutiondate":i["fields"]["resolutiondate"],
                    "updated":i["fields"]["updated"]} for i in json.load(open(p, encoding='utf-8'))],
                  key=lambda r: r["key"])

delta = False
for name in ['planned','overdue','sent','resolved','rework']:
    rows = LIVE[name]; n = name + '_' + K
    a, b = norm(rows), cur(n)
    if a != b:
        delta = True
        print('DELTA %s: gravado=%s vivo=%s' % (n, 0 if b is None else len(b), len(a)))
        if b is not None:
            ka = {r["key"] for r in a}; kb = {r["key"] for r in b}
            if ka - kb: print('   + ', sorted(ka - kb))
            if kb - ka: print('   - ', sorted(kb - ka))
            for ra in a:
                for rb in b:
                    if ra["key"] == rb["key"] and ra != rb:
                        print('   ~ %s: %s' % (ra["key"], {k:(rb[k], ra[k]) for k in ra if ra[k] != rb[k]}))
        write(n, rows)
    else:
        print('OK    %-20s %d registros identicos' % (n, len(a)))

# lookahead: conferencia por key + updated
lk = LIVE['lookahead_upd']
b = cur('lookahead_' + K) or []
bu = {r["key"]: r["updated"] for r in b}
if bu != lk:
    delta = True
    print('DELTA lookahead_%s: gravado=%d vivo=%d' % (K, len(bu), len(lk)))
    ka, kb = set(lk), set(bu)
    if ka - kb: print('   + ', sorted(ka - kb))
    if kb - ka: print('   - ', sorted(kb - ka))
    for k in sorted(ka & kb):
        if lk[k] != bu[k]: print('   ~ %s: %s -> %s' % (k, bu[k], lk[k]))
    print('   >> necessario refazer o lookahead completo')
else:
    print('OK    lookahead_%-14s %d registros identicos (key+updated)' % (K, len(lk)))
print('DELTA' if delta else 'SEM DELTA')
