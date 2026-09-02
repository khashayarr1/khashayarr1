# -*- coding: utf-8 -*-
from build import page, scaled
from pages_components import PACK_CSS, pack, ph, frame

# ───────────────────────── REEL COVER ─────────────────────────
reel = ('<div class="art art-916 g-ink"><div style="position:absolute;inset:0">'
  '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">'
  + ph(1080,1080,"فریم ویدیو") + '</div>'
  '<div style="position:absolute;left:0;right:0;top:420px;height:1080px;'
  'border:3px dashed rgba(0,194,222,.55)"></div>'
  '<div style="position:absolute;left:88px;right:88px;top:640px" dir="rtl">'
  '<div class="ng-meta" style="color:var(--ng-on-ink-70)">مستند مسئله</div>'
  '<div class="ng-display" style="margin-top:22px">چرا بعد از قهوه<br>هنوز خوابت<br>می‌آید؟</div></div>'
  '<div style="position:absolute;left:0;right:0;top:0;height:250px;background:rgba(255,122,122,.16)"></div>'
  '<div style="position:absolute;left:0;right:0;bottom:0;height:320px;background:rgba(255,122,122,.16)"></div>'
  '</div></div>')

page("components/reel-cover.html","Components","Reel cover",
  "A reel cover is designed twice: once as a 9:16 frame people watch, once as the 1:1 square your profile grid "
  "crops out of its middle. The dashed box is the square that survives.",
  '<div class="row">' + frame("Reel cover · 1080 × 1920", reel,1080,1920,.20,
      "Text block sits fully inside the centre square, clear of both red UI zones. A cover whose headline only "
      "works at full height turns your grid into a wall of cropped words.") + '</div>'
  '<p class="rule">Hook lands inside three seconds, reel runs 30–90s (§9). The cover text should be the same '
  'sentence as the first spoken or on-screen line — a cover that promises something the first second does not '
  'deliver is the fastest way to train the algorithm against you.</p>'
  '<p class="rule bad">No other-app watermarks — actively demoted. Higgsfield Object Remover is the tool. '
  'And no AI voiceover: it reads as drop-shipping, the exact suspicion an anonymous page cannot afford.</p>',
  PACK_CSS)

# ───────────────────────── STORY ─────────────────────────
story = ('<div class="art art-916 g-cyan"><div style="position:absolute;inset:0">'
  '<div style="position:absolute;left:88px;right:88px;top:330px" dir="rtl">'
  '<div class="ng-meta">قیمت امروز</div>'
  '<div class="ng-display" style="margin-top:26px;font-size:96px">قیمت این هفته<br>به‌روز شد.</div>'
  '<div class="ng-body" style="margin-top:34px;color:rgba(7,27,51,.72)">'
  'قیمت بر اساس دلار روز محاسبه می‌شود و ۲۴ ساعت اعتبار دارد.</div></div>'
  '<div style="position:absolute;left:50%;top:56%;transform:translateX(-50%)">' + pack(330,430,64,16) + '</div>'
  '<div style="position:absolute;left:0;right:0;bottom:0;height:320px;'
  'background:rgba(255,122,122,.20);display:flex;align-items:center;justify-content:center">'
  '<div style="background:#146FF8;color:#fff;border-radius:999px;padding:26px 60px;'
  'font:800 42px Vazirmatn" dir="rtl">استیکر دایرکت</div></div>'
  '</div></div>')

page("components/story-frame.html","Components","Story frame",
  "Stories are the repricing surface. Costs are in dollars and revenue is in toman, so the price moves weekly (§6) "
  "— and the story is where that gets said out loud, as import reality rather than as pressure.",
  '<div class="row">' + frame("Story · 1080 × 1920", story,1080,1920,.20,
      "Every story ends in a DM sticker in the bottom zone. The story is not the message — it is the shortest "
      "path into the thread where the sale actually happens.") + '</div>'
  '<p class="rule">Say the validity window plainly: قیمت ۲۴ ساعت اعتبار دارد. Framed as how importing works, it '
  'builds trust; framed as scarcity, it burns it.</p>'
  '<p class="rule bad">Never run the per-cup arithmetic here. Pack price ÷ 9 versus a Tehran americano stays out '
  'of content entirely — it is a DM objection-handler and only after the buyer raises price first (§6). Content '
  'sets the frame, the DM closes inside it.</p>',
  PACK_CSS)

# ───────────────────────── HIGHLIGHT COVERS ─────────────────────────
HL = [("چیست؟","NEURO","نوروگام چیست"),("چرا","WHY","چرا نوروگام"),("ترکیبات","40+60","کافئین و ال‌تیانین"),
      ("اصالت","SEAL","واردات مستقیم و پلمب"),("قیمت","IRR","قیمت و نحوه سفارش"),
      ("نظرات","★","بازخورد مشتری‌ها"),("ارسال","BOX","ارسال و پیگیری")]

def hlcover(fa, latin):
    return ('<div style="width:220px;height:220px;border-radius:50%;background:#071B33;'
      'display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;'
      'border:5px solid #F2EEE7;box-shadow:0 8px 24px rgba(7,27,51,.25)">'
      f'<div style="font:900 30px Inter;color:#00C2DE;letter-spacing:-.02em">{latin}</div>'
      f'<div dir="rtl" style="font:700 19px Vazirmatn;color:rgba(255,255,255,.82)">{fa}</div></div>')

hl_row = ('<div class="frame" style="max-width:1060px"><div class="cap">Seven Highlights · circle crop</div>'
  '<div style="background:#F2EEE7;padding:32px;border-radius:10px;display:flex;gap:22px;flex-wrap:wrap;'
  'justify-content:center">' + "".join(hlcover(fa,l) for fa,l,_ in HL) + '</div>'
  '<div class="swuse" style="margin-top:12px">Rendered at true on-screen size. This is roughly how big they '
  'actually are — which is the whole argument against putting a sentence on one.</div></div>')

hl_table = '<table><tr><th>Cover</th><th>Carries</th></tr>' + "".join(
  f'<tr><td dir="rtl">{fa}</td><td>{d}</td></tr>' for fa,_,d in HL) + '</table>'

page("components/highlight-covers.html","Components","Highlight covers",
  "Highlights carry the entire education load so the feed never explains the category twice — the @neurogumindia "
  "pattern. Build all seven before the first post (§9).",
  hl_row + '<h2>The seven</h2>' + hl_table +
  '<p class="rule">Highlights are the anonymous seller\'s substitute for a storefront. A stranger who lands on the '
  'profile should be able to answer “what is this, is it real, what does it cost, how does it arrive” without ever '
  'scrolling the feed.</p>'
  '<p class="rule">Upload as 1080×1920 with the icon centred in a 640px circle — Instagram crops hard and '
  'unforgivingly, and anything near the edge is gone.</p>'
  '<p class="rule bad">No words longer than one short Farsi noun. At ~64px on screen a phrase is a smudge.</p>',
  PACK_CSS)

print("components part 2 built")
