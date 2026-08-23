/* ===========================================================================
   PR.03 — Relatorio de Indicadores de EPICs — DADOS ESTATICOS DO SNAPSHOT
   Gerado em: 2026-08-23 (America/Sao_Paulo)
   Fonte: Jira Cloud ead785de-33f3-4746-9bdb-a2a58cf5213b (projetos-engeplus)
   Este arquivo congela os dados e desliga qualquer consulta ao vivo ao Jira.
   Nao contem accountIds, e-mails nem avatares.
   =========================================================================== */
(function () {
  'use strict';

  var GEN = '2026-08-23';

  /* --- nomes de projeto (evita repeticao) --- */
  var P239 = 'EG0239 - CARPINA/ COMPESA',
      P240 = 'EG0240 - GOITÁ/ COMPESA',
      P241 = 'EG0241 - XARÉU/ COMPESA',
      P256 = 'EG0256 - SOPS_RS - EIA RIMA',
      P273 = 'EG0273 - DNIT AP',
      P274 = 'EG0274 - DNIT',
      P275 = 'EG0275 - CODEVASF',
      P280 = 'EG0280 - DMAE',
      P285 = 'EG0285 - EMBASA - BARREIRAS',
      P286 = 'EG0286 - DNIT/AC ',
      P287 = 'EG0287 - Dique de Camboriú';

  /* I(key, summary, statusName, statusCat, projKey, projName, duedate, resolutiondate, updated) */
  function I(k, s, n, c, pk, pn, d, r, u) {
    return {
      key: k,
      fields: {
        summary: s,
        status: { name: n, statusCategory: { key: c } },
        project: { key: pk, name: pn },
        duedate: d,
        resolutiondate: r,
        updated: u
      }
    };
  }
  /* L(key, summary, projKey) — objeto leve para sent/resolved/rework */
  function L(k, s, pk) {
    return { key: k, fields: { summary: s, project: { key: pk } } };
  }

  /* ======================= MARCO 2026 (acumulado) ======================= */
  var PL_03 = [
    I('EG0256-23', 'Áreas de Influência Direta e Indireta', 'Enviado - Aguardando Análise1', 'done', 'EG0256', P256, '2026-03-31', null, '2026-04-01T09:07:29.995-0300'),
    I('EG0273-2', 'Estudos Topográficos Complementares', 'Enviado - Aguardando Análise1', 'done', 'EG0273', P273, '2026-03-05', '2026-03-09T20:28:03.860-0300', '2026-05-19T09:31:01.762-0300'),
    I('EG0274-17', 'Caracterização Funcional/Estrutural do Pavimento', 'Enviado - Aguardando Análise', 'done', 'EG0274', P274, '2026-03-06', '2026-03-12T08:59:10.783-0300', '2026-03-12T08:59:10.803-0300'),
    I('EG0274-40', 'Estudos Topográficos, interferências e cadastramento de OAE/OAC  ', 'Medido e Faturado', 'done', 'EG0274', P274, '2026-03-13', '2026-03-23T14:51:02.855-0300', '2026-07-31T09:31:15.122-0300'),
    I('EG0274-41', 'Estudos Geotécnicos', 'Em andamento', 'indeterminate', 'EG0274', P274, '2026-03-25', null, '2026-03-27T09:06:10.644-0300'),
    I('EG0287-6', 'RT 1 - Diagnóstico, Estudo de Concepção e Proposição de Alternativas', 'Enviado - Aguardando Análise', 'done', 'EG0287', P287, '2026-03-27', '2026-04-15T13:55:50.095-0300', '2026-04-27T09:25:08.131-0300'),
    I('EG0287-9', 'RT 6 - Projeto Executivo', 'Enviado - Aguardando Análise', 'done', 'EG0287', P287, '2026-03-31', '2026-04-15T13:55:40.520-0300', '2026-04-15T13:55:40.541-0300')
  ];

  /* ========================== JULHO 2026 =========================== */
  var PL_07 = [
    I('EG0239-27', 'TOMO Vl - PAE', 'Concluído', 'done', 'EG0239', P239, '2026-07-10', '2026-07-14T15:00:18.092-0300', '2026-08-03T09:48:29.168-0300'),
    I('EG0241-43', 'TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'Medido e Faturado', 'done', 'EG0241', P241, '2026-07-06', '2026-07-09T09:40:19.623-0300', '2026-07-13T09:17:31.776-0300'),
    I('EG0256-27', 'Diagnóstico Ambiental - Meio Físico - Avaliação Agrícola', 'Enviado - Aguardando Análise1', 'done', 'EG0256', P256, '2026-07-31', '2026-07-27T10:58:30.736-0300', '2026-07-27T10:59:14.278-0300'),
    I('EG0256-26', 'Diagnóstico Ambiental - Meio Físico - Pedologia', 'Enviado - Aguardando Análise1', 'done', 'EG0256', P256, '2026-07-31', '2026-07-27T10:58:40.378-0300', '2026-07-27T10:59:07.601-0300'),
    I('EG0256-25', 'Diagnóstico Ambiental - Meio Físico - Geologia e Geomorfologia', 'Enviado - Aguardando Análise1', 'done', 'EG0256', P256, '2026-07-31', '2026-07-27T10:58:45.012-0300', '2026-07-27T10:59:11.112-0300'),
    I('EG0274-38', 'Estudos de Tráfego', 'Em Revisão', 'indeterminate', 'EG0274', P274, '2026-07-17', null, '2026-07-03T17:49:06.646-0300'),
    I('EG0274-43', 'Estudos Hidrológicos ', 'Enviado - Aguardando Análise', 'done', 'EG0274', P274, '2026-07-15', '2026-08-21T11:38:34.684-0300', '2026-08-21T11:38:34.692-0300'),
    I('EG0275-5', 'Relatório Parcial Projeto Básico', 'Concluído', 'done', 'EG0275', P275, '2026-07-15', '2026-07-03T10:16:50.117-0300', '2026-07-03T10:16:50.137-0300'),
    I('EG0275-20', 'Atividades Complementares', 'Concluído', 'done', 'EG0275', P275, '2026-07-17', '2026-02-19T10:39:29.318-0300', '2026-05-15T13:36:14.177-0300'),
    I('EG0286-2', 'Relatório de planejamento de atividades', 'Enviado - Aguardando Análise', 'done', 'EG0286', P286, '2026-07-17', '2026-07-28T16:08:52.158-0300', '2026-07-28T16:08:52.179-0300')
  ];

  var OV_07 = [
    I('EG0274-41', 'Estudos Geotécnicos', 'Em andamento', 'indeterminate', 'EG0274', P274, '2026-03-25', null, '2026-03-27T09:06:10.644-0300')
  ];

  var LK_07 = [
    I('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'Enviado - Aguardando Análise', 'done', 'EG0241', P241, '2026-08-07', '2026-08-20T17:08:46.275-0300', '2026-08-20T17:08:46.294-0300'),
    I('EG0286-9', 'Estudo geotécnico de subleito/ e ocorrências', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-08', null, '2026-06-17T17:37:13.728-0300'),
    I('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Enviado - Aguardando Análise1', 'done', 'EG0239', P239, '2026-08-10', '2026-08-11T14:33:08.831-0300', '2026-08-11T14:33:08.855-0300'),
    I('G0280-51', 'EBE Baronesa do Gravataí', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-08-14', null, '2026-06-25T15:42:21.024-0300'),
    I('EG0286-12', 'Levantamento ambiental', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-24', null, '2026-07-28T16:06:56.265-0300'),
    I('EG0286-11', 'Estudos hidrológicos', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-24', null, '2026-07-30T09:33:02.337-0300'),
    I('EG0286-10', 'Estudos geológicos', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-26', null, '2026-07-30T09:33:11.828-0300'),
    I('EG0286-8', 'Estudo topográfico', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-31', null, '2026-07-30T09:33:06.932-0300'),
    I('EG0286-7', 'Estudo de tráfego', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-31', null, '2026-07-30T09:37:47.572-0300'),
    I('EG0286-6', 'Estudo de traçado', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-31', null, '2026-07-28T16:06:13.739-0300'),
    I('EG0275-112', 'Licenças Ambientais', 'Em andamento', 'indeterminate', 'EG0275', P275, '2026-08-31', null, '2026-08-19T09:40:10.499-0300'),
    I('EG0241-42', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Em Revisão', 'indeterminate', 'EG0241', P241, '2026-08-31', null, '2026-08-19T10:59:55.028-0300'),
    I('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', 'Em Revisão', 'indeterminate', 'EG0240', P240, '2026-08-31', null, '2026-08-11T14:42:26.748-0300'),
    I('EG0240-4', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Tarefas pendentes', 'new', 'EG0240', P240, '2026-08-31', null, '2026-08-11T14:39:18.595-0300'),
    I('EG0275-6', 'Relatório Final Projeto Básico', 'Em Revisã', 'indeterminate', 'EG0275', P275, '2026-09-04', null, '2026-08-11T14:54:01.361-0300'),
    I('G0280-53', 'EBE Gaspar Martins', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-08', null, '2026-07-28T16:03:46.832-0300'),
    I('EG0286-13', 'Estudo geotécnico - sondagem para oae', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-09-14', null, '2026-07-03T11:07:40.831-0300'),
    I('G0280-52', 'EBE Barros Cassal', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-09-16', null, '2026-07-28T16:05:36.102-0300'),
    I('G0280-50', 'EBE Ponta da Cadeia', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-09-16', null, '2026-07-28T16:04:10.678-0300'),
    I('EG0274-58', 'Proj. Básico - Projeto de Terraplenagem', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-09-17', null, '2026-05-28T17:47:27.192-0300'),
    I('EG0274-21', 'Proj. Básico - Projeto de Pavimentação', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-09-17', null, '2026-05-28T17:47:32.287-0300'),
    I('EG0285-19', 'SERVIÇOS TOPOGRÁFICOS', 'Em andamento', 'indeterminate', 'EG0285', P285, '2026-09-18', null, '2026-05-18T10:57:07.064-0300'),
    I('G0280-54', 'EBE Asa Branca', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-22', null, '2026-07-28T16:03:54.494-0300'),
    I('G0280-55', 'EBE Nova Brasília', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-29', null, '2026-07-28T16:04:01.727-0300'),
    I('EG0286-14', 'Projeto geométrico e de interseções (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-09-29', null, '2026-06-17T17:38:16.515-0300'),
    I('EG0241-45', 'Administração e Coordenação do Contrato', 'Tarefas pendentes', 'new', 'EG0241', P241, '2026-09-30', null, '2026-04-16T17:08:58.500-0300'),
    I('EG0240-5', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'Em Revisão', 'indeterminate', 'EG0240', P240, '2026-09-30', null, '2026-07-31T17:27:54.489-0300')
  ];

  var SENT_07 = [
    L('EG0286-2', 'Relatório de planejamento de atividades', 'EG0286'),
    L('EG0285-8', 'ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)', 'EG0285'),
    L('EG0274-44', 'Levantamento Ambiental', 'EG0274'),
    L('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'EG0241'),
    L('EG0241-43', 'TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'EG0241')
  ];
  var RES_07 = [
    L('EG0286-2', 'Relatório de planejamento de atividades', 'EG0286'),
    L('EG0275-5', 'Relatório Parcial Projeto Básico', 'EG0275'),
    L('EG0256-27', 'Diagnóstico Ambiental - Meio Físico - Avaliação Agrícola', 'EG0256'),
    L('EG0256-26', 'Diagnóstico Ambiental - Meio Físico - Pedologia', 'EG0256'),
    L('EG0256-25', 'Diagnóstico Ambiental - Meio Físico - Geologia e Geomorfologia', 'EG0256'),
    L('EG0241-43', 'TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'EG0241'),
    L('EG0239-27', 'TOMO Vl - PAE', 'EG0239'),
    L('EG0239-26', 'TOMO IV -  PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'EG0239')
  ];
  var RW_07 = [
    L('EG0286-2', 'Relatório de planejamento de atividades', 'EG0286'),
    L('EG0285-8', 'ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)', 'EG0285'),
    L('EG0274-44', 'Levantamento Ambiental', 'EG0274'),
    L('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'EG0241'),
    L('EG0241-43', 'TOMO IV - PLANO DE OPERAÇÃO, MANUTENÇÃO E INSTRUMENTAÇÃO (POMI)', 'EG0241')
  ];

  /* ========================== AGOSTO 2026 ========================== */
  var PL_08 = [
    I('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Enviado - Aguardando Análise1', 'done', 'EG0239', P239, '2026-08-10', '2026-08-11T14:33:08.831-0300', '2026-08-11T14:33:08.855-0300'),
    I('EG0240-43', 'TOMO IV - PROJETO DE INSTRUMENTAÇÃO', 'Em Revisão', 'indeterminate', 'EG0240', P240, '2026-08-31', null, '2026-08-11T14:42:26.748-0300'),
    I('EG0240-4', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Tarefas pendentes', 'new', 'EG0240', P240, '2026-08-31', null, '2026-08-11T14:39:18.595-0300'),
    I('EG0241-42', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'Em Revisão', 'indeterminate', 'EG0241', P241, '2026-08-31', null, '2026-08-19T10:59:55.028-0300'),
    I('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'Enviado - Aguardando Análise', 'done', 'EG0241', P241, '2026-08-07', '2026-08-20T17:08:46.275-0300', '2026-08-20T17:08:46.294-0300'),
    I('EG0275-112', 'Licenças Ambientais', 'Em andamento', 'indeterminate', 'EG0275', P275, '2026-08-31', null, '2026-08-19T09:40:10.499-0300'),
    I('G0280-51', 'EBE Baronesa do Gravataí', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-08-14', null, '2026-06-25T15:42:21.024-0300'),
    I('EG0286-9', 'Estudo geotécnico de subleito/ e ocorrências', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-08', null, '2026-06-17T17:37:13.728-0300'),
    I('EG0286-12', 'Levantamento ambiental', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-24', null, '2026-07-28T16:06:56.265-0300'),
    I('EG0286-11', 'Estudos hidrológicos', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-24', null, '2026-07-30T09:33:02.337-0300'),
    I('EG0286-10', 'Estudos geológicos', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-26', null, '2026-07-30T09:33:11.828-0300'),
    I('EG0286-8', 'Estudo topográfico', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-31', null, '2026-07-30T09:33:06.932-0300'),
    I('EG0286-7', 'Estudo de tráfego', 'Em andamento', 'indeterminate', 'EG0286', P286, '2026-08-31', null, '2026-07-30T09:37:47.572-0300'),
    I('EG0286-6', 'Estudo de traçado', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-08-31', null, '2026-07-28T16:06:13.739-0300')
  ];

  var OV_08 = [
    I('EG0274-41', 'Estudos Geotécnicos', 'Em andamento', 'indeterminate', 'EG0274', P274, '2026-03-25', null, '2026-03-27T09:06:10.644-0300'),
    I('EG0274-38', 'Estudos de Tráfego', 'Em Revisão', 'indeterminate', 'EG0274', P274, '2026-07-17', null, '2026-07-03T17:49:06.646-0300')
  ];

  var LK_08 = [
    I('EG0275-6', 'Relatório Final Projeto Básico', 'Em Revisã', 'indeterminate', 'EG0275', P275, '2026-09-04', null, '2026-08-11T14:54:01.361-0300'),
    I('G0280-53', 'EBE Gaspar Martins', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-08', null, '2026-07-28T16:03:46.832-0300'),
    I('EG0286-13', 'Estudo geotécnico - sondagem para oae', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-09-14', null, '2026-07-03T11:07:40.831-0300'),
    I('G0280-52', 'EBE Barros Cassal', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-09-16', null, '2026-07-28T16:05:36.102-0300'),
    I('G0280-50', 'EBE Ponta da Cadeia', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-09-16', null, '2026-07-28T16:04:10.678-0300'),
    I('EG0274-58', 'Proj. Básico - Projeto de Terraplenagem', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-09-17', null, '2026-05-28T17:47:27.192-0300'),
    I('EG0274-21', 'Proj. Básico - Projeto de Pavimentação', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-09-17', null, '2026-05-28T17:47:32.287-0300'),
    I('EG0285-19', 'SERVIÇOS TOPOGRÁFICOS', 'Em andamento', 'indeterminate', 'EG0285', P285, '2026-09-18', null, '2026-05-18T10:57:07.064-0300'),
    I('G0280-54', 'EBE Asa Branca', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-22', null, '2026-07-28T16:03:54.494-0300'),
    I('G0280-55', 'EBE Nova Brasília', 'Tarefas pendentes', 'new', 'G0280', P280, '2026-09-29', null, '2026-07-28T16:04:01.727-0300'),
    I('EG0286-14', 'Projeto geométrico e de interseções (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-09-29', null, '2026-06-17T17:38:16.515-0300'),
    I('EG0241-45', 'Administração e Coordenação do Contrato', 'Tarefas pendentes', 'new', 'EG0241', P241, '2026-09-30', null, '2026-04-16T17:08:58.500-0300'),
    I('EG0240-5', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'Em Revisão', 'indeterminate', 'EG0240', P240, '2026-09-30', null, '2026-07-31T17:27:54.489-0300'),
    I('G0280-75', 'Administração e Coordenação do Contrato', 'Em andamento', 'indeterminate', 'G0280', P280, '2026-10-01', null, '2026-03-16T15:13:40.422-0300'),
    I('EG0256-28', 'Diagnóstico Ambiental - Meio Físico - Recursos Hídricos', 'Em andamento', 'indeterminate', 'EG0256', P256, '2026-10-01', null, '2026-04-07T13:44:09.762-0300'),
    I('EG0274-63', 'Proj. Básico - Projeto de Sinalização e Segurança Viária', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-10-06', null, '2026-05-28T17:47:13.793-0300'),
    I('EG0274-59', 'Proj. Básico - Projeto de Drenagem e OAC', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-10-06', null, '2026-05-28T17:47:24.997-0300'),
    I('EG0286-21', 'Projeto de sinalização e segurança viária (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-12', null, '2026-06-17T17:38:54.156-0300'),
    I('EG0286-20', 'Projeto de obras complementares - oc (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-12', null, '2026-06-17T17:38:44.118-0300'),
    I('EG0286-17', 'Projeto de pavimentação (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-14', null, '2026-06-17T17:38:32.376-0300'),
    I('EG0286-16', 'Projeto de drenagem (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-14', null, '2026-06-17T17:38:28.787-0300'),
    I('EG0286-15', 'Projeto de terraplenagem (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-14', null, '2026-06-17T17:38:22.692-0300'),
    I('EG0286-23', 'Projeto de desapropriação (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-20', null, '2026-06-17T17:39:00.759-0300'),
    I('EG0286-22', 'Projeto de componentes ambientais e paisagismo (pb)', 'Tarefas pendentes', 'new', 'EG0286', P286, '2026-10-22', null, '2026-06-17T17:38:57.611-0300'),
    I('EG0274-64', 'Proj. Básico - Projeto de Componentes Ambientais e Paisagismo', 'Em andamento', 'indeterminate', 'EG0274', P274, '2026-10-25', null, '2026-07-01T16:15:49.824-0300'),
    I('EG0274-62', 'Proj. Básico - Projeto de Obras Complementares', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-10-25', null, '2026-05-28T17:47:16.641-0300'),
    I('EG0274-61', 'Proj. Básico - Projetos de Contenções', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-10-25', null, '2026-05-28T17:47:19.482-0300'),
    I('EG0274-60', 'Proj. Básico - Projetos de OAEs', 'Tarefas pendentes', 'new', 'EG0274', P274, '2026-10-25', null, '2026-05-28T17:47:22.404-0300'),
    I('EG0256-30', 'Diagnóstico Ambiental - Meio Antrópico', 'Em andamento', 'indeterminate', 'EG0256', P256, '2026-10-31', null, '2026-06-03T14:39:13.026-0300')
  ];

  var SENT_08 = [
    L('EG0274-43', 'Estudos Hidrológicos ', 'EG0274'),
    L('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'EG0241')
  ];
  var RES_08 = [
    L('EG0285-8', 'ESTUDOS DE CONCEPÇÃO E VIABILIDADE (RECV)', 'EG0285'),
    L('EG0274-43', 'Estudos Hidrológicos ', 'EG0274'),
    L('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'EG0241'),
    L('EG0239-28', 'TOMO V - PROJETO DE RECUPERAÇÃO ESTRUTURAL (PRE)', 'EG0239')
  ];
  var RW_08 = [
    L('EG0274-43', 'Estudos Hidrológicos ', 'EG0274'),
    L('EG0241-44', 'TOMO VI - PLANO DE AÇÃO EMERGENCIAL (PAE)', 'EG0241')
  ];

  /* ---- consolida sent+resolved (mesma regra do artifact: sent primeiro) ---- */
  function mergeSent(sent, resolved, rework) {
    var seen = {}, out = [], rw = {};
    rework.forEach(function (i) { rw[i.key] = true; });
    sent.concat(resolved).forEach(function (i) {
      if (seen[i.key]) return;
      seen[i.key] = true;
      out.push({ key: i.key, sm: i.fields.summary, pj: i.fields.project.key, rw: !!rw[i.key] });
    });
    out.sort(function (a, b) { return a.rw === b.rw ? 0 : (a.rw ? -1 : 1); });
    return { total: out.length, rework: out.filter(function (x) { return x.rw; }).length, details: out };
  }

  var SNAP = {
    generated: GEN,
    epicTypeNames: ['Epic', 'Fluxo de trabalho'],
    projects: [
      { key: 'CREA', name: 'GESTÃO - CREA ', issueTypes: [{ name: 'Epic', hierarchyLevel: 1 }, { name: 'Fluxo de trabalho', hierarchyLevel: 1 }] },
      { key: 'EG0232', name: 'EG0232 - EMBASA' },
      { key: 'EG0235', name: 'EG0235 - SEMOBI' },
      { key: 'EG0239', name: P239 },
      { key: 'EG0240', name: P240 },
      { key: 'EG0241', name: P241 },
      { key: 'EG0256', name: P256 },
      { key: 'EG0257', name: 'EG0257 - DMAE ' },
      { key: 'EG0272', name: 'EG0272 - CASAN' },
      { key: 'EG0273', name: P273 },
      { key: 'EG0274', name: P274 },
      { key: 'EG0275', name: P275 },
      { key: 'EG0285', name: P285 },
      { key: 'EG0286', name: P286 },
      { key: 'EG0287', name: P287 },
      { key: 'EG0292', name: 'EG0292 - PREFEITURA DE BLUMENAU' },
      { key: 'G0120', name: 'EG0120 - DAER' },
      { key: 'G0280', name: P280 },
      { key: 'PE', name: 'Projetos -  Engenharia' }
    ],
    months: {
      '2026-03': { planned: PL_03, overdue: [], look: [], sent: [], resolved: [], rework: [] },
      '2026-07': { planned: PL_07, overdue: OV_07, look: LK_07, sent: SENT_07, resolved: RES_07, rework: RW_07 },
      '2026-08': { planned: PL_08, overdue: OV_08, look: LK_08, sent: SENT_08, resolved: RES_08, rework: RW_08 }
    }
  };

  window.__SNAPSHOT__ = SNAP;

  /* ---- injeta os periodos no cache historico do artifact ---- */
  window.__HISTORY__ = window.__HISTORY__ || {};

  window.__HISTORY__['2026-03'] = {
    planned: PL_03, overdue: [], sent: { total: 0, rework: 0, details: [] }, look: [],
    period: { s: '2026-03-01', e: '2026-03-31', l: 'Março 2026', m: 2, y: 2026 },
    _frozen_at: GEN,
    _note: 'Periodo encerrado. Dados congelados pelo snapshot estatico.'
  };

  window.__HISTORY__['2026-07'] = {
    planned: PL_07, overdue: OV_07, sent: mergeSent(SENT_07, RES_07, RW_07), look: LK_07,
    period: { s: '2026-07-01', e: '2026-07-31', l: 'Julho 2026', m: 6, y: 2026 },
    _frozen_at: GEN,
    _note: 'Periodo encerrado. Dados congelados pelo snapshot estatico.'
  };

  window.__HISTORY__['2026-08'] = {
    planned: PL_08, overdue: OV_08, sent: mergeSent(SENT_08, RES_08, RW_08), look: LK_08,
    period: { s: '2026-08-01', e: '2026-08-31', l: 'Agosto 2026', m: 7, y: 2026 },
    _frozen_at: GEN,
    _note: 'Mes corrente na data do snapshot. Dados congelados em ' + GEN + '.'
  };

  /* ---- desliga o acesso ao vivo: callMcpTool servido pelo snapshot ---- */
  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  function resolveJql(jql) {
    jql = String(jql || '');
    var m, key, d;

    // rework / sent  (status changed to "Enviado - Aguardando Analise" DURING (...))
    if (/status\s+changed\s+to\s+"Enviado/i.test(jql)) {
      m = /DURING\s*\(\s*"(\d{4})-(\d{2})/i.exec(jql);
      key = m ? m[1] + '-' + m[2] : null;
      d = key && SNAP.months[key];
      if (!d) return [];
      return /status\s+changed\s+from\s+"Enviado/i.test(jql) ? d.rework : d.sent;
    }

    // resolved no periodo
    if (/resolved\s*>=/i.test(jql)) {
      m = /resolved\s*>=\s*"(\d{4})-(\d{2})/i.exec(jql);
      key = m ? m[1] + '-' + m[2] : null;
      d = key && SNAP.months[key];
      return d ? d.resolved : [];
    }

    // atrasados acumulados (duedate < inicio do mes AND statusCategory != Done)
    if (/statusCategory\s*!=\s*Done/i.test(jql) && /duedate\s*</.test(jql)) {
      m = /duedate\s*<\s*"(\d{4})-(\d{2})/.exec(jql);
      key = m ? m[1] + '-' + m[2] : null;
      d = key && SNAP.months[key];
      return d ? d.overdue : [];
    }

    // janela de duedate: mesmo mes => planned; meses futuros => lookahead
    var ge = /duedate\s*>=\s*"(\d{4})-(\d{2})-\d{2}"/.exec(jql);
    var le = /duedate\s*<=\s*"(\d{4})-(\d{2})-\d{2}"/.exec(jql);
    if (ge && le) {
      var k1 = ge[1] + '-' + ge[2], k2 = le[1] + '-' + le[2];
      if (k1 === k2) {
        d = SNAP.months[k1];
        return d ? d.planned : [];
      }
      // lookahead: chaveado pelo mes IMEDIATAMENTE ANTERIOR ao inicio da janela
      var y = parseInt(ge[1], 10), mi = parseInt(ge[2], 10) - 1;
      var py = mi === 0 ? y - 1 : y, pm = mi === 0 ? 12 : mi;
      d = SNAP.months[py + '-' + pad2(pm)];
      return d ? d.look : [];
    }

    return [];
  }

  window.cowork = window.cowork || {};
  window.cowork.callMcpTool = function (tool, params) {
    var t = String(tool || '');
    if (/getVisibleJiraProjects/i.test(t)) {
      return Promise.resolve({ values: SNAP.projects, total: SNAP.projects.length, isLast: true });
    }
    if (/searchJiraIssuesUsingJql/i.test(t)) {
      return Promise.resolve({
        issues: { nodes: resolveJql(params && params.jql) },
        isLast: true
      });
    }
    return Promise.resolve({ isLast: true });
  };
  window.cowork.askClaude = function () { return Promise.resolve(''); };
  window.cowork.runScheduledTask = function () { return Promise.resolve({ ok: false, offline: true }); };

  console.log('[PR03] Snapshot estatico carregado — gerado em ' + GEN + '; consultas ao Jira desativadas.');
})();
