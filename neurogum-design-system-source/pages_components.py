# -*- coding: utf-8 -*-
from build import page, scaled

PACK_CSS = """
.pack{border-radius:26px;background:linear-gradient(155deg,#00C2DE 0%,#00A8C4 55%,#0090AC 100%);
  box-shadow:0 34px 70px rgba(7,27,51,.28);display:flex;flex-direction:column;
  justify-content:space-between;padding:38px 34px;color:#fff;flex:none;}
.pack .pw{font-family:"Inter",sans-serif;font-weight:900;letter-spacing:-.03em;line-height:.9;}
.pack .pd{font-family:"Inter",sans-serif;font-weight:600;letter-spacing:.02em;opacity:.9;}
.ph{background:repeating-linear-gradient(45deg,rgba(7,27,51,.05) 0 14px,rgba(7,27,51,.09) 14px 28px);
  display:flex;align-items:center;justify-content:center;font:600 26px "Inter";color:rgba(7,27,51,.42);
  border-radius:20px;text-align:center;line-height:1.4;}
.slidenum{position:absolute;top:88px;left:88px;font-family:"Inter";font-weight:700;font-size:26px;
  letter-spacing:.1em;opacity:.45;}
.cta-pill{display:inline-flex;align-items:center;gap:18px;background:#146FF8;color:#fff;
  border-radius:999px;padding:30px 52px;font-family:"Vazirmatn";font-weight:800;font-size:46px;}
"""

def pack(w, h, ws=52, ds=17):
    return (f'<div class="pack" style="width:{w}px;height:{h}px">'
            f'<div class="pw" style="font-size:{ws}px">NEURO<br>GUM</div>'
            f'<div class="pd" style="font-size:{ds}px">40mg CAFFEINE · L-THEANINE</div></div>')

def ph(w, h, label):
    return f'<div class="ph" style="width:{w}px;height:{h}px">{label}</div>'

def frame(cap, art, w, h, s, note, width=None):
    ww = f'style="width:{width}px"' if width else ""
    return (f'<div class="frame" {ww}><div class="cap">{cap}</div>{scaled(art,w,h,s)}'
            f'<div class="swuse" style="max-width:{int(w*s)}px;margin-top:10px">{note}</div></div>')

# ───────────────────────── CAROUSEL COVERS ─────────────────────────
cover_occasion = ('<div class="art art-45 g-ink"><div class="pad" dir="rtl">'
  '<div class="ng-meta">ساعت ۴ بعدازظهر</div>'
  '<div style="flex:1"></div>'
  '<div class="ng-hero">سه ساعت<br>کار مانده.</div>'
  '<div class="ng-lede" style="color:var(--ng-on-ink-70);margin-top:40px;max-width:760px">'
  'و یک قهوه‌ی دیگر، خواب امشب را می‌گیرد.</div>'
  '<div style="flex:.35"></div>'
  '<div class="ng-meta" style="opacity:.6">۱ / ۷ &nbsp;·&nbsp; بکشید</div>'
  '</div></div>')

cover_number = ('<div class="art art-45 g-bone"><div class="pad" dir="rtl">'
  '<div class="ng-meta">فرمول</div><div style="flex:1"></div>'
  '<div class="ng-latin" style="font-size:230px;font-weight:900;color:#071B33;line-height:.85">40<span '
  'style="color:#00C2DE">+</span>60</div>'
  '<div class="ng-lede" style="margin-top:36px;max-width:800px">کافئین و ال‌تیانین. دو ماده که '
  'جداگانه معنی ندارند.</div><div style="flex:.4"></div>'
  '<div class="ng-meta">۱ / ۶</div></div></div>')

cover_question = ('<div class="art art-45 g-cyan"><div class="pad" dir="rtl">'
  '<div class="ng-meta">مستند مسئله</div><div style="flex:1"></div>'
  '<div class="ng-display">چرا بعد از قهوه<br>هنوز خوابت<br>می‌آید؟</div>'
  '<div style="flex:.5"></div><div class="ng-meta">۱ / ۵</div></div></div>')

page("components/carousel-cover.html","Components","Carousel — cover slide",
  "The cover has one job: name an occasion from §4 so specifically that someone recognises their own afternoon. "
  "Three variants, one occasion each, never an adjective.",
  '<div class="row">'
  + frame("Occasion cover · ink ground", cover_occasion,1080,1350,.235,
      "The default. Entry point named in the نشانه line, the stakes in the hero, the twist in the lede. "
      "Nothing here is a benefit claim — you can film 4pm, you cannot film “sharper”.")
  + frame("Arithmetic cover · bone ground", cover_number,1080,1350,.235,
      "The @neurogumindia move: numbers instead of adjectives. Latin numerals in Inter, Farsi copy in Vazirmatn — "
      "the one place mixed scripts are correct, because the numbers are dosages.")
  + frame("Question cover · cyan ground", cover_question,1080,1350,.235,
      "The briefed first reel, as a carousel. Note the ink text on cyan — white here would be 2.15:1. "
      "Cyan is the shout slide: once per carousel, never twice.")
  + '</div>'
  '<h2>Rules</h2>'
  '<p class="rule">One occasion per carousel, named in the first three words. If the cover could describe two '
  'different moments, it describes neither and nothing gets retrieved at 4pm.</p>'
  '<p class="rule bad">No adjectives on a cover. Not تازه, not سالم, not بهتر — and not a generic promise like '
  'تمرکز بیشتر. The occasion <em>is</em> the hook.</p>'
  '<p class="rule">Headline sits inside the centre 1080×1080 or it gets guillotined on your profile grid.</p>',
  PACK_CSS)

# ───────────────────────── CAROUSEL BODY ─────────────────────────
body_statement = ('<div class="art art-45 g-ink"><div class="pad" dir="rtl">'
  '<div class="ng-meta">۳ / ۷</div><div style="flex:1"></div>'
  '<div class="ng-title">قهوه بیدارت می‌کند.<br>تمرکز نمی‌دهد.</div>'
  '<div class="ng-body" style="color:var(--ng-on-ink-70);margin-top:36px;max-width:820px">'
  'کافئین سیستم را روشن می‌کند، اما همان چیزی که بیدارت نگه می‌دارد، لبه‌ی اضطراب را هم تیز می‌کند. '
  'این دو با هم می‌آیند — مگر اینکه چیزی جلوی دومی را بگیرد.</div>'
  '<div style="flex:.6"></div></div></div>')

body_mech = ('<div class="art art-45 g-paper"><div class="pad" dir="rtl">'
  '<div class="ng-meta">۴ / ۷ &nbsp;·&nbsp; مکانیزم</div>'
  '<div class="ng-title" style="margin-top:28px">دو ماده، یک اثر</div>'
  '<div style="flex:1;display:flex;align-items:center;gap:28px;margin-top:40px">'
  '<div style="flex:1;background:#fff;border-radius:28px;padding:44px 36px;border:2px solid rgba(7,27,51,.10)">'
  '<div class="ng-latin" style="font-size:64px;color:#00C2DE">40mg</div>'
  '<div class="ng-title" style="font-size:44px;margin-top:14px">کافئین</div>'
  '<div class="ng-body" style="font-size:32px;color:var(--ng-ink-70);margin-top:14px">سیستم را بالا می‌آورد</div></div>'
  '<div style="flex:1;background:#fff;border-radius:28px;padding:44px 36px;border:2px solid rgba(7,27,51,.10)">'
  '<div class="ng-latin" style="font-size:64px;color:#146FF8">60mg</div>'
  '<div class="ng-title" style="font-size:44px;margin-top:14px">ال‌تیانین</div>'
  '<div class="ng-body" style="font-size:32px;color:var(--ng-ink-70);margin-top:14px">لبه‌ی تیزش را می‌گیرد</div></div>'
  '</div>'
  '<div class="ng-body" style="margin-top:36px">جذب از طریق مخاط دهان — بدون انتظار برای معده.</div>'
  '</div></div>')

body_flatlay = ('<div class="art art-45 g-sand" style="background:#E3DBD0"><div class="pad" dir="rtl" '
  'style="justify-content:flex-end">'
  '<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">'
  + ph(760,760,"عکاسی خودتان<br>موجودی خودتان") + '</div>'
  '<div style="position:absolute;left:50%;top:46%;transform:translate(-50%,-50%) rotate(-7deg)">'
  + pack(300,392,60,15) + '</div>'
  '<div class="ng-title" style="position:relative;z-index:2">این برای کسی است که<br>روی خودش سرمایه‌گذاری می‌کند.</div>'
  '</div></div>')

page("components/carousel-body.html","Components","Carousel — body slides",
  "Three body layouts cover all four locked formats. Statement carries the problem documentary, mechanism carries "
  "the explainer, flatlay carries identity. Proof gets its own card.",
  '<div class="row">'
  + frame("Statement · ink", body_statement,1080,1350,.235,
      "Title states the tension in two lines, body resolves it. Never more than 60 Farsi words on a slide — "
      "at feed size that is already a wall.")
  + frame("Mechanism · paper", body_mech,1080,1350,.235,
      "The only slide type where a diagram beats a sentence. Cyan and Electric Blue used as data colors here, "
      "which is the one exception to Electric-Blue-is-CTA-only.")
  + frame("Identity flatlay · sand", body_flatlay,1080,1350,.235,
      "Placeholder marks where your own photography goes. Nothing in frame outranks the pack (§8) — props stay "
      "recognisable and quiet, the pack is the only loud object.")
  + '</div>'
  '<p class="rule bad">The photo box is a <strong>placeholder, not an asset</strong>. Playbook §8: no borrowed '
  'flatlays. The audience fluent enough to read this vocabulary is exactly the audience that spots a repost, and a '
  'spotted repost is the drop-shipping tell an anonymous import page cannot survive.</p>',
  PACK_CSS)

# ───────────────────────── CTA SLIDE ─────────────────────────
cta = ('<div class="art art-45 g-bone"><div class="pad" dir="rtl">'
  '<div class="ng-meta">۷ / ۷</div><div style="flex:1"></div>'
  '<div class="ng-display" style="font-size:88px">این را برای کسی بفرست<br>که روزی چهار قهوه<br>می‌خورد.</div>'
  '<div style="margin-top:56px"><span class="cta-pill">سفارش در دایرکت</span></div>'
  '<div class="ng-meta" style="margin-top:40px">واردات مستقیم &nbsp;·&nbsp; قیمت ۲۴ ساعت اعتبار دارد</div>'
  '<div style="flex:.3"></div></div></div>')

page("components/carousel-cta.html","Components","Carousel — CTA slide",
  "DM sends are the heaviest distribution signal on Instagram in 2026, ahead of likes (§9). So the last slide is "
  "not “link in bio” — it is an instruction to send this to one named person.",
  '<div class="row">' + frame("Send + DM · bone", cta,1080,1350,.28,
      "One Electric Blue object on the slide, and it is the pill. The validity window sits in the نشانه role — "
      "stated as import reality, never as pressure (§6).") + '</div>'
  '<p class="rule"><strong>Name the person, do not describe an audience.</strong> “Send to a friend who works hard” '
  'gets sent to nobody. “روزی چهار قهوه” makes one specific face appear in the reader\'s head — and that face is '
  'often the Gift Buyer, the highest-AOV entry point in §4.</p>'
  '<p class="rule bad">Never “لینک در بایو”. The landing page is a fallback, not the funnel (§7). The DM is the store.</p>',
  PACK_CSS)

# ───────────────────────── PROOF CARD ─────────────────────────
proof = ('<div class="art art-45 g-ink"><div class="pad" dir="rtl">'
  '<div class="ng-meta">اصالت کالا</div>'
  '<div class="ng-display" style="font-size:92px;margin-top:28px">واردات مستقیم</div>'
  '<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:44px">'
  + "".join(f'<div class="ph" style="background:repeating-linear-gradient(45deg,rgba(255,255,255,.06) 0 14px,'
            f'rgba(255,255,255,.11) 14px 28px);color:rgba(255,255,255,.55)">{c}</div>'
            for c in ("کارتن پلمب‌شده","کد بچ روی بسته","برچسب ارسال","باز کردن موجودی"))
  + '</div>'
  '<div class="ng-body" style="color:var(--ng-on-ink-70);margin-top:36px">همه‌ی عکس‌ها از موجودی خودمان.</div>'
  '</div></div>')

page("components/proof-card.html","Components","Authenticity proof",
  "In a gray-import market nobody compares formulas — they decide whether you are real. واردات مستقیم is the "
  "primary credibility mechanic, not one anchor among five. Trust is the product.",
  '<div class="row">' + frame("Proof grid · ink", proof,1080,1350,.28,
      "Four photographic slots: sealed carton, batch code, shipping label, own-inventory unboxing. These are the "
      "assets in playbook §12 item 6 — the card exists so the shoot list is unambiguous.") + '</div>'
  '<p class="rule">This card is also the permanent Highlight. Build it before the feed (§9).</p>'
  '<p class="rule bad">Never write in the register of a pill or medicine. No dosage instructions, no health claims, '
  'no سالم. Regulated-goods language is suppressed on Explore and Reels, and it invites the safety objection you '
  'are trying to walk around.</p>',
  PACK_CSS)

print("components part 1 built")
