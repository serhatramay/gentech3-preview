"""Offline acceptance checks for all published HTML, links, facts and SEO."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import json
from content import HUBS, HERO, INTRO, PLATFORMS

ROOT=Path(__file__).resolve().parent.parent
class Document(HTMLParser):
    def __init__(self,path):
        super().__init__(convert_charrefs=True)
        self.path=path; self.ids=[]; self.links=[]; self.text=[]; self.h1=0; self.canonicals=[]; self.metas={}; self.sections=[]; self.scripts=[]
        self.feed(path.read_text())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='section' and 'id' in a:self.sections.append(a['id'])
        if tag=='link' and a.get('rel')=='canonical':self.canonicals.append(a['href'])
        if tag=='meta':self.metas[a.get('name',a.get('property',''))]=a.get('content','')
        if tag=='script' and a.get('src'):self.scripts.append(a['src'])
        if tag=='img':assert a.get('alt'),f'{self.path.name}: image missing alt'
        for key in ('href','src'):
            if key in a:self.links.append(a[key])
    def handle_data(self,data):self.text.append(data)

docs={p.name:Document(p) for p in ROOT.glob('*.html')}
for name,d in docs.items():
    text=' '.join(d.text)
    assert len(d.ids)==len(set(d.ids)),f'{name}: duplicate IDs'
    assert len(d.canonicals)==1,f'{name}: canonical count'
    assert 'noindex' in d.metas.get('robots',''),f'{name}: preview indexing enabled'
    assert d.h1 in (0,1),f'{name}: multiple H1s'
    if d.h1:
        assert d.metas.get('description'),f'{name}: missing description'
        assert 'mainNav' in d.ids and 'main' in d.ids,f'{name}: shared layout absent'
        assert 'assets/js/holding.js' in d.scripts,f'{name}: shared JS absent'
    for pattern in [r'concession',r'\bsovereign\b',r'65\s*(?:million|M)\s+commuters',r'Al Hamra',r'Al Shohada',r'\+012',r'CAPITAL HOLDING \(PTY\)',r'global powerhouse',r'singular.{0,10}global power',r'supreme holding',r'CC EAL6',r'PCI-DSS',r'EMVCo',r'sub-50ms',r'securely logged']:
        assert not re.search(pattern,text,re.I),f'{name}: prohibited claim {pattern}'
    assert not re.search('[\U0001F1E6-\U0001F1FF]',text),f'{name}: flag emoji'
    for raw in d.links:
        u=urlsplit(raw)
        if u.scheme or u.netloc:continue
        local=unquote(u.path)
        target=(ROOT/local) if local else ROOT/name
        assert target.exists(),f'{name}: broken local link {raw}'
        if u.fragment and target.suffix=='.html':
            assert u.fragment in docs[target.name].ids,f'{name}: broken anchor {raw}'
home=docs['index.html']
assert home.sections==['opening','what-we-do','business-platforms','featured-projects','global-presence','chairmans-vision','technology-portfolio','partnerships','news','contact'],home.sections
assert HERO in ' '.join(home.text) and INTRO in ' '.join(home.text)
assert 'canvas3D' not in home.ids
assert 'canvas3D' in docs['solutions-cards.html'].ids
assert 'configurator' in docs['solutions-cards.html'].ids
for name in ['index.html','contact.html','about.html','legal.html']:
    text=' '.join(docs[name].text)
    for h in HUBS:
        assert h['name'] in text and h['address'] in text,f'{name}: corporate mismatch {h["key"]}'
for h in HUBS:
    text=' '.join(docs['group-'+h['key']+'.html'].text)
    assert h['description'] in text
html=(ROOT/'index.html').read_text()
positions=[html.index(p['title'].replace('&','&amp;'),html.index('id="business-platforms"')) for p in PLATFORMS]
assert positions==sorted(positions),'Platform order incorrect'
print(f'PASS: {len(docs)} HTML URLs; local links and anchors; unique IDs; shared layout; metadata; noindex; approved names and addresses; prohibited claims; homepage and platform order; product studio relocation.')
