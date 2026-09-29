# -*- coding: utf-8 -*-
# Consultas refeitas ao vivo no Jira em 2026-09-29 ~05:30 UTC (2026-09-29 02:30 BRT).
# Sessao agendada. 6 conjuntos do mes corrente (2026-09); lookahead out+nov/2026.
# ETQ = issuetype in ("Epic","Fluxo de trabalho"), derivado dos epicTypeNames correntes.
# getVisibleJiraProjects refeito ao vivo: 20 projetos, isLast=true; minimal canonico
#   md5 93d932092a5e272ebe7b4184b829eea5 - identico ao _projects_min.json do repo.
#   epicTypeNames = ['Epic','Fluxo de trabalho'].
# Artifact: pasta Artifacts NAO montada nesta sessao; HTML ao vivo obtido por staging
#   do id do artifact: md5 6a2b6462a4efbec1890af4494a7f0b74, 87.509 bytes ->
#   identico ao _artifact_src.html do repo.
# Meses congelados (2026-04..2026-08) nao sao reconsultados por design.
# Os dados ao vivo desta rodada estao em ~/pr03tmp/live.json (fora do repo).
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
for name in ['planned','overdue','sent','resolved','rework','lookahead']:
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
print('DELTA' if delta else 'SEM DELTA')
