# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-02 ~14:30 UTC (11:30 BRT). Mes corrente: 2026-10.
# 6 conjuntos de out/2026 reconsultados ao vivo via MCP Atlassian.
# ETQ = issuetype in ("Epic","Fluxo de trabalho").
import sys, os, json
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
from _w import write

planned=[
("EG0286-7","Estudo de tráfego","Em Revisão","indeterminate","EG0286","2026-10-01",None,"2026-09-28T09:21:47.778-0300"),
("EG0256-28","Diagnóstico Ambiental - Meio Físico - Recursos Hídricos","Em andamento","indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300"),
("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300"),
("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC","Tarefas pendentes","new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300"),
("EG0286-21","Projeto de sinalização e segurança viária (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:54.156-0300"),
("EG0286-20","Projeto de obras complementares - oc (pb)","Tarefas pendentes","new","EG0286","2026-10-12",None,"2026-06-17T17:38:44.118-0300"),
("EG0286-17","Projeto de pavimentação (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:32.376-0300"),
("EG0286-16","Projeto de drenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:28.787-0300"),
("EG0286-15","Projeto de terraplenagem (pb)","Tarefas pendentes","new","EG0286","2026-10-14",None,"2026-06-17T17:38:22.692-0300"),
("EG0286-11","Estudos hidrológicos","Em andamento","indeterminate","EG0286","2026-10-15",None,"2026-09-28T09:29:27.853-0300"),
("EG0286-12","Levantamento ambiental","Em andamento","indeterminate","EG0286","2026-10-19",None,"2026-09-28T09:31:11.033-0300"),
("EG0286-23","Projeto de desapropriação (pb)","Tarefas pendentes","new","EG0286","2026-10-20",None,"2026-06-17T17:39:00.759-0300"),
("EG0286-22","Projeto de componentes ambientais e paisagismo (pb)","Tarefas pendentes","new","EG0286","2026-10-22",None,"2026-06-17T17:38:57.611-0300"),
("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo","Em andamento","indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300"),
("EG0274-62","Proj. Básico - Projeto de Obras Complementares","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300"),
("EG0274-61","Proj. Básico - Projetos de Contenções","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300"),
("EG0274-60","Proj. Básico - Projetos de OAEs","Tarefas pendentes","new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300"),
("G0280-54","EBE Asa Branca","Em andamento","indeterminate","G0280","2026-10-29",None,"2026-09-30T14:59:57.634-0300"),
("EG0274-21","Proj. Básico - Projeto de Pavimentação","Tarefas pendentes","new","EG0274","2026-10-29",None,"2026-09-25T09:56:37.062-0300"),
("G0280-55","EBE Nova Brasília","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:43.601-0300"),
("G0280-53","EBE Gaspar Martins","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:30.308-0300"),
("G0280-51","EBE Baronesa do Gravataí","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T15:00:04.232-0300"),
("G0280-50","EBE Ponta da Cadeia","Em andamento","indeterminate","G0280","2026-10-30",None,"2026-09-30T14:59:50.045-0300"),
("EG0286-10","Estudos geológicos","Em andamento","indeterminate","EG0286","2026-10-30",None,"2026-09-30T14:55:35.086-0300"),
("EG0274-58","Proj. Básico - Projeto de Terraplenagem","Tarefas pendentes","new","EG0274","2026-10-30",None,"2026-09-25T09:56:03.350-0300"),
("EG0274-43","Estudos Hidrológicos ","Em Revisão","indeterminate","EG0274","2026-10-31",None,"2026-09-28T09:26:55.035-0300"),
("EG0256-30","Diagnóstico Ambiental - Meio Antrópico","Em andamento","indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
lookahead=[
("EG0286-19","Projeto de contenções (pb)","Tarefas pendentes","new","EG0286","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
("EG0285-16","RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ","Tarefas pendentes","new","EG0285","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Em Revisão","indeterminate","EG0285","2026-11-03",None,"2026-09-30T11:46:00.212-0300"),
("EG0285-18","SERVIÇOS GEOTÉCNICOS","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
("EG0285-14","RELATÓRIO GEOTÉCNICO ","Tarefas pendentes","new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
("EG0286-6","Estudo de traçado","Tarefas pendentes","new","EG0286","2026-11-18",None,"2026-09-30T11:08:02.268-0300"),
("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
("EG0274-65","Proj. Básico - Projeto de Desapropriação","Tarefas pendentes","new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
("G0280-75","Administração e Coordenação do Contrato","Em andamento","indeterminate","G0280","2026-11-30",None,"2026-09-30T11:29:49.398-0300"),
("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções","Tarefas pendentes","new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
("EG0241-45","Administração e Coordenação do Contrato","Tarefas pendentes","new","EG0241","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
("EG0286-18","Projeto de obras de arte especiais (pb)","Tarefas pendentes","new","EG0286","2026-12-03",None,"2026-06-17T17:38:36.976-0300"),
("EG0286-14","Projeto geométrico e de interseções (pb)","Tarefas pendentes","new","EG0286","2026-12-09",None,"2026-09-30T11:08:32.515-0300"),
("EG0286-24","Orçamento e plano de execução de obra (pb)","Tarefas pendentes","new","EG0286","2026-12-16",None,"2026-06-17T17:39:06.103-0300"),
("EG0286-9","Estudo geotécnico de subleito/ e ocorrências","Tarefas pendentes","new","EG0286","2026-12-30",None,"2026-09-30T11:08:11.622-0300"),
("EG0275-108","Administração e Coordenação do Contrato","Em andamento","indeterminate","EG0275","2026-12-31",None,"2026-05-05T09:21:58.639-0300"),
("EG0240-44","Administração e Coordenação do Contrato","Em andamento","indeterminate","EG0240","2026-12-31",None,"2026-05-05T09:21:36.085-0300"),
("EG0239-54","Administração e Coordenação do Contrato","Em andamento","indeterminate","EG0239","2026-12-31",None,"2026-05-11T16:20:36.026-0300"),
]
# 2o envio de out/2026: EG0241-42 transitou para "Enviado - Aguardando Analise" em 02/10 09:30 BRT
sent=[
("EG0275-112","Licenças Ambientais","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-10-02T09:27:36.092-0300","2026-10-02T09:27:36.111-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","EG0241","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
]
resolved=[
("EG0275-112","Licenças Ambientais","Enviado - Aguardando Análise","done","EG0275","2026-09-04","2026-10-02T09:27:36.092-0300","2026-10-02T09:27:36.111-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","EG0241","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
]
# EG0241-42 ja havia saido do status "Enviado - Aguardando Analise" antes -> conta como retrabalho
rework=[
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","EG0241","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
]

K="2026-10"
old={}
for name in ['planned','overdue','lookahead','sent','resolved','rework']:
    p=os.path.join(D,name+'_'+K+'.json')
    old[name]=json.load(open(p,encoding='utf-8')) if os.path.exists(p) else None

for name, rows in [('planned',planned),('overdue',overdue),('lookahead',lookahead),
                   ('sent',sent),('resolved',resolved),('rework',rework)]:
    write(name+'_'+K, rows)

print('--- diff vs rodada anterior ---')
for name in ['planned','overdue','lookahead','sent','resolved','rework']:
    new=json.load(open(os.path.join(D,name+'_'+K+'.json'),encoding='utf-8'))
    if old[name] is None:
        print('%-10s NOVO (%d)'%(name,len(new))); continue
    if old[name]==new:
        print('%-10s sem alteracao (%d)'%(name,len(new)))
    else:
        ok={i['key'] for i in old[name]}; nk={i['key'] for i in new}
        print('%-10s ALTERADO %d->%d  +%s  -%s'%(name,len(old[name]),len(new),
              sorted(nk-ok) or '-', sorted(ok-nk) or '-'))
