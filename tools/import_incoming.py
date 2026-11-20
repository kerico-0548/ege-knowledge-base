"""Rebuild the published data from committed incoming files. No credentials required."""
from pathlib import Path
import json,hashlib,re,zipfile,io,xml.etree.ElementTree as ET,subprocess,tempfile
from datetime import datetime
from pypdf import PdfReader
from bs4 import BeautifulSoup
import openpyxl

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'data'/'base.json'
data=json.loads(BASE.read_text(encoding='utf-8'));incoming=ROOT/'incoming';issues=[]
allowed={'.pdf','.docx','.pptx','.xlsx','.xls','.txt','.py','.md','.csv','.tsv','.png','.jpg','.jpeg','.webp','.svg','.kum','.step','.json','.zip'}
def clean(s):return str(s).replace('\xa0',' ').strip()
def ns(root,n):return [e for e in root.iter() if e.tag.split('}')[-1]==n]
def plain(root):return ''.join(e.text or '' for e in root.iter() if e.tag.split('}')[-1]=='t')
def inference(name):
    m=re.search(r'(?:задани[ея]|№|^)[\s_-]*(\d{1,2})(?:\D|$)',name,re.I)
    if not m or not 1<=int(m[1])<=27:return ''
    return '19-21' if m[1] in ('19','20','21') else m[1]
def text_bytes(b):
    for enc in ('utf-8-sig','cp1251'):
        try:return b.decode(enc)
        except UnicodeError:pass
    return b.decode('utf-8',errors='replace')
def ocr(path):
    p=subprocess.run(['tesseract',str(path),'stdout','-l','rus+eng'],capture_output=True,text=True,timeout=120)
    if p.returncode:raise RuntimeError('OCR failed')
    return p.stdout.strip()
def parse(f):
    ext=f.suffix.lower();text='';tables=[];images=[];meta={}
    if ext in ('.py','.txt','.md','.csv','.tsv','.kum','.json','.step'):
        text=text_bytes(f.read_bytes())
        if ext=='.step':
            j=json.loads(text);b=j.get('block',j);text=BeautifulSoup(b.get('text',''),'html.parser').get_text('\n')
        if ext=='.kum' and text.lstrip().startswith('<'):text='\n'.join(ET.fromstring(text).itertext())
        if len(text)>180000:text='\n'.join(text.splitlines()[:120]);meta['preview_only']=True
    elif ext in ('.docx','.pptx'):
        with zipfile.ZipFile(f) as z:
            parts=['word/document.xml'] if ext=='.docx' else sorted([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)],key=lambda n:int(re.search(r'(\d+)\.xml$',n)[1]))
            chunks=[]
            for i,n in enumerate(parts,1):
                r=ET.fromstring(z.read(n));chunks.append(('Слайд '+str(i)+'\n' if ext=='.pptx' else '')+'\n'.join(plain(p) for p in ns(r,'p')))
                for t in ns(r,'tbl'):tables.append({'title':'Таблица из документа','columns':[],'rows':[[plain(c) for c in ns(row,'tc')] for row in ns(t,'tr')]})
            text='\n\n'.join(chunks)
            for n in z.namelist():
                if re.match(r'^(word|ppt)/media/',n) and Path(n).suffix.lower() in ('.png','.jpg','.jpeg','.webp','.svg'):
                    b=z.read(n);h=hashlib.sha256(b).hexdigest()[:24];dest=ROOT/'media'/(h+Path(n).suffix.lower());dest.write_bytes(b)
                    try:t=ocr(dest) if dest.suffix!='.svg' else BeautifulSoup(b,'xml').get_text('\n')
                    except Exception:t='';issues.append({'file':f.name,'image':n,'reason':'Нужна ручная сверка изображения'})
                    data['media'][h]={'id':h,'name':f.name+' · '+Path(n).name,'url':str(dest.relative_to(ROOT)).replace('\\','/'),'text':t,'status':'recognized_automatically','description':'Вложение документа. Автоматический текст требует сверки.','sources':[str(f.relative_to(ROOT))+'::'+n]};images.append(h)
    elif ext=='.pdf':
        r=PdfReader(f);chunks=[];meta['pages']=len(r.pages)
        for i,p in enumerate(r.pages):
            t=p.extract_text() or ''
            if len(t.strip())<15:
                try:
                    with tempfile.TemporaryDirectory() as tmp:
                        out=Path(tmp)/'page';subprocess.run(['pdftoppm','-f',str(i+1),'-l',str(i+1),'-singlefile','-scale-to','2000','-png',str(f),str(out)],check=True,capture_output=True,timeout=90);t=ocr(out.with_suffix('.png'))
                except Exception:issues.append({'file':f.name,'page':i+1,'reason':'Не удалось распознать страницу'})
            chunks.append('Страница '+str(i+1)+'\n'+t)
        text='\n\n'.join(chunks)
    elif ext=='.xlsx':
        w=openpyxl.load_workbook(f,read_only=True,data_only=True)
        for s in w:
            rows=[]
            for i,r in enumerate(s.iter_rows(values_only=True)):
                if i>=100:break
                rows.append([str(v) if v is not None else '' for v in r[:30]])
            tables.append({'title':s.title,'columns':[],'rows':rows,'total_rows':s.max_row,'preview_only':s.max_row>100})
        text='\n\n'.join(t['title']+'\n'+'\n'.join('\t'.join(row) for row in t['rows']) for t in tables);w.close()
    elif ext in ('.png','.jpg','.jpeg','.webp','.svg'):
        text=BeautifulSoup(f.read_bytes(),'xml').get_text('\n') if ext=='.svg' else ocr(f)
    else:text='Оригинальный файл сохранён для скачивания.'
    return {'text':clean(text),'tables':tables,'images':images,**meta}
def all_codes():
    for r in data['tasks']+data['methods']:
        yield from r.get('codes',[])
    for l in data['lessons']:
        for s in l['steps']:yield from s.get('codes',[])
def apply_patch(j):
    if j.get('version')!=1:return
    for t in j.get('tasks',[]):
        if not isinstance(t,dict) or not t.get('id'):continue
        t={k:v for k,v in t.items() if k not in ('blob','url','html')};t['status']='user';t['status_label']='Авторский разбор · нужна проверка';t['local']=False
        data['tasks']=[x for x in data['tasks'] if x['id']!=t['id']]+[t]
    codes={c['id']:c for c in all_codes()}
    for key,text in j.get('edits',{}).items():
        if not isinstance(text,str):continue
        if key in codes:
            c=codes[key];c.setdefault('original_code',c['code']);c['code']=text;c['status']='Редакция общей базы · нужна проверка'
            for t in data['tasks']:
                if any(x['id']==key for x in t.get('codes',[])):t['status']='edited';t['status_label']='Редакция общей базы · нужна проверка'
        elif key.startswith('image:') and key[6:] in data['media']:data['media'][key[6:]]['text']=text;data['media'][key[6:]]['status']='edited'
        elif key.startswith('filetext:'):
            for f in data['files']:
                if f['id']==key[9:]:f['text']=text
        elif key.startswith('table:'):
            for t in data['tasks']:
                for i,b in enumerate(t.get('visuals',[])):
                    if key=='table:'+t['id']+'_'+str(i):
                        rows=[r.split('\t') for r in text.splitlines()]
                        if b.get('columns'):b['columns']=rows.pop(0) if rows else []
                        b['rows']=rows;t['status']='edited';t['status_label']='Редакция общей базы · нужна проверка'
    for key,vals in j.get('overrides',{}).items():
        for t in data['tasks']:
            if t['id']==key:
                t.update({k:v for k,v in vals.items() if k in ('title','condition','solution','answer','task','group') and isinstance(v,str)});t['status']='edited';t['status_label']='Редакция общей базы · нужна проверка'
    data.setdefault('publicNotes',{}).update({k:v for k,v in j.get('notes',{}).items() if isinstance(v,str)})
    for note in j.get('materials',[]):append_note(note)

def append_note(note):
    if not isinstance(note,dict) or not note.get('id'):return
    text=str(note.get('text',''));raw=text.encode('utf-8');h=hashlib.sha256(raw).hexdigest();dest=ROOT/'files'/(h[:24]+'.md');dest.write_bytes(raw)
    r={'id':note['id'],'kind':'file','title':str(note.get('title','Заметка')),'name':str(note.get('title','Заметка'))+'.md','extension':'md','url':str(dest.relative_to(ROOT)).replace('\\','/'),'bytes':len(raw),'sha256':h,'text':text,'tasks':note.get('tasks',[]),'sources':['Добавлено из личной библиотеки'],'tables':[],'images':[],'local':False}
    data['files']=[x for x in data['files'] if x['id']!=r['id']]+[r]

files=sorted((f for f in incoming.rglob('*') if f.is_file() and f.suffix.lower() in allowed and f!=incoming/'README.md'),key=lambda p:str(p).casefold())
for f in files:
    rel=str(f.relative_to(ROOT)).replace('\\','/')
    if re.search(r'(testkey|credential|доступ|секрет|\.env)',f.name,re.I):issues.append({'file':rel,'reason':'Файл доступа исключён'});continue
    try:
        if f.suffix.lower()=='.json':
            j=json.loads(f.read_text(encoding='utf-8-sig'))
            if isinstance(j,dict) and j.get('type')=='ege-knowledge-patch':apply_patch(j);continue
        if f.suffix.lower()=='.zip':
            with zipfile.ZipFile(f) as z:
                if 'knowledge-backup.json' not in z.namelist():issues.append({'file':rel,'reason':'Для ZIP нужен экспорт резервной копии базы'});continue
                j=json.loads(z.read('knowledge-backup.json'));st=j.get('state',{})
                for item in j.get('items',[]):
                    if item.get('kind')=='note':append_note(item);continue
                    if item.get('kind') not in ('file','image'):continue
                    asset=item.get('backup_asset');raw=z.read(asset) if asset else None
                    if not raw:continue
                    h=hashlib.sha256(raw).hexdigest()[:24];ext='.'+re.sub(r'[^A-Za-z0-9]','',item.get('extension','txt'));target=ROOT/'files'/(h+ext);target.write_bytes(raw)
                    r={k:v for k,v in item.items() if k not in ('backup_asset','blob')};r['url']=str(target.relative_to(ROOT)).replace('\\','/');r['local']=False
                    if r['kind']=='image':data['media'][r['id']]=r
                    else:data['files']=[x for x in data['files'] if x['id']!=r['id']]+[r]
                apply_patch({'version':1,**st,'tasks':[x for x in j.get('items',[]) if x.get('kind')=='task']})
            continue
        h=hashlib.sha256(f.read_bytes()).hexdigest();fid='file_'+h[:24]
        if any(x['id']==fid for x in data['files']):continue
        result=parse(f);task=inference(f.name);r={'id':fid,'kind':'file','title':f.name,'name':f.name,'extension':f.suffix[1:].lower(),'bytes':f.stat().st_size,'sha256':h,'url':rel,'tasks':[task] if task else [],'sources':[rel],**result}
        if f.suffix.lower() in ('.png','.jpg','.jpeg','.webp','.svg'):
            r['kind']='image';r['status']='recognized_automatically';data['media'][fid]=r
        else:data['files'].append(r)
    except Exception as e:issues.append({'file':rel,'reason':type(e).__name__})
data['build']=datetime.now().strftime('%Y-%m-%d');data['incomingIssues']=issues
data['manifest']['verified_total']=sum(x.get('status')=='verified' for x in data['tasks'])
data['manifest']['course_verified']=sum(x.get('status')=='verified' and x.get('source_kind')=='course' for x in data['tasks'])
(ROOT/'data.js').write_text('window.KNOWLEDGE_BASE='+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';',encoding='utf-8')
print(json.dumps({'incoming_files':len(files),'tasks':len(data['tasks']),'files':len(data['files']),'issues':issues},ensure_ascii=False))
