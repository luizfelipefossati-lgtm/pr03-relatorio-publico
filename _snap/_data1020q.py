# -*- coding: utf-8 -*-
"""Datasets minimos do Jira - execucao 2026-10-20 ~23:3x UTC (17a rodada).
Tipos: Epic + Fluxo de trabalho (hierarchyLevel==1), confirmados via getVisibleJiraProjects."""
import json, io, os

SNAPDIR = os.path.join(os.environ['HOME'], 'mnt', 'pr03-relatorio-publico', '_snap')

def I(key, summary, pk, pn, st, cat, due, res, upd):
    return {'key': key, 'fields': {'summary': summary,
            'status': {'name': st, 'statusCategory': {'key': cat}},
            'project': {'key': pk, 'name': pn},
            'duedate': due, 'resolutiondate': res, 'updated': upd}}

GOITA    = ('EG0240', u'EG0240 - GOITÁ/ COMPESA')
XAREU    = ('EG0241', u'EG0241 - XARÉU/ COMPESA')
CARPINA  = ('EG0239', u'EG0239 - CARPINA/ COMPESA')
CODEVASF = ('EG0275', u'EG0275 - CODEVASF')
DNIT     = ('EG0274', u'EG0274 - DNIT')
DNITAC   = ('EG0286', u'EG0286 - DNIT/AC ')
FEIJO    = ('EG291',  u'EG0291 - Arroio Feijó')
DMAE     = ('G0280',  u'EG0280 - DMAE')
SOPS     = ('EG0256', u'EG0256 - SOPS_RS - EIA RIMA')

AND  = (u'Em andamento', 'indeterminate')
REV  = (u'Em Revisão', 'indeterminate')
ENV  = (u'Enviado - Aguardando Análise', 'done')
ENV1 = (u'Enviado - Aguardando Análise1', 'done')
CONC = (u'Concluído', 'done')
MEDF = (u'Medido e Faturado', 'done')

PRE  = u'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)'
PAE  = u'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)'

# ---- itens ----
e0240_43 = I('EG0240-43', u'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-23', None, '2026-10-15T14:50:41.722-0300')
e0240_4  = I('EG0240-4', PRE, GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-23', None, '2026-10-15T13:58:30.870-0300')
e0240_5  = I('EG0240-5', PAE, GOITA[0], GOITA[1], REV[0], REV[1], '2026-10-26', None, '2026-10-15T13:58:00.568-0300')
e0274_38 = I('EG0274-38', u'Estudos de Tráfego', DNIT[0], DNIT[1], ENV[0], ENV[1], '2026-10-07', '2026-10-15T15:30:49.463-0300', '2026-10-15T15:30:49.471-0300')
e0274_43 = I('EG0274-43', u'Estudos Hidrológicos ', DNIT[0], DNIT[1], REV[0], REV[1], '2026-10-31', None, '2026-09-28T09:26:55.035-0300')
g54 = I('G0280-54', u'EBE Asa Branca', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-29', None, '2026-09-30T14:59:57.634-0300')
g55 = I('G0280-55', u'EBE Nova Brasília', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:43.601-0300')
g53 = I('G0280-53', u'EBE Gaspar Martins', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:30.308-0300')
g51 = I('G0280-51', u'EBE Baronesa do Gravataí', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T15:00:04.232-0300')
g50 = I('G0280-50', u'EBE Ponta da Cadeia', DMAE[0], DMAE[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:59:50.045-0300')
e0286_7  = I('EG0286-7', u'Estudo de tráfego', DNITAC[0], DNITAC[1], ENV[0], ENV[1], '2026-10-01', '2026-10-02T13:40:01.911-0300', '2026-10-02T13:40:01.929-0300')
e0286_11 = I('EG0286-11', u'Estudos hidrológicos', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-15', None, '2026-09-28T09:29:27.853-0300')
e0286_12 = I('EG0286-12', u'Levantamento ambiental', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-19', None, '2026-09-28T09:31:11.033-0300')
e0286_10 = I('EG0286-10', u'Estudos geológicos', DNITAC[0], DNITAC[1], AND[0], AND[1], '2026-10-30', None, '2026-09-30T14:55:35.086-0300')
e291_4   = I('EG291-4', u'PEB - Plano de Execução BIM', FEIJO[0], FEIJO[1], ENV[0], ENV[1], '2026-10-07', '2026-10-15T13:59:49.573-0300', '2026-10-15T14:05:50.668-0300')
e0275_112 = I('EG0275-112', u'Licenças Ambientais', CODEVASF[0], CODEVASF[1], ENV[0], ENV[1], '2026-09-04', '2026-10-02T09:27:36.092-0300', '2026-10-02T09:27:36.111-0300')
e0241_42 = I('EG0241-42', PRE, XAREU[0], XAREU[1], ENV[0], ENV[1], '2026-09-10', '2026-10-02T09:30:29.370-0300', '2026-10-02T09:30:46.892-0300')
e0239_28 = I('EG0239-28', PRE, CARPINA[0], CARPINA[1], ENV1[0], ENV1[1], '2026-08-10', '2026-10-09T09:36:29.171-0300', '2026-10-09T09:36:29.198-0300')
# maio/junho (visao acumulada)
e0239_26 = I('EG0239-26', u'TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', CARPINA[0], CARPINA[1], CONC[0], CONC[1], '2026-05-15', '2026-07-13T16:10:44.098-0300', '2026-07-14T15:00:07.129-0300')
e0274_39 = I('EG0274-39', u'Estudo de Concepção e Traçado', DNIT[0], DNIT[1], CONC[0], CONC[1], '2026-05-15', '2026-06-29T19:25:06.525-0300', '2026-09-28T09:26:14.228-0300')
g49 = I('G0280-49', u'EBE 5S', DMAE[0], DMAE[1], MEDF[0], MEDF[1], '2026-05-29', '2026-06-26T09:13:08.021-0300', '2026-09-30T11:24:05.018-0300')
g48 = I('G0280-48', u'EBE 4S', DMAE[0], DMAE[1], MEDF[0], MEDF[1], '2026-05-29', '2026-06-26T09:13:06.542-0300', '2026-09-30T11:24:03.760-0300')
g47 = I('G0280-47', u'EBE 3S', DMAE[0], DMAE[1], MEDF[0], MEDF[1], '2026-05-29', '2026-06-26T09:13:05.132-0300', '2026-09-30T11:24:02.649-0300')
g46 = I('G0280-46', u'EBE 2S', DMAE[0], DMAE[1], MEDF[0], MEDF[1], '2026-05-29', '2026-06-26T09:13:03.281-0300', '2026-09-30T11:24:01.415-0300')
g45 = I('G0280-45', u'EBE 1S', DMAE[0], DMAE[1], MEDF[0], MEDF[1], '2026-05-29', '2026-06-26T09:13:01.173-0300', '2026-09-30T11:23:59.909-0300')
e0256_24 = I('EG0256-24', u'Diagnóstico Ambiental - Meio Físico - Condições Meteorológicas', SOPS[0], SOPS[1], ENV1[0], ENV1[1], '2026-06-30', '2026-06-29T11:06:29.534-0300', '2026-06-29T11:06:39.573-0300')

DATA = {
 'planned_2026-10': [e0240_43, e0240_4, e0240_5, e0274_38, e0274_43, g54, g55, g53, g51, g50,
                     e0286_7, e0286_11, e0286_12, e0286_10, e291_4],
 'overdue_2026-10': [],
 'sent_2026-10':    [e291_4, e0286_7, e0275_112, e0274_38, e0241_42, e0240_5],
 'resolved_2026-10':[e291_4, e0286_7, e0275_112, e0274_38, e0241_42, e0239_28],
 'rework_2026-10':  [e0286_7, e0274_38, e0241_42, e0240_5],
 'planned_2026-05': [e0239_26, e0274_39, g49, g48, g47, g46, g45],
 'planned_2026-06': [e0256_24],
}

for name, rows in DATA.items():
    with io.open(os.path.join(SNAPDIR, name + '.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)
    print(name, len(rows))
