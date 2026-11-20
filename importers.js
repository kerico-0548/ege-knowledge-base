/* Local file readers. No document or token is sent to an external service. */
window.KBImport=(()=>{
 const utf8=new TextDecoder(),NS='*';let workerPromise;
 const decode=b=>{let s=utf8.decode(b);if((s.match(/�/g)||[]).length>8){try{s=new TextDecoder('windows-1251').decode(b)}catch{}}return s.replace(/^\uFEFF/,'')};
 const xml=s=>new DOMParser().parseFromString(s,'application/xml');
 const els=(n,name)=>[...n.getElementsByTagNameNS(NS,name)];
 const unzip=b=>fflate.unzipSync(new Uint8Array(b),{filter:f=>f.originalSize<80*1024*1024});
 const content=n=>els(n,'t').map(t=>t.textContent).join('');
 const clean=s=>s.replace(/\u00a0/g,' ').replace(/\u200b/g,'').trim();
 async function loadOCR(progress){
  if(!workerPromise)workerPromise=(async()=>{
   if(!window.Tesseract)await new Promise((res,rej)=>{const s=document.createElement('script');s.src='vendor/tesseract/tesseract.min.js';s.onload=res;s.onerror=()=>rej(Error('Не удалось открыть локальный модуль распознавания'));document.head.append(s)});
   const base=new URL('.',location.href);
   return Tesseract.createWorker('rus+eng',1,{workerPath:new URL('vendor/tesseract/worker.min.js',base).href,corePath:new URL('vendor/tesseract/core/',base).href,langPath:new URL('vendor/tesseract/lang',base).href,logger:m=>progress?.(m.status==='recognizing text'?'Распознаю текст: '+Math.round(m.progress*100)+'%':'Подготавливаю распознавание…')});
  })().catch(e=>{workerPromise=null;throw e});
  return workerPromise;
 }
 async function ocr(blob,progress){
  if(blob.type==='image/svg+xml'){
   const d=xml(await blob.text()),lines=[...d.querySelectorAll('.CodeMirror-line')];
   if(lines.length)return {text:lines.map(n=>n.textContent.replace(/\u00a0/g,' ')).join('\n'),code:true,status:'Текст извлечён из SVG'};
  }
  const w=await loadOCR(progress),url=URL.createObjectURL(blob);
  try{const r=await w.recognize(url);return {text:clean(r.data.text),confidence:r.data.confidence,status:'Распознано автоматически, нужна сверка'}}finally{URL.revokeObjectURL(url)}
 }
 function office(data,ext){
  const z=unzip(data);let parts=[],chunks=[],tables=[],embeddedImages=[];
  if(ext==='docx')parts=['word/document.xml'];
  else if(ext==='pptx')parts=Object.keys(z).filter(n=>/^ppt\/slides\/slide\d+\.xml$/.test(n)).sort((a,b)=>parseInt(a.match(/\d+/)[0])-parseInt(b.match(/\d+/)[0]));
  else if(ext==='xlsx'){
   const ss=z['xl/sharedStrings.xml']?els(xml(utf8.decode(z['xl/sharedStrings.xml'])),'si').map(content):[];
   const book=z['xl/workbook.xml']?xml(utf8.decode(z['xl/workbook.xml'])):null,names=book?els(book,'sheet').map(n=>n.getAttribute('name')):[];
   const sheets=Object.keys(z).filter(n=>/^xl\/worksheets\/sheet\d+\.xml$/.test(n)).sort((a,b)=>parseInt(a.match(/\d+/)[0])-parseInt(b.match(/\d+/)[0]));
   sheets.forEach((name,i)=>{
    const d=xml(utf8.decode(z[name])),allRows=els(d,'row'),rows=allRows.slice(0,120).map(r=>{
     const arr=[];els(r,'c').forEach(c=>{const a=(c.getAttribute('r')||'A1').replace(/\d/g,''),index=[...a].reduce((v,ch)=>v*26+ch.charCodeAt(0)-64,0)-1;if(index>60)return;const v=els(c,'v')[0]?.textContent??'',type=c.getAttribute('t');arr[index]=type==='s'?ss[Number(v)]??'':type==='inlineStr'?content(c):v;});return Array.from({length:Math.min(Math.max(arr.length,1),61)},(_,i)=>arr[i]??'');
    });tables.push({title:names[i]||'Лист '+(i+1),columns:[],rows,total_rows:allRows.length,preview_only:allRows.length>120});chunks.push((names[i]||name)+'\n'+rows.map(r=>r.join('\t')).join('\n'));
   });return {text:chunks.join('\n\n'),tables,sheets:names,embeddedImages};
  }else parts=['content.xml'];
  for(const [i,name] of parts.entries()){
   if(!z[name])continue;const d=xml(utf8.decode(z[name]));
   const ps=els(d,'p').map(p=>ext==='ods'||ext==='odt'?p.textContent:content(p)).filter(s=>s.trim());
   chunks.push((ext==='pptx'?'Слайд '+(i+1)+'\n':'')+ps.join('\n'));
   if(ext==='docx')for(const tbl of els(d,'tbl'))tables.push({title:'Таблица из документа',columns:[],rows:els(tbl,'tr').map(tr=>els(tr,'tc').map(content))});
  }
  for(const name of Object.keys(z).filter(n=>/^(word|ppt)\/media\//.test(n)&&/\.(png|jpe?g|webp|svg)$/i.test(n))){const ext=name.split('.').pop().toLowerCase();embeddedImages.push({name:name.split('/').pop(),blob:new Blob([z[name]],{type:ext==='svg'?'image/svg+xml':ext==='jpg'?'image/jpeg':'image/'+ext})});}
  return {text:clean(chunks.join('\n\n')),tables,embeddedImages,slides:ext==='pptx'?parts.length:undefined};
 }
 async function pdf(data,progress){
  const pdfjs=await import('./vendor/pdfjs/pdf.mjs');pdfjs.GlobalWorkerOptions.workerSrc=new URL('vendor/pdfjs/pdf.worker.mjs',new URL('.',location.href)).href;
  const loading=pdfjs.getDocument({data:new Uint8Array(data),standardFontDataUrl:new URL('vendor/pdfjs/standard_fonts/',new URL('.',location.href)).href,wasmUrl:new URL('vendor/pdfjs/wasm/',new URL('.',location.href)).href});const d=await loading.promise;let chunks=[];
  for(let i=1;i<=d.numPages;i++){
   progress?.('Читаю PDF: '+i+' / '+d.numPages);const p=await d.getPage(i),c=await p.getTextContent();let t=c.items.map(x=>x.str+(x.hasEOL?'\n':' ')).join('');
   if(t.trim().length<15){
    const view=p.getViewport({scale:1.7}),canvas=document.createElement('canvas');canvas.width=view.width;canvas.height=view.height;await p.render({canvasContext:canvas.getContext('2d'),viewport:view}).promise;
    const blob=await new Promise(res=>canvas.toBlob(res));const r=await ocr(blob,progress);t=r.text;canvas.width=canvas.height=0;
   }
   chunks.push('Страница '+i+'\n'+t);p.cleanup();
  }
  await loading.destroy();return {text:clean(chunks.join('\n\n')),pages:chunks.length,tables:[]};
 }
 async function read(file,progress){
  if(file.size>100*1024*1024)throw Error('Этот файл больше 100 МБ. Добавь его через папку входящих материалов на GitHub.');
  const ext=file.name.split('.').pop().toLowerCase(),data=await file.arrayBuffer();
  if(['png','jpg','jpeg','webp','svg'].includes(ext))return {...await ocr(file,progress),image:true,tables:[]};
  if(['docx','pptx','xlsx','ods','odt'].includes(ext))return office(data,ext);
  if(ext==='pdf')return pdf(data,progress);
  if(ext==='xls')return {text:'Исходная книга XLS сохранена. Для текстового просмотра сохрани её в XLSX и добавь ещё раз.',tables:[],preview_only:true};
  let text=decode(data);
  if(ext==='step'){
   const j=JSON.parse(text),b=j.block||j,d=new DOMParser().parseFromString(b.text||'','text/html');text=d.body.innerText||d.body.textContent;return {text:clean(text),tables:[],codes:[...d.querySelectorAll('pre')].map(n=>n.textContent)};
  }
  if(ext==='kum'&&text.trim().startsWith('<'))text=xml(text).documentElement.textContent;
  return {text,tables:[],code:ext==='py'||ext==='kum',language:ext==='kum'?'kumir':'python'};
 }
 return {read,ocr,office,decode};
})();
