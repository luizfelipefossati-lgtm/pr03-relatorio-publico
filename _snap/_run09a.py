# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _w import write

N="Tarefas pendentes"; A="Em andamento"; R="Em Revisão"; R2="Em Revisã"
EA="Enviado - Aguardando Análise"; EA1="Enviado - Aguardando Análise1"

planned=[
("EG0240-43","TOMO IV - PROJETO DE INSTRUMENTAÇÃO",R,"indeterminate","EG0240","2026-09-10",None,"2026-08-31T16:45:21.119-0300"),
("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",N,"new","EG0240","2026-09-10",None,"2026-08-31T16:45:50.827-0300"),
("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",R,"indeterminate","EG0240","2026-09-30",None,"2026-07-31T17:27:54.489-0300"),
("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)",R,"indeterminate","EG0241","2026-09-10",None,"2026-08-31T16:44:47.690-0300"),
("EG0241-45","Administração e Coordenação do Contrato",N,"new","EG0241","2026-09-30",None,"2026-04-16T17:08:58.500-0300"),
("EG0274-58","Proj. Básico - Projeto de Terraplenagem",N,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:27.192-0300"),
("EG0274-21","Proj. Básico - Projeto de Pavimentação",N,"new","EG0274","2026-09-17",None,"2026-05-28T17:47:32.287-0300"),
("EG0275-6","Relatório Final Projeto Básico",R2,"indeterminate","EG0275","2026-09-04",None,"2026-08-11T14:54:01.361-0300"),
("EG0275-112","Licenças Ambientais",A,"indeterminate","EG0275","2026-09-04",None,"2026-08-31T16:42:35.491-0300"),
("G0280-53","EBE Gaspar Martins",N,"new","G0280","2026-09-08",None,"2026-07-28T16:03:46.832-0300"),
("G0280-51","EBE Baronesa do Gravataí",A,"indeterminate","G0280","2026-09-15",None,"2026-08-31T00:42:45.248-0300"),
("G0280-52","EBE Barros Cassal",A,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:05:36.102-0300"),
("G0280-50","EBE Ponta da Cadeia",A,"indeterminate","G0280","2026-09-16",None,"2026-07-28T16:04:10.678-0300"),
("G0280-54","EBE Asa Branca",N,"new","G0280","2026-09-22",None,"2026-07-28T16:03:54.494-0300"),
("G0280-55","EBE Nova Brasília",N,"new","G0280","2026-09-29",None,"2026-07-28T16:04:01.727-0300"),
("EG0285-19","SERVIÇOS TOPOGRÁFICOS",A,"indeterminate","EG0285","2026-09-18",None,"2026-05-18T10:57:07.064-0300"),
("EG0286-13","Estudo geotécnico - sondagem para oae",N,"new","EG0286","2026-09-14",None,"2026-07-03T11:07:40.831-0300"),
("EG0286-11","Estudos hidrológicos",A,"indeterminate","EG0286","2026-09-23",None,"2026-08-30T23:27:03.793-0300"),
("EG0286-14","Projeto geométrico e de interseções (pb)",N,"new","EG0286","2026-09-29",None,"2026-06-17T17:38:16.515-0300"),
("EG0286-10","Estudos geológicos",A,"indeterminate","EG0286","2026-09-30",None,"2026-08-28T16:30:11.901-0300"),
("EG0286-6","Estudo de traçado",N,"new","EG0286","2026-09-30",None,"2026-08-30T23:26:14.328-0300"),
("EG0286-12","Levantamento ambiental",N,"new","EG0286","2026-09-25",None,"2026-08-26T10:47:34.779-0300"),
]
overdue=[
("EG0286-8","Estudo topográfico",A,"indeterminate","EG0286","2026-08-31",None,"2026-07-30T09:33:06.932-0300"),
("EG0286-7","Estudo de tráfego",A,"indeterminate","EG0286","2026-08-31",None,"2026-07-30T09:37:47.572-0300"),
]
write("planned_2026-09", planned)
write("overdue_2026-09", overdue)
