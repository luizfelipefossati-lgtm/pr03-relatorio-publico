# -*- coding: utf-8 -*-
# Datasets do snapshot PR03 - coletados via MCP Atlassian em 2026-08-31
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _w import write

EA  = "Enviado - Aguardando Análise"
EA1 = "Enviado - Aguardando Análise1"
MF  = "Medido e Faturado"
CO  = "Concluído"
EAND= "Em andamento"
EREV= "Em Revisão"
EREV2="Em Revisã"
TP  = "Tarefas pendentes"

# key: (key, summary, status, statusCategory, projectKey, duedate, resolutiondate, updated)
I = {}
def d(*t): I[t[0]] = t

d("EG0275-112","Licenças Ambientais",EAND,"indeterminate","EG0275","2026-08-31",None,"2026-08-19T09:40:10.499-0300")
d("EG0241-44","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",EA,"done","EG0241","2026-08-07","2026-08-20T17:08:46.275-0300","2026-08-20T17:08:46.294-0300")
d("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",EREV,"indeterminate","EG0241","2026-08-31",None,"2026-08-19T10:59:55.028-0300")
d("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",EREV,"indeterminate","EG0240","2026-08-31",None,"2026-08-11T14:42:26.748-0300")
d("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",TP,"new","EG0240","2026-08-31",None,"2026-08-11T14:39:18.595-0300")
d("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",EA1,"done","EG0239","2026-08-10","2026-08-11T14:33:08.831-0300","2026-08-11T14:33:08.855-0300")
d("EG0274-43","Estudos Hidrológicos ",EA,"done","EG0274","2026-07-15","2026-08-21T11:38:34.684-0300","2026-08-21T11:38:34.692-0300")
d("EG0274-41","Estudos Geotécnicos",EA,"done","EG0274","2026-03-25","2026-08-30T23:13:21.019-0300","2026-08-30T23:13:21.027-0300")
d("EG0274-38","Estudos de Tráfego",EA,"done","EG0274","2026-07-17","2026-08-24T13:48:05.656-0300","2026-08-24T13:49:25.954-0300")
d("EG0274-44","Levantamento Ambiental",EA,"done","EG0274","2026-04-01","2026-07-31T09:31:10.611-0300","2026-07-31T09:31:10.632-0300")
d("EG0241-43","TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)",MF,"done","EG0241","2026-07-06","2026-07-09T09:40:19.623-0300","2026-07-13T09:17:31.776-0300")
d("EG0275-20","Atividades Complementares",CO,"done","EG0275","2026-07-17","2026-02-19T10:39:29.318-0300","2026-05-15T13:36:14.177-0300")
d("EG0275-5","Relatório Parcial Projeto Básico",CO,"done","EG0275","2026-07-15","2026-07-03T10:16:50.117-0300","2026-07-03T10:16:50.137-0300")
d("EG0256-27","Diagnóstico Ambiental - Meio Físico - Avaliação Agrícola",EA1,"done","EG0256","2026-07-31","2026-07-27T10:58:30.736-0300","2026-07-27T10:59:14.278-0300")
d("EG0256-26","Diagnóstico Ambiental - Meio Físico - Pedologia",EA1,"done","EG0256","2026-07-31","2026-07-27T10:58:40.378-0300","2026-07-27T10:59:07.601-0300")
d("EG0256-25","Diagnóstico Ambiental - Meio Físico - Geologia e Geomorfologia",EA1,"done","EG0256","2026-07-31","2026-07-27T10:58:45.012-0300","2026-07-27T10:59:11.112-0300")
d("EG0239-27","TOMO Vl - PAE",CO,"done","EG0239","2026-07-10","2026-07-14T15:00:18.092-0300","2026-08-03T09:48:29.168-0300")
d("EG0239-26","TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)",CO,"done","EG0239","2026-05-15","2026-07-13T16:10:44.098-0300","2026-07-14T15:00:07.129-0300")
d("G0280-75","Administração e Coordenação do Contrato",EAND,"indeterminate","G0280","2026-10-01",None,"2026-03-16T15:13:40.422-0300")
d("G0280-55","EBE Nova Brasília",TP,"new","G0280","2026-09-29",None,"2026-07-28T16:04:01.727-0300")
d("G0280-54","EBE Asa Branca",TP,"new","G0280","2026-09-22",None,"2026-07-28T16:03:54.494-0300")
d("G0280-53","EBE Gaspar Martins",TP,"new","G0280","2026-09-08",None,"2026-07-28T16:03:46.832-0300")
d("G0280-52","EBE Barros Cassal",EAND,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:05:36.102-0300")
d("G0280-51","EBE Baronesa do Gravataí",EAND,"indeterminate","G0280","2026-09-15",None,"2026-08-31T00:42:45.248-0300")
d("G0280-50","EBE Ponta da Cadeia",EAND,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:04:10.678-0300")
d("EG0275-6","Relatório Final Projeto Básico",EREV2,"indeterminate","EG0275","2026-09-04",None,"2026-08-11T14:54:01.361-0300")
d("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo",EAND,"indeterminate","EG0274","2026-10-25",None,"2026-07-01T16:15:49.824-0300")
d("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária",TP,"new","EG0274","2026-10-06",None,"2026-05-28T17:47:13.793-0300")
d("EG0274-62","Proj. Básico - Projeto de Obras Complementares",TP,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:16.641-0300")
d("EG0274-61","Proj. Básico - Projetos de Contenções",TP,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:19.482-0300")
d("EG0274-60","Proj. Básico - Projetos de OAEs",TP,"new","EG0274","2026-10-25",None,"2026-05-28T17:47:22.404-0300")
d("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC",TP,"new","EG0274","2026-10-06",None,"2026-05-28T17:47:24.997-0300")
d("EG0274-58","Proj. Básico - Projeto de Terraplenagem",TP,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:27.192-0300")
d("EG0274-21","Proj. Básico - Projeto de Pavimentação",TP,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:32.287-0300")
d("EG0256-30","Diagnóstico Ambiental - Meio Antrópico",EAND,"indeterminate","EG0256","2026-10-31",None,"2026-06-03T14:39:13.026-0300")
d("EG0256-28","Diagnóstico Ambiental - Meio Físico - Recursos Hídricos",EAND,"indeterminate","EG0256","2026-10-01",None,"2026-04-07T13:44:09.762-0300")
d("EG0241-45","Administração e Coordenação do Contrato",TP,"new","EG0241","2026-09-30",None,"2026-04-16T17:08:58.500-0300")
d("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",EREV,"indeterminate","EG0240","2026-09-30",None,"2026-07-31T17:27:54.489-0300")
d("EG0256-24","Diagnóstico Ambiental - Meio Físico - Condições Meteorológicas",EA1,"done","EG0256","2026-06-30","2026-06-29T11:06:29.534-0300","2026-06-29T11:06:39.573-0300")
d("G0280-49","EBE 5S",EA,"done","G0280","2026-05-29","2026-06-26T09:13:08.021-0300","2026-06-26T09:13:08.044-0300")
d("G0280-48","EBE 4S",EA,"done","G0280","2026-05-29","2026-06-26T09:13:06.542-0300","2026-06-26T09:13:06.571-0300")
d("G0280-47","EBE 3S",EA,"done","G0280","2026-05-29","2026-06-26T09:13:05.132-0300","2026-06-26T09:13:05.150-0300")
d("G0280-46","EBE 2S",EA,"done","G0280","2026-05-29","2026-06-26T09:13:03.281-0300","2026-06-26T09:13:03.309-0300")
d("G0280-45","EBE 1S",EA,"done","G0280","2026-05-29","2026-06-26T09:13:01.173-0300","2026-06-26T09:13:01.199-0300")
d("EG0274-39","Estudo de Concepção e Traçado",EA,"done","EG0274","2026-05-15","2026-06-29T19:25:06.525-0300","2026-06-29T19:25:06.553-0300")
d("EG0273-15","Análise e Aprovação DNIT - Relatório Projeto Executivo",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-14","Relatório Projeto Executivo",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-13","Orçamento e Plano de Execução da Obra",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-12","Projeto de Componentes Ambientais e Paisagismo",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-11","Projeto de Sinalização e Segurança Viária",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-10","Projeto de Obras Complementares",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-9","Verificação Projetos de OAEs ",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-8","Projeto de Pavimentação",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-7","Projeto de Drenagem e OAC",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-6","Projeto de Terrraplenagem",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-5","Projeto Geométrico",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-4","Estudos Hidrológicos",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0273-3","Estudos Geológicos",EA1,"done","EG0273","2026-04-13",None,"2026-04-30T16:40:04.648-0300")
d("EG0240-1","TOMO III - REVISÃO PERIÓDICA DE SEGURANÇA DE BARRAGEM (RPSB)",MF,"done","EG0240","2026-04-30","2026-04-30T16:24:47.919-0300","2026-05-18T10:20:55.123-0300")
d("EG0274-40","Estudos Topográficos, interferências e cadastramento de OAE/OAC  ",MF,"done","EG0274","2026-03-13","2026-03-23T14:51:02.855-0300","2026-07-31T09:31:15.122-0300")
d("EG0274-17","Caracterização Funcional/Estrutural do Pavimento",EA,"done","EG0274","2026-03-06","2026-03-12T08:59:10.783-0300","2026-03-12T08:59:10.803-0300")
d("EG0273-2","Estudos Topográficos Complementares",EA1,"done","EG0273","2026-03-05","2026-03-09T20:28:03.860-0300","2026-05-19T09:31:01.762-0300")
d("EG0256-23","Áreas de Influência Direta e Indireta",EA1,"done","EG0256","2026-03-31",None,"2026-04-01T09:07:29.995-0300")

DS = {
 "planned_2026-03": ["EG0274-41","EG0274-40","EG0274-17","EG0273-2","EG0256-23"],
 "planned_2026-04": ["EG0274-44","EG0273-15","EG0273-14","EG0273-13","EG0273-12","EG0273-11","EG0273-10","EG0273-9","EG0273-8","EG0273-7","EG0273-6","EG0273-5","EG0273-4","EG0273-3","EG0240-1"],
 "planned_2026-05": ["G0280-49","G0280-48","G0280-47","G0280-46","G0280-45","EG0274-39","EG0239-26"],
 "planned_2026-06": ["EG0256-24"],
 "planned_2026-07": ["EG0275-20","EG0275-5","EG0274-43","EG0274-38","EG0256-27","EG0256-26","EG0256-25","EG0241-43","EG0239-27"],
 "planned_2026-08": ["EG0275-112","EG0241-44","EG0241-42","EG0240-43","EG0240-4","EG0239-28"],
 "overdue_2026-07": [],
 "overdue_2026-08": [],
 "lookahead_2026-07": ["G0280-55","G0280-54","G0280-53","G0280-52","G0280-51","G0280-50","EG0275-112","EG0275-6","EG0274-58","EG0274-21","EG0241-45","EG0241-44","EG0241-42","EG0240-43","EG0240-5","EG0240-4","EG0239-28"],
 "lookahead_2026-08": ["G0280-75","G0280-55","G0280-54","G0280-53","G0280-52","G0280-51","G0280-50","EG0275-6","EG0274-64","EG0274-63","EG0274-62","EG0274-61","EG0274-60","EG0274-59","EG0274-58","EG0274-21","EG0256-30","EG0256-28","EG0241-45","EG0240-5"],
 "sent_2026-07": ["EG0274-44","EG0241-44","EG0241-43"],
 "rework_2026-07": ["EG0274-44","EG0241-44","EG0241-43"],
 "resolved_2026-07": ["EG0275-5","EG0256-27","EG0256-26","EG0256-25","EG0241-43","EG0239-27","EG0239-26"],
 "sent_2026-08": ["EG0274-43","EG0274-41","EG0274-38","EG0241-44"],
 "rework_2026-08": ["EG0274-43","EG0274-38","EG0241-44"],
 "resolved_2026-08": ["EG0274-43","EG0274-41","EG0274-38","EG0241-44","EG0239-28"],
}

for name in sorted(DS):
    write(name, [I[k] for k in DS[name]])
