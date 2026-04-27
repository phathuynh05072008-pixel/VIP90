import re,sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')
# within each lesson-button, extract label and first loadAudio call args
btn_re=re.compile(r'<button(?P<attrs>[\s\S]*?)class="lesson-button"(?P<attrs2>[\s\S]*?)>(?P<inner>[\s\S]*?)</button>', re.I)

def strip_label(inner):
    inner=re.sub(r'<!--([\s\S]*?)-->', ' ', inner)
    inner=re.sub(r'<[^>]+>', ' ', inner)
    return ' '.join(inner.split())

def get_onclick(attrs):
    m=re.search(r'onclick\s*=\s*"(?P<val>[\s\S]*?)"', attrs, re.I)
    return m.group('val') if m else ''

def parse_loadAudio_args(onclick):
    # find loadAudio('path','name') allowing whitespace/newlines and trailing comma
    m=re.search(r"loadAudio\(\s*'([^']*)'\s*,\s*'([^']*)'", onclick, re.I)
    if not m:
        return None
    return m.group(1), m.group(2)

bad=[]
for m in btn_re.finditer(html):
    attrs=(m.group('attrs') or '')+(m.group('attrs2') or '')
    if 'lesson-button' not in attrs:
        continue
    label=strip_label(m.group('inner'))
    onclick=get_onclick(attrs)
    args=parse_loadAudio_args(onclick)
    if not args:
        continue
    path,name=args
    if name.strip()!=label.strip():
        bad.append((label,name,path))

print('mismatch_count=',len(bad))
for label,name,path in bad[:30]:
    print('MISMATCH')
    print('  button:',label)
    print('  arg2  :',name)
    print('  path  :',path)
