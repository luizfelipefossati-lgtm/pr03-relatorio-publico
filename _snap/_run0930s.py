# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~23:30 UTC (20:30 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
# Os 6 conjuntos de set/2026 foram reconsultados ao vivo via MCP Atlassian.
# Meses congelados (<= 2026-08) NAO sao reconsultados.
# Nota: EG0285-19 tem status "Enviado- Aguardando Analise" (sem espaco antes do
# hifen) e por isso continua fora do JQL de `sent`/`rework`. Quirk do Jira.
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from _w import write

planned=[
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-30T17:27:26.264-0300","2026-09-30T17:27:26.288-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0275-112","Licenças Ambientais","Em Revisã","indeterminate","EG0275","2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
("EG0285-19","SERVIÇOS TOPOGRÁFICOS","Enviado- Aguardando Análise","done","EG0285","2026-09-18","2026-09-30T15:15:52.506-0300","2026-09-30T15:15:52.527-0300"),
("G0280-52","EBE Barros Cassal","Enviado - Aguardando Análise","done","G0280","2026-09-16","2026-09-30T11:23:49.943-0300","2026-09-30T11:23:49.965-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
]
sent=[
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-30T17:27:26.264-0300","2026-09-30T17:27:26.288-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
("EG0286-8","Estudo topográfico","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-28T09:29:40.809-0300","2026-09-28T09:29:40.830-0300"),
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
("G0280-52","EBE Barros Cassal","Enviado - Aguardando Análise","done","G0280","2026-09-16","2026-09-30T11:23:49.943-0300","2026-09-30T11:23:49.965-0300"),
]
resolved=[
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0286-8","Estudo topográfico","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-28T09:29:40.809-0300","2026-09-28T09:29:40.830-0300"),
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
]
rework=[
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
]

K="2026-09"
LIVE={'planned':planned,'overdue':overdue,'sent':sent,'resolved':resolved,'rework':rework}

def norm(rows):
    return sorted([{"key":k,"summary":sm,"status":st,"cat":cat,"project":pj,"duedate":du,
                    "resolutiondate":rd,"updated":up} for k,sm,st,cat,pj,du,rd,up in rows],
                  key=lambda r: r["key"])

def cur(name):
    p=os.path.join(D,name+'.json')
    if not os.path.exists(p): return None
    return sorted([{"key":i["key"],"summary":i["fields"]["summary"],
                    "status":i["fields"]["status"]["name"],
                    "cat":i["fields"]["status"]["statusCategory"]["key"],
                    "project":i["fields"]["project"]["key"],
                    "duedate":i["fields"]["duedate"],
                    "resolutiondate":i["fields"]["resolutiondate"],
                    "updated":i["fields"]["updated"]} for i in json.load(open(p,encoding='utf-8'))],
                  key=lambda r: r["key"])

for name in ['planned','overdue','sent','resolved','rework']:
    rows=LIVE[name]; n=name+'_'+K
    a,b=norm(rows),cur(n)
    if a!=b:
        print('DELTA %s: gravado=%s vivo=%s'%(n, 0 if b is None else len(b), len(a)))
        if b is not None:
            ka={r["key"] for r in a}; kb={r["key"] for r in b}
            if ka-kb: print('   + ', sorted(ka-kb))
            if kb-ka: print('   - ', sorted(kb-ka))
            da={r["key"]:r for r in a}; db={r["key"]:r for r in b}
            for k in sorted(ka&kb):
                if da[k]!=db[k]: print('   ~ ', k, db[k]["status"], '->', da[k]["status"])
    else:
        print('igual  %s (%d)'%(n,len(a)))
    write(n, rows)

# lookahead_2026-09: conferido por digest contra a consulta ao vivo (38 linhas,
# identico ao gravado). Nao reescrito.
print('igual  lookahead_2026-09 (38)  [conferido por digest, nao reescrito]')
