# -*- coding: utf-8 -*-
# Dados verificados contra o Jira ao vivo em 2026-09-22 ~15:30 UTC (12:30 BRT).
# Delta vs _run0922a: NENHUM. Os 6 conjuntos de 2026-09 conferiram registro a
# registro (key/status/duedate/resolutiondate/updated): planned=20, overdue=2,
# sent=5, resolved=4, rework=2, lookahead=27.
# getVisibleJiraProjects tambem sem delta: 20 projetos, epicTypes=[Epic, Fluxo de trabalho].
# Regeracao apenas para atualizar o carimbo de data/hora do snapshot.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _w import write

N="Tarefas pendentes"; A="Em andamento"; R="Em Revisão"; R2="Em Revisã"
EA="Enviado - Aguardando Análise"; EA2="Enviado- Aguardando Análise"

planned=[
("EG0275-112","Licenças Ambientais",R2,"indeterminate","EG0275","2026-09-04",None,"2026-09-21T09:51:05.827-0300"),
("EG0275-6","Relatório Final Projeto Básico",EA,"done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("G0280-53","EBE Gaspar Martins",N,"new","G0280","2026-09-08",None,"2026-07-28T16:03:46.832-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",R,"indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",EA,"done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",N,"new","EG0240","2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
("EG0286-13","Estudo geotécnico - sondagem para oae",N,"new","EG0286","2026-09-14",None,"2026-07-03T11:07:40.831-0300"),
("G0280-51","EBE Baronesa do Gravataí",A,"indeterminate","G0280","2026-09-15",None,"2026-08-31T00:42:45.248-0300"),
("G0280-52","EBE Barros Cassal",A,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:05:36.102-0300"),
("G0280-50","EBE Ponta da Cadeia",A,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:04:10.678-0300"),
("EG0274-58","Proj. Básico - Projeto de Terraplenagem",N,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:27.192-0300"),
("EG0274-21","Proj. Básico - Projeto de Pavimentação",N,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:32.287-0300"),
("EG0285-19","SERVIÇOS TOPOGRÁFICOS",A,"indeterminate","EG0285","2026-09-18",None,"2026-05-18T10:57:07.064-0300"),
("G0280-54","EBE Asa Branca",N,"new","G0280","2026-09-22",None,"2026-07-28T16:03:54.494-0300"),
("EG0286-11","Estudos hidrológicos",A,"indeterminate","EG0286","2026-09-23",None,"2026-08-30T23:27:03.793-0300"),
("G0280-55","EBE Nova Brasília",N,"new","G0280","2026-09-29",None,"2026-07-28T16:04:01.727-0300"),
("EG0286-14","Projeto geométrico e de interseções (pb)",N,"new","EG0286","2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
("EG0286-10","Estudos geológicos",A,"indeterminate","EG0286","2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
("EG0286-6","Estudo de traçado",N,"new","EG0286","2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",R,"indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
overdue=[
("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",R,"indeterminate","EG0239","2026-08-10",None,"2026-09-21T10:55:55.586-0300"),
("EG0286-8","Estudo topográfico",A,"indeterminate","EG0286","2026-08-31",None,"2026-07-30T09:33:06.932-0300"),
]
sent=[
("EG0286-7","Estudo de tráfego",EA,"done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6","Relatório Final Projeto Básico",EA,"done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",EA,"done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",R,"indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
("EG0286-30","Relatório Periódico",EA,"done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
]
resolved=[
("EG0286-7","Estudo de tráfego",EA,"done","EG0286","2026-08-31","2026-09-03T16:50:04.999-0300","2026-09-03T16:50:05.010-0300"),
("EG0275-6","Relatório Final Projeto Básico",EA,"done","EG0275","2026-09-04","2026-09-21T09:50:27.970-0300","2026-09-21T09:50:29.197-0300"),
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",EA,"done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0286-30","Relatório Periódico",EA,"done","EG0286","2028-01-28","2026-09-16T10:43:24.635-0300","2026-09-16T10:43:24.656-0300"),
]
rework=[
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",EA,"done","EG0240","2026-09-10","2026-09-21T10:07:18.825-0300","2026-09-21T10:07:18.849-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",R,"indeterminate","EG0240","2026-09-30",None,"2026-09-21T10:07:17.904-0300"),
]
look=[
("G0280-75","Administração e Coordenação do Contrato",A,"indeterminate","G0280","2026-10-01",None,"2026-03-16T15:13:40.422-0300"),
("EG0256-28","Diagnóstico Ambiental - Meio Físico - Recursos Hídricos",A,"indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300"),
("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária",N,"new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300"),
("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC",N,"new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300"),
("EG0286-21","Projeto de sinalização e segurança viária (pb)",N,"new","EG0286","2026-10-12",None,"2026-06-17T17:38:54.156-0300"),
("EG0286-20","Projeto de obras complementares - oc (pb)",N,"new","EG0286","2026-10-12",None,"2026-06-17T17:38:44.118-0300"),
("EG0286-17","Projeto de pavimentação (pb)",N,"new","EG0286","2026-10-14",None,"2026-06-17T17:38:32.376-0300"),
("EG0286-16","Projeto de drenagem (pb)",N,"new","EG0286","2026-10-14",None,"2026-06-17T17:38:28.787-0300"),
("EG0286-15","Projeto de terraplenagem (pb)",N,"new","EG0286","2026-10-14",None,"2026-06-17T17:38:22.692-0300"),
("EG0286-12","Levantamento ambiental",N,"new","EG0286","2026-10-19",None,"2026-09-11T12:12:51.299-0300"),
("EG0286-23","Projeto de desapropriação (pb)",N,"new","EG0286","2026-10-20",None,"2026-06-17T17:39:00.759-0300"),
("EG0286-22","Projeto de componentes ambientais e paisagismo (pb)",N,"new","EG0286","2026-10-22",None,"2026-06-17T17:38:57.611-0300"),
("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo",A,"indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300"),
("EG0274-62","Proj. Básico - Projeto de Obras Complementares",N,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300"),
("EG0274-61","Proj. Básico - Projetos de Contenções",N,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300"),
("EG0274-60","Proj. Básico - Projetos de OAEs",N,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300"),
("EG0286-9","Estudo geotécnico de subleito/ e ocorrências",N,"new","EG0286","2026-10-28",None,"2026-08-28T16:30:25.519-0300"),
("EG0256-30","Diagnóstico Ambiental - Meio Antrópico",A,"indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300"),
("EG0286-19","Projeto de contenções (pb)",N,"new","EG0286","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
("EG0285-16","RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ",N,"new","EG0285","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)",EA2,"done","EG0285","2026-11-03","2026-08-11T15:04:12.928-0300","2026-08-11T15:04:12.955-0300"),
("EG0285-18","SERVIÇOS GEOTÉCNICOS",N,"new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
("EG0285-14","RELATÓRIO GEOTÉCNICO ",N,"new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra",N,"new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
("EG0274-65","Proj. Básico - Projeto de Desapropriação",N,"new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções",N,"new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
("EG0241-45","Administração e Coordenação do Contrato",N,"new","EG0241","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
]
write("planned_2026-09", planned)
write("overdue_2026-09", overdue)
write("sent_2026-09", sent)
write("resolved_2026-09", resolved)
write("rework_2026-09", rework)
write("lookahead_2026-09", look)
