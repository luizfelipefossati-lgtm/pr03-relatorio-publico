# -*- coding: utf-8 -*-
# Consultas refeitas ao vivo no Jira em 2026-09-28 ~12:30 UTC (09:30 BRT).
# ETQ = issuetype in ("Epic","Fluxo de trabalho"); cloudId ead785de-...
# getVisibleJiraProjects: total=20, isLast=true.
# lookahead (out+nov/2026, 32 registros) estourou o limite de tokens do MCP e foi
# reduzido fora daqui, gravado direto em _snap/lookahead_2026-09.json.
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from _w import write

planned=[
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Tarefas pendentes","new","EG0240","2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0275-112","Licenças Ambientais","Em Revisã","indeterminate","EG0275","2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("G0280-53","EBE Gaspar Martins","Tarefas pendentes","new","G0280","2026-09-08",None,"2026-07-28T16:03:46.832-0300"),
("G0280-51","EBE Baronesa do Gravataí","Em andamento","indeterminate","G0280","2026-09-15",None,"2026-08-31T00:42:45.248-0300"),
("G0280-52","EBE Barros Cassal","Em andamento","indeterminate","G0280","2026-09-16",None,"2026-07-28T16:05:36.102-0300"),
("G0280-50","EBE Ponta da Cadeia","Em andamento","indeterminate","G0280","2026-09-16",None,"2026-07-28T16:04:10.678-0300"),
("G0280-54","EBE Asa Branca","Tarefas pendentes","new","G0280","2026-09-22",None,"2026-07-28T16:03:54.494-0300"),
("G0280-55","EBE Nova Brasília","Tarefas pendentes","new","G0280","2026-09-29",None,"2026-07-28T16:04:01.727-0300"),
("EG0285-19","SERVIÇOS TOPOGRÁFICOS","Em andamento","indeterminate","EG0285","2026-09-18",None,"2026-05-18T10:57:07.064-0300"),
("EG0286-13","Estudo geotécnico - sondagem para oae","Tarefas pendentes","new","EG0286","2026-09-14",None,"2026-07-03T11:07:40.831-0300"),
("EG0286-14","Projeto geométrico e de interseções (pb)","Tarefas pendentes","new","EG0286","2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
("EG0286-10","Estudos geológicos","Em andamento","indeterminate","EG0286","2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
("EG0286-6","Estudo de traçado","Tarefas pendentes","new","EG0286","2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
]
sent=[
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
("EG0286-8","Estudo topográfico","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-28T09:29:40.809-0300","2026-09-28T09:29:40.830-0300"),
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
resolved=[
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
("EG0286-8","Estudo topográfico","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-28T09:29:40.809-0300","2026-09-28T09:29:40.830-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
]
rework=[
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
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

delta=False
for name,rows in LIVE.items():
    n=name+'_'+K
    a,b=norm(rows),cur(n)
    if a!=b:
        delta=True
        print('DELTA %s: gravado=%s vivo=%s'%(n, 0 if b is None else len(b), len(a)))
        if b is not None:
            ka={r["key"] for r in a}; kb={r["key"] for r in b}
            if ka-kb: print('   + ', sorted(ka-kb))
            if kb-ka: print('   - ', sorted(kb-ka))
            for ra in a:
                for rb in b:
                    if ra["key"]==rb["key"] and ra!=rb:
                        print('   ~ %s: %s'%(ra["key"], {k:(rb[k],ra[k]) for k in ra if ra[k]!=rb[k]}))
        write(n, rows)
    else:
        print('OK    %-20s %d registros identicos'%(n, len(a)))
print('DELTA' if delta else 'SEM DELTA')
