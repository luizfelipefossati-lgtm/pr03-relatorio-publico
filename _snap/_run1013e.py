# -*- coding: utf-8 -*-
# Rodada agendada 2026-10-13 ~16:30 UTC (13:30 BRT). Mes corrente: 2026-10.
# Assinaturas abaixo transcritas da resposta ao vivo do MCP Atlassian nesta rodada.
import json, os, hashlib
B = os.path.expanduser('~/mnt/pr03-relatorio-publico')
S = os.path.join(B, '_snap')
EAA = "Enviado - Aguardando Analise"  # so rotulo interno; comparacao usa o arquivo

TOMOV = "TOMO V - PROJETO DE RECUPERACAO ESTRUTURAL (PRE)"

# (key, summary, status.name, statusCategory.key, duedate, resolutiondate, updated)
LIVE = {
 'planned': [
  ("EG0240-4","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Em Revisão","indeterminate","2026-10-16",None,"2026-10-09T09:35:08.823-0300"),
  ("EG0274-38","Estudos de Tráfego","Em Revisão","indeterminate","2026-10-07",None,"2026-10-02T13:51:19.692-0300"),
  ("EG0274-43","Estudos Hidrológicos ","Em Revisão","indeterminate","2026-10-31",None,"2026-09-28T09:26:55.035-0300"),
  ("G0280-54","EBE Asa Branca","Em andamento","indeterminate","2026-10-29",None,"2026-09-30T14:59:57.634-0300"),
  ("G0280-55","EBE Nova Brasília","Em andamento","indeterminate","2026-10-30",None,"2026-09-30T14:59:43.601-0300"),
  ("G0280-53","EBE Gaspar Martins","Em andamento","indeterminate","2026-10-30",None,"2026-09-30T14:59:30.308-0300"),
  ("G0280-51","EBE Baronesa do Gravataí","Em andamento","indeterminate","2026-10-30",None,"2026-09-30T15:00:04.232-0300"),
  ("G0280-50","EBE Ponta da Cadeia","Em andamento","indeterminate","2026-10-30",None,"2026-09-30T14:59:50.045-0300"),
  ("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300","2026-10-02T13:40:01.929-0300"),
  ("EG0286-11","Estudos hidrológicos","Em andamento","indeterminate","2026-10-15",None,"2026-09-28T09:29:27.853-0300"),
  ("EG0286-12","Levantamento ambiental","Em andamento","indeterminate","2026-10-19",None,"2026-09-28T09:31:11.033-0300"),
  ("EG0286-10","Estudos geológicos","Em andamento","indeterminate","2026-10-30",None,"2026-09-30T14:55:35.086-0300"),
  ("EG291-4","PEB - Plano de Execução BIM","Em andamento","indeterminate","2026-10-07",None,"2026-10-07T15:27:45.699-0300"),
 ],
 'overdue': [
  ("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","2026-09-30",None,"2026-10-13T09:51:44.629-0300"),
 ],
 'sent': [
  ("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300","2026-10-02T13:40:01.929-0300"),
  ("EG0275-112","Licenças Ambientais","Enviado - Aguardando Análise","done","2026-09-04","2026-10-02T09:27:36.092-0300","2026-10-02T09:27:36.111-0300"),
  ("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
  ("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","2026-09-30",None,"2026-10-13T09:51:44.629-0300"),
 ],
 'resolved': [
  ("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300","2026-10-02T13:40:01.929-0300"),
  ("EG0275-112","Licenças Ambientais","Enviado - Aguardando Análise","done","2026-09-04","2026-10-02T09:27:36.092-0300","2026-10-02T09:27:36.111-0300"),
  ("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
  ("EG0239-28","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise1","done","2026-08-10","2026-10-09T09:36:29.171-0300","2026-10-09T09:36:29.198-0300"),
 ],
 'rework': [
  ("EG0286-7","Estudo de tráfego","Enviado - Aguardando Análise","done","2026-10-01","2026-10-02T13:40:01.911-0300","2026-10-02T13:40:01.929-0300"),
  ("EG0241-42","TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)","Enviado - Aguardando Análise","done","2026-09-10","2026-10-02T09:30:29.370-0300","2026-10-02T09:30:46.892-0300"),
  ("EG0240-5","TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)","Em Revisão","indeterminate","2026-09-30",None,"2026-10-13T09:51:44.629-0300"),
 ],
 'lookahead': [
  ("EG0286-19","Projeto de contenções (pb)","Tarefas pendentes","new","2026-11-03",None,"2026-06-17T17:38:40.836-0300"),
  ("EG0285-16","RELATÓRIO DOS IMPACTOS SOCIAIS (RIS) ","Tarefas pendentes","new","2026-11-03",None,"2026-05-14T11:31:20.526-0300"),
  ("EG0285-8","ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)","Em Revisão","indeterminate","2026-11-03",None,"2026-09-30T11:46:00.212-0300"),
  ("EG0285-18","SERVIÇOS GEOTÉCNICOS","Tarefas pendentes","new","2026-11-09",None,"2026-05-14T11:31:30.030-0300"),
  ("EG0285-14","RELATÓRIO GEOTÉCNICO ","Tarefas pendentes","new","2026-11-09",None,"2026-05-14T11:31:11.610-0300"),
  ("EG0294-3","São Roque","Tarefas pendentes","new","2026-11-18",None,"2026-10-02T13:45:46.124-0300"),
  ("EG0294-2","Navegantes/Artlot","Tarefas pendentes","new","2026-11-18",None,"2026-10-02T13:45:37.682-0300"),
  ("EG0294-1","Baía/Artlot","Tarefas pendentes","new","2026-11-18",None,"2026-10-02T13:45:29.242-0300"),
  ("EG0286-6","Estudo de traçado","Tarefas pendentes","new","2026-11-18",None,"2026-09-30T11:08:02.268-0300"),
  ("G0280-75","Administração e Coordenação do Contrato","Em andamento","indeterminate","2026-11-30",None,"2026-09-30T11:29:49.398-0300"),
  ("EG0241-45","Administração e Coordenação do Contrato","Tarefas pendentes","new","2026-11-30",None,"2026-09-21T14:45:40.371-0300"),
  ("EG0286-18","Projeto de obras de arte especiais (pb)","Tarefas pendentes","new","2026-12-03",None,"2026-06-17T17:38:36.976-0300"),
  ("EG0286-14","Projeto geométrico e de interseções (pb)","Tarefas pendentes","new","2026-12-09",None,"2026-09-30T11:08:32.515-0300"),
  ("EG0274-64","Proj. Básico - Projeto de Componentes Ambientais e Paisagismo","Em andamento","indeterminate","2026-12-16",None,"2026-10-07T15:10:38.615-0300"),
  ("EG0256-30","Diagnóstico Ambiental - Meio Antrópico","Em andamento","indeterminate","2026-12-19",None,"2026-10-08T11:14:55.973-0300"),
  ("EG0286-23","Projeto de desapropriação (pb)","Tarefas pendentes","new","2026-12-22",None,"2026-10-07T15:14:52.336-0300"),
  ("EG0274-57","Proj. Básico - Projeto Geométrico e Interseções","Tarefas pendentes","new","2026-12-28",None,"2026-10-07T15:12:37.179-0300"),
  ("EG0286-9","Estudo geotécnico de subleito/ e ocorrências","Tarefas pendentes","new","2026-12-30",None,"2026-09-30T11:08:11.622-0300"),
  ("EG0274-66","Proj. Básico - Orçamento e Plano de Execução da Obra","Tarefas pendentes","new","2026-12-30",None,"2026-10-07T15:12:55.017-0300"),
  ("EG0274-65","Proj. Básico - Projeto de Desapropriação","Tarefas pendentes","new","2026-12-30",None,"2026-10-07T15:12:50.939-0300"),
  ("EG0274-59","Proj. Básico - Projeto de Drenagem e OAC","Tarefas pendentes","new","2026-12-30",None,"2026-10-07T15:12:39.174-0300"),
  ("EG0274-21","Proj. Básico - Projeto de Pavimentação","Tarefas pendentes","new","2026-12-30",None,"2026-10-07T15:10:59.297-0300"),
  ("EG0286-22","Projeto de componentes ambientais e paisagismo (pb)","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T16:39:37.820-0300"),
  ("EG0286-17","Projeto de pavimentação (pb)","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:14:36.171-0300"),
  ("EG0286-16","Projeto de drenagem (pb)","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:14:39.402-0300"),
  ("EG0286-15","Projeto de terraplenagem (pb)","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:14:41.891-0300"),
  ("EG0275-108","Administração e Coordenação do Contrato","Em andamento","indeterminate","2026-12-31",None,"2026-05-05T09:21:58.639-0300"),
  ("EG0274-63","Proj. Básico - Projeto de Sinalização e Segurança Viária","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:12:47.131-0300"),
  ("EG0274-62","Proj. Básico - Projeto de Obras Complementares","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:12:42.729-0300"),
  ("EG0274-61","Proj. Básico - Projetos de Contenções","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:10:17.792-0300"),
  ("EG0274-60","Proj. Básico - Projetos de OAEs","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:11:13.308-0300"),
  ("EG0274-58","Proj. Básico - Projeto de Terraplenagem","Tarefas pendentes","new","2026-12-31",None,"2026-10-07T15:10:03.315-0300"),
  ("EG0240-44","Administração e Coordenação do Contrato","Em andamento","indeterminate","2026-12-31",None,"2026-05-05T09:21:36.085-0300"),
  ("EG0239-54","Administração e Coordenação do Contrato","Em andamento","indeterminate","2026-12-31",None,"2026-05-11T16:20:36.026-0300"),
 ],
}

def sig(i):
    f = i['fields']
    return (i['key'], f.get('summary'), f['status']['name'], f['status']['statusCategory']['key'],
            f.get('duedate'), f.get('resolutiondate'), f.get('updated'))

changed = []
for name, rows in LIVE.items():
    p = os.path.join(S, '%s_2026-10.json' % name)
    old = json.load(open(p, encoding='utf-8'))
    old_sig = [sig(i) for i in old]
    new_sig = [tuple(r) for r in rows]
    ok = (old_sig == new_sig)
    if not ok:
        changed.append(name)
        so, sn = {s[0] for s in old_sig}, {s[0] for s in new_sig}
        if so - sn: print('   - saiu  : %s' % ', '.join(sorted(so - sn)))
        if sn - so: print('   + entrou: %s' % ', '.join(sorted(sn - so)))
        for a, b in zip(old_sig, new_sig):
            if a != b: print('   ~ difere: %s\n          -> %s' % (a, b))
    h = hashlib.sha256(json.dumps(sorted(new_sig), ensure_ascii=False).encode('utf-8')).hexdigest()[:24]
    print('%-10s %2d itens (cache %2d) sig=%s %s' % (name, len(new_sig), len(old_sig), h,
          'IGUAL' if ok else '*** ALTERADO ***'))

print('ALTERADOS:', ', '.join(changed) if changed else '(nenhum)')
