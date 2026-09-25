# -*- coding: utf-8 -*-
# Consultas refeitas ao vivo no Jira em 2026-09-25 ~18:30 UTC (15:31 BRT).
# ETQ = issuetype in ("Epic","Fluxo de trabalho"); cloudId ead785de-...
# getVisibleJiraProjects: total=20, isLast=true - mesmas 20 chaves de _projects_min.json.
# lookahead (out+nov/2026) estourou o limite de tokens do MCP e foi reduzido com jq
# sobre a resposta salva, mantendo apenas os campos minimais.
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
("EG0286-11","Estudos hidrológicos","Em andamento","indeterminate","EG0286","2026-09-23",None,"2026-08-30T23:27:03.793-0300"),
("EG0286-14","Projeto geométrico e de interseções (pb)","Tarefas pendentes","new","EG0286","2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
("EG0286-10","Estudos geológicos","Em andamento","indeterminate","EG0286","2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
("EG0286-6","Estudo de traçado","Tarefas pendentes","new","EG0286","2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
("EG0286-8","Estudo topográfico","Em andamento","indeterminate","EG0286","2026-08-31",None,"2026-07-30T09:33:06.932-0300"),
]
sent=[
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
resolved=[
("EG0286-30","Relatório Periódico","Enviado - Aguardando Análise","done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
]
rework=[
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
lookahead=[
("G0280-75","Administração e Coordenação do Contrato","Em andamento","indeterminate","G0280","2026-10-01",None,"2026-03-16T15:13:40.422-0300"),
("EG0256-28","Diagnóstico Ambiental - Meio Físico - Recursos Hídricos","Em andamento","indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300"),
("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300"),
("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300"),
("EG0286-21","Projeto de sinalização e segurança viária (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:54.156-0300"),
("EG0286-20","Projeto de obras complementares - oc (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:44.118-0300"),
("EG0286-17","Projeto de pavimentação (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:32.376-0300"),
("EG0286-16","Projeto de drenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:28.787-0300"),
("EG0286-15","Projeto de terraplenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:22.692-0300"),
("EG0286-12","Levantamento ambiental","Tarefas pendentes","new","EG0286","2026-10-19",None,"2026-09-11T12:12:51.299-0300"),
("EG0286-23","Projeto de desapropriação (pb)","Tarefas pendentes","new","EG0286","2026-10-20",None,"2026-06-17T17:39:00.759-0300"),
("EG0286-22","Projeto de componentes ambientais e paisagismo (pb)","Tarefas pendentes","new","EG0286","2026-10-22",None,"2026-06-17T17:38:57.611-0300"),
("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo","Em andamento","indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300"),
("EG0274-62","Proj. Básico - Projeto de Obras Complementares","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300"),
("EG0274-61","Proj. Básico - Projetos de Contenções","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300"),
("EG0274-60","Proj. Básico - Projetos de OAEs","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300"),
("EG0286-9","Estudo geotécnico de subleito/ e ocorrências","Tarefas pendentes","new","EG0286","2026-10-28",None,"2026-08-28T16:30:25.519-0300"),
("EG0274-21","Proj. Básico - Projeto de Pavimentação","Tarefas pendentes","new","EG0274","2026-10-29",None,"2026-09-25T09:56:37.062-0300"),
("EG0274-58","Proj. Básico - Projeto de Terraplenagem","Tarefas pendentes","new","EG0274","2026-10-30",None,"2026-09-25T09:56:03.350-0300"),
("EG0256-30","Diagnóstico Ambiental - Meio Antrópico","Em andamento","indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300"),
("EG0286-19","Projeto de contenções (pb)","Tarefas pendentes","new","EG0286","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
("EG0285-16","RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ","Tarefas pendentes","new","EG0285","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Enviado- Aguardando Análise","done","EG0285","2026-11-03","2026-08-11T15:04:12.928-0300","2026-08-11T15:04:12.955-0300"),
("EG0285-18","SERVIÇOS GEOTÉCNICOS","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
("EG0285-14","RELATÓRIO GEOTÉCNICO ","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
("EG0274-65","Proj. Básico - Projeto de Desapropriação","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções","Tarefas pendentes","new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
("EG0241-45","Administração e Coordenação do Contrato","Tarefas pendentes","new","EG0241","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
]

K="2026-09"
LIVE={'planned':planned,'overdue':overdue,'sent':sent,'resolved':resolved,'rework':rework,'lookahead':lookahead}

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
print('DELTA' if delta else 'SEM DELTA - nenhum _snap/*.json reescrito')
