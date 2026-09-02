# -*- coding: utf-8 -*-
from build import page, scaled

# ─────────────────────────────── COLOR ───────────────────────────────
SW = [
 ("Brand Blue","#00C2DE","--ng-cyan","Ground only. Never carries white text — 2.15:1."),
 ("Electric Blue","#146FF8","--ng-electric","CTA fills and links. White on it = 4.51:1, AA body."),
 ("White","#FFFFFF","--ng-white","Type on ink. Pack negative space."),
 ("Ink","#071B33","--ng-ink","Every line of Farsi text, on every ground."),
 ("Ink 2","#0E2A4A","--ng-ink-2","Raised surfaces on the ink ground."),
 ("Bone","#F2EEE7","--ng-bone","Default ground. The flatlay floor."),
 ("Sand","#E3DBD0","--ng-sand","Second warm ground. Cards on bone."),
 ("Stone","#C9BEB0","--ng-stone","Dividers, prop tones, quiet fills."),
 ("Clay","#8A7C6D","--ng-clay","Warm accent. Large text only — 3.5:1 on bone."),
 ("Paper","#F5F8F9","--ng-paper","Mechanism / diagram ground. Clinical."),
]
RATIOS = [
 ("Ink","Bone","14.96",1,1),("Ink","White","17.30",1,1),("Ink","Paper","16.21",1,1),
 ("Ink","Sand","12.61",1,1),("Ink","Stone","9.46",1,1),("Ink","Brand Blue","8.05",1,1),
 ("White","Ink","17.30",1,1),("Brand Blue","Ink","8.05",1,1),
 ("White","Electric Blue","4.51",1,1),("Electric Blue","White","4.51",1,1),
 ("Electric Blue","Bone","3.90",0,1),("Clay","Bone","3.50",0,1),
 ("White","Brand Blue","2.15",0,0),("Brand Blue","White","2.15",0,0),
]
sw_html = '<div class="swgrid">' + "".join(
  f'<div><div class="sw" style="background:{h}"></div><div class="swname">{n}</div>'
  f'<div class="swhex">{h} · <code>{t}</code></div><div class="swuse">{u}</div></div>'
  for n,h,t,u in SW) + '</div>'

rows = "".join(
  f'<tr><td>{f}</td><td>{b}</td><td><code>{r}:1</code></td>'
  f'<td class="{"pass" if body else "fail"}">{"PASS" if body else "FAIL"}</td>'
  f'<td class="{"pass" if lg else "fail"}">{"PASS" if lg else "FAIL"}</td></tr>'
  for f,b,r,body,lg in RATIOS)

GROUNDS = [
 ("g-bone","Bone","هویت · فلت‌لی","Identity + flatlay. The default. Warm, expensive, self-selecting."),
 ("g-ink","Ink","مستند مسئله","Problem documentary. 4pm going dark, hour three, the long drive."),
 ("g-cyan","Cyan","فریاد برند","One slide per carousel, maximum. The brand shout. Ink text only."),
 ("g-paper","Paper","توضیح مکانیزم","Mechanism explainer. Diagrams, absorption, the two-ingredient story."),
]
g_html = '<div class="row">' + "".join(
  f'<div class="frame"><div class="cap">{lbl}</div>' +
  scaled(f'<div class="art art-45 {cls}"><div class="pad">'
         f'<div class="ng-meta">{fa}</div>'
         f'<div style="flex:1"></div>'
         f'<div class="ng-display">تمرکز بدون اضطراب</div></div></div>',1080,1350,.20) +
  f'<div class="swuse" style="max-width:216px;margin-top:10px">{use}</div></div>'
  for cls,lbl,fa,use in GROUNDS) + '</div>'

page("foundations/color.html","Foundations","Color",
  "Three brand hexes are a logo palette, not a design system. Ink and the warm studio ramp are what make the "
  "feed read as a premium-wellness object instead of a telecom ad — they are the bridge between a cold cyan "
  "brand and the warm flatlay grammar the playbook commits to (§8).",
  f'<h2>Palette</h2>{sw_html}'
  '<h2>The one rule that breaks most feeds</h2>'
  '<p class="rule bad"><strong>Never put white Farsi text on Brand Blue.</strong> It measures 2.15:1 — below every '
  'accessibility floor, and at feed-thumbnail size it is genuinely unreadable. Brand Blue is a <em>ground</em>. '
  'Ink on Brand Blue is 8.05:1 and looks more expensive anyway.</p>'
  '<p class="rule">Electric Blue is the only color that carries white text (4.51:1). That is exactly why it is the '
  'CTA color and nothing else. If Electric Blue appears twice on a slide, one of them is not a CTA.</p>'
  f'<h2>Measured contrast (WCAG 2.1)</h2>'
  f'<table><tr><th>Text</th><th>On</th><th>Ratio</th><th>AA body</th><th>AA large</th></tr>{rows}</table>'
  '<h2>Four grounds — pick one per carousel</h2>'
  '<p class="note">A carousel uses <strong>one ground plus one accent</strong>. Ten slides across four grounds is '
  'how a feed stops looking like a brand and starts looking like a Canva account.</p>'
  f'{g_html}')

# ─────────────────────────────── TYPE ───────────────────────────────
SPEC = [
 ("ng-hero","تیتر / Hero","140 / 1.14 / tracking 0","900","Carousel cover. One line, two at most. The occasion, named."),
 ("ng-display","تیتر / Display","104 / 1.24 / tracking 0","900","Slide headline, reel cover, story hook."),
 ("ng-title","تیتر / Title","72 / 1.34 / tracking 0","800","Body-slide headline, Highlight cover."),
 ("ng-lede","متن / Lede","52 / 1.55","500","The sentence under a hook. Sets up the next slide."),
 ("ng-body","متن / Body","40 / 1.78","400","Explanation. Mechanism. Proof copy."),
 ("ng-meta","نشانه / Meta","24 / 1.4 / +.09em","600","Labels, slide numbers, واردات مستقیم, price validity."),
]
samples = {
 "ng-hero":"ساعت ۴ بعدازظهر", "ng-display":"چرا بعد از قهوه\nهنوز خوابت می‌آید؟",
 "ng-title":"کافئین به‌تنهایی کافی نیست",
 "ng-lede":"سه ساعت کار مانده و یک قهوه، خواب امشب را می‌گیرد.",
 "ng-body":"کافئین و ال‌تیانین با هم کار می‌کنند: یکی بیدارت می‌کند، دیگری لبه‌ی تیزش را می‌گیرد. نتیجه تمرکزی است که بالا و پایین ندارد.",
 "ng-meta":"واردات مستقیم",
}
spec_rows = "".join(
  f'<div class="frame" style="width:100%;max-width:1000px;margin-bottom:14px">'
  f'<div class="cap">{name} · {size} · weight {w}</div>'
  f'<div dir="rtl" class="g-bone" style="padding:26px 30px;border-radius:8px">'
  f'<div class="{cls}" style="white-space:pre-line;'
  f'{"font-size:56px" if cls=="ng-hero" else "font-size:42px" if cls=="ng-display" else "font-size:32px" if cls=="ng-title" else "font-size:24px" if cls=="ng-lede" else "font-size:19px" if cls=="ng-body" else "font-size:14px"}">'
  f'{samples[cls]}</div></div>'
  f'<div class="swuse" style="margin-top:9px">{use}</div></div>'
  for cls,name,size,w,use in SPEC)

page("foundations/type.html","Foundations","Type — three roles",
  "Three roles, not three fonts for their own sake. تیتر names the occasion, متن explains it, نشانه labels it. "
  "Vazirmatn carries all three (Google Fonts, variable 100–900) and Inter carries Latin and technical numerals. "
  "Sizes below are literal px on a 1080-wide artboard; the previews are scaled down to fit.",
  f'<h2>The scale</h2>{spec_rows}'
  '<h2>Farsi rules that Latin systems do not teach you</h2>'
  '<p class="rule"><strong>Farsi has no uppercase, so a label cannot be made with caps.</strong> The نشانه role '
  'substitutes the three signals Latin gets free from small-caps: heavier weight (600), open tracking (+.09em), '
  'and reduced opacity (55%). That is the entire trick, and skipping it is why most Persian layouts have no '
  'visible third tier.</p>'
  '<p class="rule"><strong>Leading runs higher than Latin at every size, headlines included.</strong> Body is 1.78, '
  'never below 1.7. Display is 1.24 and hero is 1.14 — a Latin display face is happy at .95, but Persian stacks '
  'dots above the letters and descenders below them, so a two-line Farsi headline at Latin leading physically '
  'collides. I built this system at .98 first and the rendered proof is what forced the change.</p>'
  '<p class="rule bad"><strong>Never track Farsi negative.</strong> Latin display type is tightened by habit '
  '(-.02em), but Persian is a <em>connected</em> script — squeezing the tracking pulls the joins apart and the word '
  'stops reading as one shape. Tracking is 0 on every Farsi role and positive (+.09em) only on نشانه, where '
  'breaking the joins is the point.</p>'
  '<p class="rule"><strong>Persian digits in Farsi copy, Latin digits only inside Latin phrases.</strong> '
  '<span dir="rtl">ساعت ۴ بعدازظهر</span> — not "4". But <code>40mg</code> and <code>L-Theanine</code> stay Latin, '
  'set in Inter with tabular figures. Mixing digit systems inside one sentence is the loudest amateur tell in '
  'Persian typesetting.</p>'
  '<p class="rule bad"><strong>Never justify Farsi text</strong> and never center more than two lines. '
  'RTL justification stretches kashida joins and wrecks the word rhythm. Right-align, ragged left.</p>'
  '<h2>Latin lane</h2>'
  '<div class="frame" style="max-width:1000px"><div class="cap">Inter · brand name, ingredients, technical numerals</div>'
  '<div class="g-bone" style="padding:26px 30px;border-radius:8px">'
  '<div class="ng-latin" style="font-size:34px;font-weight:900;color:#071B33">NeuroGum</div>'
  '<div class="ng-latin" style="font-size:18px;font-weight:600;color:rgba(7,27,51,.7);margin-top:8px">'
  '40mg Caffeine &nbsp;·&nbsp; 60mg L-Theanine &nbsp;·&nbsp; B6 / B12</div></div>'
  '<div class="swuse" style="margin-top:9px">Latin appears in exactly three places: the brand name, ingredient '
  'names, and dosage numerals. Nowhere else — the playbook constraint is Farsi only.</div></div>')

# ─────────────────────── DISPLAY BAKE-OFF ───────────────────────
CANDS = [
 ("Vazirmatn 900","'Vazirmatn'","900","Default. Neutral geometric Naskh-sans. Reads Iranian-modern and lets the "
  "flatlay carry identity. Free, Google Fonts, variable — renders anywhere including Canva."),
 ("Noto Kufi Arabic 900","'Noto Kufi Arabic'","900","Architectural, low-contrast, technical. More distinct at "
  "thumbnail size. Risk: Kufi reads Gulf/Arab-tech to Persian eyes more than Tehran-premium."),
 ("Vazirmatn 500 (contrast test)","'Vazirmatn'","500","Same family, light weight, big size. Proof that hierarchy "
  "comes from weight and size before it comes from a second family."),
]
bake = '<div class="row">' + "".join(
  f'<div class="frame" style="width:330px"><div class="cap">{n}</div>'
  f'<div dir="rtl" class="g-bone" style="padding:24px;border-radius:8px;height:190px;display:flex;align-items:center">'
  f'<div style="font-family:{fam},sans-serif;font-weight:{w};font-size:40px;line-height:1.14;'
  f'letter-spacing:0;color:#071B33">ساعت ۴ بعدازظهر</div></div>'
  f'<div class="swuse" style="margin-top:10px">{d}</div></div>'
  for n,fam,w,d in CANDS) + '</div>'

page("foundations/display-bakeoff.html","Foundations","Display face — pick one",
  "The headline family is the one decision I did not want to make for you, so here it is side by side at the "
  "size it will actually be seen. Swapping is one token: <code>--ng-font-display</code>.",
  bake +
  '<h2>My read</h2>'
  '<p class="rule"><strong>Ship Vazirmatn 900 and keep Noto Kufi in reserve.</strong> Not because one font is '
  'enough — because in Persian, the number of good families is small and their baselines and letter-widths do not '
  'agree the way Latin families do. Two mismatched Farsi faces stacked in one layout is the single most reliable '
  'way to look like a Telegram shop. Digikala, Snapp and Filimo all run one superfamily across the whole hierarchy '
  'for exactly this reason.</p>'
  '<p class="rule">The second family that <em>does</em> earn its place is the Latin one, because your own brand '
  'name is Latin and Persian fonts have mediocre Latin glyphs. That is why the system is '
  '<strong>one Farsi superfamily + Inter</strong> rather than two Farsi faces.</p>'
  '<p class="rule bad">If you want a genuinely different headline face anyway, the correct move is a licensed '
  'display family designed as a sibling to your text face — Yekan Bakh or Morabba paired with Vazirmatn. Both are '
  'commercial licenses and neither is on Google Fonts, so they must be embedded as font files in Canva and in this '
  'system. Say the word and I will rebuild the tokens around one of them.</p>')

# ─────────────────────────────── GRID ───────────────────────────────
def gridart():
    cols = "".join('<div style="flex:1;background:rgba(0,194,222,.30)"></div>' for _ in range(6))
    return ('<div class="art art-45 g-bone"><div class="pad" style="padding:0">'
      '<div style="position:absolute;inset:0 88px;display:flex;gap:32px">' + cols + '</div>'
      '<div style="position:absolute;left:0;right:0;top:88px;height:2px;background:rgba(20,111,248,.5)"></div>'
      '<div style="position:absolute;left:0;right:0;bottom:88px;height:2px;background:rgba(20,111,248,.5)"></div>'
      '<div style="position:absolute;left:0;right:0;top:0;height:88px;background:rgba(138,124,109,.18)"></div>'
      '<div style="position:absolute;left:0;right:0;bottom:0;height:88px;background:rgba(138,124,109,.18)"></div>'
      '</div></div>')

def storyart():
    return ('<div class="art art-916 g-ink"><div style="position:absolute;inset:0">'
      '<div style="position:absolute;left:0;right:0;top:0;height:250px;background:rgba(255,122,122,.22);'
      'display:flex;align-items:center;justify-content:center;font:700 34px Inter;color:#fff">Instagram UI — keep clear</div>'
      '<div style="position:absolute;left:0;right:0;bottom:0;height:320px;background:rgba(255,122,122,.22);'
      'display:flex;align-items:center;justify-content:center;font:700 34px Inter;color:#fff">reply bar + stickers</div>'
      '<div style="position:absolute;left:88px;right:88px;top:250px;bottom:320px;border:3px dashed rgba(0,194,222,.75);'
      'display:flex;align-items:center;justify-content:center" dir="rtl">'
      '<div class="ng-display" style="color:#fff;text-align:center">همه‌ی محتوا<br>اینجا</div></div>'
      '</div></div>')

def feedcrop():
    return ('<div class="art art-45 g-bone"><div style="position:absolute;inset:0">'
      '<div style="position:absolute;left:0;right:0;top:135px;height:1080px;border:3px dashed rgba(20,111,248,.85)"></div>'
      '<div style="position:absolute;left:0;right:0;top:0;height:135px;background:rgba(255,122,122,.18)"></div>'
      '<div style="position:absolute;left:0;right:0;bottom:0;height:135px;background:rgba(255,122,122,.18)"></div>'
      '<div class="pad" style="justify-content:center;align-items:flex-end" dir="rtl">'
      '<div class="ng-display">ساعت سوم</div></div></div></div>')

page("foundations/grid.html","Foundations","Grid &amp; safe areas",
  "Every artboard is 1080 wide. Side margin is 88px, six columns, 32px gutters. The red zones are where Instagram "
  "puts its own interface — anything you place there is destroyed by the platform, not by the design.",
  '<div class="row">'
  f'<div class="frame"><div class="cap">Carousel · 1080 × 1350 · margin 88 · 6 col</div>{scaled(gridart(),1080,1350,.22)}'
  '<div class="swuse" style="max-width:238px;margin-top:10px">Type never crosses the 88px margin. Photography '
  'always bleeds to the edge — that contrast is what makes the pack read as a product shot rather than a poster.</div></div>'
  f'<div class="frame"><div class="cap">Story · 1080 × 1920 · safe 250 top / 320 bottom</div>{scaled(storyart(),1080,1920,.155)}'
  '<div class="swuse" style="max-width:238px;margin-top:10px">The bottom 320px is where the reply bar and your DM '
  'sticker live. Since the DM is the store (§7), that zone is reserved for the sticker on every single story.</div></div>'
  f'<div class="frame"><div class="cap">Feed-grid crop · the 4:5 → 1:1 problem</div>{scaled(feedcrop(),1080,1350,.22)}'
  '<div class="swuse" style="max-width:238px;margin-top:10px">Your profile grid shows a centered 1080×1080 crop of '
  'every 4:5 post. The top and bottom 135px vanish on the grid. Headlines sit inside the blue box or your profile '
  'reads as a wall of half-sentences.</div></div>'
  '</div>'
  '<h2>Sizes</h2>'
  '<table><tr><th>Surface</th><th>Export</th><th>Safe area</th><th>Note</th></tr>'
  '<tr><td>Carousel slide</td><td>1080 × 1350</td><td>88px all sides</td><td>Primary format. Playbook §9 is carousel-forward.</td></tr>'
  '<tr><td>Reel cover</td><td>1080 × 1920</td><td>centered 1080×1080</td><td>Cover is chosen from the video; the grid crops it square.</td></tr>'
  '<tr><td>Story</td><td>1080 × 1920</td><td>250 top / 320 bottom</td><td>Bottom zone reserved for the DM sticker.</td></tr>'
  '<tr><td>Highlight cover</td><td>1080 × 1920</td><td>centered 640px circle</td><td>Cropped to a circle at ~64px on screen. Icon only, no words.</td></tr>'
  '</table>')

print("foundations built")
