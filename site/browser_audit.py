"""Exercise all published routes at three viewport widths through agent-browser."""
import subprocess
import json
from pathlib import Path
from urllib.request import urlopen

ROOT=Path(__file__).resolve().parent.parent
BASE='http://127.0.0.1:8765/'
CLI=['npx','--yes','agent-browser','--session','gentech-audit','--json']
def run(*args):
    p=subprocess.run(CLI+list(args),capture_output=True,text=True,timeout=45)
    assert p.returncode==0,(args,p.stdout,p.stderr)
    data=json.loads(p.stdout)
    assert data.get('success',True),(args,data)
    return data.get('data',data)

pages=sorted(p.name for p in ROOT.glob('*.html'))
for page in pages:
    with urlopen(BASE+page) as r:assert r.status==200
print(f'HTTP PASS: {len(pages)} routes',flush=True)
results=[]
for width,height in [(1440,1000),(768,1024),(390,844)]:
    run('set','viewport',str(width),str(height))
    for page in pages:
        run('open',BASE+page)
        result=run('eval','''(async()=>{await document.fonts.ready; await Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch(e){}}));return {url:location.pathname,h1:document.querySelector('h1')?.textContent,width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth+1,brokenImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overlay:!!document.querySelector('[data-nextjs-dialog],.vite-error-overlay'),blank:document.body.innerText.trim().length<100}})()''')
        value=result.get('result',result)
        if isinstance(value,str):value=json.loads(value)
        assert value.get('h1') and not value['overflow'] and not value['brokenImages'] and not value['overlay'] and not value['blank'],(page,width,value)
        errors=run('errors')
        assert not errors.get('errors'),(page,width,errors)
        results.append(dict(page=page,viewport=f'{width}x{height}',**value))
        print(f'PASS {width} {page}',flush=True)
    run('open',BASE)
    run('eval',"Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch(e){}})).then(()=>true)")
    run('screenshot','--full',str(ROOT/f'docs/qa/home-{width}-full.png'))
(ROOT/'docs/qa/browser-results.json').write_text(json.dumps(results,indent=2))
run('close')
print(f'PASS: {len(results)} route/viewport checks; no page errors, horizontal overflow, broken images or blank pages.',flush=True)
