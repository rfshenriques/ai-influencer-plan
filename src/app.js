(function(){
'use strict';
var D=window.__DATA__;
var MK={},NK={},PK={};
D.markets.forEach(function(m){MK[m.id]=m});D.niches.forEach(function(n){NK[n.id]=n});D.personas.forEach(function(p){PK[p.id]=p});
var PLK={};D.plan.forEach(function(s){PLK[s.id]=s});

/* ---------- storage ---------- */
var mem={};
function sget(k,d){try{var v=localStorage.getItem(k);return v==null?d:JSON.parse(v)}catch(e){return k in mem?mem[k]:d}}
function sset(k,v){mem[k]=v;try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}
var S=sget('aiplan.v1',{st:{},nt:{},ck:{},theme:'auto',f:{niche:'all',mkt:'all',g:'all'}});
function save(){sset('aiplan.v1',S)}
function applyTheme(){var r=document.documentElement;if(S.theme==='auto')r.removeAttribute('data-theme');else r.setAttribute('data-theme',S.theme);
 var dark=S.theme==='dark'||(S.theme==='auto'&&matchMedia('(prefers-color-scheme:dark)').matches);
 document.querySelectorAll('meta[name=theme-color]').forEach(function(m){m.setAttribute('content',dark?'#000000':'#F2F2F7')});}

/* ---------- helpers ---------- */
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
var copyStore=[];
function reg(t){copyStore.push(t);return copyStore.length-1}
var IC={
 person:'<circle cx="12" cy="8" r="3.6"/><path d="M4.5 20c.8-4 3.7-6 7.5-6s6.7 2 7.5 6"/>',
 grid:'<rect x="4" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="4" width="6.5" height="6.5" rx="1.6"/><rect x="4" y="13.5" width="6.5" height="6.5" rx="1.6"/><rect x="13.5" y="13.5" width="6.5" height="6.5" rx="1.6"/>',
 globe:'<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.6 2.6 3.6 5.5 3.6 8.5s-1 5.9-3.6 8.5c-2.6-2.6-3.6-5.5-3.6-8.5s1-5.9 3.6-8.5z"/>',
 plan:'<path d="M8 6h12M8 12h12M8 18h12"/><circle cx="4" cy="6" r=".6"/><circle cx="4" cy="12" r=".6"/><circle cx="4" cy="18" r=".6"/>',
 back:'<path d="M14.5 5.5L8 12l6.5 6.5"/>',
 search:'<circle cx="11" cy="11" r="6.5"/><path d="M20 20l-4.3-4.3"/>',
 fork:'<path d="M7 4v7a2 2 0 002 2v7M11 4v7a2 2 0 01-2 2M17 4c-2 2-2.5 5-2.5 8h2.5v8"/>',
 code:'<path d="M9 7l-5 5 5 5M15 7l5 5-5 5"/>',pen:'<path d="M4 20l1-4L16.5 4.5a2 2 0 013 3L8 19z"/>',
 ball:'<circle cx="12" cy="12" r="8.5"/><path d="M12 7l4 3-1.5 5h-5L8 10z"/>',bolt:'<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
 home:'<path d="M4 11l8-7 8 7v8.5a.5.5 0 01-.5.5H15v-5H9v5H4.5a.5.5 0 01-.5-.5z"/>',speech:'<path d="M4 6.5A2.5 2.5 0 016.5 4h11A2.5 2.5 0 0120 6.5v7a2.5 2.5 0 01-2.5 2.5H11l-4.5 4v-4A2.5 2.5 0 014 13.5z"/>',
 flag:'<path d="M5 21V4M5 5h12l-2 4 2 4H5"/>',steps:'<path d="M5 7h4M5 12h8M5 17h12"/>',hook:'<path d="M12 4v10a4 4 0 11-4-4"/>',tag:'<path d="M3.5 12.5V4.5h8l9 9-8 8z"/><circle cx="8" cy="9" r="1.2"/>',
 text:'<path d="M5 6h14M5 11h14M5 16h9"/>',eye:'<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
 mic:'<rect x="9" y="3.5" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"/>',shield:'<path d="M12 3.5l7 2.5v5.5c0 4.5-3 8-7 9.5-4-1.5-7-5-7-9.5V6z"/>',
 lock:'<rect x="5" y="10.5" width="14" height="10" rx="2.5"/><path d="M8.5 10.5V8a3.5 3.5 0 017 0v2.5"/>',scale:'<path d="M12 4v16M6 20h12M5 8h14M5 8l-2.5 6a3 3 0 005 0zM19 8l-2.5 6a3 3 0 005 0z"/>',calendar:'<rect x="4" y="5.5" width="16" height="14.5" rx="2.5"/><path d="M4 10h16M8.5 3.5v4M15.5 3.5v4"/>',
 gear:'<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.5 1.5M16.5 16.5L18 18M18 6l-1.5 1.5M7.5 16.5L6 18"/>',
 check:'<path d="M5 12.5l4.5 4.5L19 7.5"/>',filter:'<path d="M4 7h16M7 12h10M10 17h4"/>'
};
function svg(n,sw){return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="'+(sw||1.9)+'" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+IC[n]+'</svg>'}

var FLAG={
 us:'<rect width="36" height="24" fill="#fff"/>'+[0,2,4,6,8,10,12].map(function(i){return '<rect y="'+(i*24/13).toFixed(2)+'" width="36" height="'+(24/13).toFixed(2)+'" fill="#D22F3E"/>'}).join('')+'<rect width="16" height="'+(7*24/13).toFixed(2)+'" fill="#2B3A8C"/>'+[[3,2.5],[7,2.5],[11,2.5],[5,5.5],[9,5.5],[13,5.5],[3,8.5],[7,8.5],[11,8.5]].map(function(p){return '<circle cx="'+p[0]+'" cy="'+p[1]+'" r=".8" fill="#fff"/>'}).join(''),
 uk:'<rect width="36" height="24" fill="#243A7C"/><path d="M0 0L36 24M36 0L0 24" stroke="#fff" stroke-width="4.5"/><path d="M0 0L36 24M36 0L0 24" stroke="#CF2B3C" stroke-width="1.6"/><path d="M18 0v24M0 12h36" stroke="#fff" stroke-width="7"/><path d="M18 0v24M0 12h36" stroke="#CF2B3C" stroke-width="4"/>',
 es:'<rect width="12" height="24" fill="#1E8A4C"/><rect x="12" width="12" height="24" fill="#fff"/><rect x="24" width="12" height="24" fill="#D8343D"/><circle cx="18" cy="12" r="3.4" fill="#A9743B"/><circle cx="18" cy="12" r="1.7" fill="#1E8A4C"/>',
 br:'<rect width="36" height="24" fill="#1E9B4B"/><path d="M18 2.5L32 12 18 21.5 4 12z" fill="#F7D117"/><circle cx="18" cy="12" r="5.2" fill="#2A3E8E"/><path d="M13 11.2c3.5-1 7-.4 10 1.6" stroke="#fff" stroke-width="1" fill="none"/>',
 pt:'<rect width="36" height="24" fill="#D8343D"/><rect width="14" height="24" fill="#1E7A3C"/><circle cx="14" cy="12" r="4.6" fill="#F7D117"/><circle cx="14" cy="12" r="2.6" fill="#D8343D"/><circle cx="14" cy="12" r="1.2" fill="#fff"/>',
 fr:'<rect width="12" height="24" fill="#2A4DA0"/><rect x="12" width="12" height="24" fill="#fff"/><rect x="24" width="12" height="24" fill="#D8343D"/>',
 it:'<rect width="12" height="24" fill="#1E9B4B"/><rect x="12" width="12" height="24" fill="#fff"/><rect x="24" width="12" height="24" fill="#D8343D"/>',
 de:'<rect width="36" height="8" fill="#1C1C1E"/><rect y="8" width="36" height="8" fill="#D8343D"/><rect y="16" width="36" height="8" fill="#F7C61B"/>',
 fi:'<rect width="36" height="24" fill="#fff"/><rect x="9.5" width="5.5" height="24" fill="#2A4DA0"/><rect y="9.25" width="36" height="5.5" fill="#2A4DA0"/>',
 dk:'<rect width="36" height="24" fill="#D8343D"/><rect x="10" width="4.5" height="24" fill="#fff"/><rect y="9.75" width="36" height="4.5" fill="#fff"/>',
 no:'<rect width="36" height="24" fill="#D8343D"/><rect x="9" width="7" height="24" fill="#fff"/><rect y="8.5" width="36" height="7" fill="#fff"/><rect x="10.5" width="4" height="24" fill="#2A4DA0"/><rect y="10" width="36" height="4" fill="#2A4DA0"/>'
};
function flag(id,cls){return '<span class="fl '+(cls||'')+'" role="img" aria-label="'+esc(MK[id].name)+' flag"><svg viewBox="6 0 24 24" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'+FLAG[id]+'</svg></span>'}
function avHtml(p,cls){var n=NK[p.niche];return '<span class="av '+(cls||'')+' g'+p.g+'" style="'+cvars(n)+'">'+esc(p.name[0])+'<span class="nb" aria-hidden="true">'+svg(n.icon,2.2)+'</span></span>'}
var CHEV='<svg class="chev" viewBox="0 0 8 14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1.5 1.5L6.5 7l-5 5.5"/></svg>';
function cvars(n){return '--c1:'+n.color[0]+';--c2:'+n.color[1]}
function gtxt(g){return g==='w'?'Woman':'Man'}
function stText(s){return s==='ok'?'Approved':s==='skip'?'Skipped':'To review'}
function pStatus(id){return S.st[id]||'review'}
function wl(w){return w===0?'Pilot':'Wave '+w}
function tagW(w){return '<span class="tag w'+w+'">'+wl(w)+'</span>'}
function betTag(m){var b=m.bet[0];return '<span class="tag '+b+'">'+(b==='ok'?'Betting: allowed, strict rules':b==='no'?'Betting: not allowed':'Betting: verify')+'</span>'}

/* ---------- navigation state ---------- */
var nav={tab:'personas',stack:[],sec:'Overview'},scrolls=[];
var cur=function(){return nav.stack[nav.stack.length-1]||{v:nav.tab}};
var navbg=document.querySelector('.nav-bg'),root=document.getElementById('root'),top=document.getElementById('top'),tabbar=document.getElementById('tabbar'),toastEl=document.getElementById('toast');
var TABS=[['personas','Personas','person'],['niches','Niches','grid'],['markets','Languages','globe'],['plan','Plan','plan']];

/* ---------- views ---------- */
function blocksHtml(bl){
 return bl.map(function(b){
  var t=b[0];
  if(t==='h')return '<h2>'+esc(b[1])+'</h2>';
  if(t==='p')return '<p>'+esc(b[1])+'</p>';
  if(t==='note')return '<div class="note">'+esc(b[1])+'</div>';
  if(t==='list')return '<div class="card"><ul class="l">'+b[1].map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
  if(t==='steps')return '<div class="card"><ol class="s">'+b[1].map(function(x){return '<li><div class="st">'+esc(x[0])+'</div><div class="sd">'+esc(x[1])+'</div></li>'}).join('')+'</ol></div>';
  if(t==='cards')return b[1].map(function(x){return '<div class="card"><h3>'+esc(x[0])+'</h3><p style="margin:.2rem 0 0;color:var(--label2)">'+esc(x[1])+'</p></div>'}).join('');
  if(t==='prompt')return promptHtml(b[1],b[2]);
  if(t==='src')return srcHtml(b[1]);
  return '';
 }).join('');
}
function srcHtml(a){return '<h2>Sources</h2><div class="card"><ul class="l">'+a.map(function(x){return '<li><a href="'+esc(x[1])+'" target="_blank" rel="noopener noreferrer">'+esc(x[0])+'</a></li>'}).join('')+'</ul></div>'}
function resNicheHtml(r){
 if(!r)return '';
 var h='<h2>Research: what sells and how</h2>';
 var sec=[['What sells',r.sells],['How to present it',r.present],['How to sell it',r.how],['Watch out',r.watch]];
 sec.forEach(function(s){if(s[1]&&s[1].length)h+='<div class="card"><h3>'+s[0]+'</h3><ul class="l">'+s[1].map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>'});
 return h+srcHtml(r.src);
}
function resMarketHtml(r){
 if(!r)return '';
 var h='<h2>Research: this market</h2><div class="card">'+kv('Shop and selling',r.shop)+kv('Best fit',r.fit)+'</div>';
 h+='<div class="card"><h3>Rules to follow</h3><ul class="l">'+r.rules.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 h+='<div class="card"><h3>Audience and content</h3><ul class="l">'+r.culture.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 return h+srcHtml(r.src);
}
function promptHtml(title,text){
 return '<div class="ph"><h3>'+esc(title)+'</h3><button class="btn sm sec" data-do="copy" data-i="'+reg(text)+'">Copy</button></div><div class="prompt">'+esc(text)+'</div>';
}
function kv(k,v){return '<div class="kv"><div class="k">'+esc(k)+'</div><div class="v">'+esc(v)+'</div></div>'}
function personaRow(p){
 var n=NK[p.niche],m=MK[p.mkt];
 return '<button class="row" data-do="open" data-v="persona" data-id="'+p.id+'">'+avHtml(p)+
  '<span class="grow"><div class="t1">'+esc(p.name)+' · '+esc(n.name)+'</div><div class="t2">'+flag(p.mkt,'s')+esc(m.name)+' · '+gtxt(p.g)+' · '+wl(p.wave)+(pStatus(p.id)==='review'?'':' · '+stText(pStatus(p.id)))+'</div></span>'+CHEV+'</button>';
}
function filtered(){
 var f=S.f,q=(nav.q||'').toLowerCase().trim();
 return D.personas.filter(function(p){
  if(f.niche!=='all'&&p.niche!==f.niche)return false;
  if(f.mkt!=='all'&&p.mkt!==f.mkt)return false;
  if(f.g!=='all'&&p.g!==f.g)return false;
  if(q&&(p.name+' '+NK[p.niche].name+' '+MK[p.mkt].name+' '+p.angle).toLowerCase().indexOf(q)<0)return false;
  return true;
 });
}
function listHtml(){
 var l=filtered();
 if(!l.length)return '<div class="empty">No personas match these filters.</div>';
 return '<div class="grp">'+l.map(personaRow).join('')+'</div>';
}
function nFilters(){var f=S.f;return (f.niche!=='all'?1:0)+(f.mkt!=='all'?1:0)+(f.g!=='all'?1:0)}
function activeHtml(){
 var f=S.f,a=[];
 if(f.niche!=='all')a.push(['niche',NK[f.niche].name]);
 if(f.mkt!=='all')a.push(['mkt',MK[f.mkt].name]);
 if(f.g!=='all')a.push(['g',f.g==='w'?'Women':'Men']);
 if(!a.length)return '';
 return '<div class="act">'+a.map(function(x){return '<button class="ac" data-do="clear" data-k="'+x[0]+'" aria-label="Remove filter '+esc(x[1])+'">'+esc(x[1])+' <svg viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M2 2l8 8M10 2l-8 8"/></svg></button>'}).join('')+'</div>';
}
function countHtml(){var n=filtered().length;return '<div class="cnt">'+n+' of '+D.personas.length+' personas</div>'}
function fbtnHtml(){var nf=nFilters();return svg('filter')+(nf?'<span class="bd">'+nf+'</span>':'')}
function vPersonas(){
 var ok=0,sk=0;D.personas.forEach(function(p){var s=pStatus(p.id);if(s==='ok')ok++;if(s==='skip')sk++});
 var tot=D.personas.length,nf=nFilters();
 var h='<h1 class="lt">Personas</h1><p class="sub">'+tot+' personas across '+D.niches.length+' niches and '+D.markets.length+' markets. Tap one to read the whole plan.</p>';
 h+='<div class="sr"><div class="search">'+svg('search')+'<input id="q" type="search" inputmode="search" placeholder="Search" value="'+esc(nav.q||'')+'" aria-label="Search personas"></div>'+
  '<button class="fbtn" data-do="filters" aria-label="Filters'+(nf?', '+nf+' active':'')+'">'+fbtnHtml()+'</button></div>';
 h+='<div id="act">'+activeHtml()+'</div>';
 h+='<div id="cnt">'+countHtml()+'</div><div id="plist">'+listHtml()+'</div>';
 h+='<div class="card" style="margin-top:.9rem"><div style="display:flex;justify-content:space-between"><b>Review progress</b><span style="color:var(--label2)">'+ok+' approved · '+sk+' skipped</span></div><div class="bar"><i style="width:'+Math.round(ok/tot*100)+'%"></i></div></div>';
 return h;
}
function refreshList(){
 var l=document.getElementById('plist');if(!l)return;copyStore=[];
 l.innerHTML=listHtml();var a=document.getElementById('act');if(a)a.innerHTML=activeHtml();var c=document.getElementById('cnt');if(c)c.innerHTML=countHtml();
 var b=document.querySelector('.fbtn');if(b)b.innerHTML=fbtnHtml();
}
var sheetEl=null,scrimEl=null;
function optList(key,items){
 return '<div class="grp">'+items.map(function(i){return '<button class="opt" role="radio" aria-checked="'+(S.f[key]===i[0])+'" data-do="fset" data-k="'+key+'" data-v="'+i[0]+'"><span style="display:flex;align-items:center;gap:.6rem">'+(i[3]||'')+'<span>'+esc(i[1])+(i[2]?'<small>'+esc(i[2])+'</small>':'')+'</span></span>'+svg('check',2.6)+'</button>'}).join('')+'</div>';
}
function sheetBody(){
 var cnt={};D.personas.forEach(function(p){cnt[p.niche]=(cnt[p.niche]||0)+1});
 return '<div class="sl">Niche</div>'+optList('niche',[['all','All niches']].concat(D.niches.map(function(n){return [n.id,n.name,String(cnt[n.id])]})))+
  '<div class="sl">Language</div>'+optList('mkt',[['all','All languages']].concat(D.markets.map(function(m){return [m.id,m.name,'',flag(m.id)]})))+
  '<div class="sl">Gender</div><div class="seg" role="radiogroup" aria-label="Gender">'+[['all','All'],['w','Women'],['m','Men']].map(function(t){return '<button class="'+(t[0]==='w'?'gw':t[0]==='m'?'gm':'')+'" role="radio" aria-pressed="'+(S.f.g===t[0])+'" data-do="fset" data-k="g" data-v="'+t[0]+'">'+t[1]+'</button>'}).join('')+'</div>';
}
function sheetInner(){return '<div class="sh" id="sh"><button data-do="freset">Reset</button><b>Filters</b><button class="dn" data-do="fclose">Done</button></div><div class="sb" id="sb">'+sheetBody()+'</div>'}
function openSheet(){
 if(sheetEl)return;
 scrimEl=document.createElement('div');scrimEl.className='scrim';scrimEl.dataset.do='fclose';
 sheetEl=document.createElement('div');sheetEl.className='sheet';sheetEl.setAttribute('role','dialog');sheetEl.setAttribute('aria-modal','true');sheetEl.setAttribute('aria-label','Filters');
 sheetEl.innerHTML=sheetInner();
 document.body.appendChild(scrimEl);document.body.appendChild(sheetEl);
 requestAnimationFrame(function(){requestAnimationFrame(function(){if(scrimEl){scrimEl.classList.add('on');sheetEl.classList.add('on')}})});
 dragInit();
}
function closeSheet(){
 if(!sheetEl)return;var s=sheetEl,c=scrimEl;sheetEl=null;scrimEl=null;
 s.style.transform='';s.classList.remove('on');c.classList.remove('on');setTimeout(function(){s.remove();c.remove()},350);
}
function dragInit(){
 var sh=document.getElementById('sh'),y0=0,dy=0,t0=0,on=false;
 sh.addEventListener('touchstart',function(e){on=true;y0=e.touches[0].clientY;t0=Date.now();dy=0;sheetEl.style.transition='none'},{passive:true});
 sh.addEventListener('touchmove',function(e){if(!on)return;dy=Math.max(0,e.touches[0].clientY-y0);sheetEl.style.transform='translateY('+dy+'px)'},{passive:true});
 sh.addEventListener('touchend',function(){if(!on)return;on=false;var v=dy/Math.max(1,Date.now()-t0);sheetEl.style.transition='';if(dy>sheetEl.offsetHeight*.28||v>.5)closeSheet();else sheetEl.style.transform=''});
}
function vNiches(){
 var h='<h1 class="lt">Niches</h1><p class="sub">Seven niches. Open one for its format, series, clips and offer.</p><div class="grp">';
 D.niches.forEach(function(n){
  var c=D.personas.filter(function(p){return p.niche===n.id}).length;
  h+='<button class="row" data-do="open" data-v="niche" data-id="'+n.id+'"><span class="ic" style="'+cvars(n)+'">'+svg(n.icon)+'</span><span class="grow"><div class="t1">'+esc(n.name)+'</div><div class="t2">'+esc(n.tagline)+'</div></span><span class="t2">'+c+'</span>'+CHEV+'</button>';
 });
 return h+'</div>';
}
function vMarkets(){
 var h='<h1 class="lt">Languages</h1><p class="sub">Eleven markets. Open one for speech notes, rules and its personas.</p><div class="grp">';
 D.markets.forEach(function(m){
  var c=D.personas.filter(function(p){return p.mkt===m.id}).length;
  h+='<button class="row" data-do="open" data-v="market" data-id="'+m.id+'">'+flag(m.id,'m')+'<span class="grow"><div class="t1">'+esc(m.name)+'</div><div class="t2">'+esc(m.city)+' · '+c+' personas</div></span>'+CHEV+'</button>';
 });
 return h+'</div>';
}
function vPlan(){
 var h='<h1 class="lt">Plan</h1><p class="sub">How the business works: build steps, hooks, selling, rules and cost.</p><div class="grp">';
 D.plan.forEach(function(s){
  h+='<button class="row" data-do="open" data-v="plan" data-id="'+s.id+'"><span class="ic" style="--c1:#8B7CC7;--c2:#5A3B8C">'+svg(s.icon)+'</span><span class="grow"><div class="t1">'+esc(s.title)+'</div><div class="t2">'+esc(s.sub)+'</div></span>'+CHEV+'</button>';
 });
 h+='</div><h2>Appearance</h2><div class="seg" role="group" aria-label="Appearance">'+[['auto','Auto'],['light','Light'],['dark','Dark']].map(function(t){return '<button aria-pressed="'+(S.theme===t[0])+'" data-do="theme" data-v="'+t[0]+'">'+t[1]+'</button>'}).join('')+'</div>';
 h+='<div class="grp"><button class="row" data-do="export"><span class="grow"><div class="t1">Copy my review notes</div><div class="t2">Statuses, notes and checklists as text</div></span></button></div>';
 return h;
}
function vPlanPage(id){
 var s=PLK[id];
 return '<h1 class="lt">'+esc(s.title)+'</h1><p class="sub">'+esc(s.sub)+'</p>'+blocksHtml(s.blocks);
}
function vNiche(id){
 var n=NK[id],ps=D.personas.filter(function(p){return p.niche===id});
 var h='<div class="hero" style="'+cvars(n)+'"><div class="big">'+esc(n.name)+'</div><p>'+esc(n.tagline)+'</p></div>';
 h+='<div class="card"><div class="kv"><div class="k">What it is</div><div class="v">'+esc(n.what)+'</div></div><div class="kv"><div class="k">Why it works</div><div class="v">'+esc(n.why)+'</div></div><div class="kv"><div class="k">Genders</div><div class="v">'+esc(n.genders)+'</div></div></div>';
 h+='<h2>Content pillars</h2><div class="card"><ul class="l">'+n.pillars.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 h+='<h2>Series formats</h2>'+n.series.map(function(s){return '<div class="card"><h3>'+esc(s[0].replace('{cur}','')) +'</h3><p style="margin:.2rem 0 0;color:var(--label2)">'+esc(s[1])+'</p></div>'}).join('');
 h+='<h2>First 10 clips</h2><div class="card"><ol class="s">'+n.clips.map(function(c){return '<li><div class="st">'+esc(c[1].replace('{dish}','local dish').replace('{cur}','local currency '))+'</div><div class="sd">'+esc(c[0].replace('{cur}',''))+'</div></li>'}).join('')+'</ol></div>';
 h+='<h2>Hook patterns</h2><div class="card"><ul class="l">'+n.hooks.map(function(x){return '<li>'+esc(x.replace('{c}','first clip title'))+'</li>'}).join('')+'</ul></div>';
 h+='<h2>What it sells</h2><div class="card"><p style="margin-top:0">'+esc(n.offer)+'</p><div class="kv"><div class="k">Product ladder</div><div class="v">'+n.ladder.map(esc).join(' → ')+'</div></div></div>';
 h+=resNicheHtml(n.research);
 h+='<h2>Honesty and rules</h2><div class="note">'+esc(n.honesty)+'</div>';
 h+='<h2>What to measure</h2><div class="card"><ul class="l">'+n.kpis.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 if(id==='lang'){
  h+='<h2>30-episode plan</h2>'+D.epis.map(function(s,si){return '<div class="card"><h3>'+esc(s[0])+'</h3><ol class="s" style="counter-reset:s '+(si*10)+'">'+s[1].map(function(e){return '<li><div class="st">'+esc(e)+'</div></li>'}).join('')+'</ol></div>'}).join('');
 }
 h+='<h2>Personas in this niche</h2>';
 D.markets.forEach(function(m){
  var l=ps.filter(function(p){return p.mkt===m.id});if(!l.length)return;
  h+='<div class="grp">'+l.map(personaRow).join('')+'</div>';
 });
 return h;
}
function vMarket(id){
 var m=MK[id],ps=D.personas.filter(function(p){return p.mkt===id});
 var h='<div class="hero" style="--c1:#8B7CC7;--c2:#5A3B8C">'+flag(m.id)+'<div class="big">'+esc(m.name)+'</div><p>Target city: '+esc(m.city)+' · prices in '+esc(m.cur)+'</p></div>';
 h+='<div class="card">'+kv('Speak it as',m.speech)+kv('Voice accent',m.accent)+kv('Watch out for',m.watch)+kv('Natural filler words',m.fillers)+'</div>';
 h+=resMarketHtml(m.research);
 h+='<h2>Local details to show</h2><div class="card"><ul class="l">'+m.local.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 h+='<h2>AI label and sponsored posts</h2><div class="note">'+esc(m.ai)+'</div>';
 h+='<h2>Sports betting here</h2><p>'+betTag(m)+'</p><div class="card"><p style="margin:0">'+esc(m.bet[1])+'</p></div>';
 h+='<h2>Local dish for the food persona</h2><div class="card"><p style="margin:0">'+esc(m.dish)+'</p></div>';
 var lp=ps.filter(function(p){return p.niche==='lang'})[0];
 if(lp&&lp.ph){
  h+='<h2>Language-learning sample phrases</h2><div class="card">'+kv('Hello',lp.ph.hello[0]+'  '+lp.ph.hello[1])+kv('Thank you',lp.ph.thanks[0]+'  '+lp.ph.thanks[1])+kv('Where is the station?',lp.ph.station[0]+'  '+lp.ph.station[1])+'<div style="color:var(--label2);font-size:.875rem">Respellings are approximate. A native speaker must confirm every phrase.</div></div>';
 }
 h+='<h2>Personas</h2>';
 D.niches.forEach(function(n){
  var l=ps.filter(function(p){return p.niche===n.id});if(!l.length)return;
  h+='<div style="color:var(--label2);font-size:.8125rem;font-weight:600;margin:.4rem .25rem">'+esc(n.name)+'</div><div class="grp">'+l.map(personaRow).join('')+'</div>';
 });
 return h;
}

/* ---------- content plan ---------- */
function lgOf(p){return p.mkt==='pt'?'pt':'en'}
function pk(x,l){return x&&typeof x==='object'&&!Array.isArray(x)&&(x.en!==undefined||x.pt!==undefined)?x[l]:x}
function sb(s,p){return typeof s==='string'?s.replace(/\{name\}/g,p.name).replace(/\{city\}/g,MK[p.mkt].city).replace(/\{a\}/g,p.g==='w'?'a':'o').replace(/\{ora\}/g,p.g==='w'?'ora':'or'):s}
function bankOf(p){return D.bank[p.bank||p.niche]}
function planOf(p){var b=bankOf(p);return p.plan&&b?b:null}
function pdKey(p,t,i){return p.id+':'+t+i}
function isDone(p,t,i){return !!(S.pd&&S.pd[pdKey(p,t,i)])}
function doneBtn(p,t,i,o){var on=isDone(p,t,i);return '<button class="btn sm sec dn2" data-do="pdone" data-k="'+pdKey(p,t,i)+'" data-o="'+o+'" aria-pressed="'+on+'">'+(on?'Done':'Mark as done')+'</button>'}
function ul(a){return '<ul class="l">'+a.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul>'}
var KW={food:['RECIPE','RECEITA'],shred:['PLAN','PLANO'],code:['TRICKS','TRUQUES'],design:['PALETTE','PALETA'],gadget:['LINK','LINK'],home:['LINK','LINK'],lang:['WORKBOOK','CADERNO'],glam:['PAGE','PÁGINA']};
 function topicDone(p,n){return ['tp','ts','tr','tl'].filter(function(t){return isDone(p,t,n)}).length}
function calOf(){
 var c=[['Before launch',[['Day 0','i',-1],['Sun','t',0]]]];
 for(var w=0;w<4;w++){var b=3*w,r=[['Mon','r',b],['Tue','t',b+1],['Wed','r',b+1],['Fri','t',b+2],['Sat','r',b+2]];if(w<3)r.push(['Sun','t',b+3]);c.push(['Week '+(w+1),r])}
 return c;
}
function stepHead(n,t){return '<h3 class="sm">'+n+'. '+t+'</h3>'}
function topicHtml(p,x,n,L){
 var l=lgOf(p),en='en',open=nav.openItem==='t'+n,d=topicDone(p,n);
 var h='<details class="det" id="it-t'+n+'"'+(open?' open':'')+'><summary><span class="dnum'+(d===4?' ok':'')+'">'+(n+1)+'</span><span class="grow"><div class="t1">'+esc(sb(x.t,p))+'</div><div class="t2">'+d+' of 4 steps done</div></span>'+CHEV+'</summary><div class="db">';
 h+='<h3 class="sm">The problem it solves</h3><p class="pp">'+esc(sb(x.prob,p))+'</p>';
 h+='<h3 class="sm">Where it leads</h3><p class="pp">'+esc(p.offer||'')+'</p>';
 var wd=(bankOf(p).intro.world||[]).filter(function(w){return w.k===x.loc})[0];
 if(wd)h+='<h3 class="sm">Location lock</h3><p class="pp"><b>'+esc(wd.t)+'.</b> Use the saved empty-room reference image and this exact description in every photo, story and reel of this topic.</p>'+promptHtml('Locked description',wd.d);
 h+=stepHead(1,'Teaser photo (the day before)')+'<p class="pp">'+esc(sb(pk(x.ph,en),p))+'</p>'+promptHtml('Caption ('+L+')',sb(pk(x.cap,l),p));
 if(l!==en)h+='<div class="ref">English: '+esc(sb(pk(x.cap,en),p))+'</div>';
 h+=doneBtn(p,'tp',n,n);
 h+=stepHead(2,'Teaser story (the day before)')+ul(['Frame 1: a close crop of the teaser photo with the text "Tomorrow: '+sb(x.t,p)+'".','Frame 2: a poll or quiz sticker with the question below.','Frame 3: a countdown sticker for the reel tomorrow.'])+promptHtml('Sticker question ('+L+')',sb(pk(x.q,l),p));
 if(l!==en)h+='<div class="ref">English: '+esc(sb(pk(x.q,en),p))+'</div>';
 h+=doneBtn(p,'ts',n,n);
 var bs=x.b,says=bs.map(function(b){return pk(b[1],l)}),saysEn=bs.map(function(b){return pk(b[1],en)}),T=['0 to 3 s','3 to 9 s','9 to 12 s'];
 h+=stepHead(3,'The reel (day of posting)')+'<div><span class="tag">'+esc(x.tech)+'</span></div>';
 h+=promptHtml('Hook, first line ('+L+')',sb(says[0],p));
 h+='<h3 class="sm">Show and say at the same time</h3><ol class="s" style="counter-reset:s 0">'+bs.map(function(b,k){return '<li><div class="st">'+T[k]+'</div><div class="sd"><b>Show:</b> '+esc(sb(pk(b[0],en),p))+'</div><div class="sd"><b>Say:</b> '+esc(sb(says[k],p))+'</div></li>'}).join('')+'</ol>';
 h+=promptHtml('Full spoken script ('+L+')',sb(says.join(' '),p));
 if(l!==en)h+='<div class="ref">English: '+esc(sb(saysEn.join(' '),p))+'</div>';
 h+='<h3 class="sm">On-screen text</h3><p class="pp">'+esc(sb(pk(x.ot,l),p))+'</p>';
 h+='<h3 class="sm">What we show or teach</h3><p class="pp">'+esc(sb(x.te,p))+'</p>';
 h+=doneBtn(p,'tr',n,n);
 h+=stepHead(4,'Reel-is-live story (same day)')+ul(['Frame 1: the reel cover with the text "New reel".','Frame 2: the problem in one line: '+sb(x.prob,p),'Frame 3: a link sticker or "link in bio" pointing to: '+(p.offer||'the product')+'.'])+promptHtml('Soft sell line ('+L+')',sb(pk(x.cta,l),p))+promptHtml('Comment-to-DM line ('+L+', optional)',l==='pt'?'Comenta '+KW[p.bank||p.niche][1]+' e envio-te o link.':'Comment '+KW[p.bank||p.niche][0]+' and I will send you the link.')+'<p class="pp">Needs a DM automation tool (a few euros a month) so the link goes out by itself. Without it, reply by hand.</p>';
 h+=doneBtn(p,'tl',n,n)+'</div></details>';
 return h;
}
function setupHtml(p,b,L){
 var l=lgOf(p),en='en',it=b.intro,h='';
 h+='<div class="note">Post these before the first reel so the page is not empty. They use the same saved character, 4:5.</div>';
 h+='<h2>Intro photos</h2>'+it.photos.map(function(x,i){
  var d=isDone(p,'ip',i);
  return '<details class="det" id="it-i'+i+'"'+(nav.openItem==='i'+i?' open':'')+'><summary><span class="dnum'+(d?' ok':'')+'">'+(i+1)+'</span><span class="grow"><div class="t1">'+esc(sb(x.t,p))+'</div></span>'+CHEV+'</summary><div class="db"><h3 class="sm">What is in the frame</h3><p class="pp">'+esc(sb(x.img,p))+'</p><h3 class="sm">Why it is on the grid</h3><p class="pp">'+esc(sb(x.why,p))+'</p>'+promptHtml('Caption ('+L+')',sb(pk(x.cap,l),p))+(l!==en?'<div class="ref">English: '+esc(sb(pk(x.cap,en),p))+'</div>':'')+doneBtn(p,'ip',i,'i'+i)+'</div></details>'}).join('');
 var m=it.meet,dm=isDone(p,'im',0);
 h+='<h2>Intro story</h2><details class="det" id="it-m0"'+(nav.openItem==='m0'?' open':'')+'><summary><span class="dnum'+(dm?' ok':'')+'">1</span><span class="grow"><div class="t1">'+esc(sb(m.t,p))+'</div><div class="t2">'+esc(m.go)+'</div></span>'+CHEV+'</summary><div class="db"><h3 class="sm">Frames</h3>'+ul(m.fr.map(function(f){return sb(f,p)}))+'<h3 class="sm">Sticker</h3><p class="pp">'+esc(m.st)+'</p>'+(m.q?promptHtml('Question text ('+L+')',sb(pk(m.q,l),p)):'')+doneBtn(p,'im',0,'m0')+'</div></details>';
 var wl2=it.world;
 if(wl2&&wl2.length){h+='<h2>World bible: places that never change</h2><div class="note">Make each place once as an empty-room image with no person, save it, and use it as the reference image in every later generation together with the character sheet. A hotel room stays the same room for the whole trip, and her bedroom is the same bedroom in every reel, photo and story. Before posting, compare the new image with the reference: wall colour, bed, window, lamp, mirror.</div>'+wl2.map(function(w){return promptHtml(w.t,w.d)}).join('')}
 h+='<h2>How the product fits in</h2><div class="card"><ul class="l"><li>Product: '+esc(p.offer||'')+'</li><li>Bio line: '+esc(p.bio||'')+'</li><li>Every reel ends with one calm line that points to the product. The photo before it teases, the story before it asks a question, and the story on the day says the reel is live.</li><li>The first eleven topics help first. The twelfth shows the product itself.</li></ul></div>';
 return h;
}
function planHtml(p){
 var b=planOf(p);
 if(!b)return '<div class="card"><h3>Not planned yet</h3><p style="margin:.2rem 0 0;color:var(--label2)">The connected content plan (12 topics with teaser photo, teaser story, reel and reel-is-live story) is written for the pilot, Wave 1 and Wave 2 in English (US) and Portuguese (Portugal). Other personas get theirs when their wave starts.</p></div>';
 var L=lgOf(p)==='pt'?'European Portuguese':'English',t=nav.pl||'Calendar',total=4+48,done=0;
 b.intro.photos.forEach(function(_,i){if(isDone(p,'ip',i))done++});if(isDone(p,'im',0))done++;
 b.topics.forEach(function(_,n){done+=topicDone(p,n)});
 var h='<div class="seg" role="group" aria-label="Plan view">'+['Calendar','Topics','Setup'].map(function(s){return '<button aria-pressed="'+(t===s)+'" data-do="plt" data-v="'+s+'">'+s+'</button>'}).join('')+'</div>';
 h+='<div class="bar" aria-hidden="true"><i style="width:'+Math.round(done/total*100)+'%"></i></div><div style="color:var(--label2);font-size:.875rem;margin:0 0 .8rem">'+done+' of '+total+' done</div>';
 if(t==='Calendar'){
  h+='<div class="note">Four weeks, 12 connected topics. Each topic: a teaser photo and story the day before, then the reel and a reel-is-live story. Reels also go to TikTok and YouTube Shorts; stories are Instagram. '+(lgOf(p)==='pt'?'Spoken lines and on-screen text are in European Portuguese with an English reference; directions are in English.':'')+'</div>';
  calOf().forEach(function(w){
   h+='<h2>'+w[0]+'</h2><div class="grp">'+w[1].map(function(e){
    var k=e[1],n=e[2],tn=k==='i'?'Setup':'Topics',title,sub,d;
    if(k==='i'){title='Intro photos and the Meet story';sub='Three photos and the intro story';d=isDone(p,'im',0)}
    else{var x=b.topics[n];title=sb(x.t,p);
     if(k==='t'){sub='Teaser photo and teaser story';d=isDone(p,'tp',n)&&isDone(p,'ts',n)}else{sub='Reel and reel-is-live story';d=isDone(p,'tr',n)&&isDone(p,'tl',n)}}
    return '<button class="row" data-do="plgo" data-v="'+tn+'" data-k="'+(k==='i'?'i0':'t'+n)+'"><span class="dnum'+(d?' ok':'')+'">'+e[0].slice(0,3)+'</span><span class="grow"><div class="t1">'+esc(title)+'</div><div class="t2">'+esc(sub)+'</div></span>'+CHEV+'</button>'}).join('')+'</div>';
  });
  h+='<div class="note">Before filming: cook, build, test or measure it for real. Replace every [BRACKET] with something the team actually did and its real result. Numbers in scripts are examples. For products you sell, use only items you have ordered and tested.</div>';
 }else if(t==='Topics'){
  h+=b.topics.map(function(x,n){return topicHtml(p,x,n,L)}).join('');
 }else{
  h+=setupHtml(p,b,L);
 }
 return h;
}

var SECS=['Overview','Look and voice','Content','Content plan','Sell','Rules','Prompts','Checklist'];
function vPersona(id){
 var p=PK[id],n=NK[p.niche],m=MK[p.mkt],st=pStatus(id);
 var h='<div style="display:flex;gap:1rem;align-items:center;margin:.3rem 0 1rem">'+avHtml(p,'lg')+'<div><h1 class="lt" style="margin:0">'+esc(p.name)+'</h1><div style="color:var(--label2)">'+esc(n.name)+' · '+flag(p.mkt,'s')+esc(m.name)+'</div></div></div>';
 h+='<div>'+tagW(p.wave)+'<span class="tag g'+p.g+'">'+gtxt(p.g)+', '+p.age+'</span><span class="tag">'+esc(m.city)+'</span>'+(p.niche==='bet'?betTag(m):'')+'</div>';
 h+='<div class="seg" role="group" aria-label="Review status" style="margin-top:.5rem">'+[['review','To review'],['ok','Approved'],['skip','Skip']].map(function(s){return '<button aria-pressed="'+(st===s[0])+'" data-do="status" data-id="'+id+'" data-v="'+s[0]+'">'+s[1]+'</button>'}).join('')+'</div>';
 h+='<div class="pw"><div class="pills" role="tablist">'+SECS.map(function(s){return '<button class="pill" role="tab" aria-current="'+(nav.sec===s)+'" data-do="sec" data-v="'+s+'">'+s+'</button>'}).join('')+'</div></div>';
 h+=secHtml(p,n,m);
 return h;
}
function secHtml(p,n,m){
 var s=nav.sec,h='',id=p.id;
 if(s==='Overview'){
  h+='<div class="card"><div class="big">'+esc(p.angle)+'</div><p style="color:var(--label2);margin-bottom:0">The signature angle that makes this persona distinctive rather than generic.</p></div>';
  h+='<div class="card">'+kv('Niche',n.name+': '+n.tagline)+kv('Market',m.name+' · '+m.city)+kv('Wave',p.wave===0?'Pilot: build first. Two personas for four weeks, then decide':p.wave===1?'Wave 1: build first (default test languages: English US and Portuguese Portugal)':p.wave===2?'Wave 2: after Wave 1 works':p.wave===3?'Wave 3: only after a legal check':'Wave 4: later markets'+(['fi','dk','no'].indexOf(p.mkt)>=0?' (Nordic: last)':''))+kv('Credits',p.wave===0?'Setup about 2,000 to 2,500 credits. One 12 s talking video 3,850; one 4K photo 245. See Credits and cost.':'A 12 s talking video is 3,850 credits and a 4K photo 245. See Credits and cost before adding this persona.')+kv('Account bio',p.bio)+(p.learner?kv('Audience',(p.niche==='lang'&&['us','uk'].indexOf(p.mkt)>=0?'Learners of English; captions in '+p.learner:'English speakers learning '+m.lang+'; captions in English')):'')+'</div>';
  h+='<h2>Backstory</h2><div class="card"><p style="margin:0">'+esc(p.backstory)+'</p></div>';
  h+='<div class="note">'+esc(n.what)+'</div>';
 }else if(s==='Look and voice'){
  h+='<div class="card">'+kv('Age and gender',p.age+', '+gtxt(p.g).toLowerCase())+kv('Hair',p.hair)+kv('Outfit for the saved look',p.outfit)+kv('Setting',p.setting)+kv('Weather note',p.weather)+'</div>';
  h+='<div class="card">'+kv('Voice',p.voice)+kv('Speak it as',m.speech)+kv('Natural filler words',m.fillers)+kv('Watch out for',m.watch)+'</div>';
  h+='<div class="note">The face is yours to choose from the generated photo. Check that it resembles no real person. Native voice quality in '+esc(m.lang)+' is untested: test it on an ordinary sentence.</div>';
  h+='<h2>Local details to show</h2><div class="card"><ul class="l">'+m.local.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 }else if(s==='Content'){
  h+='<h2 style="margin-top:.2rem">Series</h2>'+n.series.map(function(x){return '<div class="card"><h3>'+esc(x[0].replace('{cur}',m.cur))+'</h3><p style="margin:.2rem 0 0;color:var(--label2)">'+esc(x[1])+'</p></div>'}).join('');
  h+='<h2>First 10 clips</h2><div class="card"><ol class="s">'+p.clips.map(function(c){return '<li><div class="st">'+esc(c.title)+'</div><div class="sd">'+esc(c.kind)+'</div></li>'}).join('')+'</ol></div>';
  h+='<h2>Hook variants for clip 1</h2><div class="card"><ul class="l">'+p.hooks.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div><div class="note">These are English patterns. Ask Claude (Prompts tab) to write native '+esc(m.lang)+' versions.</div>';
  if(p.niche==='lang'){
   h+='<h2>30-episode plan</h2>'+D.epis.map(function(se,si){return '<div class="card"><h3>'+esc(se[0])+'</h3><ol class="s" style="counter-reset:s '+(si*10)+'">'+se[1].map(function(e){return '<li><div class="st">'+esc(e)+'</div></li>'}).join('')+'</ol></div>'}).join('');
   if(p.ph)h+='<h2>First phrases</h2><div class="card">'+kv('Hello',p.ph.hello[0]+'  '+p.ph.hello[1])+kv('Thank you',p.ph.thanks[0]+'  '+p.ph.thanks[1])+kv('Where is the station?',p.ph.station[0]+'  '+p.ph.station[1])+'<div style="color:var(--label2);font-size:.875rem">Approximate respellings. A native speaker must confirm.</div></div>';
  }
 }else if(s==='Content plan'){
  h+=planHtml(p);
 }else if(s==='Sell'){
  h+='<div class="card">'+kv('Offer',p.offer||n.offer)+kv('Price range',p.price)+kv('Product ladder',n.ladder.join(' → '))+'</div>';
  h+=resNicheHtml(n.research)+resMarketHtml(m.research);
  h+='<h2>How it sells without selling</h2><div class="card"><ul class="l"><li>About 60% value-first posts, 25% story posts, 15% soft call to action.</li><li>Show the result first, then let the offer appear as the next step.</li><li>One calm line: "The full plan is in my bio if you want it, no pressure."</li></ul></div>';
  h+='<h2>Descriptions for clip 1 (English draft)</h2>'+promptHtml('TikTok',p.desc.tt)+promptHtml('Instagram Reels',p.desc.ig)+promptHtml('YouTube Shorts title',p.desc.yt_title)+promptHtml('YouTube Shorts description',p.desc.yt);
  h+='<div class="note">Claude writes the finished versions in '+esc(m.lang)+'. Use the request in the Prompts tab.</div>';
  h+='<h2>What to measure</h2><div class="card"><ul class="l">'+n.kpis.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul></div>';
 }else if(s==='Rules'){
  h+=p.rules.map(function(r){return '<div class="card"><h3>'+esc(r[0])+'</h3><p style="margin:.2rem 0 0;color:var(--label2)">'+esc(r[1])+'</p></div>'}).join('');
  h+='<div class="note">Checked 5 Nov 2026 from web sources. Not legal advice. Verify locally before launch.</div>';
 }else if(s==='Prompts'){
  h+='<p style="color:var(--label2)">Ready to paste. Brackets and details are already filled for '+esc(p.name)+'.</p>';
  h+=promptHtml('1. First photo (OpenArt Image)',p.photo);
  h+=promptHtml('2. Voice description (Design a voice)',p.voice);
  h+=promptHtml('3. Backstory (paste in the character)',p.backstory);
  h+=promptHtml('4. Character sheet (16:9, with @'+p.name+')',p.sheet);
  h+=promptHtml('5. First video (Seedance 2.5)',p.video);
  h+=promptHtml('6. Ask Claude for native hooks and descriptions',p.ask);
  h+='<div class="note">Settings: GPT Image 2.5, 4:5, 4K, quality High, Auto Polish off. Video: Seedance 2.5, 9:16, 1080p, 12 s, audio on. Run the phonetic step for any brand name before the final line.</div>';
 }else if(s==='Checklist'){
  var ck=S.ck[id]||[];
  h+='<div class="grp">'+p.check.map(function(c,i){var on=ck.indexOf(i)>=0;return '<button class="check'+(on?' on':'')+'" data-do="ck" data-id="'+id+'" data-i="'+i+'" aria-pressed="'+on+'"><span class="box">'+svg('check',3)+'</span><span class="tx">'+esc(c)+'</span></button>'}).join('')+'</div>';
  h+='<h2>My notes</h2><textarea class="nt" id="nt" data-id="'+id+'" placeholder="Notes about '+esc(p.name)+'" aria-label="Notes">'+esc(S.nt[id]||'')+'</textarea>';
 }
 return h;
}

/* ---------- render ---------- */
function titleOf(c){
 if(c.v==='persona')return PK[c.id].name;if(c.v==='niche')return NK[c.id].name;if(c.v==='market')return MK[c.id].name;if(c.v==='plan-page')return PLK[c.id].title;
 return ({personas:'Personas',niches:'Niches',markets:'Languages',plan:'Plan'})[c.v]||'';
}
function viewHtml(c){
 copyStore=[];
 switch(c.v){case'personas':return vPersonas();case'niches':return vNiches();case'markets':return vMarkets();case'plan':return vPlan();
  case'persona':return vPersona(c.id);case'niche':return vNiche(c.id);case'market':return vMarket(c.id);case'plan-page':return vPlanPage(c.id);}
 return '';
}
function renderTop(){
 var c=cur(),back=nav.stack.length>0;
 top.innerHTML=(back?'<button class="glassbtn" data-do="back" aria-label="Back">'+svg('back',2.2)+'</button>':'<span></span>')+'<div class="t">'+esc(titleOf(c))+'</div>'+'<span></span>';
 top.classList.toggle('sc',scrollY>50);navbg.classList.toggle('sc',scrollY>8);navbg.classList.toggle('tall',c.v==='persona');
}
function renderTab(){
 tabbar.style.setProperty('--n',TABS.length);
 tabbar.innerHTML='<div class="tb-ind" style="width:calc((100% - .5rem)/'+TABS.length+');transform:translateX('+TABS.findIndex(function(t){return t[0]===nav.tab})*100+'%)"></div>'+
  TABS.map(function(t){return '<button class="tab" data-do="tab" data-v="'+t[0]+'" aria-label="'+t[1]+'"'+(t[0]===nav.tab?' aria-current="page"':'')+'>'+svg(t[2])+'<span>'+t[1]+'</span></button>'}).join('');
}
function renderView(){
 var c=cur();
 root.innerHTML='<main class="view cur'+(nav.stack.length?' pushed':'')+'">'+viewHtml(c)+'</main>';
 renderTop();
}
var animUntil=0;
function go(kind,fn){ // kind: fwd|back|none
 var old=root.querySelector('.view');var snap=null;
 if(kind!=='none'&&old&&!matchMedia('(prefers-reduced-motion:reduce)').matches){
  snap=document.createElement('div');snap.className='pg pg-old';
  var inner=old.cloneNode(true);inner.classList.remove('cur');inner.removeAttribute('id');
  inner.querySelectorAll('[id]').forEach(function(e){e.removeAttribute('id')});inner.setAttribute('aria-hidden','true');
  inner.style.transform='translateY('+(-scrollY)+'px)';snap.appendChild(inner);
 }
 fn();
 if(snap){
  document.body.appendChild(snap);
  var h=document.documentElement;h.classList.add('pg-run','pg-'+kind);
  if(kind==='back')snap.style.pointerEvents='none';
  animUntil=Date.now()+460;
  setTimeout(function(){snap.remove();h.classList.remove('pg-run','pg-fwd','pg-back')},460);
 }
}
function setTab(t){
 nav.tab=t;nav.stack=[];scrolls=[];nav.sec='Overview';renderTab();renderView();scrollTo(0,0);
}

/* ---------- toast ---------- */
var tt;function toast(m){toastEl.textContent=m;toastEl.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){toastEl.classList.remove('on')},1600)}
function copy(t){
 var done=function(){toast('Copied')};
 try{navigator.clipboard.writeText(t).then(done,function(){fallback(t);done()})}catch(e){fallback(t);done()}
}
function fallback(t){var a=document.createElement('textarea');a.value=t;a.style.cssText='position:fixed;opacity:0;font-size:16px';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove()}

/* ---------- events ---------- */
document.addEventListener('click',function(e){
 var el=e.target.closest('[data-do]');if(!el)return;
 var d=el.dataset,a=d.do;
 if(Date.now()<animUntil&&(a==='open'||a==='back'))return;
 if(a==='tab'){
  tabbar.classList.remove('tap');void tabbar.offsetWidth;tabbar.classList.add('tap');setTimeout(function(){tabbar.classList.remove('tap')},650);
  if(d.v===nav.tab&&nav.stack.length===0){scrollTo({top:0,behavior:'smooth'});return}
  setTab(d.v);
 }else if(a==='open'){
  var vv=d.v==='plan'?'plan-page':d.v;
  scrolls.push(scrollY);go('fwd',function(){nav.stack.push({v:vv,id:d.id});nav.sec='Overview';renderView();scrollTo(0,0)});
 }else if(a==='back'){
  var by=scrolls.pop()||0;go('back',function(){nav.stack.pop();nav.sec='Overview';renderView();scrollTo(0,by)});
 }else if(a==='filters'){openSheet();
 }else if(a==='fclose'){closeSheet();
 }else if(a==='freset'){S.f={niche:'all',mkt:'all',g:'all'};save();if(sheetEl){document.getElementById('sb').innerHTML=sheetBody()}refreshList();
 }else if(a==='fset'){S.f[d.k]=d.v;save();if(sheetEl){var sb=document.getElementById('sb'),st=sb.scrollTop;sb.innerHTML=sheetBody();sb.scrollTop=st}refreshList();
 }else if(a==='clear'){S.f[d.k]='all';save();refreshList();
 }else if(a==='sec'){
  nav.sec=d.v;var y2=scrollY;var pill=document.querySelector('.pills');var left=pill?pill.scrollLeft:0;renderView();var p2=document.querySelector('.pills');if(p2)p2.scrollLeft=left;scrollTo(0,Math.min(y2,200));
 }else if(a==='plt'){
  nav.pl=d.v;nav.openItem=null;renderView();scrollTo(0,Math.min(scrollY,200));
 }else if(a==='plgo'){
  nav.pl=d.v;nav.openItem=d.k;renderView();var el=document.getElementById('it-'+d.k);if(el)scrollTo(0,Math.max(0,el.getBoundingClientRect().top+scrollY-150));
 }else if(a==='pdone'){
  S.pd=S.pd||{};S.pd[d.k]=!S.pd[d.k];if(!S.pd[d.k])delete S.pd[d.k];save();var y5=scrollY;if(d.o)nav.openItem=d.o;renderView();scrollTo(0,y5);
 }else if(a==='status'){
  S.st[d.id]=d.v;save();var y3=scrollY;renderView();scrollTo(0,y3);
 }else if(a==='ck'){
  var ck=S.ck[d.id]||[],i=+d.i,ix=ck.indexOf(i);if(ix>=0)ck.splice(ix,1);else ck.push(i);S.ck[d.id]=ck;save();var y4=scrollY;renderView();scrollTo(0,y4);
 }else if(a==='copy'){
  var t=copyStore[+d.i];if(t!=null)copy(t);
 }else if(a==='theme'){
  S.theme=d.v;save();applyTheme();var y5=scrollY;renderView();scrollTo(0,y5);
 }else if(a==='export'){
  var lines=[];D.personas.forEach(function(p){var s=pStatus(p.id),n=S.nt[p.id],ck=(S.ck[p.id]||[]).length;if(s!=='review'||n||ck)lines.push(p.name+' ('+NK[p.niche].name+', '+MK[p.mkt].name+', '+gtxt(p.g)+'): '+stText(s)+', checklist '+ck+'/'+p.check.length+(n?'. Notes: '+n:''))});
  copy(lines.length?lines.join('\n'):'No review notes yet.');
 }
});
document.addEventListener('input',function(e){
 if(e.target.id==='q'){nav.q=e.target.value;refreshList()}
 else if(e.target.id==='nt'){S.nt[e.target.dataset.id]=e.target.value;save()}
});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeSheet()});
var lastY=0,ticking=false;
addEventListener('scroll',function(){
 if(ticking)return;ticking=true;
 requestAnimationFrame(function(){
  ticking=false;var y=scrollY;
  top.classList.toggle('sc',y>50);navbg.classList.toggle('sc',y>8);
  if(y>lastY+8&&y>12)tabbar.classList.add('min');else if(y<lastY-8||y<=12)tabbar.classList.remove('min');
  lastY=y;
 });
},{passive:true});
var saved={};
function restore(){}
addEventListener('popstate',function(){});
matchMedia('(prefers-color-scheme:dark)').addEventListener&&matchMedia('(prefers-color-scheme:dark)').addEventListener('change',applyTheme);


/* ---------- swipe back from the left edge ---------- */
var sw={on:false,lock:false,x0:0,y0:0,dx:0,t0:0,view:null,prev:null,inner:null,dim:null};
function prevCtx(){var i=nav.stack.length-2;return i>=0?nav.stack[i]:{v:nav.tab}}
function swStart(){
 sw.view=root.querySelector('.view');if(!sw.view)return false;
 var c=prevCtx(),store=copyStore,html=viewHtml(c);copyStore=store;
 var pushed=nav.stack.length-1>0;
 sw.prev=document.createElement('div');sw.prev.className='pg-prev';sw.prev.setAttribute('aria-hidden','true');
 var y=scrolls.length?scrolls[scrolls.length-1]:0;
 sw.prev.innerHTML='<div class="view'+(pushed?' pushed':'')+'" style="transform:translateY('+(-y)+'px) translateX(-28%);transition:none">'+html+'</div><div class="dim"></div>';
 sw.inner=sw.prev.firstChild;sw.dim=sw.prev.lastChild;
 sw.prev.querySelectorAll('[id]').forEach(function(e){e.removeAttribute('id')});
 document.body.appendChild(sw.prev);
 sw.view.classList.add('sw');sw.view.style.transition='none';
 return true;
}
function swApply(dx){
 var W=innerWidth,p=Math.min(1,dx/W);
 sw.view.style.transform='translateX('+dx+'px)';
 var y=scrolls.length?scrolls[scrolls.length-1]:0;
 sw.inner.style.transform='translateY('+(-y)+'px) translateX('+(-28*(1-p))+'%)';
 sw.dim.style.opacity=(.22*(1-p)).toFixed(3);
}
function swClean(){if(sw.prev){sw.prev.remove()}if(sw.view){sw.view.classList.remove('sw');sw.view.style.transform='';sw.view.style.transition=''}sw.prev=sw.view=sw.inner=sw.dim=null;sw.on=false;sw.lock=false}
function swEnd(commit){
 var W=innerWidth,v=sw.view,inner=sw.inner,dim=sw.dim;animUntil=Date.now()+360;
 var ease='transform .32s cubic-bezier(.32,.72,0,1)';
 v.style.transition=ease;inner.style.transition=ease;dim.style.transition='opacity .32s';
 var y=scrolls.length?scrolls[scrolls.length-1]:0;
 if(commit){
  v.style.transform='translateX('+W+'px)';inner.style.transform='translateY('+(-y)+'px) translateX(0)';dim.style.opacity=0;
  setTimeout(function(){var by=scrolls.pop()||0;nav.stack.pop();nav.sec='Overview';var prev=sw.prev;sw.prev=null;renderView();scrollTo(0,by);if(prev)prev.remove();sw.view=null;swClean()},330);
 }else{
  v.style.transform='translateX(0)';inner.style.transform='translateY('+(-y)+'px) translateX(-28%)';dim.style.opacity=.22;
  setTimeout(swClean,330);
 }
}
document.addEventListener('touchstart',function(e){
 if(nav.stack.length===0||sheetEl||e.touches.length!==1||Date.now()<animUntil||sw.prev)return;
 var t=e.touches[0];if(t.clientX>30)return;
 sw.on=true;sw.lock=false;sw.x0=t.clientX;sw.y0=t.clientY;sw.dx=0;sw.t0=Date.now();
},{passive:true});
document.addEventListener('touchmove',function(e){
 if(!sw.on)return;var t=e.touches[0],dx=t.clientX-sw.x0,dy=t.clientY-sw.y0;
 if(!sw.lock){
  if(Math.abs(dx)<8&&Math.abs(dy)<8)return;
  if(Math.abs(dy)>Math.abs(dx)||dx<0){sw.on=false;return}
  if(!swStart()){sw.on=false;return}
  sw.lock=true;
 }
 e.preventDefault();sw.dx=Math.max(0,dx);swApply(sw.dx);
},{passive:false});
function swFinish(){
 if(!sw.on)return;if(!sw.lock){sw.on=false;return}
 sw.on=false;var dt=Math.max(1,Date.now()-sw.t0),v=sw.dx/dt;
 swEnd(sw.dx>innerWidth*.33||v>.5);
}
document.addEventListener('touchend',swFinish);
document.addEventListener('touchcancel',function(){if(sw.on&&sw.lock){sw.on=false;swEnd(false)}else sw.on=false});

/* ---------- boot ---------- */
applyTheme();renderTab();renderView();
if('serviceWorker' in navigator&&location.protocol!=='file:'){navigator.serviceWorker.register('sw.js').catch(function(){})}
})();
