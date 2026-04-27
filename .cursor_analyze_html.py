import re,sys,html
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')
text=Path('index.html').read_text(encoding='utf-8')
# extract week sections
week_re=re.compile(r"<div id=\"(week\d+|C1-C2)\" class=\"week-section\">([\s\S]*?)</div>\s*</div>", re.I)
# fallback: just locate by id div start and next <!-- WEEK ... -->

def iter_weeks(src):
    # simple scanning for <div id="weekX" class="week-section">
    for m in re.finditer(r'<div\s+id="(?P<id>(?:week\d+|C1-C2))"\s+class="week-section"[^>]*>(?P<body>[\s\S]*?)(?=\n\s*<div\s+id="(?:week\d+|C1-C2)"\s+class="week-section"|\n\s*<div\s+class="main-content"|\n\s*</div>\s*\n\s*<div\s+class="main-content")', src, flags=re.I):
        yield m.group('id'), m.group('body')

def extract_buttons(body):
    # match <button ... class="lesson-button" ...> ...text... </button>
    buttons=[]
    for bm in re.finditer(r'<button(?P<attrs>[\s\S]*?)>\s*(?P<inner>[\s\S]*?)\s*</button>', body, flags=re.I):
        attrs=bm.group('attrs')
        if 'lesson-button' not in attrs:
            continue
        # onclick value (single/double quotes)
        om=re.search(r'onclick\s*=\s*"(?P<val>[\s\S]*?)"', attrs, flags=re.I)
        onclick=om.group('val') if om else None
        # visible text: strip HTML comments/tags
        inner=bm.group('inner')
        inner=re.sub(r'<!--([\s\S]*?)-->', ' ', inner)
        inner=re.sub(r'<[^>]+>', ' ', inner)
        label=' '.join(inner.split())
        buttons.append((label, onclick))
    return buttons

report={}
for wid, body in iter_weeks(text):
    btns=extract_buttons(body)
    report[wid]=[{"label":l, "onclick":o} for l,o in btns]

for wid in sorted(report.keys(), key=lambda s:(0, s) if s=='C1-C2' else (1, int(re.sub(r'\D','',s)))):
    btns=report[wid]
    missing=[b for b in btns if not b['onclick'] or 'tailieu/' not in b['onclick']]
    print(f"{wid}: total={len(btns)} missing_or_placeholder={len(missing)}")
    for b in missing[:20]:
        print('  -', b['label'], '|| onclick=', (b['onclick'] or 'NONE')[:60].replace('\n',' '))
