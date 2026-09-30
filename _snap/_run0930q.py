# -*- coding: utf-8 -*-
# Rodada agendada 2026-09-30 ~18:10 UTC (15:10 BRT). Mes corrente 2026-09.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
#
# Sonda: ETQ AND updated >= "2026-09-30 14:28" -> 6 issues. DELTA REAL.
#   G0280-50/51/53/54/55 e EG0286-10 tiveram duedate empurrado de set/2026
#   para out/2026 (entre 14:55 e 15:00 BRT). Saem de planned_2026-09 e entram
#   em lookahead_2026-09.
#
# Os 6 conjuntos de set/2026 foram reconsultados ao vivo.
# Meses congelados (<= 2026-08) NAO sao reconsultados.
# lookahead buscado em 2 consultas (out/2026, nov/2026) e concatenado aqui.
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from _w import write

planned=[
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Tarefas pendentes","new","EG0240","2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO","Enviado - Aguardando Análise","done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0275-6","Relatório Final Projeto Básico","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0275-112","Licenças Ambientais","Em Revisã","indeterminate","EG0275","2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
("EG0285-19","SERVIÇOS TOPOGRÁFICOS","Em Revisão","indeterminate","EG0285","2026-09-18",None,"2026-09-30T11:46:18.213-0300"),
("G0280-52","EBE Barros Cassal","Enviado - Aguardando Análise","done","G0280","2026-09-16","2026-09-30T11:23:49.943-0300","2026-09-30T11:23:49.965-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
]
sent=[
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
lookahead=[
("EG0256-28","Diagnóstico Ambiental - Meio Físico - Recursos Hídricos","Em andamento","indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300"),
("EG0256-30","Diagnóstico Ambiental - Meio Antrópico","Em andamento","indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300"),
("EG0274-21","Proj. Básico - Projeto de Pavimentação","Tarefas pendentes","new","EG0274","2026-10-29",None,"2026-09-25T09:56:37.062-0300"),
("EG0274-43","Estudos Hidrológicos ","Em Revisão","indeterminate","EG0274","2026-10-31",None,"2026-09-28T09:26:55.035-0300"),
("EG0274-58","Proj. Básico - Projeto de Terraplenagem","Tarefas pendentes","new","EG0274","2026-10-30",None,"2026-09-25T09:56:03.350-0300"),
("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300"),
("EG0274-60","Proj. Básico - Projetos de OAEs","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300"),
("EG0274-61","Proj. Básico - Projetos de Contenções","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300"),
("EG0274-62","Proj. Básico - Projeto de Obras Complementares","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300"),
("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300"),
("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo","Em andamento","indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300"),
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
("EG0286-10","Estudos geológicos","Em andamento","indeterminate","EG0286","2026-10-30",None,"2026-09-30T14:55:35.086-0300"),
("EG0286-11","Estudos hidrológicos","Em andamento","indeterminate","EG0286","2026-10-15",None,"2026-09-28T09:29:27.853-0300"),
("EG0286-12","Levantamento ambiental","Em andamento","indeterminate","EG0286","2026-10-19",None,"2026-09-28T09:31:11.033-0300"),
("EG0286-15","Projeto de terraplenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:22.692-0300"),
("EG0286-16","Projeto de drenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:28.787-0300"),
("EG0286-17","Projeto de pavimentação (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:32.376-0300"),
("EG0286-20","Projeto de obras complementares - oc (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:44.118-0300"),
("EG0286-21","Projeto de sinalização e segurança viária (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:54.156-0300"),
("EG0286-22","Projeto de componentes ambientais e paisagismo (pb)","Tarefas pendentes","new","EG0286","2026-10-22",None,"2026-06-17T17:38:57.611-0300"),
("EG0286-23","Projeto de desapropriação (pb)","Tarefas pendentes","new","EG0286","2026-10-20",None,"2026-06-17T17:39:00.759-0300"),
("G0280-50","EBE Ponta da Cadeia","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:50.045-0300"),
("G0280-51","EBE Baronesa do Gravataí","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T15:00:04.232-0300"),
("G0280-53","EBE Gaspar Martins","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:30.308-0300"),
("G0280-54","EBE Asa Branca","Em andamento","indeterminate","G0280","2026-10-29",None,"2026-09-30T14:59:57.634-0300"),
("G0280-55","EBE Nova Brasília","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:43.601-0300"),
("EG0241-45","Administração e Coordenação do Contrato","Tarefas pendentes","new","EG0241","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções","Tarefas pendentes","new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
("EG0274-65","Proj. Básico - Projeto de Desapropriação","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Em Revisão","indeterminate","EG0285","2026-11-03",None,"2026-09-30T11:46:00.212-0300"),
("EG0285-14","RELATÓRIO GEOTÉCNICO ","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
("EG0285-16","RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ","Tarefas pendentes","new","EG0285","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
("EG0285-18","SERVIÇOS GEOTÉCNICOS","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
("EG0286-6","Estudo de traçado","Tarefas pendentes","new","EG0286","2026-11-18",None,"2026-09-30T11:08:02.268-0300"),
("EG0286-19","Projeto de contenções (pb)","Tarefas pendentes","new","EG0286","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
("G0280-75","Administração e Coordenação do Contrato","Em andamento","indeterminate","G0280","2026-11-30",None,"2026-09-30T11:29:49.398-0300"),
]

K="2026-09"
LIVE={'planned':planned,'overdue':overdue,'sent':sent,'resolved':resolved,
      'rework':rework,'lookahead':lookahead}

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

for name in ['planned','overdue','sent','resolved','rework','lookahead']:
    rows=LIVE[name]; n=name+'_'+K
    a,b=norm(rows),cur(n)
    if a!=b:
        print('DELTA %s: gravado=%s vivo=%s'%(n, 0 if b is None else len(b), len(a)))
        if b is not None:
            ka={r["key"] for r in a}; kb={r["key"] for r in b}
            if ka-kb: print('   + ', sorted(ka-kb))
            if kb-ka: print('   - ', sorted(kb-ka))
    else:
        print('igual  %s (%d)'%(n,len(a)))
    write(n, rows)
