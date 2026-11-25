(() => {
  "use strict";
  const $=id=>document.getElementById(id), G=window.Guide;
  const api="https://api.github.com/repos/kerico-0548/ege-knowledge-base";
  const endpoint=api+"/contents/student-guide/materials.js";
  const prefix="window.STUDY_GUIDE = ";
  const copy=x=>JSON.parse(JSON.stringify(x));
  const uid=()=>crypto.randomUUID();
  const fresh=()=>({book:copy(window.STUDY_GUIDE),base:window.STUDY_GUIDE.revision,chapter:window.STUDY_GUIDE.chapters[0].id,lesson:null});
  let state=fresh(),db,stamp=null,queue=Promise.resolve(),busy=false,conflict=false,dirty=false,activeBox=null,range=null;
  const boxes={};
  const chapter=()=>state.book.chapters.find(c=>c.id===state.chapter);
  const lesson=()=>chapter()?.lessons.find(l=>l.id===state.lesson);
  const item=()=>lesson()||chapter();
  function openDB(){
    return new Promise((resolve,reject)=>{const req=indexedDB.open("kerico-study-author",1);
      req.onupgradeneeded=()=>req.result.createObjectStore("draft");req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error);});
  }
  function readDraft(){return new Promise((resolve,reject)=>{const req=db.transaction("draft").objectStore("draft").get("current");req.onsuccess=()=>resolve(req.result);req.onerror=()=>reject(req.error);});}
  function writeDraft(snapshot){
    return new Promise((resolve,reject)=>{const tx=db.transaction("draft","readwrite"),store=tx.objectStore("draft"),check=store.get("current");const next=uid();
      check.onsuccess=()=>{if((check.result?.stamp??null)!==stamp){conflict=true;tx.abort();return;}store.put({stamp:next,state:snapshot},"current");};
      tx.oncomplete=()=>{stamp=next;resolve();};tx.onabort=tx.onerror=()=>reject(tx.error||new Error("Черновик изменён в другой вкладке."));});
  }
  function saved(message){$("save-state").textContent=message;}
  let sequence=0,saveTimer;
  function saveNow(){
    clearTimeout(saveTimer);
    if(!dirty)return queue;
    const current=sequence,snapshot=copy(state);
    queue=queue.then(async()=>{
      if(!db||conflict)throw new Error("Хранилище недоступно.");
      await writeDraft(snapshot);
      if(current===sequence){dirty=false;saved("Черновик сохранён в этом браузере.");}
    }).catch(()=>saved(conflict?"Черновик изменён в другой вкладке. Скачай свои правки перед перезагрузкой.":"Не удалось сохранить в браузере. Скачай materials.js в окне публикации."));
    return queue;
  }
  function change(){dirty=true;sequence++;saved("Сохраняем черновик…");clearTimeout(saveTimer);saveTimer=setTimeout(saveNow,250);}
  window.addEventListener("beforeunload",e=>{if(dirty){e.preventDefault();e.returnValue="";}});
  document.addEventListener("visibilitychange",()=>{if(document.hidden&&dirty)saveNow();});
  function tree(){
    const host=$("tree");host.replaceChildren();
    for(const [i,c] of state.book.chapters.entries()){
      const b=document.createElement("button");b.type="button";b.textContent=(i+1)+". "+(c.title||"Без названия");b.className="chapter-btn";
      b.setAttribute("aria-pressed",String(c.id===state.chapter&&!state.lesson));b.onclick=()=>pick(c.id,null);host.append(b);
      if(c.id!==state.chapter)continue;
      const nested=document.createElement("div");nested.className="nested";
      c.lessons.forEach((l,k)=>{const a=document.createElement("button");a.type="button";a.textContent=(i+1)+"."+(k+1)+" "+(l.title||"Без названия");a.setAttribute("aria-pressed",String(state.lesson===l.id));a.onclick=()=>pick(c.id,l.id);nested.append(a);});
      const add=document.createElement("button");add.type="button";add.className="add";add.textContent="+ Добавить урок";add.onclick=()=>{const id="l-"+uid();c.lessons.push({id,title:"Новый урок",description:"",body:"<p><br></p>"});pick(c.id,id,true);};nested.append(add);host.append(nested);
    }
  }
  function pick(cid,lid,focus=false){
    state.chapter=cid;state.lesson=lid;range=null;activeBox=null;tree();fill();mode(false);change();
    document.querySelector(".editnav").classList.remove("expanded");$("nav-toggle").setAttribute("aria-expanded","false");
    if(focus){$("title").focus();$("title").select();}
  }
  $("new-chapter").onclick=()=>{const id="c-"+uid();state.book.chapters.push({id,title:"Новая глава",description:"",cover:"",alt:"",lessons:[]});pick(id,null,true);};
  function remember(box){const sel=window.getSelection();if(sel?.rangeCount&&box.contains(sel.anchorNode)&&box.contains(sel.focusNode)){range=sel.getRangeAt(0).cloneRange();activeBox=box;}}
  function restore(box){
    box.focus();const sel=window.getSelection();let r=range;
    if(!r||!box.contains(r.commonAncestorContainer)){r=document.createRange();r.selectNodeContents(box);r.collapse(false);}
    sel.removeAllRanges();sel.addRange(r);
  }
  function syncBox(box){item()[box.dataset.field]=G.clean(box.innerHTML);change();}
  function insert(box,html){restore(box);document.execCommand("insertHTML",false,html);remember(box);syncBox(box);}
  function prepareWidgetView(box){for(const el of box.querySelectorAll("[data-widget]"))el.contentEditable="false";}
  function createBox(key,host,label){
    const wrap=$(host);const name=document.createElement("div");name.className="field-label";name.textContent=label;name.id=key+"-label";
    const toolbar=document.createElement("div");toolbar.className="toolbar";toolbar.setAttribute("role","group");toolbar.setAttribute("aria-label","Форматирование: "+label);
    const box=document.createElement("div");box.className="rich";box.contentEditable="true";box.setAttribute("role","textbox");box.setAttribute("aria-multiline","true");box.setAttribute("aria-labelledby",name.id);box.dataset.field=key;boxes[key]=box;
    const add=(caption,title,fn)=>{const b=document.createElement("button");b.type="button";b.textContent=caption;b.title=title;b.setAttribute("aria-label",title);b.onmousedown=e=>{e.preventDefault();remember(box);};b.onclick=()=>{if(activeBox!==box){range=null;activeBox=box;}restore(box);fn();};toolbar.append(b);};
    for(const [cap,title,cmd,val] of [["Ж","Жирный","bold"],["К","Курсив","italic"],["Ч","Подчёркивание","underline"],["Абзац","Обычный абзац","formatBlock","p"],["H2","Заголовок раздела","formatBlock","h2"],["H3","Подзаголовок","formatBlock","h3"],["• Список","Маркированный список","insertUnorderedList"],["1. Список","Нумерованный список","insertOrderedList"],["Цитата","Цитата или пример","formatBlock","blockquote"]]){
      add(cap,title,()=>{document.execCommand(cmd,false,val||null);remember(box);syncBox(box);});
    }
    add("Ссылка","Вставить ссылку",()=>{remember(box);$("link-text").value=window.getSelection().toString();$("link-url").value="";$("link-dialog").showModal();});
    add("Фото","Вставить изображение",()=>{remember(box);$("image-form").reset();$("image-state").textContent="";$("image-dialog").showModal();});
    box.oninput=()=>{remember(box);syncBox(box);};for(const evt of ["focus","keyup","mouseup","touchend"])box.addEventListener(evt,()=>remember(box));
    function pasteContent(e){
      e.preventDefault();const transfer=e.clipboardData||e.dataTransfer;if(!transfer)return;remember(box);
      const file=[...transfer.files].find(f=>f.type.startsWith("image/"));
      if(file){const dest=item().id;readImage(file).then(src=>{if(item().id!==dest)return;insert(box,figure(src,file.name.replace(/\.[^.]+$/,"")));}).catch(err=>saved(err.message));return;}
      const html=transfer.getData("text/html");
      if(html){insert(box,G.clean(html));return;}
      insert(box,transfer.getData("text/plain").split(/\r?\n/).map(l=>"<p>"+G.escape(l)+"</p>").join(""));
    }
    box.addEventListener("paste",pasteContent);box.addEventListener("drop",pasteContent);
    wrap.append(name,toolbar,box);
  }
  createBox("description","desc-field","Описание");createBox("body","body-field","Текст урока");
  function fill(){
    const x=item(),c=chapter(),isLesson=!!lesson();$("title-label").textContent=isLesson?"Название урока":"Название главы";$("title").value=x.title;
    $("body-field").hidden=!isLesson;$("cover-row").hidden=isLesson;
    for(const [k,b] of Object.entries(boxes)){b.innerHTML=G.clean(x[k]||"");prepareWidgetView(b);}
    $("cover-alt").value=c.alt||"";const src=G.safeURL(c.cover,true);$("cover-preview").hidden=!src;
    if(src)$("cover-preview").src=src;else $("cover-preview").removeAttribute("src");
  }
  $("title").oninput=()=>{item().title=$("title").value;tree();change();};$("cover-alt").oninput=()=>{chapter().alt=$("cover-alt").value;change();};
  function mode(preview){
    $("edit-mode").setAttribute("aria-pressed",String(!preview));$("preview-mode").setAttribute("aria-pressed",String(preview));
    $("fields").hidden=preview;$("preview").hidden=!preview;
    if(preview){const body=lesson()?G.lesson(state.book,chapter(),lesson()):G.chapter(state.book,chapter());const tmp=document.createElement("template");tmp.innerHTML=body;$("preview").replaceChildren(tmp.content.querySelector(".coursebody"));G.initExtras($("preview"));}
  }
  $("edit-mode").onclick=()=>mode(false);$("preview-mode").onclick=()=>mode(true);
  async function readImage(file){
    if(!file||!["image/png","image/jpeg","image/webp","image/gif"].includes(file.type))throw Error("Выбери файл JPG, PNG, WebP или GIF.");
    const url=URL.createObjectURL(file),im=new Image();
    try{im.src=url;await im.decode();const factor=Math.min(1,1280/Math.max(im.width,im.height));const cv=document.createElement("canvas");cv.width=Math.max(1,Math.round(im.width*factor));cv.height=Math.max(1,Math.round(im.height*factor));cv.getContext("2d").drawImage(im,0,0,cv.width,cv.height);return cv.toDataURL("image/webp",.82);}
    finally{URL.revokeObjectURL(url);}
  }
  const figure=(src,caption)=>'<figure><img src="'+G.escape(src)+'" alt="'+G.escape(caption)+'">'+(caption?'<figcaption>'+G.escape(caption)+'</figcaption>':"")+'</figure><p><br></p>';
  $("cover-change").onclick=()=>$("cover-file").click();
  $("cover-file").onchange=async e=>{const f=e.target.files[0],c=chapter();if(!f)return;try{c.cover=await readImage(f);if(chapter()===c){$("cover-preview").src=c.cover;$("cover-preview").hidden=false;}change();}catch(err){saved(err.message);}e.target.value="";};
  $("image-form").onsubmit=async e=>{e.preventDefault();if(busy)return;const file=$("image-file").files[0],caption=$("image-caption").value.trim(),box=activeBox;
    try{busy=true;const src=file?await readImage(file):G.safeURL($("image-url").value,true);if(!src)throw Error("Выбери файл или вставь HTTPS-ссылку на изображение.");
      $("image-dialog").close();insert(box,figure(src,caption));}catch(err){$("image-state").textContent=err.message;}finally{busy=false;}
  };
  $("link-form").onsubmit=e=>{e.preventDefault();const url=G.safeURL($("link-url").value);if(!url){$("link-url").setCustomValidity("Укажи адрес http или https.");$("link-url").reportValidity();return;}
    const box=activeBox;$("link-dialog").close();insert(box,'<a href="'+G.escape(url)+'">'+G.escape($("link-text").value||url)+'</a>');};
  $("link-url").oninput=()=>$("link-url").setCustomValidity("");
  document.querySelectorAll("[data-close]").forEach(b=>b.onclick=()=>b.closest("dialog").close());
  $("publish-open").onclick=()=>{$("publish-state").textContent="";$("publish-dialog").showModal();};
  $("publish-dialog").onclose=()=>{$("key").value="";};
  function edition(){
    for(const c of state.book.chapters){if(!c.title.trim())throw Error("В одной из глав пустое название.");for(const l of c.lessons){if(!l.title.trim())throw Error("В одном из уроков пустое название.");if(!G.text(l.body)&&!/<img |data-widget/.test(l.body))throw Error("Добавь текст или изображение в урок «"+l.title+"».");}}
    const book=copy(state.book);book.revision=uid();return {book,source:prefix+JSON.stringify(book,null,2)+";\n"};
  }
  function download(source){const url=URL.createObjectURL(new Blob([source],{type:"text/javascript;charset=utf-8"}));const a=document.createElement("a");a.href=url;a.download="materials.js";a.click();setTimeout(()=>URL.revokeObjectURL(url),3000);}
  $("export").onclick=()=>{try{download(edition().source);$("publish-state").textContent="Файл с текстами и добавленными фотографиями подготовлен для загрузки."; }catch(err){$("publish-state").textContent=err.message;}};
  function base64(str){const arr=new TextEncoder().encode(str);let out="";for(let i=0;i<arr.length;i+=24000)out+=String.fromCharCode(...arr.subarray(i,i+24000));return btoa(out);}
  function decode(str){return new TextDecoder().decode(Uint8Array.from(atob(str),x=>x.charCodeAt(0)));}
  function unpack(source){if(!source.startsWith(prefix))throw Error("Формат материалов на GitHub изменён.");return JSON.parse(source.slice(prefix.length).trim().replace(/;$/,""));}
  async function publish(){
    if(busy)return;const key=$("key").value.trim();if(!key){$("publish-state").textContent="Введи ключ или выбери публикацию без ключа ниже.";$("key").focus();return;}
    const msg=$("publish-state");busy=true;$("send").disabled=true;
    try{
      const {book,source}=edition();
      const headers={Authorization:"Bearer "+key,Accept:"application/vnd.github+json"};
      async function gh(url,options={}){
        const r=await fetch(url,{...options,headers:{...headers,...options.headers},referrerPolicy:"no-referrer",cache:"no-store"});
        if(!r.ok)throw Error(({401:"GitHub отклонил ключ.",403:"У ключа недостаточно прав или исчерпан лимит GitHub.",404:"GitHub не нашёл файл или этот ключ не имеет доступа к репозиторию.",409:"Файл изменился на GitHub. Правки остались в черновике.",422:"GitHub не принял изменения. Проверь доступ к ветке main."})[r.status]||"Ответ GitHub: "+r.status);
        return r.json();
      }
      msg.textContent="Сверяем текущую версию на GitHub…";
      const remote=await gh(endpoint+"?ref=main");let encoded=remote.content;
      if(!encoded){const blob=await gh(api+"/git/blobs/"+encodeURIComponent(remote.sha));encoded=blob.content;}
      const remoteBook=unpack(decode(encoded));
      if(remoteBook.revision!==state.base){throw Error("На GitHub уже другая версия. Скачай свои правки для сверки. Случайной перезаписи не произошло.");}
      msg.textContent="Отправляем материалы…";
      const result=await gh(endpoint,{method:"PUT",headers:{"Content-Type":"application/json"},body:JSON.stringify({message:"Обновить главы и уроки справочника",branch:"main",sha:remote.sha,content:base64(source)})});
      state.base=book.revision;state.book.revision=book.revision;change();await saveNow();$("key").value="";
      msg.replaceChildren(document.createTextNode("Изменения сохранены на GitHub. После сборки они появятся у учеников. "));
      const a=document.createElement("a");a.href="https://github.com/kerico-0548/ege-knowledge-base/actions";a.target="_blank";a.rel="noopener noreferrer";a.textContent="Статус публикации ↗";msg.append(a);
    }catch(err){msg.textContent=err.message||"Отправка не завершена. Черновик сохранён.";}finally{busy=false;$("send").disabled=false;}
  }
  $("send").onclick=publish;
  $("copy-address").onclick=async()=>{
    const base="https://kerico-0548.github.io/ege-knowledge-base/student-guide/";
    const url=new URL(G.address(item(),lesson()?"lesson":"chapter"),base).href;
    try{await navigator.clipboard.writeText(url);saved("Адрес скопирован. Новые материалы откроются после публикации.");}
    catch{window.prompt("Ссылка для учеников",url);}
  };
  const nav=document.querySelector(".editnav");
  const navSwitch=document.createElement("button");navSwitch.id="nav-toggle";navSwitch.type="button";navSwitch.textContent="Выбрать главу или урок";navSwitch.setAttribute("aria-expanded","false");nav.prepend(navSwitch);
  navSwitch.onclick=()=>navSwitch.setAttribute("aria-expanded",String(nav.classList.toggle("expanded")));
  const tools=document.createElement("details");tools.className="tools-menu";tools.innerHTML='<summary>Работа с черновиком</summary><button type="button" id="backup">Скачать копию черновика</button><button type="button" id="reset">Открыть опубликованную версию заново</button>';nav.append(tools);
  $("backup").onclick=()=>download(prefix+JSON.stringify(state.book,null,2)+";\n");
  $("reset").onclick=async()=>{
    if(!confirm("Заменить черновик опубликованными материалами? Текущую копию можно предварительно скачать."))return;
    try {
      const source=location.protocol==="file:"?window.STUDY_GUIDE:unpack(await (async()=>{const r=await fetch("materials.js",{cache:"no-store"});if(!r.ok)throw Error("Не удалось загрузить опубликованные материалы.");return r.text();})());
      await saveNow();if(db){const old=await readDraft();stamp=old?.stamp??null;}conflict=false;state={book:copy(source),base:source.revision,chapter:source.chapters[0].id,lesson:null};tree();fill();mode(false);change();await saveNow();
    }catch(err){saved(err.message);}
  };
  async function init(){
    try{db=await openDB();const old=await readDraft();if(old?.state?.book?.version===1){stamp=old.stamp;state=old.state;}saved(old?"Открыт черновик из этого браузера.":"Открыта опубликованная версия.");}
    catch{saved("Хранилище браузера недоступно. Сохрани правки через окно публикации.");}
    if(!chapter()){state.chapter=state.book.chapters[0].id;state.lesson=null;}
    tree();fill();
  }
  init();
})();
