import re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')
MEDIA_EXT={'.mp4','.mp3','.pdf','.m4a','.wav','.aac','.mov','.mkv','.flac'}
# find all onclick attributes with loadAudio
onclicks=re.findall(r'onclick\s*=\s*"([\s\S]*?)"', html, flags=re.I)
items=[]
for oc in onclicks:
    m=re.search(r"loadAudio\(\s*'([^']+)'\s*,\s*'([^']*)'", oc, flags=re.I)
    if not m:
        continue
    p=m.group(1)
    name=m.group(2)
    items.append((p,name))

bad=[]
for p,name in items:
    if p.startswith('tailieu/'):
        ext=Path(p).suffix.lower()
        exists=Path(p).exists()
        if (ext not in MEDIA_EXT) or (not exists):
            bad.append((p,name,exists,ext))

print('loadAudio_calls=',len(items))
print('tailieu_calls=',sum(1 for p,_ in items if p.startswith('tailieu/')))
print('bad_tailieu_calls=',len(bad))
for p,name,exists,ext in bad:
    print('BAD',p,'exists='+str(exists),'ext='+ext,'button='+name)
