# -*- coding: utf-8 -*-
"""Conjuntos consultados ao vivo em 2026-10-21 ~05:3x UTC (21/10 02:3x BRT).
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
 'EG0285': 'EG0285 - EMBASA - BARREIRAS',
 'EG0286': 'EG0286 - DNIT/AC ',
 'EG0294': 'EG0294 - ARTLOT - Topografia',
 'EG291':  'EG0291 - Arroio Feijó',
 'G0280':  'EG0280 - DMAE',
}
REV  = ('Em Revisão', 'indeterminate')
AND  = ('Em andamento', 'indeterminate')
PEN  = ('Tarefas pendentes', 'new')
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
 EG0286_7,
 EG291_4,
 EG0274_38,
 r('EG0286-11', 'Estudos hidrológicos', AND, 'EG0286', '2026-10-15', None, '2026-09-28T09:29:27.853-0300'),
 r('EG0286-12', 'Levantamento ambiental', AND, 'EG0286', '2026-10-19', None, '2026-09-28T09:31:11.033-0300'),
 r('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', REV, 'EG0240', '2026-10-23', None, '2026-10-15T14:50:41.722-0300'),
 r('EG0240-4', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', REV, 'EG0240', '2026-10-23', None, '2026-10-15T13:58:30.870-0300'),
 EG0240_5,
 r('G0280-54', 'EBE Asa Branca', AND, 'G0280', '2026-10-29', None, '2026-09-30T14:59:57.634-0300'),
 r('G0280-55', 'EBE Nova Brasília', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:43.601-0300'),
 r('G0280-53', 'EBE Gaspar Martins', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:30.308-0300'),
 r('G0280-51', 'EBE Baronesa do Gravataí', AND, 'G0280', '2026-10-30', None, '2026-09-30T15:00:04.232-0300'),
 r('G0280-50', 'EBE Ponta da Cadeia', AND, 'G0280', '2026-10-30', None, '2026-09-30T14:59:50.045-0300'),
 r('EG0286-10', 'Estudos geológicos', AND, 'EG0286', '2026-10-30', None, '2026-09-30T14:55:35.086-0300'),
 r('EG0274-43', 'Estudos Hidrológicos ', REV, 'EG0274', '2026-10-31', None, '2026-09-28T09:26:55.035-0300'),
]
DATA['overdue_2026-10']  = []
DATA['sent_2026-10']     = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0240_5]
DATA['resolved_2026-10'] = [EG291_4, EG0286_7, EG0275_112, EG0274_38, EG0241_42, EG0239_28]
DATA['rework_2026-10']   = [EG0286_7, EG0274_38, EG0241_42, EG0240_5]

DATA['lookahead_2026-10'] = [
 r('EG0286-19', 'Projeto de contenções (pb)', PEN, 'EG0286', '2026-11-03', None, '2026-06-17T17:38:40.836-0300'),
 r('EG0285-16', 'RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ', PEN, 'EG0285', '2026-11-03', None, '2026-05-14T11:31:20.526-0300'),
 r('EG0285-8', 'ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)', REV, 'EG0285', '2026-11-03', None, '2026-09-30T11:46:00.212-0300'),
 r('EG0285-18', 'SERVIÇOS GEOTÉCNICOS', PEN, 'EG0285', '2026-11-09', None, '2026-05-14T11:31:30.030-0300'),
 r('EG0285-14', 'RELATÓRIO GEOTÉCNICO ', PEN, 'EG0285', '2026-11-09', None, '2026-05-14T11:31:11.610-0300'),
 r('EG0294-3', 'São Roque', PEN, 'EG0294', '2026-11-18', None, '2026-10-02T13:45:46.124-0300'),
 r('EG0294-2', 'Navegantes/Artlot', PEN, 'EG0294', '2026-11-18', None, '2026-10-02T13:45:37.682-0300'),
 r('EG0294-1', 'Baía/Artlot', PEN, 'EG0294', '2026-11-18', None, '2026-10-02T13:45:29.242-0300'),
 r('EG0286-6', 'Estudo de traçado', PEN, 'EG0286', '2026-11-18', None, '2026-09-30T11:08:02.268-0300'),
 r('G0280-75', 'Administração e Coordenação do Contrato', AND, 'G0280', '2026-11-30', None, '2026-09-30T11:29:49.398-0300'),
 r('EG0241-45', 'Administração e Coordenação do Contrato', PEN, 'EG0241', '2026-11-30', None, '2026-09-21T14:45:40.371-0300'),
 r('EG0286-18', 'Projeto de obras de arte especiais (pb)', PEN, 'EG0286', '2026-12-03', None, '2026-06-17T17:38:36.976-0300'),
 r('EG0286-14', 'Projeto geométrico e de interseções (pb)', PEN, 'EG0286', '2026-12-09', None, '2026-09-30T11:08:32.515-0300'),
 r('EG0274-64', 'Proj. Básico - Projeto de Componentes Ambientais e Paisagismo', AND, 'EG0274', '2026-12-16', None, '2026-10-07T15:10:38.615-0300'),
 r('EG0286-23', 'Projeto de desapropriação (pb)', PEN, 'EG0286', '2026-12-22', None, '2026-10-07T15:14:52.336-0300'),
 r('EG0274-57', 'Proj. Básico - Projeto Geométrico e Interseções', PEN, 'EG0274', '2026-12-28', None, '2026-10-07T15:12:37.179-0300'),
 r('EG0286-9', 'Estudo geotécnico de subleito/ e ocorrências', PEN, 'EG0286', '2026-12-30', None, '2026-09-30T11:08:11.622-0300'),
 r('EG0274-66', 'Proj. Básico - Orçamento e Plano de Execução da Obra', PEN, 'EG0274', '2026-12-30', None, '2026-10-07T15:12:55.017-0300'),
 r('EG0274-65', 'Proj. Básico - Projeto de Desapropriação', PEN, 'EG0274', '2026-12-30', None, '2026-10-07T15:12:50.939-0300'),
 r('EG0274-59', 'Proj. Básico - Projeto de Drenagem e OAC', PEN, 'EG0274', '2026-12-30', None, '2026-10-07T15:12:39.174-0300'),
 r('EG0274-21', 'Proj. Básico - Projeto de Pavimentação', PEN, 'EG0274', '2026-12-30', None, '2026-10-07T15:10:59.297-0300'),
 r('EG0286-22', 'Projeto de componentes ambientais e paisagismo (pb)', PEN, 'EG0286', '2026-12-31', None, '2026-10-07T16:39:37.820-0300'),
 r('EG0286-17', 'Projeto de pavimentação (pb)', PEN, 'EG0286', '2026-12-31', None, '2026-10-07T15:14:36.171-0300'),
 r('EG0286-16', 'Projeto de drenagem (pb)', PEN, 'EG0286', '2026-12-31', None, '2026-10-07T15:14:39.402-0300'),
 r('EG0286-15', 'Projeto de terraplenagem (pb)', PEN, 'EG0286', '2026-12-31', None, '2026-10-07T15:14:41.891-0300'),
 r('EG0275-108', 'Administração e Coordenação do Contrato', AND, 'EG0275', '2026-12-31', None, '2026-05-05T09:21:58.639-0300'),
 r('EG0274-63', 'Proj. Básico - Projeto de Sinalização e Segurança Viária', PEN, 'EG0274', '2026-12-31', None, '2026-10-07T15:12:47.131-0300'),
 r('EG0274-62', 'Proj. Básico - Projeto de Obras Complementares', PEN, 'EG0274', '2026-12-31', None, '2026-10-07T15:12:42.729-0300'),
 r('EG0274-61', 'Proj. Básico - Projetos de Contenções', PEN, 'EG0274', '2026-12-31', None, '2026-10-07T15:10:17.792-0300'),
 r('EG0274-60', 'Proj. Básico - Projetos de OAEs', PEN, 'EG0274', '2026-12-31', None, '2026-10-07T15:11:13.308-0300'),
 r('EG0274-58', 'Proj. Básico - Projeto de Terraplenagem', PEN, 'EG0274', '2026-12-31', None, '2026-10-07T15:10:03.315-0300'),
 r('EG0240-44', 'Administração e Coordenação do Contrato', AND, 'EG0240', '2026-12-31', None, '2026-05-05T09:21:36.085-0300'),
 r('EG0239-54', 'Administração e Coordenação do Contrato', AND, 'EG0239', '2026-12-31', None, '2026-05-11T16:20:36.026-0300'),
]

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
