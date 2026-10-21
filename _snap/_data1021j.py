# -*- coding: utf-8 -*-
"""Datasets ao vivo do Jira - rodada 2026-10-21 ~10:3x UTC / 07:3x BRT."""
P = {
 'EG0239': 'EG0239 - CARPINA/ COMPESA',
 'EG0240': 'EG0240 - GOITÁ/ COMPESA',
 'EG0241': 'EG0241 - XARÉU/ COMPESA',
 'EG0256': 'EG0256 - SOPS_RS - EIA RIMA',
 'EG0274': 'EG0274 - DNIT',
 'EG0275': 'EG0275 - CODEVASF',
 'EG0285': 'EG0285 - EMBASA - BARREIRAS',
 'EG0286': 'EG0286 - DNIT/AC ',
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
EAA2 = 'Enviado- Aguardando Análise'
REV  = 'Em Revisão'
AND_ = 'Em andamento'
CON  = 'Concluído'
MED  = 'Medido e Faturado'
IND  = 'indeterminate'
DONE = 'done'

# --- registros reutilizados entre conjuntos ---
EG0240_5    = R('EG0240-5',   'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', REV, IND, 'EG0240', '2026-10-26', None, '2026-10-15T13:58:00.568-0300')
EG0241_42   = R('EG0241-42',  'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', EAA, DONE, 'EG0241', '2026-09-10', '2026-10-02T09:30:29.370-0300', '2026-10-02T09:30:46.892-0300')
EG0274_38   = R('EG0274-38',  'Estudos de Tráfego', EAA, DONE, 'EG0274', '2026-10-07', '2026-10-15T15:30:49.463-0300', '2026-10-15T15:30:49.471-0300')
EG0275_112  = R('EG0275-112', 'Licenças Ambientais', EAA, DONE, 'EG0275', '2026-09-04', '2026-10-02T09:27:36.092-0300', '2026-10-02T09:27:36.111-0300')
EG0286_7    = R('EG0286-7',   'Estudo de tráfego', EAA, DONE, 'EG0286', '2026-10-01', '2026-10-02T13:40:01.911-0300', '2026-10-02T13:40:01.929-0300')
EG291_4     = R('EG291-4',    'PEB - Plano de Execução BIM', EAA, DONE, 'EG291', '2026-10-07', '2026-10-15T13:59:49.573-0300', '2026-10-15T14:05:50.668-0300')

DATA = {}

DATA['planned_2026-10'] = [
 R('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', REV, IND, 'EG0240', '2026-10-23', None, '2026-10-15T14:50:41.722-0300'),
 R('EG0240-4',  'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', REV, IND, 'EG0240', '2026-10-23', None, '2026-10-15T13:58:30.870-0300'),
 EG0240_5,
 EG0274_38,
 R('EG0274-43', 'Estudos Hidrológicos ', REV, IND, 'EG0274', '2026-10-31', None, '2026-09-28T09:26:55.035-0300'),
 R('G0280-54',  'EBE Asa Branca', AND_, IND, 'G0280', '2026-10-29', None, '2026-09-30T14:59:57.634-0300'),
 R('G0280-55',  'EBE Nova Brasília', AND_, IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:43.601-0300'),
 R('G0280-53',  'EBE Gaspar Martins', AND_, IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:30.308-0300'),
 R('G0280-51',  'EBE Baronesa do Gravataí', AND_, IND, 'G0280', '2026-10-30', None, '2026-09-30T15:00:04.232-0300'),
 R('G0280-50',  'EBE Ponta da Cadeia', AND_, IND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:50.045-0300'),
 EG0286_7,
 R('EG0286-11', 'Estudos hidrológicos', AND_, IND, 'EG0286', '2026-10-15', None, '2026-09-28T09:29:27.853-0300'),
 R('EG0286-12', 'Levantamento ambiental', AND_, IND, 'EG0286', '2026-10-19', None, '2026-09-28T09:31:11.033-0300'),
 R('EG0286-10', 'Estudos geológicos', AND_, IND, 'EG0286', '2026-10-30', None, '2026-09-30T14:55:35.086-0300'),
 EG291_4,
]

DATA['overdue_2026-10'] = []

DATA['sent_2026-10'] = [EG0240_5, EG0241_42, EG0274_38, EG0275_112, EG0286_7, EG291_4]

DATA['rework_2026-10'] = [EG0240_5, EG0241_42, EG0274_38, EG0286_7]

DATA['resolved_2026-10'] = [
 R('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', EAA1, DONE, 'EG0239', '2026-08-10', '2026-10-09T09:36:29.171-0300', '2026-10-09T09:36:29.198-0300'),
 EG0241_42, EG0274_38, EG0275_112, EG0286_7, EG291_4,
]

DATA['planned_2026-05'] = [
 R('EG0239-26', 'TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', CON, DONE, 'EG0239', '2026-05-15', '2026-07-13T16:10:44.098-0300', '2026-07-14T15:00:07.129-0300'),
 R('EG0274-39', 'Estudo de Concepção e Traçado', CON, DONE, 'EG0274', '2026-05-15', '2026-06-29T19:25:06.525-0300', '2026-09-28T09:26:14.228-0300'),
 R('G0280-49', 'EBE 5S', MED, DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:08.021-0300', '2026-09-30T11:24:05.018-0300'),
 R('G0280-48', 'EBE 4S', MED, DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:06.542-0300', '2026-09-30T11:24:03.760-0300'),
 R('G0280-47', 'EBE 3S', MED, DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:05.132-0300', '2026-09-30T11:24:02.649-0300'),
 R('G0280-46', 'EBE 2S', MED, DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:03.281-0300', '2026-09-30T11:24:01.415-0300'),
 R('G0280-45', 'EBE 1S', MED, DONE, 'G0280', '2026-05-29', '2026-06-26T09:13:01.173-0300', '2026-09-30T11:23:59.909-0300'),
]

DATA['planned_2026-06'] = [
 R('EG0256-24', 'Diagnóstico Ambiental - Meio Físico - Condições Meteorológicas', EAA1, DONE, 'EG0256', '2026-06-30', '2026-06-29T11:06:29.534-0300', '2026-06-29T11:06:39.573-0300'),
]

DATA['planned_2026-09'] = [
 EG0241_42,
 EG0275_112,
 R('EG0275-6',  'Relatório Final Projeto Básico', EAA, DONE, 'EG0275', '2026-09-04', '2026-09-21T09:50:27.970-0300', '2026-09-21T09:50:29.197-0300'),
 R('G0280-52',  'EBE Barros Cassal', EAA, DONE, 'G0280', '2026-09-16', '2026-09-30T11:23:49.943-0300', '2026-09-30T11:23:49.965-0300'),
 R('EG0285-19', 'SERVIÇOS TOPOGRÁFICOS', EAA2, DONE, 'EG0285', '2026-09-18', '2026-09-30T15:15:52.506-0300', '2026-09-30T15:15:52.527-0300'),
]
