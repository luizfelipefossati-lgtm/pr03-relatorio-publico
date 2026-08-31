# -*- coding: utf-8 -*-
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _w import write
EA="Enviado - Aguardando Análise"
OVER=[("EG0274-41","Estudos Geotécnicos","Em andamento","indeterminate","EG0274","2026-03-25",None,"2026-03-27T09:06:10.644-0300")]
write('overdue_2026-07',OVER)
write('overdue_2026-08',OVER)
S7=[
("EG0286-2","Relatório de planejamento de atividades",EA,"done","EG0286","2026-07-17","2026-07-28T16:08:52.158-0300","2026-07-28T16:08:52.179-0300"),
("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Enviado- Aguardando Análise","done","EG0285","2026-11-03","2026-08-11T15:04:12.928-0300","2026-08-11T15:04:12.955-0300"),
("EG0274-44","Levantamento Ambiental",EA,"done","EG0274","2026-04-01","2026-07-31T09:31:10.611-0300","2026-07-31T09:31:10.632-0300"),
("EG0241-44","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",EA,"done","EG0241","2026-08-07","2026-08-20T17:08:46.275-0300","2026-08-20T17:08:46.294-0300"),
("EG0241-43","TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)","Medido e Faturado","done","EG0241","2026-07-06","2026-07-09T09:40:19.623-0300","2026-07-13T09:17:31.776-0300"),
]
write('sent_2026-07',S7); write('rework_2026-07',S7)
S8=[
("EG0274-43","Estudos Hidrológicos ",EA,"done","EG0274","2026-07-15","2026-08-21T11:38:34.684-0300","2026-08-21T11:38:34.692-0300"),
("EG0274-38","Estudos de Tráfego",EA,"done","EG0274","2026-07-17","2026-08-24T13:48:05.656-0300","2026-08-24T13:49:25.954-0300"),
("EG0241-44","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)",EA,"done","EG0241","2026-08-07","2026-08-20T17:08:46.275-0300","2026-08-20T17:08:46.294-0300"),
]
write('sent_2026-08',S8); write('rework_2026-08',S8)
