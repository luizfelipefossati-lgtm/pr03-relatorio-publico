# -*- coding: utf-8 -*-
# Reconferencia ao vivo em 2026-09-24 ~18:28 UTC (15:28 BRT), rodada seguinte a
# _verify0924c.py. As 6 consultas de setembro/2026 foram refeitas no Jira com
# ETQ = issuetype in ("Epic","Fluxo de trabalho") e devolveram exatamente os
# mesmos registros: planned=20, overdue=2, sent=5, resolved=4, rework=2,
# lookahead=27 -- mesmas chaves, mesma ordem, mesmos status e prazos.
# getVisibleJiraProjects: 20 projetos, mesmas 20 chaves de _projects_min.json
# (CREA..PE). Artifact: a pasta do artifact nao esta montada nesta sessao
# (somente pr03-relatorio-publico); usada a copia local _artifact_src.html,
# md5 6a2b6462a4efbec1890af4494a7f0b74 -- identico ao usado nas geracoes
# anteriores. Nenhum _snap/*.json precisou ser reescrito; a geracao apenas
# renovou o carimbo de data/hora do snapshot.
# Verificacao headless (Chromium/Playwright) sobre uma copia byte a byte do
# index.html publicado: 2 requisicoes (o proprio arquivo + chart.js do CDN),
# 0 para atlassian.net; 0 erros de JS; nenhum aviso de JQL sem correspondencia;
# unica mensagem de console = "[PR03] Snapshot estatico carregado - gerado em
# 2026-09-24T15:28:36-03:00"; __SNAPSHOT__ com 20 projetos e epicTypeNames
# [Epic, Fluxo de trabalho]; __HISTORY__ com 2026-04..2026-08; as 3 abas
# percorridas e os 5 canvas com dimensoes nao nulas.
import sys, os
D = os.path.expanduser('~/mnt/pr03-relatorio-publico/_snap')
sys.path.insert(0, D)
from _verify0924c import *  # noqa: F401,F403  (mesmos dados ao vivo, sem delta)
