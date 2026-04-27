import re,sys,os
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')
paths=re.findall(r"'(?P<p>tailieu/[^']+?)'", html)
# de-dup preserve order
seen=set(); ordered=[]
for p in paths:
    if p not in seen:
        seen.add(p); ordered.append(p)
missing=[]
for p in ordered:
    if not Path(p).exists():
        missing.append(p)
print('total_paths_in_html=',len(ordered))
print('missing_paths=',len(missing))
for p in missing:
    print('MISSING',p)
