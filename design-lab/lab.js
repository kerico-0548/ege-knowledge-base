(() => {
  'use strict';
  const samples = window.KERYA_SAMPLES, root = document.querySelector('#content');
  const E = s => String(s ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const themes = {
    amethyst: {name:'Аметист',tag:'Личный кабинет',description:'Список задач всегда слева. Светлый заголовок, графитовая область чтения и немного фиолетового.'},
    contrast: {name:'Контраст',tag:'Учебный атлас',description:'Светлый каталог. Условие, разбор и код на одной странице, с быстрыми переходами между разделами.'},
    focus: {name:'Фокус',tag:'Рабочий стол',description:'Условие и разбор или код рядом. Можно смотреть на задачу и сразу работать с решением.'}
  };
  const icons = {
    arrow:'<path d="M4 12h15m-6-6 6 6-6 6"/>',back:'<path d="M20 12H5m6-6-6 6 6 6"/>',
    book:'<path d="M4 4h6a3 3 0 0 1 3 3v14a4 4 0 0 0-4-2H4zM13 7a3 3 0 0 1 3-3h4v15h-3a4 4 0 0 0-4 2"/>',
    code:'<path d="m8 7-5 5 5 5m8-10 5 5-5 5m-2-14-4 18"/>',
    copy:'<rect x="8" y="8" width="12" height="13" rx="2"/><path d="M15 8V3H3v13h5"/>',
    share:'<path d="M12 16V3m-5 5 5-5 5 5M5 13v7h14v-7"/>',
    eye:'<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    menu:'<path d="M4 6h16M4 12h16M4 18h16"/>',check:'<path d="m5 12 4 4 10-10"/>',
    download:'<path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/>',reset:'<path d="M4 10a8 8 0 1 1 1 8M4 3v7h7"/>',
    grid:'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    link:'<path d="M10 6h-6v14h14v-6M13 3h8v8m0-8L10 14"/>'
  };
  const I = name => '<svg viewBox="0 0 24 24" aria-hidden="true">'+icons[name]+'</svg>';
  let state, toastTimer, edits = {};
  try { edits = JSON.parse(localStorage.getItem('kerya-design-lab.v1') || '{}'); if (!edits || typeof edits !== 'object' || Array.isArray(edits)) edits = {}; } catch {}
  const code = s => typeof edits[s.id] === 'string' ? edits[s.id] : s.code;
  const index = s => String(samples.indexOf(s)+1).padStart(2,'0');
  const sourceShort = s => s.id.startsWith('fipi') ? 'Демо 2027' : 'Из курса';
  function notify(text) {
    const el = document.querySelector('#toast'); el.textContent = text; el.classList.add('show');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('show'), 3000);
  }
  async function copy(text, message = 'Скопировано') {
    try { await navigator.clipboard.writeText(text); }
    catch {
      const el = document.createElement('textarea'); el.value=text; el.style.cssText='position:fixed;opacity:0'; document.body.append(el); el.select();
      const ok = document.execCommand('copy'); el.remove(); if (!ok) { notify('Выдели текст и скопируй его вручную'); return; }
    }
    notify(message);
  }
  function save() {
    try { localStorage.setItem('kerya-design-lab.v1', JSON.stringify(edits)); }
    catch { notify('Не удалось сохранить правки. Скачай код отдельным файлом.'); }
  }
  function parse() {
    const p = new URLSearchParams(location.search);
    state = {theme:p.get('style'), id:p.get('task')||samples[0].id, view:p.get('view')||'condition', student:p.get('student')==='1', filter:'', nav:false};
    if (state.theme === 'wine') state.theme = 'contrast';
    if (!themes[state.theme]) state.theme = null;
    if (!samples.some(s => s.id === state.id)) state.id = samples[0].id;
    if (!['condition','solution','code'].includes(state.view)) state.view = 'condition';
    const current = samples.find(s => s.id === state.id);
    if (state.view === 'code' && !current.code) state.view = 'solution';
    const raw = new URLSearchParams(location.hash.slice(1)).get('code');
    if (raw && raw.length < 40000) try {
      const b = raw.replace(/-/g,'+').replace(/_/g,'/');
      const text = new TextDecoder().decode(Uint8Array.from(atob(b+'='.repeat((4-b.length%4)%4)),c=>c.charCodeAt(0)));
      const j = JSON.parse(text);
      if (typeof j.code === 'string' && j.code.length < 7000 && current.code) { edits[state.id]=j.code; save(); }
    } catch {}
  }
  function writeUrl({replace=false}={}) {
    const u = new URL(location.href); u.search=''; u.hash='';
    u.searchParams.set('style',state.theme); u.searchParams.set('task',state.id);
    if (state.view !== 'condition') u.searchParams.set('view',state.view);
    if (state.student) u.searchParams.set('student','1');
    history[replace?'replaceState':'pushState']({},'',u);
  }
  function brand() { return '<a class="brand" href="./"><span class="brand-symbol" aria-hidden="true">k<span>.</span></span><span>Kerya<small>Информатика · ЕГЭ</small></span></a>'; }
  function topbar(gallery=false) {
    return '<header class="app-top">'+brand()+'<div class="top-divider"></div><span class="top-caption">'+(gallery?'Выбрать оформление':themes[state.theme].tag)+'</span><div class="top-right">'+
      (gallery?'<a class="top-link" href="../">Основная база '+I('link')+'</a>':
        (state.student?'<span class="student-badge">Материал для ученика</span>':'<label class="theme-controls">Стиль<select id="theme-select" aria-label="Вариант оформления">'+Object.entries(themes).map(([id,t])=>'<option value="'+id+'"'+(state.theme===id?' selected':'')+'>'+t.name+'</option>').join('')+'</select></label>')+
        '<a class="top-link gallery-return" href="./">'+I('grid')+'<span>Все варианты</span></a>')+'</div></header>';
  }
  function miniPreview(id) {
    return '<div class="preview preview-'+id+'" aria-hidden="true"><div class="mini-top"><b>k.</b><span></span><i></i></div><div class="mini-work"><div class="mini-nav"><small>ЗАДАЧИ</small><i class="selected"></i><i></i><i></i><i></i></div><div class="mini-page"><div class="mini-heading"><small>ЗАДАНИЕ 08</small><b>Номер слова<br>в списке</b></div><div class="mini-tabs"><i></i><i></i><i></i></div><div class="mini-columns"><div class="mini-condition"><div class="mini-lines"><i></i><i></i><i></i></div><div class="mini-table"><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="mini-ask"></div></div><div class="mini-solution"><small>РЕШЕНИЕ</small><code><em>from</em> itertools<br><em>import</em> product<br><br>k = <b>0</b><br><em>for</em> x <em>in</em> product:</code></div></div></div></div></div>';
  }
  function gallery() {
    document.body.className='gallery-page'; document.title='Kerya · Три новых оформления';
    root.innerHTML=topbar(true)+'<section class="gallery"><div class="gallery-intro"><div><p class="eyebrow"><span></span> Новые варианты</p><h1>Меньше шума.<br><span>Больше ясности.</span></h1></div><p>Три разных способа работать с одной задачей. Сдержанный фиолетовый, графит, светлые участки и бордовые детали.</p></div><div class="style-grid">'+Object.entries(themes).map(([id,t],n)=>'<article class="style-card">'+miniPreview(id)+'<div class="style-copy"><div class="style-title"><span>0'+(n+1)+'</span><h2>'+t.name+'</h2></div><p>'+t.description+'</p><div class="style-foot"><span>'+t.tag+'</span><a class="style-open" href="?style='+id+'" aria-label="Открыть '+t.name+'">Открыть '+I('arrow')+'</a></div></div></article>').join('')+'</div><footer class="gallery-foot"><span>В каждом варианте — одинаковые 4 задачи.</span><span>Условие · разбор · редактируемый код · ссылка ученику</span></footer></section>';
  }
  function taskNav() {
    const visible=samples.filter(s=>!state.filter||s.number===state.filter);
    return '<aside id="task-catalog" class="task-rail" aria-label="Каталог задач"><div class="catalog-heading"><div><p class="eyebrow">Учебная подборка</p><h2>Задачи<span>04</span></h2></div><button class="catalog-close icon-button" data-action="choose-task" aria-label="Закрыть список задач">'+I('back')+'</button></div><div class="topic-filters" aria-label="Фильтр по номеру">'+[['','Все'],['8','№ 8'],['23','№ 23'],['1','№ 1']].map(([v,label])=>'<button data-filter="'+v+'" aria-pressed="'+(state.filter===v)+'">'+label+'</button>').join('')+'</div><nav class="sample-list">'+visible.map(s=>'<button class="sample-button" data-task="'+s.id+'" aria-current="'+(s.id===state.id)+'"><span class="sample-index">'+index(s)+'</span><span class="sample-text"><small>№ '+s.number+' <span>· '+sourceShort(s)+'</span></small><strong>'+E(s.title)+'</strong></span><span class="sample-arrow">'+I('arrow')+'</span></button>').join('')+'</nav><div class="catalog-bottom"><span class="catalog-dot"></span><p>Одна задача за раз.<br>Всё нужное — рядом.</p><a href="../">Все материалы '+I('link')+'</a></div></aside>';
  }
  function actions(s) {
    return '<div class="workbar"><div class="breadcrumbs"><button class="catalog-toggle" data-action="choose-task" aria-controls="task-catalog" aria-expanded="'+state.nav+'">'+I('menu')+' Задачи</button><span class="crumb-home">Задачи</span><span class="crumb-separator">/</span><span>№ '+s.number+'</span><span class="source-badge">'+sourceShort(s)+'</span></div><div class="work-actions">'+(!state.student?'<button class="action-link teacher-only" data-action="student" aria-label="Открыть вид ученика" title="Открыть вид ученика">'+I('eye')+'<span>Вид ученика</span></button>':'')+'<button class="share-button" data-action="share">'+I('share')+'<span>Поделиться</span></button></div></div>';
  }
  function taskHeader(s) {
    return '<header class="task-header"><div class="task-meta"><span class="number-label">Задание '+String(s.number).padStart(2,'0')+'</span><span class="meta-dot"></span><span>'+E(s.topic)+'</span></div><h1>'+E(s.title)+'</h1><div class="hero-bottom"><span>'+I(s.code?'code':'book')+(s.code?'Python · авторский шаблон':'Ручное решение')+'</span><span class="verified-label">'+I('check')+' Проверенный пример</span></div></header>';
  }
  function tabs(s,{prefix='tab',focus=false}={}) {
    const items=(focus?[['solution','Разбор'],['code','Код']]:[['condition','Условие'],['solution','Разбор'],['code','Код']]).filter(([id])=>id!=='code'||s.code);
    const current=focus&&state.view==='condition'?'solution':state.view;
    return '<nav class="tabs '+(focus?'dock-tabs':'')+'" role="tablist" aria-label="'+(focus?'Решение рядом с условием':'Разделы задачи')+'">'+items.map(([id,label])=>'<button id="'+prefix+'-'+id+'" role="tab" aria-controls="'+(focus?'method-content':prefix==='mobile'?(id==='condition'?'condition-side':'method-content'):'panel-'+id)+'" aria-selected="'+(current===id)+'" data-view="'+id+'"><span class="tab-number">'+({condition:'01',solution:'02',code:'03'}[id])+'</span>'+label+'</button>').join('')+'</nav>';
  }
  function original(s) { return '<details class="original"><summary>Исходная формулировка '+I('book')+'</summary><p>'+E(s.original)+'</p></details>'; }
  function graph(s) {
    const table=s.visuals.find(b=>b.type==='table'),edges=s.visuals.find(b=>b.type==='edges'); if(!table||!edges)return '';
    const pos={F:[40,145],C:[110,30],B:[290,50],E:[270,180],A:[150,245],D:[190,120]};
    return '<div class="graph-grid"><div><h3>Длины дорог, км</h3><div class="table-wrap"><table class="matrix"><thead><tr>'+table.columns.map(c=>'<th scope="col">'+E(c)+'</th>').join('')+'</tr></thead><tbody>'+table.rows.map(r=>'<tr>'+r.map(c=>'<td>'+E(c)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div></div><div><h3>Схема дорог</h3><svg class="graph" viewBox="0 0 340 285" role="img" aria-label="Граф дорог. Связи перечислены под рисунком.">'+edges.edges.map(([a,b])=>'<line x1="'+pos[a][0]+'" y1="'+pos[a][1]+'" x2="'+pos[b][0]+'" y2="'+pos[b][1]+'"/>').join('')+Object.entries(pos).map(([n,[x,y]])=>'<circle cx="'+x+'" cy="'+y+'" r="3"/><text x="'+(x+(n==='F'?-22:9))+'" y="'+(y+(n==='A'?22:-8))+'">'+n+'</text>').join('')+'</svg><p class="graph-description">Связи: '+edges.edges.map(e=>E(e.join('–'))).join(', ')+'.</p></div></div>';
  }
  function condition(s,compact=false) {
    return '<section class="paper condition-paper"><div class="section-label"><span>01</span><h2>Условие</h2></div><p class="intro">'+E(s.intro)+'</p>'+(s.start?'<h3>Начало списка</h3><div class="start-list">'+s.start.map((w,i)=>'<span><b>'+(i+1)+'</b>'+E(w)+'</span>').join('')+'</div>':'')+(s.commands?'<div class="table-wrap"><table><thead><tr><th>Команда</th><th>Действие</th><th>Когда применяется</th></tr></thead><tbody>'+s.commands.map(r=>'<tr>'+r.map(c=>'<td>'+E(c)+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>':'')+(s.rules.length?'<h3>'+(s.commands?'Начало и результат':'Что нужно учесть')+'</h3><ul class="requirements">'+s.rules.map(r=>'<li>'+E(r)+'</li>').join('')+'</ul>':'')+graph(s)+'<div class="question-box"><span class="question-caption">Нужно найти</span><p class="ask">'+E(s.ask)+'</p></div>'+(s.note?'<p class="question-note">'+E(s.note)+'</p>':'')+'</section>'+(!compact?'<div class="next-view"><button class="button primary" data-view="solution">Разобрать задачу '+I('arrow')+'</button>'+(s.code?'<button class="action-link" data-view="code">'+I('code')+' Открыть код</button>':'')+'</div>':'')+original(s);
  }
  function solution(s,compact=false) {
    return '<section class="paper solution-paper"><div class="section-label"><span>02</span><h2>Разбор по шагам</h2></div><ol class="steps">'+s.steps.map(r=>'<li><h3>'+E(r.title)+'</h3><p>'+E(r.text)+'</p></li>').join('')+'</ol><div class="check-note">'+I('check')+'<p>'+E(s.check)+'</p></div></section>'+(!compact?'<div class="next-view">'+(s.code?'<button class="button primary" data-view="code">Перейти к коду '+I('arrow')+'</button>':'')+'<button class="action-link" data-view="condition">'+I('back')+' К условию</button></div>':'');
  }
  function highlight(text) {
    const re=/(#[^\n]*|(?:[rfbu])?(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')|\b(?:from|import|for|in|if|else|elif|def|return|and|or|not|break|while|True|False|None|as|with|continue|print|range|len|int|str|list|sum|min|max|set|any|all|enumerate|open|sorted|product)\b|\b\d+(?:\.\d+)?\b)/g;
    let out='',at=0;
    for (const match of text.matchAll(re)) {
      const token=match[0],cls=token.startsWith('#')?'comment':/^[rfbu]?["']/.test(token)?'string':/^\d/.test(token)?'number':/^(print|range|len|int|str|list|sum|min|max|set|any|all|enumerate|open|sorted|product)$/.test(token)?'function':'keyword';
      out+=E(text.slice(at,match.index))+'<span class="token-'+cls+'">'+E(token)+'</span>'; at=match.index+token.length;
    }
    return out+E(text.slice(at))+'\n';
  }
  function editor(s) {
    const text=code(s),rows=Math.max(12,Math.min(25,text.split('\n').length+2));
    return '<section class="editor"><div class="editor-title"><span>'+I('code')+' solution.py</span><span class="language-dot"></span><small>Python 3</small></div><div class="editor-tools"><button class="copy-code" data-action="copy-code">'+I('copy')+' Копировать код</button><button class="icon-button" data-action="download" aria-label="Скачать код .py" title="Скачать .py">'+I('download')+'</button><button class="icon-button" data-action="reset" aria-label="Восстановить исходный код" title="Восстановить исходный код">'+I('reset')+'</button></div><div class="editor-body"><div class="line-numbers" aria-hidden="true">'+text.split('\n').map((_,i)=>i+1).join('\n')+'</div><div class="editor-code"><div class="syntax-window" aria-hidden="true"><pre id="syntax-layer">'+highlight(text)+'</pre></div><textarea id="code-input" class="code-input" rows="'+rows+'" wrap="off" spellcheck="false" autocapitalize="off" autocomplete="off" aria-label="Редактируемый код решения">'+E(text)+'</textarea></div></div><div class="code-note"><span id="save-state">'+(text!==s.code?'Личная редакция · не проверена':'Исходный код проверенного примера')+'</span><span>Tab — отступ</span></div></section><p class="share-note">Код можно менять прямо здесь. Правки сохраняются в браузере и передаются ученику через «Поделиться». Запускай программу в своём редакторе Python.</p>';
  }
  function answer(s) { return '<details class="answer"><summary><span>Сверить ответ</span><span class="answer-plus" aria-hidden="true">+</span></summary><strong>'+E(s.answer)+'</strong></details>'; }
  function footer(s) { return '<footer class="reader-footer"><span>'+E(s.source)+'</span><a href="'+E(s.source_url)+'" target="_blank" rel="noopener">Источник '+I('link')+'</a></footer>'; }
  function reader(s) {
    if(state.theme==='contrast') {
      const chapters=[['condition','Условие'],['solution','Разбор'],['code','Код']].filter(([id])=>id!=='code'||s.code);
      const nav='<nav class="tabs chapters" aria-label="Перейти к разделу">'+chapters.map(([id,label],i)=>'<button data-view="'+id+'" aria-controls="chapter-'+id+'" aria-current="'+(state.view===id?'location':'false')+'"><span class="tab-number">0'+(i+1)+'</span>'+label+'</button>').join('')+'</nav>';
      return '<article class="reader">'+taskHeader(s)+'<p class="reading-hint">Вся задача на одной странице. Ниже — переходы к разделам.</p>'+nav+'<section id="chapter-condition" class="chapter">'+condition(s,true)+'</section><section id="chapter-solution" class="chapter">'+solution(s,true)+'</section>'+(s.code?'<section id="chapter-code" class="chapter"><div class="section-label"><span>03</span><h2>Код решения</h2></div>'+editor(s)+'</section>':'')+answer(s)+footer(s)+'</article>';
    }
    if(state.theme==='focus') {
      const view=state.view==='code'?'code':'solution';
      return '<article class="reader">'+taskHeader(s)+'<div class="mobile-tabs">'+tabs(s,{prefix:'mobile'})+'</div><div class="focus-layout" data-current-view="'+state.view+'"><div id="condition-side" class="condition-side">'+condition(s,true)+answer(s)+'</div><aside id="method-side" class="method-side">'+tabs(s,{prefix:'dock',focus:true})+'<section id="method-content" role="tabpanel" aria-labelledby="dock-'+view+'">'+(view==='code'?editor(s):solution(s,true))+'</section></aside></div>'+footer(s)+'</article>';
    }
    return '<article class="reader">'+taskHeader(s)+tabs(s)+'<section id="panel-'+state.view+'" role="tabpanel" aria-labelledby="tab-'+state.view+'">'+(state.view==='condition'?condition(s):state.view==='solution'?solution(s):editor(s))+'</section>'+answer(s)+footer(s)+'</article>';
  }
  function bindEditor(s) {
    const input=document.querySelector('#code-input'); if(!input)return;
    const layer=document.querySelector('#syntax-layer'),nums=document.querySelector('.line-numbers');
    input.oninput=()=>{edits[s.id]=input.value;save();layer.innerHTML=highlight(input.value);nums.textContent=input.value.split('\n').map((_,i)=>i+1).join('\n');document.querySelector('#save-state').textContent='Личная редакция · сохранено в браузере';};
    input.onscroll=()=>{layer.style.transform='translate('+(-input.scrollLeft)+'px,'+(-input.scrollTop)+'px)';nums.scrollTop=input.scrollTop;};
    input.onkeydown=e=>{
      if(e.key==='Tab'){e.preventDefault();input.setRangeText('    ',input.selectionStart,input.selectionEnd,'end');input.dispatchEvent(new Event('input'));}
      if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='s'){e.preventDefault();edits[s.id]=input.value;save();notify('Код сохранён в этом браузере');}
    };
  }
  function render() {
    if(!state.theme){gallery();return;}
    const t=themes[state.theme],s=samples.find(s=>s.id===state.id);
    document.title='Kerya · '+s.title+' · '+t.name;
    document.body.className=state.theme+(state.student?' student':'')+(state.nav?' nav-open':'');
    root.innerHTML=topbar()+'<div class="app-layout">'+taskNav()+'<div class="workarea">'+actions(s)+reader(s)+'</div></div>';
    bindEditor(s);
    if(state.theme==='contrast'&&state.view!=='condition')requestAnimationFrame(()=>document.querySelector('#chapter-'+state.view)?.scrollIntoView({block:'start'}));
    const select=document.querySelector('#theme-select');
    if(select)select.onchange=e=>{state.theme=e.target.value;state.nav=false;writeUrl();render();};
  }
  function share() {
    const s=samples.find(x=>x.id===state.id),u=new URL(location.href);u.search='';u.hash='';
    u.searchParams.set('style',state.theme);u.searchParams.set('task',s.id);u.searchParams.set('student','1');u.searchParams.set('view',state.view);
    const edited=code(s);
    if(s.code&&edited!==s.code){
      if(edited.length>6000){notify('Код длиннее 6000 символов. Его можно скачать отдельным файлом.');return;}
      const bytes=new TextEncoder().encode(JSON.stringify({code:edited}));
      u.hash='code='+btoa(String.fromCharCode(...bytes)).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
    }
    copy(u.href,'Ссылка для ученика скопирована');
  }
  document.addEventListener('click',e=>{
    const el=e.target.closest('button');if(!el)return;
    if(el.dataset.task){state.id=el.dataset.task;state.view='condition';state.nav=false;writeUrl();render();return;}
    if(el.dataset.view){
      state.view=el.dataset.view;writeUrl();
      if(state.theme==='contrast'){
        document.querySelectorAll('.chapters button').forEach(b=>b.setAttribute('aria-current',b.dataset.view===state.view?'location':'false'));
        document.querySelector('#chapter-'+state.view)?.scrollIntoView({block:'start'});
      }else{render();}
      return;
    }
    if(Object.hasOwn(el.dataset,'filter')){
      state.filter=el.dataset.filter;const group=samples.filter(s=>!state.filter||s.number===state.filter);
      if(!group.some(s=>s.id===state.id)){state.id=group[0].id;state.view='condition';writeUrl();}render();return;
    }
    const s=samples.find(x=>x.id===state.id);
    switch(el.dataset.action){
      case 'choose-task':state.nav=!state.nav;document.body.classList.toggle('nav-open',state.nav);document.querySelectorAll('[aria-controls="task-catalog"]').forEach(x=>x.setAttribute('aria-expanded',String(state.nav)));break;
      case 'copy-code':copy(code(s),'Код скопирован');break;
      case 'reset':delete edits[s.id];save();writeUrl({replace:true});render();notify('Восстановлен исходный код');break;
      case 'download':{const a=document.createElement('a'),u=URL.createObjectURL(new Blob([code(s)],{type:'text/x-python;charset=utf-8'}));a.href=u;a.download='Kerya_'+s.number+'_'+s.id+'.py';a.click();setTimeout(()=>URL.revokeObjectURL(u),2000);break;}
      case 'share':share();break;
      case 'student':state.student=true;state.nav=false;writeUrl();render();break;
    }
  });
  document.addEventListener('keydown',e=>{
    if(!e.target.matches('[role="tab"]')||!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;
    const buttons=[...e.target.closest('[role="tablist"]').querySelectorAll('[role="tab"]')],at=buttons.indexOf(e.target);
    const next=e.key==='Home'?buttons[0]:e.key==='End'?buttons.at(-1):buttons[(at+(e.key==='ArrowRight'?1:buttons.length-1))%buttons.length];
    e.preventDefault();const id=next.id;next.click();document.getElementById(id)?.focus();
  });
  window.addEventListener('popstate',()=>{parse();render();});parse();render();
})();
