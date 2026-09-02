# -*- coding: utf-8 -*-
import re, pathlib
from build import TOKENS
ROOT = pathlib.Path("/root/neurogum-ds")

ORDER = [
 ("Foundations", [("foundations/color.html","§1 · §8"),
                  ("foundations/type.html","Farsi typesetting"),
                  ("foundations/display-bakeoff.html","open decision"),
                  ("foundations/grid.html","Instagram surfaces")]),
 ("Components",  [("components/carousel-cover.html","§4 entry points"),
                  ("components/carousel-body.html","§9 formats"),
                  ("components/carousel-cta.html","§7 funnel"),
                  ("components/proof-card.html","§5 credibility"),
                  ("components/reel-cover.html","§9 mechanics"),
                  ("components/story-frame.html","§6 pricing"),
                  ("components/highlight-covers.html","§9 highlights")]),
 ("Patterns",    [("patterns/formats.html","§4 · §9"),
                  ("patterns/rules.html","the whole playbook")]),
]

def body_of(rel):
    h = (ROOT/rel).read_text(encoding="utf-8")
    return re.search(r"<body>(.*)</body>", h, re.S).group(1)

SHELL = """
:root{
  --gr:#F3F6F7; --sf:#FFFFFF; --sf2:#EAEFF2;
  --ink:#0B1B2B; --mut:#556A7C; --hair:#D8E1E7;
  --acc:#0C6E80; --acc-soft:#E1F1F4;
  --warn:#A8342F; --warn-soft:#FBE9E7;
  --shadow:0 1px 2px rgba(11,27,43,.05),0 8px 26px rgba(11,27,43,.06);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --gr:#080E15; --sf:#0E1822; --sf2:#16222E;
  --ink:#E6EDF3; --mut:#8FA3B4; --hair:#1D2A37;
  --acc:#4CD4E8; --acc-soft:#0F2A31;
  --warn:#FF8A82; --warn-soft:#2A1512;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}}
:root[data-theme="dark"]{
  --gr:#080E15; --sf:#0E1822; --sf2:#16222E;
  --ink:#E6EDF3; --mut:#8FA3B4; --hair:#1D2A37;
  --acc:#4CD4E8; --acc-soft:#0F2A31;
  --warn:#FF8A82; --warn-soft:#2A1512;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 30px rgba(0,0,0,.35);
}

*{box-sizing:border-box;}
body{margin:0;background:var(--gr);color:var(--ink);
  font-family:"Source Serif 4",Georgia,serif;font-size:17px;line-height:1.65;
  -webkit-font-smoothing:antialiased;}
.wrap{display:grid;grid-template-columns:236px minmax(0,1fr);gap:0;max-width:1560px;margin:0 auto;}
@media (max-width:940px){.wrap{grid-template-columns:1fr;} nav.rail{position:static!important;height:auto!important;
  border-inline-end:none!important;border-bottom:1px solid var(--hair);}}

nav.rail{position:sticky;top:0;height:100vh;overflow-y:auto;padding:34px 22px 40px;
  border-inline-end:1px solid var(--hair);background:var(--sf);}
nav.rail .brandmark{display:flex;align-items:center;gap:9px;margin-bottom:6px;}
nav.rail .dot{width:11px;height:11px;border-radius:50%;background:#00C2DE;flex:none;
  box-shadow:0 0 0 3px rgba(0,194,222,.18);}
nav.rail .bt{font-family:"Archivo",system-ui,sans-serif;font-weight:800;font-size:14.5px;letter-spacing:-.01em;}
nav.rail .bs{font-size:12.5px;color:var(--mut);font-family:"Archivo",sans-serif;margin-bottom:26px;}
nav.rail h4{font-family:"Archivo",sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.13em;
  text-transform:uppercase;color:var(--mut);margin:22px 0 8px;}
nav.rail a{display:block;font-family:"Archivo",sans-serif;font-size:13.5px;line-height:1.35;
  color:var(--ink);text-decoration:none;padding:6px 9px;border-radius:6px;margin-inline-start:-9px;}
nav.rail a:hover{background:var(--sf2);color:var(--acc);}
nav.rail a:focus-visible{outline:2px solid var(--acc);outline-offset:1px;}

main{padding:44px 40px 120px;min-width:0;}
@media (max-width:640px){main{padding:28px 18px 80px;}}

.masthead{border-bottom:1px solid var(--hair);padding-bottom:34px;margin-bottom:12px;}
.masthead .eyebrow{font-family:"Archivo",sans-serif;font-size:11px;font-weight:700;letter-spacing:.15em;
  text-transform:uppercase;color:var(--acc);}
.masthead h1{font-family:"Archivo",system-ui,sans-serif;font-weight:800;font-size:clamp(34px,5vw,52px);
  line-height:1.04;letter-spacing:-.035em;margin:12px 0 0;text-wrap:balance;max-width:16ch;}
.masthead p{max-width:64ch;color:var(--mut);font-size:18px;margin:18px 0 0;}
.facts{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px;}
.facts span{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:11.5px;
  border:1px solid var(--hair);border-radius:999px;padding:5px 12px;color:var(--mut);background:var(--sf);}

section.doc{padding-top:56px;}
section.doc + section.doc{border-top:1px solid var(--hair);}
.sechead{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin-bottom:2px;}
.sechead .ref{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--acc);
  background:var(--acc-soft);border-radius:5px;padding:3px 8px;white-space:nowrap;}

h1{font-family:"Archivo",system-ui,sans-serif;font-weight:800;font-size:30px;letter-spacing:-.025em;
  line-height:1.15;margin:0;text-wrap:balance;}
h2{font-family:"Archivo",sans-serif;font-size:11px;font-weight:700;letter-spacing:.15em;
  text-transform:uppercase;color:var(--mut);margin:40px 0 4px;}
p.note{max-width:66ch;color:var(--mut);margin:12px 0 0;font-size:16.5px;}
p.rule{max-width:70ch;margin:12px 0 0;padding:13px 17px;border-radius:9px;background:var(--sf);
  border:1px solid var(--hair);border-inline-start:3px solid var(--acc);font-size:16px;box-shadow:var(--shadow);}
p.rule.bad{border-inline-start-color:var(--warn);background:var(--warn-soft);}
p.rule strong{font-family:"Archivo",sans-serif;font-weight:700;}
code{font-family:"JetBrains Mono",ui-monospace,monospace;font-size:.86em;background:var(--sf2);
  padding:2px 6px;border-radius:5px;color:var(--acc);}

.row{display:flex;gap:22px;flex-wrap:nowrap;align-items:flex-start;margin-top:20px;
  overflow-x:auto;padding-bottom:12px;scrollbar-width:thin;}
.frame{background:var(--sf);border:1px solid var(--hair);border-radius:12px;padding:14px;
  flex:none;box-shadow:var(--shadow);}
.frame > .cap{font-family:"Archivo",sans-serif;font-size:10.5px;font-weight:700;letter-spacing:.11em;
  text-transform:uppercase;color:var(--mut);margin-bottom:11px;}
.scaler{overflow:hidden;border-radius:4px;}
.scaler > *{transform-origin:top left;}

table{border-collapse:collapse;font-size:14.5px;margin-top:16px;width:100%;max-width:900px;
  font-family:"Archivo",sans-serif;}
.tablewrap{overflow-x:auto;}
th,td{text-align:left;padding:10px 13px;border-bottom:1px solid var(--hair);vertical-align:top;}
th{color:var(--mut);font-weight:700;font-size:10.5px;letter-spacing:.11em;text-transform:uppercase;}
td{font-variant-numeric:tabular-nums;}
.pass{color:#12805F;font-weight:700;}
.fail{color:var(--warn);font-weight:700;}
:root:not([data-theme="light"]) .pass{color:#4FD6A2;}
@media (prefers-color-scheme:light){:root:not([data-theme="dark"]) .pass{color:#12805F;}}
:root[data-theme="dark"] .pass{color:#4FD6A2;}

.sw{width:100%;height:70px;border-radius:9px;border:1px solid var(--hair);}
.swgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:16px;max-width:1060px;margin-top:18px;}
.swname{font-family:"Archivo",sans-serif;font-size:13px;font-weight:700;margin-top:9px;}
.swhex{font-family:"JetBrains Mono",monospace;font-size:11px;color:var(--mut);margin-top:2px;}
.swuse{font-size:13.5px;color:var(--mut);line-height:1.5;margin-top:4px;font-family:"Archivo",sans-serif;}

@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;}}
"""

def build():
    nav, secs = [], []
    for group, items in ORDER:
        nav.append(f'<h4>{group}</h4>')
        for rel, ref in items:
            sid = rel.replace("/","-").replace(".html","")
            b = body_of(rel)
            title = re.search(r"<h1>(.*?)</h1>", b, re.S).group(1)
            b = b.replace(f"<h1>{title}</h1>", "", 1)
            b = re.sub(r"(<table>.*?</table>)", r'<div class="tablewrap">\1</div>', b, flags=re.S)
            nav.append(f'<a href="#{sid}">{title}</a>')
            secs.append(f'<section class="doc" id="{sid}">'
                        f'<div class="sechead"><h1>{title}</h1><span class="ref">{ref}</span></div>'
                        f'{b}</section>')

    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=Archivo:wght@400;600;700;800&'
             'family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&'
             'family=JetBrains+Mono:wght@400;700&'
             'family=Vazirmatn:wght@100..900&'
             'family=Noto+Kufi+Arabic:wght@100..900&'
             'family=Inter:wght@400..900&display=swap">')

    head = ('<div class="masthead">'
            '<div class="eyebrow">neurogum.ir · Farsi · anonymous</div>'
            '<h1>NeuroGum.ir Design System</h1>'
            '<p>Every token here is derived from the playbook, not invented. The brand ships three hexes and one '
            'font decision; this is the working system underneath them — grounds, a Farsi type scale that survives '
            'Persian descenders, Instagram safe areas, and the eight occasions that content attaches to. '
            'Artboards are literal export sizes, scaled down to fit.</p>'
            '<div class="facts"><span>1080 × 1350 carousel</span><span>1080 × 1920 story</span>'
            '<span>margin 88 · 6 col</span><span>Vazirmatn + Inter</span><span>4 grounds</span>'
            '<span>8 entry points</span></div></div>')

    html = (f'<title>NeuroGum.ir Design System</title>{fonts}'
            f'<style>{TOKENS}{SHELL}</style>'
            f'<div class="wrap">'
            f'<nav class="rail"><div class="brandmark"><span class="dot"></span>'
            f'<span class="bt">Neuro Gum ایران</span></div>'
            f'<div class="bs">design system · v1</div>' + "".join(nav) + '</nav>'
            f'<main>{head}' + "".join(secs) + '</main></div>')

    out = ROOT/"neurogum-design-system.html"
    out.write_text(html, encoding="utf-8")
    print("wrote", out, len(html), "bytes")

build()
