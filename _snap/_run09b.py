# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _w import write
N="Tarefas pendentes"; A="Em andamento"
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
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Enviado- Aguardando Análise","done","EG0285","2026-11-03","2026-08-11T15:04:12.928-0300","2026-08-11T15:04:12.955-0300"),
("EG0285-18","SERVIÇOS GEOTÉCNICOS",N,"new","EG0285","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
("EG0285-14","RELATÓRIO GEOTÉCNICO ",N,"new","EG0285","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra",N,"new","EG0274","2026-11-18",None,"2026-05-28T17:47:05.587-0300"),
("EG0274-65","Proj. Básico - Projeto de Desapropriação",N,"new","EG0274","2026-11-18",None,"2026-05-28T17:47:08.171-0300"),
("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções",N,"new","EG0274","2026-11-30",None,"2026-08-20T17:04:14.132-0300"),
]
write("lookahead_2026-09", look)
write("sent_2026-09", [])
write("resolved_2026-09", [])
write("rework_2026-09", [])
