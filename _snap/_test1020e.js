const fs=require('fs');
const src=fs.readFileSync('snapshot-data.js','utf8').replace(/^<script>/,'').replace(/<\/script>\s*$/,'');
global.window={}; global.console=console;
eval(src);
const ET='issuetype in ("Epic","Fluxo de trabalho")';
const months=[['2026-05','2026-05-01','2026-05-31'],['2026-06','2026-06-01','2026-06-30'],
 ['2026-07','2026-07-01','2026-07-31'],['2026-08','2026-08-01','2026-08-31'],
 ['2026-09','2026-09-01','2026-09-30'],['2026-10','2026-10-01','2026-10-31']];
const qs=[];
for(const [m,s,e] of months) qs.push(['planned_'+m, ET+' AND duedate>="'+s+'" AND duedate<="'+e+'" ORDER BY project ASC, duedate ASC']);
qs.push(['overdue_2026-10', ET+' AND duedate<"2026-10-01" AND statusCategory!=Done ORDER BY duedate ASC']);
qs.push(['lookahead_2026-10', ET+' AND duedate>="2026-11-01" AND duedate<="2026-12-31" ORDER BY duedate ASC']);
qs.push(['sent_2026-10', ET+' AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31")']);
qs.push(['resolved_2026-10', ET+' AND statusCategory=Done AND resolved>="2026-10-01" AND resolved<="2026-10-31"']);
qs.push(['rework_2026-10', ET+' AND status changed to "Enviado - Aguardando Análise" DURING ("2026-10-01","2026-10-31") AND status changed from "Enviado - Aguardando Análise"']);
let fail=0;
(async()=>{
 for(const [name,jql] of qs){
   const r=await window.cowork.callMcpTool('searchJiraIssuesUsingJql',{jql});
   const n=r.structuredContent.issues.nodes;
   const exp=window.__SNAPSHOT__.datasets[name];
   const ok=JSON.stringify(n)===JSON.stringify(exp);
   if(!ok)fail++;
   const f=n[0]&&n[0].fields;
   console.log((ok?'OK  ':'FAIL')+'  '+name+'  n='+n.length+(f?'  campos='+(f.status&&f.status.name?'ok':'FALTA'):''));
 }
 const p=await window.cowork.callMcpTool('getVisibleJiraProjects',{});
 console.log('projetos:', p.structuredContent.values.length, '| epicTypes:', window.__SNAPSHOT__.epicTypeNames.join(', '));
 console.log('historico meses:', Object.keys(window.__HISTORY__).join(', '));
 console.log(fail===0?'TODAS AS CONSULTAS RESOLVERAM':'FALHAS: '+fail);
})();
