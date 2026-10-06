# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-06 ~13:30 UTC (10:30 BRT). Mes corrente: 2026-10.
# Os 6 conjuntos de out/2026 foram reconsultados ao vivo via MCP Atlassian.
# ETQ = issuetype in ("Epic","Fluxo de trabalho"); cloudId ead785de-...
# planned em 2 consultas (10-01..10-15 = 12, 10-16..10-31 = 17) -> 29.
# lookahead em 2 consultas (nov = 14, dez = 7) -> 21.
# getVisibleJiraProjects NAO reconsultado (chaves ja constam de _projects_min.json).
# Meses congelados (<= 2026-09) NAO sao reconsultados.
# OBS: ARTIFACT_HTML (Documents\Claude\Artifacts\...) e local protegido e nao e
#      legivel por device_bash; o HTML ao vivo foi obtido via staging do artifact
#      (list_legacy_live_artifacts + device_stage_files) e conferido por md5
#      contra o template versionado _artifact_src.html -> identicos.
import json, os
D = os.path.dirname(os.path.abspath(__file__))
K = '2026-10'

PJ = {
 'EG0256': 'EG0256 - SOPS_RS - EIA RIMA',
 'EG0274': 'EG0274 - DNIT',
 'EG0286': 'EG0286 - DNIT/AC ',
 'EG291':  'EG0291 - Arroio Feijó',
 'G0280':  'EG0280 - DMAE',
 'EG0239': 'EG0239 - CARPINA/ COMPESA',
 'EG0240': 'EG0240 - GOITÁ/ COMPESA',
 'EG0285': 'EG0285 - EMBASA - BARREIRAS',
 'EG0294': 'EG0294 - ARTLOT - Topografia',
 'EG0241': 'EG0241 - XARÉU/ COMPESA',
 'EG0275': 'EG0275 - CODEVASF',
}
CAT = {
 'Em andamento': 'indeterminate',
 'Tarefas pendentes': 'new',
 'Em Revisão': 'indeterminate',
 'Enviado - Aguardando Análise': 'done',
}

def I(key, summary, status, duedate, updated, resolutiondate=None):
    pk = key.rsplit('-', 1)[0]
    return {'key': key, 'fields': {
        'summary': summary,
        'status': {'name': status, 'statusCategory': {'key': CAT[status]}},
        'project': {'key': pk, 'name': PJ[pk]},
        'duedate': duedate,
        'resolutiondate': resolutiondate,
        'updated': updated}}

PLANNED = [
 I('EG0256-28','Diagnóstico Ambiental - Meio Físico - Recursos Hídricos','Em andamento','2026-10-01','2026-04-07T13:44:09.762-0300'),
 I('EG0274-63','Proj. Básico - Projeto de Sinalização e Segurança Viária','Tarefas pendentes','2026-10-06','2026-05-28T17:47:13.793-0300'),
 I('EG0274-59','Proj. Básico - Projeto de Drenagem e OAC','Tarefas pendentes','2026-10-06','2026-05-28T17:47:24.997-0300'),
 I('EG0274-38','Estudos de Tráfego','Em Revisão','2026-10-07','2026-10-02T13:51:19.692-0300'),
 I('EG0286-7','Estudo de tráfego','Enviado - Aguardando Análise','2026-10-01','2026-10-02T13:40:01.929-0300','2026-10-02T13:40:01.911-0300'),
 I('EG0286-21','Projeto de sinalização e segurança viária (pb)','Tarefas pendentes','2026-10-12','2026-06-17T17:38:54.156-0300'),
 I('EG0286-20','Projeto de obras complementares - oc (pb)','Tarefas pendentes','2026-10-12','2026-06-17T17:38:44.118-0300'),
 I('EG0286-17','Projeto de pavimentação (pb)','Tarefas pendentes','2026-10-14','2026-06-17T17:38:32.376-0300'),
 I('EG0286-16','Projeto de drenagem (pb)','Tarefas pendentes','2026-10-14','2026-06-17T17:38:28.787-0300'),
 I('EG0286-15','Projeto de terraplenagem (pb)','Tarefas pendentes','2026-10-14','2026-06-17T17:38:22.692-0300'),
 I('EG0286-11','Estudos hidrológicos','Em andamento','2026-10-15','2026-09-28T09:29:27.853-0300'),
 I('EG291-4','PEB - Plano de Execução BIM','Em andamento','2026-10-07','2026-10-05T09:55:25.830-0300'),
 I('EG0256-30','Diagnóstico Ambiental - Meio Antrópico','Em andamento','2026-10-31','2026-06-03T14:39:13.026-0300'),
 I('EG0274-64','Proj. Básico - Projeto de Componentes Ambientais e Paisagismo','Em andamento','2026-10-25','2026-07-01T16:15:49.824-0300'),
 I('EG0274-62','Proj. Básico - Projeto de Obras Complementares','Tarefas pendentes','2026-10-25','2026-05-28T17:47:16.641-0300'),
 I('EG0274-61','Proj. Básico - Projetos de Contenções','Tarefas pendentes','2026-10-25','2026-05-28T17:47:19.482-0300'),
 I('EG0274-60','Proj. Básico - Projetos de OAEs','Tarefas pendentes','2026-10-25','2026-05-28T17:47:22.404-0300'),
 I('EG0274-21','Proj. Básico - Projeto de Pavimentação','Tarefas pendentes','2026-10-29','2026-09-25T09:56:37.062-0300'),
 I('EG0274-58','Proj. Básico - Projeto de Terraplenagem','Tarefas pendentes','2026-10-30','2026-09-25T09:56:03.350-0300'),
 I('EG0274-43','Estudos Hidrológicos ','Em Revisão','2026-10-31','2026-09-28T09:26:55.035-0300'),
 I('G0280-54','EBE Asa Branca','Em andamento','2026-10-29','2026-09-30T14:59:57.634-0300'),
 I('G0280-55','EBE Nova Brasília','Em andamento','2026-10-30','2026-09-30T14:59:43.601-0300'),
 I('G0280-53','EBE Gaspar Martins','Em andamento','2026-10-30','2026-09-30T14:59:30.308-0300'),
 I('G0280-51','EBE Baronesa do Gravataí','Em andamento','2026-10-30','2026-09-30T15:00:04.232-0300'),
 I('G0280-50','EBE Ponta da Cadeia','Em andamento','2026-10-30','2026-09-30T14:59:50.045-0300'),
 I('EG0286-12','Levantamento ambiental','Em andamento','2026-10-19','2026-09-28T09:31:11.033-0300'),
 I('EG0286-23','Projeto de desapropriação (pb)','Tarefas pendentes','2026-10-20','2026-06-17T17:39:00.759-0300'),
 I('EG0286-22','Projeto de componentes ambientais e paisagismo (pb)','Tarefas pendentes','2026-10-22','2026-06-17T17:38:57.611-0300'),
 I('EG0286-10','Estudos geológicos','Em andamento','2026-10-30','2026-09-30T14:55:35.086-0300'),
]

OVERDUE = [
 I('EG0239-28','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)','Em Revisão','2026-08-10','2026-09-21T10:55:55.586-0300'),
 I('EG0240-5','TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)','Em Revisão','2026-09-30','2026-09-21T10:07:17.904-0300'),
]

LOOKAHEAD = [
 I('EG0286-19','Projeto de contenções (pb)','Tarefas pendentes','2026-11-03','2026-06-17T17:38:40.836-0300'),
 I('EG0285-16','RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ','Tarefas pendentes','2026-11-03','2026-05-14T11:31:20.526-0300'),
 I('EG0285-8','ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)','Em Revisão','2026-11-03','2026-09-30T11:46:00.212-0300'),
 I('EG0285-18','SERVIÇOS GEOTÉCNICOS','Tarefas pendentes','2026-11-09','2026-05-14T11:31:30.030-0300'),
 I('EG0285-14','RELATÓRIO GEOTÉCNICO ','Tarefas pendentes','2026-11-09','2026-05-14T11:31:11.610-0300'),
 I('EG0294-3','São Roque','Tarefas pendentes','2026-11-18','2026-10-02T13:45:46.124-0300'),
 I('EG0294-2','Navegantes/Artlot','Tarefas pendentes','2026-11-18','2026-10-02T13:45:37.682-0300'),
 I('EG0294-1','Baía/Artlot','Tarefas pendentes','2026-11-18','2026-10-02T13:45:29.242-0300'),
 I('EG0286-6','Estudo de traçado','Tarefas pendentes','2026-11-18','2026-09-30T11:08:02.268-0300'),
 I('EG0274-66','Proj. Básico - Orçamento e Plano de Execução da Obra','Tarefas pendentes','2026-11-18','2026-05-28T17:47:05.587-0300'),
 I('EG0274-65','Proj. Básico - Projeto de Desapropriação','Tarefas pendentes','2026-11-18','2026-05-28T17:47:08.171-0300'),
 I('G0280-75','Administração e Coordenação do Contrato','Em andamento','2026-11-30','2026-09-30T11:29:49.398-0300'),
 I('EG0274-57','Proj. Básico - Projeto Geométrico e Interseções','Tarefas pendentes','2026-11-30','2026-08-20T17:04:14.132-0300'),
 I('EG0241-45','Administração e Coordenação do Contrato','Tarefas pendentes','2026-11-30','2026-09-21T14:45:40.371-0300'),
 I('EG0286-18','Projeto de obras de arte especiais (pb)','Tarefas pendentes','2026-12-03','2026-06-17T17:38:36.976-0300'),
 I('EG0286-14','Projeto geométrico e de interseções (pb)','Tarefas pendentes','2026-12-09','2026-09-30T11:08:32.515-0300'),
 I('EG0286-24','Orçamento e plano de execução de obra (pb)','Tarefas pendentes','2026-12-16','2026-06-17T17:39:06.103-0300'),
 I('EG0286-9','Estudo geotécnico de subleito/ e ocorrências','Tarefas pendentes','2026-12-30','2026-09-30T11:08:11.622-0300'),
 I('EG0275-108','Administração e Coordenação do Contrato','Em andamento','2026-12-31','2026-05-05T09:21:58.639-0300'),
 I('EG0240-44','Administração e Coordenação do Contrato','Em andamento','2026-12-31','2026-05-05T09:21:36.085-0300'),
 I('EG0239-54','Administração e Coordenação do Contrato','Em andamento','2026-12-31','2026-05-11T16:20:36.026-0300'),
]

_e7  = I('EG0286-7','Estudo de tráfego','Enviado - Aguardando Análise','2026-10-01','2026-10-02T13:40:01.929-0300','2026-10-02T13:40:01.911-0300')
_112 = I('EG0275-112','Licenças Ambientais','Enviado - Aguardando Análise','2026-09-04','2026-10-02T09:27:36.111-0300','2026-10-02T09:27:36.092-0300')
_42  = I('EG0241-42','TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)','Enviado - Aguardando Análise','2026-09-10','2026-10-02T09:30:46.892-0300','2026-10-02T09:30:29.370-0300')

SETS = {'planned': PLANNED, 'overdue': OVERDUE, 'lookahead': LOOKAHEAD,
        'sent': [_e7, _112, _42], 'resolved': [_e7, _112, _42], 'rework': [_e7, _42]}

print('--- diff vs rodada anterior ---')
for name, data in SETS.items():
    p = os.path.join(D, '%s_%s.json' % (name, K))
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else []
    ok, nk = [i['key'] for i in old], [i['key'] for i in data]
    if old == data:
        print('%-10s sem alteracao (%d)' % (name, len(nk)))
        continue
    if set(ok) == set(nk):
        print('%-10s campos alterados (%d itens, mesmas chaves)' % (name, len(nk)))
    else:
        print('%-10s ALTERADO %d->%d  +%s  -%s' % (name, len(ok), len(nk),
              sorted(set(nk)-set(ok)) or '-', sorted(set(ok)-set(nk)) or '-'))
    json.dump(data, open(p, 'w', encoding='utf-8'), ensure_ascii=False)
    print('           -> %s reescrito' % os.path.basename(p))
