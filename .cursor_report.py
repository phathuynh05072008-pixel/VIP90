import re,sys,os
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
MEDIA_EXT={'.mp4','.mp3','.pdf','.m4a','.wav','.aac','.mov','.mkv','.flac'}
root='tailieu'
weeks=[n for n in os.listdir(root) if re.fullmatch(r'tuan\d+',n,re.I)] if os.path.isdir(root) else []
weeks.sort(key=lambda s:int(re.sub(r'\D','',s)))
files_by_week={}
for w in weeks:
    d=os.path.join(root,w)
    files=[fn for fn in os.listdir(d) if os.path.isfile(os.path.join(d,fn)) and os.path.splitext(fn)[1].lower() in MEDIA_EXT]
    files.sort(key=lambda s:s.lower())
    files_by_week[w]=[f"{root}/{w}/{fn}" for fn in files]

html=Path('index.html').read_text(encoding='utf-8')

def iter_weeks(src):
    for m in re.finditer(r'<div\s+id="(?P<id>(?:week\d+|C1-C2))"\s+class="week-section"[^>]*>(?P<body>[\s\S]*?)(?=\n\s*<div\s+id="(?:week\d+|C1-C2)"\s+class="week-section"|\n\s*<div\s+class="main-content")', src, flags=re.I):
        yield m.group('id'), m.group('body')

def strip_label(inner):
    inner=re.sub(r'<!--([\s\S]*?)-->', ' ', inner)
    inner=re.sub(r'<[^>]+>', ' ', inner)
    return ' '.join(inner.split())

def extract_buttons(body):
    out=[]
    for bm in re.finditer(r'<button(?P<attrs>[\s\S]*?)>(?P<inner>[\s\S]*?)</button>', body, flags=re.I):
        attrs=bm.group('attrs')
        if 'lesson-button' not in attrs:
            continue
        om=re.search(r'onclick\s*=\s*"(?P<val>[\s\S]*?)"', attrs, flags=re.I)
        onclick=om.group('val') if om else ''
        label=strip_label(bm.group('inner'))
        lm=re.search(r"loadAudio\(\s*'([^']+)'\s*,\s*'([^']*)'", onclick, flags=re.I)
        path=lm.group(1) if lm else None
        out.append((label,path))
    return out

buttons_by_week={wid:extract_buttons(body) for wid,body in iter_weeks(html)}

def wid_to_tuan(wid):
    if wid=='C1-C2':
        return 'tuan1'
    m=re.fullmatch(r'week(\d+)', wid, re.I)
    if not m:
        return None
    return f"tuan{int(m.group(1))}"

filled=[]
unmatched_buttons=[]
used_files=set()
for wid, btns in buttons_by_week.items():
    tuan=wid_to_tuan(wid)
    for label,path in btns:
        if path and path.startswith('tailieu/'):
            filled.append((wid,label,path))
            used_files.add(path)
        else:
            if tuan in files_by_week and tuan in ('tuan1','tuan2','tuan3','tuan4','tuan5','tuan6','tuan7'):
                unmatched_buttons.append((wid,label))

unmatched_files=[]
for tuan, flist in files_by_week.items():
    if tuan not in ('tuan1','tuan2','tuan3','tuan4','tuan5','tuan6','tuan7'):
        continue
    for p in flist:
        if p not in used_files:
            unmatched_files.append((tuan,p))

print('[BÁO CÁO SAU XỬ LÝ]')
print('✅ Số nút đã điền đường dẫn tailieu/*:',len([1 for wid,_,p in filled if p.startswith('tailieu/')]))
for wid,label,path in filled:
    if path.startswith('tailieu/') and wid in ('C1-C2','week1','week2','week4','week5','week6','week7'):
        print(f"  ✅ {wid}: {label} — {path}")
print('')
print('⚠️ Số nút KHÔNG tìm được file khớp (trong tuần 1..7):',len(unmatched_buttons))
for wid,label in unmatched_buttons:
    print(f"  ⚠️ {wid}: {label}")
print('')
print('⚠️ Số file KHÔNG tìm được nút khớp (tuan1..tuan7):',len(unmatched_files))
for tuan,p in unmatched_files:
    print(f"  ⚠️ {tuan}: {p}")
