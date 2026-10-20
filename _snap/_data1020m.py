# -*- coding: utf-8 -*-
"""Grava os datasets minimos do Jira - 2026-10-20 ~17:4x UTC.
Tipos consultados: Epic + Fluxo de trabalho (hierarchyLevel==1), igual ao artifact."""
import json, io

def I(key, summary, pk, pn, st, cat, due, res, upd):
    return {'key': key, 'fields': {'summary': summary,
            'status': {'name': st, 'statusCategory': {'key': cat}},
            'project': {'key': pk, 'name': pn},
            'duedate': due, 'resolutiondate': res, 'updated': upd}}

GOITA = ('EG0240', u'EG0240 - GOITÁ/ COMPESA')
XAREU = ('EG0241', u'EG0241 - XARÉU/ COMPESA')
CARPINA = ('EG0239', u'EG0239 - CARPINA/ COMPESA')
CODEVASF = ('EG0275', u'EG0275 - CODEVASF')
DNIT = ('EG0274', u'EG0274 - DNIT')
DNITAC = ('EG0286', u'EG0286 - DNIT/AC ')
FEIJO = ('EG291', u'EG0291 - Arroio Feijó')
DMAE = ('G0280', u'EG0280 - DMAE')

AND = (u'Em andamento', 'indeterminate')
REV = (u'Em Revisão', 'indeterminate')
ENV = (u'Enviado - Aguardando Análise', 'done')
ENV1 = (u'Enviado - Aguardando Análise1', 'done')

PRE = u'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)'
PAE = u'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)'

e0240_4  = I('EG0240-4', PRE, GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-23', None, '2026-10-15T13:58:30.870-0300')
e0240_5  = I('EG0240-5', PAE, GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-26', None, '2026-10-15T13:58:00.568-0300')
e0240_43 = I('EG0240-43', u'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-23', None, '2026-10-15T14:50:41.722-0300')
e0274_38 = I('EG0274-38', u'Estudos de Tráfego', DNIT[0], DNIT[1], ENV[0], ENV[1], '2026-10-07', '2026-10-15T15:30:49.463-0300', '2026-10-15T15:30:49.471-0300')
e0274_43 = I('EG0274-43', u'Estudos Hidrológicos ', DNIT[0], DNIT[1], REV[0], REV[1], '2026-10-31', None, '2026-09-28T09:26:55.035-0300')
e0286_7  = I('EG0286-7', u'Estudo de tráfego', DNITAC[0], DNITAC[1], ENV[0], ENV[1], '2026-10-01', '2026-10-02T13:40:01.911-0300', '2026-10-02T13:40:01.929-0300')
e0286_10 = I('EG0286-10', u'Estudos geológicos', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:55:35.086-0300')
e0286_11 = I('EG0286-11', u'Estudos hidrológicos', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-15', None, '2026-09-28T09:29:27.853-0300')
e0286_12 = I('EG0286-12', u'Levantamento ambiental', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-19', None, '2026-09-28T09:31:11.033-0300')
e291_4   = I('EG291-4', u'PEB - Plano de Execução BIM', FEIJO[0], FEIJO[1], ENV[0], ENV[1], '2026-10-07', '2026-10-15T13:59:49.573-0300', '2026-10-15T14:05:50.668-0300')
g50 = I('G0280-50', u'EBE Ponta da Cadeia', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:50.045-0300')
g51 = I('G0280-51', u'EBE Baronesa do Gravataí', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T15:00:04.232-0300')
g53 = I('G0280-53', u'EBE Gaspar Martins', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:30.308-0300')
g54 = I('G0280-54', u'EBE Asa Branca', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-29', None, '2026-09-30T14:59:57.634-0300')
g55 = I('G0280-55', u'EBE Nova Brasília', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:43.601-0300')

e0241_42 = I('EG0241-42', PRE, XAREU[0], XAREU[1], ENV[0], ENV[1], '2026-09-10', '2026-10-02T09:30:29.370-0300', '2026-10-02T09:30:46.892-0300')
e0275_112 = I('EG0275-112', u'Licenças Ambientais', CODEVASF[0], CODEVASF[1], ENV[0], ENV[1], '2026-09-04', '2026-10-02T09:27:36.092-0300', '2026-10-02T09:27:36.111-0300')
e0239_28 = I('EG0239-28', PRE, CARPINA[0], CARPINA[1], ENV1[0], ENV1[1], '2026-08-10', '2026-10-09T09:36:29.171-0300', '2026-10-09T09:36:29.198-0300')

planned = [e0240_4, e0240_5, e0240_43, e0274_38, e0274_43, e0286_7, e0286_10,
           e0286_11, e0286_12, e291_4, g50, g51, g53, g54, g55]
overdue = []
sent = [e0240_5, e0241_42, e0274_38, e0275_112, e0286_7, e291_4]
resolved = [e0239_28, e0241_42, e0274_38, e0275_112, e0286_7, e291_4]
rework = [e0240_5, e0241_42, e0274_38, e0286_7]

for name, data in [('planned_2026-10', planned), ('overdue_2026-10', overdue),
                   ('sent_2026-10', sent), ('resolved_2026-10', resolved),
                   ('rework_2026-10', rework)]:
    with io.open(name + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    print(name, len(data))
