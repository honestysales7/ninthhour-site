"""Builds the ninthhour.org static site: index.html, privacy/index.html, terms/index.html."""
import pathlib

ROOT = pathlib.Path(__file__).parent
LEGAL = pathlib.Path('/home/claude/ninth-hour/legal')
PLAY = 'https://play.google.com/store/apps/details?id=org.ninthhour.app'

CSS = """
:root{--bg:#0B1026;--gold:#F5C451;--peach:#FFB38A;--rose:#B3577A;--violet:#2A1E5C;--text:#F4EFE6;--muted:#C9C3D9;--card:rgba(255,255,255,.06);--line:rgba(255,255,255,.12)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.6 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
a{color:var(--gold)}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px}
header.nav{position:sticky;top:0;z-index:5;background:rgba(11,16,38,.82);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
header.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:62px}
.brand{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font:600 20px Georgia,serif}
.brand img{width:34px;height:34px;border-radius:9px}
.nav a.link{color:var(--muted);text-decoration:none;margin-left:18px;font-size:15px}
.hero{background:linear-gradient(160deg,#0B1026 0%,#2A1E5C 45%,#B3577A 82%,#FFB38A 100%);padding:70px 0 80px;overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
h1{font:700 clamp(40px,7vw,68px)/1.05 Georgia,serif;margin:0 0 14px}
.tag{color:var(--gold);font-weight:600;font-size:20px;margin:0 0 14px}
.lead{color:#EDE6F5;font-size:19px;max-width:520px}
.btn{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(135deg,#F5C451,#FFB38A);color:#1A1430;font-weight:700;padding:14px 24px;border-radius:999px;text-decoration:none;box-shadow:0 10px 30px rgba(245,196,81,.35);margin-top:18px}
.small{color:var(--muted);font-size:14px;margin-top:10px}
.phone{justify-self:center;width:min(300px,80vw);border-radius:34px;border:8px solid #141a38;box-shadow:0 30px 70px rgba(0,0,0,.5)}
section{padding:70px 0}
h2{font:700 34px/1.2 Georgia,serif;margin:0 0 10px}
.sub{color:var(--muted);margin:0 0 34px;max-width:640px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.news{display:grid;gap:14px;max-width:760px}.news h3{margin:0 0 6px}.when{font-size:14px;font-weight:600;opacity:.6;margin-left:8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:24px}
.card .i{font-size:30px}.card h3{margin:8px 0 6px;font-size:19px}.card p{margin:0;color:var(--muted);font-size:15.5px}
.shots{display:flex;gap:18px;overflow-x:auto;padding-bottom:12px;scroll-snap-type:x mandatory}
.shots img{width:220px;flex:none;border-radius:22px;scroll-snap-align:start;border:1px solid var(--line)}
.hours{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.hour{border-radius:18px;padding:18px;background:var(--card);border:1px solid var(--line)}
.hour b{display:block;color:var(--gold);font-size:15px}.hour span{color:var(--muted);font-size:14px}
.verse{text-align:center;font:italic 24px/1.5 Georgia,serif;max-width:760px;margin:0 auto}
.verse small{display:block;font:15px system-ui;color:var(--gold);margin-top:10px;font-style:normal}
.price{display:grid;grid-template-columns:1fr 1fr;gap:18px;max-width:720px}
.price .card b{font-size:30px;color:var(--gold)}
footer{border-top:1px solid var(--line);padding:34px 0;color:var(--muted);font-size:14px}
footer a{color:var(--muted);margin-right:16px}
.legal{max-width:760px;padding:50px 22px 70px;margin:0 auto}.legal h1{font-size:42px}.legal h2{font-size:24px;margin-top:30px}
.legal p,.legal li{color:#E6E0F0}
@media(max-width:820px){.hero .wrap{grid-template-columns:1fr;text-align:center}.lead{margin:0 auto}.grid{grid-template-columns:1fr}.hours{grid-template-columns:1fr 1fr}.price{grid-template-columns:1fr}.nav a.link{display:none}}
"""


def page(title, desc, body, depth=0):
    up = '../' * depth
    return f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="https://ninthhour.org/img/og.jpg"><meta property="og:type" content="website">
<meta name="theme-color" content="#0B1026">
<link rel="icon" href="{up}favicon.png">
<style>{CSS}</style></head><body>
<header class="nav"><div class="wrap"><a class="brand" href="{up or './'}"><img src="{up}img/icon.png" alt="">Ninth Hour</a>
<nav><a class="link" href="{up}#features">Features</a><a class="link" href="{up}#new">What&rsquo;s new</a><a class="link" href="{up}#premium">Premium</a><a class="link" href="mailto:sales@honestysales.com">Contact</a></nav></div></header>
{body}
<footer><div class="wrap"><a href="{up}privacy/">Privacy</a><a href="{up}terms/">Terms</a><a href="mailto:sales@honestysales.com">sales@honestysales.com</a>
<p>&copy; 2026 Honesty Sales Ltd &middot; Company no. 15075596 &middot; PA103 Technology Centre, Glaisher Drive, Wolverhampton WV10 9RU, UK</p></div></footer>
</body></html>"""


FEATURES = [
    ('🔔', 'Calls to prayer', 'Gentle calls at the ancient hours, from dawn to night, with natural sounds like bells and cockcrow.'),
    ('🙏', 'Guided prayer', 'Short guided sessions that walk you through praise, confession, thanks and asking.'),
    ('📖', 'The Word every day', 'A Psalm, a Proverb and a Gospel chapter each day, plus a daily verse to share.'),
    ('🪔', 'Keep your lamp burning', 'Your streak, milestones and a calendar of every day you prayed and read.'),
    ('✍️', 'Reflect', 'A daily question and a private journal kept only on your phone.'),
    ('🌅', 'Follows the sun', 'Prayer times move with sunrise and sunset where you live.'),
    ('🔊', 'Listen to the Word', 'Hear each chapter and today&rsquo;s word read aloud, slower or faster, with the verse lit up as it is read.'),
    ('🖍️', 'Colour and share verses', 'Tap verses to colour them, copy them, or share them as text or a beautiful picture.'),
    ('📱', 'Any screen', 'Works upright or sideways, on phones and tablets.'),
]

# Newest first. Add a line here with every app update.
RELEASES = [
    ('0.7.5', 'November 2026', 'Verses you tap are now clearly marked, and the app shows how many you have picked before you colour or share them.'),
    ('0.7.4', 'November 2026', 'Tap verses to colour them in five colours, copy them, or share them as text or a picture. The app now turns sideways and works on tablets.'),
    ('0.7.2', 'November 2026', 'Listen to Bible chapters and today&rsquo;s word read aloud, with slower and faster speeds. Calls to prayer now play their sound.'),
    ('0.6.0', 'November 2026', 'Ninth Hour arrives on Google Play.'),
]

HOURS = [('Before the day', 'Mark 1:35'), ('Morning sacrifice', 'Lamentations 3:22–23'), ('The third hour', 'Acts 2:15'),
         ('The sixth hour', 'Acts 10:9'), ('The ninth hour', 'Acts 3:1'), ('Evening sacrifice', 'Psalm 141:2'),
         ('Family altar', 'Joshua 24:15'), ('Midnight watch', 'Acts 16:25')]

home = f"""
<section class="hero"><div class="wrap">
<div><h1>Ninth Hour</h1><p class="tag">Prayer &amp; Devotion</p>
<p class="lead">Pray at the hours God's people have kept since Bible times, and read His Word every day. A calm, beautiful companion for your walk with God.</p>
<a class="btn" href="{PLAY}">▶ Get it on Google Play</a>
<p class="small">Android now &middot; iPhone coming soon &middot; 7-day free trial of Premium</p></div>
<img class="phone" src="img/1-today.jpg" alt="Ninth Hour Today screen" width="300">
</div></section>

<section id="features"><div class="wrap">
<h2>Built to keep you praying</h2>
<p class="sub">Everything in Ninth Hour has one aim: to help you pray without ceasing and stay in the Word.</p>
<div class="grid">{''.join(f'<div class="card"><div class="i">{i}</div><h3>{t}</h3><p>{d}</p></div>' for i, t, d in FEATURES)}</div>
</div></section>

<section id="new"><div class="wrap">
<h2>What&rsquo;s new</h2>
<p class="sub">Ninth Hour keeps growing. Update the app from Google Play to get the latest.</p>
<div class="news">{''.join(f'<div class="card"><h3>Version {v} <span class="when">{d}</span></h3><p>{t}</p></div>' for v, d, t in RELEASES)}</div>
</div></section>

<section><div class="wrap"><div class="shots">
{''.join(f'<img src="img/{n}.jpg" alt="" loading="lazy">' for n in ['1-today', '2-walk', '3-prayer', '4-word', '5-journey', '6-welcome'])}
</div></div></section>

<section><div class="wrap">
<h2>The ancient hours of prayer</h2>
<p class="sub">Peter and John went up to the temple at the ninth hour, the hour of prayer. Choose a plan (Daniel, the Apostles, Seven times a day or the Watchman) and Ninth Hour calls you at each hour.</p>
<div class="hours">{''.join(f'<div class="hour"><b>{a}</b><span>{b}</span></div>' for a, b in HOURS)}</div>
</div></section>

<section><div class="wrap"><p class="verse">“Peter and John were going up into the temple at the hour of prayer, the ninth hour.”<small>Acts 3:1 (World English Bible)</small></p></div></section>

<section id="premium"><div class="wrap">
<h2>Free to start. Premium to go deeper.</h2>
<p class="sub">The free plan gives you daily calls, guided prayer and a Psalm every day. Premium opens every prayer plan, the full daily readings, longer sessions and your own call sounds.</p>
<div class="price"><div class="card"><h3>Monthly</h3><b>£4.99</b><p>per month, after a 7-day free trial</p></div>
<div class="card"><h3>Yearly</h3><b>£34.99</b><p>per year, after a 7-day free trial. Save over 40%.</p></div></div>
<p class="small">Cancel any time in Google Play. Prices in GBP; local prices may vary.</p>
<a class="btn" href="{PLAY}">▶ Get it on Google Play</a>
</div></section>
"""

(ROOT / 'index.html').write_text(page('Ninth Hour: Prayer & Devotion', 'Pray at the ancient hours and read the Word daily. Calls to prayer, guided prayer, daily Bible reading and a journey that keeps your lamp burning.', home))

for slug, title in [('privacy', 'Privacy Policy'), ('terms', 'Terms of Use')]:
    frag = (LEGAL / f'{slug}.html').read_text()
    body = f'<main class="legal"><h1>{title}</h1>{frag}</main>'
    d = ROOT / slug
    d.mkdir(exist_ok=True)
    (d / 'index.html').write_text(page(f'{title} | Ninth Hour', f'Ninth Hour {title.lower()}.', body, 1))

(ROOT / 'CNAME').write_text('ninthhour.org\n')
(ROOT / '404.html').write_text(page('Not found | Ninth Hour', 'Page not found', '<main class="legal"><h1>Page not found</h1><p><a href="/">Back to Ninth Hour</a></p></main>'))
print('built')
