# -*- coding: utf-8 -*-
"""Datasets ao vivo do Jira - rodada 2026-10-22 ~15:5x UTC / 12:5x BRT."""
import json, os

P = {
 'EG0239': 'EG0239 - CARPINA/ COMPESA',
 'EG0240': 'EG0240 - GOITÁ/ COMPESA',
 'EG0241': 'EG0241 - XARÉU/ COMPESA',
 'EG0274': 'EG0274 - DNIT',
 'EG0275': 'EG0275 - CODEVASF',
 'EG0285': 'EG0285 - EMBASA - BARREIRAS',
 'EG0286': 'EG0286 - DNIT/AC ',
 'EG0294': 'EG0294 - ARTLOT - Topografia',
 'EG291': 'EG0291 - Arroio Feijó',
 'G0280': 'EG0280 - DMAE',
}

def R(key, summary, sname, cat, pk, due, res, upd):
    return {'key': key, 'fields': {
        'summary': summary,
        'status': {'name': sname, 'statusCategory': {'key': cat}},
        'project': {'key': pk, 'name': P[pk]},
        'duedate': due, 'resolutiondate': res, 'updated': upd}}

EAA  = 'Enviado - Aguardando Análise'
EAA1 = 'Enviado - Aguardando Análise1'
REV  = 'Em Revisão'
AND_ = 'Em andamento'
PEN  = 'Tarefas pendentes'
IND  = 'indeterminate'
DON  = 'done'
NEW  = 'new'

planned_10 = [
 R('EG0240-43','TOMO IV - PROJETO DE INSTRUMENTAÇÃO',REV,IND,'EG0240','2026-10-23',None,'2026-10-15T14:50:41.722-0300'),
 R('EG0240-4','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',REV,IND,'EG0240','2026-10-23',None,'2026-10-15T13:58:30.870-0300'),
 R('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)',REV,IND,'EG0240','2026-10-26',None,'2026-10-15T13:58:00.568-0300'),
 R('EG0274-38','Estudos de Tráfego',EAA,DON,'EG0274','2026-10-07','2026-10-15T15:30:49.463-0300','2026-10-15T15:30:49.471-0300'),
 R('EG0274-43','Estudos Hidrológicos ',REV,IND,'EG0274','2026-10-31',None,'2026-09-28T09:26:55.035-0300'),
 R('G0280-54','EBE Asa Branca',AND_,IND,'G0280','2026-10-29',None,'2026-09-30T14:59:57.634-0300'),
 R('G0280-55','EBE Nova Brasília',AND_,IND,'G0280','2026-10-30',None,'2026-09-30T14:59:43.601-0300'),
 R('G0280-53','EBE Gaspar Martins',AND_,IND,'G0280','2026-10-30',None,'2026-09-30T14:59:30.308-0300'),
 R('G0280-51','EBE Baronesa do Gravataí',AND_,IND,'G0280','2026-10-30',None,'2026-09-30T15:00:04.232-0300'),
 R('G0280-50','EBE Ponta da Cadeia',AND_,IND,'G0280','2026-10-30',None,'2026-09-30T14:59:50.045-0300'),
 R('EG0286-7','Estudo de tráfego',EAA,DON,'EG0286','2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
 R('EG0286-11','Estudos hidrológicos',AND_,IND,'EG0286','2026-10-15',None,'2026-09-28T09:29:27.853-0300'),
 R('EG0286-12','Levantamento ambiental',AND_,IND,'EG0286','2026-10-26',None,'2026-10-21T12:03:29.291-0300'),
 R('EG0286-10','Estudos geológicos',AND_,IND,'EG0286','2026-10-30',None,'2026-09-30T14:55:35.086-0300'),
 R('EG291-4','PEB - Plano de Execução BIM',EAA,DON,'EG291','2026-10-07','2026-10-15T13:59:49.573-0300','2026-10-15T14:05:50.668-0300'),
]

overdue_10 = []

sent_10 = [
 R('EG291-4','PEB - Plano de Execução BIM',EAA,DON,'EG291','2026-10-07','2026-10-15T13:59:49.573-0300','2026-10-15T14:05:50.668-0300'),
 R('EG0286-7','Estudo de tráfego',EAA,DON,'EG0286','2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
 R('EG0275-112','Licenças Ambientais',EAA,DON,'EG0275','2026-09-04','2026-10-02T09:27:36.092-0300','2026-10-02T09:27:36.111-0300'),
 R('EG0274-38','Estudos de Tráfego',EAA,DON,'EG0274','2026-10-07','2026-10-15T15:30:49.463-0300','2026-10-15T15:30:49.471-0300'),
 R('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',EAA,DON,'EG0241','2026-09-10','2026-10-02T09:30:29.370-0300','2026-10-02T09:30:46.892-0300'),
 R('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)',REV,IND,'EG0240','2026-10-26',None,'2026-10-15T13:58:00.568-0300'),
]

resolved_10 = [
 R('EG0275-112','Licenças Ambientais',EAA,DON,'EG0275','2026-09-04','2026-10-02T09:27:36.092-0300','2026-10-02T09:27:36.111-0300'),
 R('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',EAA,DON,'EG0241','2026-09-10','2026-10-02T09:30:29.370-0300','2026-10-02T09:30:46.892-0300'),
 R('EG0286-7','Estudo de tráfego',EAA,DON,'EG0286','2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
 R('EG0239-28','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',EAA1,DON,'EG0239','2026-08-10','2026-10-09T09:36:29.171-0300','2026-10-09T09:36:29.198-0300'),
 R('EG291-4','PEB - Plano de Execução BIM',EAA,DON,'EG291','2026-10-07','2026-10-15T13:59:49.573-0300','2026-10-15T14:05:50.668-0300'),
 R('EG0274-38','Estudos de Tráfego',EAA,DON,'EG0274','2026-10-07','2026-10-15T15:30:49.463-0300','2026-10-15T15:30:49.471-0300'),
]

rework_10 = [
 R('EG0286-7','Estudo de tráfego',EAA,DON,'EG0286','2026-10-01','2026-10-02T13:40:01.911-0300','2026-10-02T13:40:01.929-0300'),
 R('EG0274-38','Estudos de Tráfego',EAA,DON,'EG0274','2026-10-07','2026-10-15T15:30:49.463-0300','2026-10-15T15:30:49.471-0300'),
 R('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)',EAA,DON,'EG0241','2026-09-10','2026-10-02T09:30:29.370-0300','2026-10-02T09:30:46.892-0300'),
 R('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)',REV,IND,'EG0240','2026-10-26',None,'2026-10-15T13:58:00.568-0300'),
]

_LOOK = [
 ['EG0286-19','Projeto de contenções (pb)',PEN,NEW,'EG0286','2026-11-03',None,'2026-06-17T17:38:40.836-0300'],
 ['EG0285-16','RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ',PEN,NEW,'EG0285','2026-11-03',None,'2026-05-14T11:31:20.526-0300'],
 ['EG0285-8','ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)',REV,IND,'EG0285','2026-11-03',None,'2026-09-30T11:46:00.212-0300'],
 ['EG0285-18','SERVIÇOS GEOTÉCNICOS',PEN,NEW,'EG0285','2026-11-09',None,'2026-05-14T11:31:30.030-0300'],
 ['EG0285-14','RELATÓRIO GEOTÉCNICO ',PEN,NEW,'EG0285','2026-11-09',None,'2026-05-14T11:31:11.610-0300'],
 ['EG0294-3','São Roque',PEN,NEW,'EG0294','2026-11-18',None,'2026-10-02T13:45:46.124-0300'],
 ['EG0294-2','Navegantes/Artlot',PEN,NEW,'EG0294','2026-11-18',None,'2026-10-02T13:45:37.682-0300'],
 ['EG0294-1','Baía/Artlot',PEN,NEW,'EG0294','2026-11-18',None,'2026-10-02T13:45:29.242-0300'],
 ['EG0286-6','Estudo de traçado',PEN,NEW,'EG0286','2026-11-18',None,'2026-09-30T11:08:02.268-0300'],
 ['G0280-75','Administração e Coordenação do Contrato',AND_,IND,'G0280','2026-11-30',None,'2026-09-30T11:29:49.398-0300'],
 ['EG0241-45','Administração e Coordenação do Contrato',PEN,NEW,'EG0241','2026-11-30',None,'2026-09-21T14:45:40.371-0300'],
 ['EG0286-18','Projeto de obras de arte especiais (pb)',PEN,NEW,'EG0286','2026-12-03',None,'2026-06-17T17:38:36.976-0300'],
 ['EG0286-14','Projeto geométrico e de interseções (pb)',PEN,NEW,'EG0286','2026-12-09',None,'2026-09-30T11:08:32.515-0300'],
 ['EG0274-64','Proj. Básico - Projeto de Componentes Ambientais e Paisagismo',AND_,IND,'EG0274','2026-12-16',None,'2026-10-07T15:10:38.615-0300'],
 ['EG0286-23','Projeto de desapropriação (pb)',PEN,NEW,'EG0286','2026-12-22',None,'2026-10-07T15:14:52.336-0300'],
 ['EG0274-57','Proj. Básico - Projeto Geométrico e Interseções',PEN,NEW,'EG0274','2026-12-28',None,'2026-10-07T15:12:37.179-0300'],
 ['EG0286-9','Estudo geotécnico de subleito/ e ocorrências',PEN,NEW,'EG0286','2026-12-30',None,'2026-09-30T11:08:11.622-0300'],
 ['EG0274-66','Proj. Básico - Orçamento e Plano de Execução da Obra',PEN,NEW,'EG0274','2026-12-30',None,'2026-10-07T15:12:55.017-0300'],
 ['EG0274-65','Proj. Básico - Projeto de Desapropriação',PEN,NEW,'EG0274','2026-12-30',None,'2026-10-07T15:12:50.939-0300'],
 ['EG0274-59','Proj. Básico - Projeto de Drenagem e OAC',PEN,NEW,'EG0274','2026-12-30',None,'2026-10-07T15:12:39.174-0300'],
 ['EG0274-21','Proj. Básico - Projeto de Pavimentação',PEN,NEW,'EG0274','2026-12-30',None,'2026-10-07T15:10:59.297-0300'],
 ['EG0286-22','Projeto de componentes ambientais e paisagismo (pb)',PEN,NEW,'EG0286','2026-12-31',None,'2026-10-07T16:39:37.820-0300'],
 ['EG0286-17','Projeto de pavimentação (pb)',PEN,NEW,'EG0286','2026-12-31',None,'2026-10-07T15:14:36.171-0300'],
 ['EG0286-16','Projeto de drenagem (pb)',PEN,NEW,'EG0286','2026-12-31',None,'2026-10-07T15:14:39.402-0300'],
 ['EG0286-15','Projeto de terraplenagem (pb)',PEN,NEW,'EG0286','2026-12-31',None,'2026-10-07T15:14:41.891-0300'],
 ['EG0275-108','Administração e Coordenação do Contrato',AND_,IND,'EG0275','2026-12-31',None,'2026-05-05T09:21:58.639-0300'],
 ['EG0274-63','Proj. Básico - Projeto de Sinalização e Segurança Viária',PEN,NEW,'EG0274','2026-12-31',None,'2026-10-07T15:12:47.131-0300'],
 ['EG0274-62','Proj. Básico - Projeto de Obras Complementares',PEN,NEW,'EG0274','2026-12-31',None,'2026-10-07T15:12:42.729-0300'],
 ['EG0274-61','Proj. Básico - Projetos de Contenções',PEN,NEW,'EG0274','2026-12-31',None,'2026-10-07T15:10:17.792-0300'],
 ['EG0274-60','Proj. Básico - Projetos de OAEs',PEN,NEW,'EG0274','2026-12-31',None,'2026-10-07T15:11:13.308-0300'],
 ['EG0274-58','Proj. Básico - Projeto de Terraplenagem',PEN,NEW,'EG0274','2026-12-31',None,'2026-10-07T15:10:03.315-0300'],
 ['EG0240-44','Administração e Coordenação do Contrato',AND_,IND,'EG0240','2026-12-31',None,'2026-05-05T09:21:36.085-0300'],
 ['EG0239-54','Administração e Coordenação do Contrato',AND_,IND,'EG0239','2026-12-31',None,'2026-05-11T16:20:36.026-0300'],
]
lookahead_10 = [R(*r) for r in _LOOK]

DATA = {
 'planned_2026-10': planned_10,
 'overdue_2026-10': overdue_10,
 'lookahead_2026-10': lookahead_10,
 'sent_2026-10': sent_10,
 'resolved_2026-10': resolved_10,
 'rework_2026-10': rework_10,
}

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    for n, v in DATA.items():
        with open(os.path.join(base, n + '.json'), 'w', encoding='utf-8') as f:
            json.dump(v, f, ensure_ascii=False)
        print('%-24s %d' % (n, len(v)))
