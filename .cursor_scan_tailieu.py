import os,sys,json,re
sys.stdout.reconfigure(encoding='utf-8')
MEDIA_EXT={'.mp4','.mp3','.pdf','.m4a','.wav','.aac','.mov','.mkv','.flac'}
root='tailieu'
weeks=[]
if os.path.isdir(root):
    for n in os.listdir(root):
        if re.fullmatch(r'tuan\d+', n, re.I):
            weeks.append(n)
weeks.sort(key=lambda s:int(re.sub(r'\D','',s)))
out={}
for w in weeks:
    d=os.path.join(root,w)
    files=[fn for fn in os.listdir(d) if os.path.isfile(os.path.join(d,fn)) and os.path.splitext(fn)[1].lower() in MEDIA_EXT]
    files.sort(key=lambda s:s.lower())
    out[w]=[f"{root}/{w}/{fn}" for fn in files]
print(json.dumps(out,ensure_ascii=False,indent=2))
