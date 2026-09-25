# -*- coding: utf-8 -*-
# Reconferencia ao vivo em 2026-09-25 (sessao agendada).
# As 6 consultas de setembro/2026 foram refeitas no Jira com
# ETQ = issuetype in ("Epic","Fluxo de trabalho") e devolveram exatamente os
# mesmos registros de _run0922h.py / _verify0924c.py:
#   planned=20, overdue=2, sent=5, resolved=4, rework=2, lookahead=27
# mesmas chaves, mesma ordem, mesmos status, duedate, resolutiondate e updated.
# getVisibleJiraProjects: 20 projetos, mesmas 20 chaves de _projects_min.json
# (CREA, EG0232, EG0235, EG0239, EG0240, EG0241, EG0256, EG0257, EG0272,
#  EG0273, EG0274, EG0275, EG0285, EG0286, EG0287, EG0292, EG291, G0120,
#  G0280, PE); tipos de nivel Epic = [Epic, Fluxo de trabalho].
# Artifact: desta vez a copia ao vivo foi obtida direto do desktop
# (device_stage_files artifact_ids=pr03-relatorio-indicadores-epics) e conferida:
# md5 6a2b6462a4efbec1890af4494a7f0b74 -- identico a _artifact_src.html.
# Nenhum _snap/*.json precisou ser reescrito; a geracao apenas renovou o
# carimbo de data/hora do snapshot.
import sys, os
D = os.path.expanduser('~/mnt/pr03-relatorio-publico/_snap')
sys.path.insert(0, D)
# sem delta: os datasets ja gravados continuam validos.
