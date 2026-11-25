(() => {
  "use strict";
  const escape = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  const tags = new Set("p div h2 h3 strong b em i u s mark ul ol li blockquote pre code a img figure figcaption br sub sup hr table caption thead tbody tfoot tr td th".split(" "));
  const classes = new Set(["worked","reference","filelinks","tablebox"]);
  function safeURL(value, image = false) {
    const raw = String(value || "").trim();
    if (!raw) return "";
    if (image && /^data:image\/(?:png|jpeg|webp|gif);base64,[a-z0-9+/=\s]+$/i.test(raw)) return raw;
    if (/^https?:\/\//i.test(raw)) {
      try { const u = new URL(raw); return !u.username && !u.password && (!image || u.protocol === "https:") ? u.href : ""; } catch { return ""; }
    }
    if (image) return /^photos\/[a-z0-9_.-]+$/i.test(raw) ? raw : "";
    return /^(?:(?:[a-z0-9_-]+\.(?:csv|html))(?:[?#][a-z0-9%&=_#-]*)?|#[a-z0-9_-]+)$/i.test(raw) ? raw : "";
  }
  function clean(raw) {
    const tpl = document.createElement("template"); tpl.innerHTML = String(raw || "");
    function copy(src, dst) {
      if (src.nodeType === 3) {dst.append(document.createTextNode(src.textContent));return;}
      if (src.nodeType !== 1) return;
      const tag = src.localName;
      if (["script","style","iframe","object","svg","math","template","form","link"].includes(tag)) return;
      if (!tags.has(tag)) { [...src.childNodes].forEach(n => copy(n,dst)); return; }
      if (tag === "div" && src.dataset.widget === "planner") {
        const x=document.createElement("div");x.dataset.widget="planner";x.textContent="Калькулятор времени";dst.append(x);return;
      }
      const el = document.createElement(tag);
      for (const c of src.classList) if (classes.has(c)) el.classList.add(c);
      if (tag === "a") {const href=safeURL(src.getAttribute("href"));if(href)el.setAttribute("href",href);if(/^[\w-]+\.csv$/.test(href))el.setAttribute("download","");}
      if (tag === "img") {
        const url=safeURL(src.getAttribute("src"),true);if(!url)return;
        el.setAttribute("src",url);el.setAttribute("alt",src.getAttribute("alt")||"");el.loading="lazy";el.decoding="async";
      }
      if (tag === "th" && ["row","col"].includes(src.getAttribute("scope"))) el.scope=src.getAttribute("scope");
      dst.append(el);[...src.childNodes].forEach(n=>copy(n,el));
    }
    const out=document.createElement("div");[...tpl.content.childNodes].forEach(n=>copy(n,out));return out.innerHTML;
  }
  function text(html) {const tmp=document.createElement("template");tmp.innerHTML=html||"";return (tmp.content.textContent||"").trim();}
  const address = (item,kind) => item.page || kind+".html?id="+encodeURIComponent(item.id);
  const link = (item,kind) => escape(address(item,kind));
  const nless = n=> n+" "+((n%100>=11&&n%100<=14)?"уроков":n%10===1?"урок":n%10>=2&&n%10<=4?"урока":"уроков");
  function topCover(c,idx) {
    const src=safeURL(c.cover,true);
    return src?'<img src="'+escape(src)+'" alt="'+escape(c.alt||"")+'" '+(idx<3?'':'loading="lazy"')+' decoding="async">':'<div class="plaincover" aria-hidden="true"></div>';
  }
  function home(book) {
    const total=book.chapters.reduce((n,c)=>n+c.lessons.length,0);
    const cards=book.chapters.map((c,i)=>'<a class="covercard" href="'+link(c,"chapter")+'"><div class="cardphoto">'+topCover(c,i)+'</div><div class="cardcopy"><p class="eyebrow">Глава '+(i+1)+' <span>·</span> '+nless(c.lessons.length)+'</p><h2>'+escape(c.title)+'</h2><p class="summary">'+escape(text(c.description))+'</p></div></a>').join("");
    return '<header class="homehead"><p class="eyebrow">ОГЭ и ЕГЭ · 9–11 классы</p><h1>Справочник для учеников</h1><p class="homecount">'+book.chapters.length+' глав · '+nless(total)+'</p></header><div class="cardgrid">'+cards+'</div><section class="resources"><h2>Для самостоятельной подготовки</h2><div><a href="https://kompege.ru/">КомпЕГЭ ↗</a><a href="https://stepik.org/a/177464">Курс на Stepik · задачи 1–23 ↗</a><a href="https://kerico-0548.github.io/ege-knowledge-base/pearl-preview/?v=5#home">Набор решений ↗</a></div></section>';
  }
  function outline(book,chapter,lesson) {
    return '<nav aria-label="Главы и уроки" class="outline"><h2>Содержание</h2>'+book.chapters.map((c,i)=>{
      const active=c.id===chapter.id;
      return '<details'+(active?' open':'')+'><summary><span class="unit">'+(i+1)+'</span>'+escape(c.title)+'</summary><div><a class="overview" href="'+link(c,"chapter")+'">Обзор главы</a>'+c.lessons.map((l,j)=>'<a href="'+link(l,"lesson")+'"'+(lesson?.id===l.id?' aria-current="page"':'')+'><span>'+(i+1)+'.'+(j+1)+'</span>'+escape(l.title)+'</a>').join("")+'</div></details>';
    }).join("")+'</nav>';
  }
  const trail = c=>'<nav class="trail" aria-label="Путь"><a href="index.html">Все главы</a>'+(c?' <span>/</span> <a href="'+link(c,"chapter")+'">'+escape(c.title)+'</a>':'')+'</nav>';
  function layout(book,c,l,body) {
    const nav=outline(book,c,l);
    return trail(l?c:null)+'<details class="mobile-outline"><summary>Главы и уроки</summary>'+nav+'</details><div class="coursegrid"><aside>'+nav+'</aside><div class="coursebody">'+body+'</div></div>';
  }
  function chapter(book,c) {
    const i=book.chapters.indexOf(c)+1;
    const photo=safeURL(c.cover,true)?'<div class="chapterphoto">'+topCover(c,0)+'</div>':'';
    const lessons=c.lessons.map((l,j)=>'<li><a href="'+link(l,"lesson")+'"><span class="indexno">'+i+'.'+(j+1)+'</span><span>'+escape(l.title)+'</span><span class="arrow" aria-hidden="true">→</span></a></li>').join("");
    return layout(book,c,null,'<article><header class="chapterhead"><p class="eyebrow">Глава '+i+' · '+nless(c.lessons.length)+'</p><h1>'+escape(c.title)+'</h1><div class="intro">'+clean(c.description)+'</div>'+photo+'</header><h2 class="units-title">Уроки главы</h2>'+(lessons?'<ol class="lesson-list">'+lessons+'</ol>':'<p>Уроки ещё не добавлены.</p>')+'</article>');
  }
  function lesson(book,c,l) {
    const div=document.createElement("div");div.innerHTML=clean(l.body);
    const heads=[...div.querySelectorAll("h2")];
    heads.forEach((h,i)=>h.id="part-"+(i+1));
    const toc=heads.length?'<details class="inlesson"><summary>В этом уроке</summary><ol>'+heads.map(h=>'<li><a href="#'+h.id+'">'+escape(h.textContent)+'</a></li>').join("")+'</ol></details>':"";
    const i=c.lessons.indexOf(l),prev=c.lessons[i-1],next=c.lessons[i+1];
    const pageLink=(v,back)=>'<a href="'+link(v||c,v?"lesson":"chapter")+'"><small>'+(v?(back?'← Предыдущий урок':'Следующий урок →'):(back?'← К главе':'К главе →'))+'</small>'+escape((v||c).title)+'</a>';
    return layout(book,c,l,'<article><header class="lessonhead"><p class="eyebrow">Урок '+(book.chapters.indexOf(c)+1)+'.'+(i+1)+'</p><h1>'+escape(l.title)+'</h1><div class="intro">'+clean(l.description)+'</div></header>'+toc+'<div class="prose">'+div.innerHTML+'</div><nav class="turn" aria-label="Переход между уроками">'+pageLink(prev,true)+pageLink(next,false)+'</nav></article>');
  }
  function initExtras(root) {
    for(const marker of root.querySelectorAll('[data-widget="planner"]')){
      marker.className="tool";
      marker.innerHTML='<form class="budget-form"><div class="fields">'+[["Занятий в неделю",21,3],["Минут за занятие",240,35],["Недель",104,6]].map(([name,max,val])=>'<label>'+name+'<input type="number" required min="1" max="'+max+'" value="'+val+'"></label>').join("")+'</div><output aria-live="polite"></output></form><a href="week-plan.csv" download>Скачать пример плана для Excel (CSV)</a>';
      const form=marker.querySelector("form"),result=form.querySelector("output"),inputs=[...form.querySelectorAll("input")];
      function update(){const [s,m,w]=inputs.map(x=>x.valueAsNumber);result.textContent=inputs.every(x=>x.validity.valid)?s*m+' мин в неделю · '+(s*m*w/60).toLocaleString("ru-RU",{maximumFractionDigits:1})+' ч за весь период':'Проверь числа в полях.';}
      form.addEventListener("input",update);form.addEventListener("submit",e=>e.preventDefault());update();
    }
    for(const im of root.querySelectorAll(".prose figure img,.intro figure img")){
      const btn=document.createElement("button");btn.type="button";btn.className="viewphoto";btn.setAttribute("aria-label","Увеличить изображение: "+im.alt);im.replaceWith(btn);btn.append(im);btn.addEventListener("click",()=>{
        const d=document.createElement("dialog");d.className="lightbox";const close=document.createElement("button");close.textContent="Закрыть";const big=im.cloneNode();big.loading="eager";d.append(close,big);document.body.append(d);close.addEventListener("click",()=>d.close());d.addEventListener("click",e=>{if(e.target===d)d.close()});d.addEventListener("close",()=>{d.remove();btn.focus()},{once:true});d.showModal();
      });
    }
  }
  function render() {
    const route=document.body.dataset.route,book=window.STUDY_GUIDE;
    if(!route||!book)return;
    const param=new URLSearchParams(location.search).get("id");
    const id=["chapter","lesson"].includes(route)?param:route;
    const c=book.chapters.find(x=>x.id===id || x.lessons.some(l=>l.id===id)),l=c?.lessons.find(x=>x.id===id);
    const root=document.querySelector("#main");
    if(route==="index"){root.innerHTML=home(book);return;}
    if(!c){root.innerHTML='<h1>Страница не найдена</h1><p><a href="index.html">Вернуться к главам</a></p>';return;}
    root.innerHTML=l?lesson(book,c,l):chapter(book,c);
    document.title=(l||c).title+' · Справочник';
    initExtras(root);
    if(/^#part-\d+$/.test(location.hash))requestAnimationFrame(()=>document.getElementById(location.hash.slice(1))?.scrollIntoView());
  }
  window.Guide={escape,clean,text,safeURL,address,home,lesson,chapter,initExtras};
  render();
})();
