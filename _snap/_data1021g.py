# -*- coding: utf-8 -*-
"""Conjuntos consultados ao vivo em 2026-10-21 ~06:3x UTC (21/10 03:3x BRT).
JQL usada: issuetype in ("Epic","Fluxo de trabalho") -- mesma clausula dinamica do artifact."""
import json, io, os
SNAP = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico', '_snap')

P = {
 'EG0239': 'EG0239 - CARPINA/ COMPESA',
 'EG0240': 'EG0240 - GOITÁ/ COMPESA',
 'EG0241': 'EG0241 - XARÉU/ COMPESA',
 'EG0256': 'EG0256 - SOPS_RS - EIA RIMA',
 'EG0274': 'EG0274 - DNIT',
 'EG0275': 'EG0275 - CODEVASF',
 'EG0286': 'EG0286 - DNIT/AC ',
 'EG291':  'EG0291 - Arroio Feijó',
 'G0280':  'EG0280 - DMAE',
}
REV  = ('Em Revisão', 'indeterminate')
AND  = ('Em andamento', 'indeterminate')
ENV  = ('Enviado - Aguardando Análise', 'done')
ENV1 = ('Enviado - Aguardando Análise1', 'done')
CON  = ('Concluído', 'done')
MED  = ('Medido e Faturado', 'done')

def r(key, summary, st, proj, due, res, upd):
    return {'key': key, 'fields': {
        'summary': summary,
        'status': {'name': st[0], 'statusCategory': {'key': st[1]}},
        'project': {'key': proj, 'name': P[proj]},
        'duedate': due, 'resolutiondate': res, 'updated': upd}}

EG291_4    = r('EG291-4', 'PEB - Plano de Execução BIM', ENV, 'EG291', '2026-10-07', '2026-10-15T13:59:49.573-0300', '2026-10-15T14:05:50.668-0300')
EG0286_7   = r('EG0286-7', 'Estudo de tráfego', ENV, 'EG0286', '2026-10-01', '2026-10-02T13:40:01.911-0300', '2026-10-02T13:40:01.929-0300')
EG0275_112 = r('EG0275-112', 'Licenças Ambientais', ENV, 'EG0275', '2026-09-04', '2026-10-02T09:27:36.092-0300', '2026-10-02T09:27:36.111-0300')
EG0274_38  = r('EG0274-38', 'Estudos de Tráfego', ENV, 'EG0274', '2026-10-07', '2026-10-15T15:30:49.463-0300', '2026-10-15T15:30:49.471-0300')
EG0241_42  = r('EG0241-42', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', ENV, 'EG0241', '2026-09-10', '2026-10-02T09:30:29.370-0300', '2026-10-02T09:30:46.892-0300')
EG0240_5   = r('EG0240-5', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', REV, 'EG0240', '2026-10-26', None, '2026-10-15T13:58:00.568-0300')
EG0239_28  = r('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', ENV1, 'EG0239', '2026-08-10', '2026-10-09T09:36:29.171-0300', '2026-10-09T09:36:29.198-0300')

DATA = {}

DATA['planned_2026-10'] = [
 r('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', REV, 'EG0240', '2026-10-23', None, '2026-10-15T14:50:41.722-0300'),
 r('EG0240-4', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', REV, 'EG0240', '2026-10-23', None, '2026-10-15T13:58:30.870-0300'),
 EG0240_5,
 EG0274_38,
 r('EG0274-43', 'Estudos Hidrológicos ', REV, 'EG0274', '2026-10-31', None, '2026-09-28T09:26:55.035-0300'),
 r('G0280-54', 'EBE Asa Branca', AND, 'G0280', '2026-10-29', None, '2026-09-30T14:59:57.634-0300'),
 r('G0280-55', 'EBE Nova Brasília', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:43.601-0300'),
 r('G0280-53', 'EBE Gaspar Martins', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:30.308-0300'),
 r('G0280-51', 'EBE Baronesa do Gravataí', AND, 'G0280', '2026-10-30', None, '2026-09-30T15:00:04.232-0300'),
 r('G0280-50', 'EBE Ponta da Cadeia', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:50.045-0300'),
 EG0286_7,
 r('EG0286-11', 'Estudos hidrológicos', AND, 'EG0286', '2026-10-15', None, '2026-09-28T09:29:27.853-0300'),
 r('EG0286-12', 'Levantamento ambiental', AND, 'EG0286', '2026-10-19', None, '2026-09-28T09:31:11.033-0300'),
 r('EG0286-10', 'Estudos geológicos', AND, 'EG0286', '2026-10-30', None, '2026-09-30T14:55:35.086-0300'),
 EG291_4,
]
DATA['overdue_2026-10']  = []
DATA['sent_2026-10']     = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0240_5]
DATA['resolved_2026-10'] = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0239_28]
DATA['rework_2026-10']   = [EG0286_7, EG0274_38, EG0241_42, EG0240_5]

DATA['planned_2026-05'] = [
 r('EG0239-26', 'TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', CON, 'EG0239', '2026-05-15', '2026-07-13T16:10:44.098-0300', '2026-07-14T15:00:07.129-0300'),
 r('EG0274-39', 'Estudo de Concepção e Traçado', CON, 'EG0274', '2026-05-15', '2026-06-29T19:25:06.525-0300', '2026-09-28T09:26:14.228-0300'),
 r('G0280-49', 'EBE 5S', MED, 'G0280', '2026-05-29', '2026-06-26T09:13:08.021-0300', '2026-09-30T11:24:05.018-0300'),
 r('G0280-48', 'EBE 4S', MED, 'G0280', '2026-05-29', '2026-06-26T09:13:06.542-0300', '2026-09-30T11:24:03.760-0300'),
 r('G0280-47', 'EBE 3S', MED, 'G0280', '2026-05-29', '2026-06-26T09:13:05.132-0300', '2026-09-30T11:24:02.649-0300'),
 r('G0280-46', 'EBE 2S', MED, 'G0280', '2026-05-29', '2026-06-26T09:13:03.281-0300', '2026-09-30T11:24:01.415-0300'),
 r('G0280-45', 'EBE 1S', MED, 'G0280', '2026-05-29', '2026-06-26T09:13:01.173-0300', '2026-09-30T11:23:59.909-0300'),
]
DATA['planned_2026-06'] = [
 r('EG0256-24', 'Diagnóstico Ambiental - Meio Físico - Condições Meteorológicas', ENV1, 'EG0256', '2026-06-30', '2026-06-29T11:06:29.534-0300', '2026-06-29T11:06:39.573-0300'),
]

def canon(rows):
    return sorted(rows, key=lambda x: x['key'])

changed = []
for name, rows in sorted(DATA.items()):
    path = os.path.join(SNAP, name + '.json')
    old = None
    if os.path.exists(path):
        try: old = json.load(io.open(path, encoding='utf-8'))
        except Exception: old = None
    if old is None:
        verdict = 'NOVO'
    elif canon(old) == canon(rows):
        verdict = 'igual'
    else:
        ok = {i['key'] for i in old}; nk = {i['key'] for i in rows}
        verdict = 'MUDOU +%s -%s' % (sorted(nk - ok), sorted(ok - nk))
        changed.append(name)
    with io.open(path, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)
    print('%-20s n=%-3d %s' % (name, len(rows), verdict))

print('\nDATASETS ALTERADOS:', changed or 'nenhum')
