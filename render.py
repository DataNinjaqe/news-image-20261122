#!/usr/bin/env python3
"""Render the news-image-20261122 front page (1024x1024) with PIL.
No Chromium on this machine; layout mirrors the 20261121 image.html spec
(same masthead, kickers, rules, column structure, palette).
Deterministic: fixed text, fixed fonts, no timestamps; PNG written with
PIL defaults so repeated runs are byte-identical.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (248, 244, 236)
INK = (20, 20, 20)
BODY = (51, 51, 51)
RULE = (154, 145, 126)
RED = (185, 28, 28)
BLUE = (30, 58, 95)
GOLD = (138, 122, 92)
GREY = (85, 85, 85)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
MX = 40
CW = W - 2 * MX

def text_w(s, f):
    return d.textbbox((0, 0), s, font=f)[2]

def wrap(s, f, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if text_w(t, f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(s, f, x, y, max_w, fill, spacing=4):
    for ln in wrap(s, f, max_w):
        d.text((x, y), ln, font=f, fill=fill)
        y += f.size + spacing
    return y

def spaced_center(s, f, y, fill, tracking=6):
    total = sum(text_w(c, f) + tracking for c in s) - tracking
    x = (W - total) // 2
    for c in s:
        d.text((x, y), c, font=f, fill=fill)
        x += text_w(c, f) + tracking
    return y + f.size

def rule(y, color=RULE, width=1):
    d.line([(MX, y), (W - MX, y)], fill=color, width=width)
    return y + width

y = 30
y = spaced_center("THE WORLD IN ONE DAY", font(SANS, 17), y, GOLD, tracking=7)
y += 10
f_mast = font(SERIF_B, 52)
t = "SUNDAY 22 NOVEMBER 2026"
d.text(((W - text_w(t, f_mast)) // 2, y), t, font=f_mast, fill=INK)
y += 62
y = spaced_center("THE DAY'S NEWS, IN ONE PICTURE", font(SANS, 16), y, GREY, tracking=3)
y += 12
d.line([(MX, y), (W - MX, y)], fill=INK, width=4)
y += 6
d.line([(MX, y), (W - MX, y)], fill=INK, width=1)
y += 18

# ---- lead ----
f_kick = font(SANS_B, 16)
d.text((MX, y), "JUSTICE  ·  THE HAGUE", font=f_kick, fill=RED)
y += 26
f_lead = font(SERIF_B, 40)
y = draw_wrapped("World court finds Myanmar guilty of Rohingya genocide", f_lead, MX, y, CW, INK, spacing=2)
y += 6
f_body = font(SERIF, 20)
y = draw_wrapped(
    "The International Court of Justice rules 9\u20136 that Myanmar committed genocide in its "
    "2017 crackdown, citing evidence of some 10,000 Rohingya killed \u2014 the first time a state "
    "has been held responsible for genocide \u2014 and orders reparations and a safe return home.",
    f_body, MX, y, CW, BODY, spacing=3)
y += 14
y = rule(y)
y += 16

# ---- row 2: two columns ----
col_w = (CW - 36) // 2
y2 = y
f_h3 = font(SERIF_B, 27)
f_p2 = font(SERIF, 18)
def col(x, w, kicker, head, body, y0):
    yy = y0
    d.text((x, yy), kicker, font=f_kick, fill=RED)
    yy += 25
    yy = draw_wrapped(head, f_h3, x, yy, w, INK, spacing=2)
    yy += 5
    yy = draw_wrapped(body, f_p2, x, yy, w, BODY, spacing=3)
    return yy
end_l = col(MX, col_w, "CONFLICT  ·  THE GULF",
            "Iran war has cost US more than $48bn, Pentagon says",
            "The cost tally lands as Hormuz shipping stays on edge \u2014 a tanker burned "
            "after a sea mine strike \u2014 and a cargo ship catches fire after a drone "
            "attack in the Baltic.", y2)
d.line([(MX + col_w + 18, y2), (MX + col_w + 18, max(end_l, y2 + 150))], fill=RULE, width=1)
end_r = col(MX + col_w + 36, col_w, "CLIMATE  ·  COP31",
            "Fossil-fuel fight threatens climate deal",
            "Negotiators say talks are close to a final deal, but the dispute over "
            "fossil fuels could still scupper it as the summit enters its final stretch.", y2)
y = max(end_l, end_r) + 14
y = rule(y)
y += 16

# ---- row 3: three columns ----
col3 = (CW - 60) // 3
f_h3b = font(SERIF_B, 23)
f_p3 = font(SERIF, 16)
def col3f(x, w, kicker, head, body, y0):
    yy = y0
    d.text((x, yy), kicker, font=f_kick, fill=RED)
    yy += 25
    yy = draw_wrapped(head, f_h3b, x, yy, w, INK, spacing=2)
    yy += 5
    yy = draw_wrapped(body, f_p3, x, yy, w, BODY, spacing=3)
    return yy
e1 = col3f(MX, col3, "FRANCE",
           "Sixth weekend of protests in France",
           "Crowds rally over living costs and public services as the president\u2019s "
           "popularity flatlines.", y)
x2 = MX + col3 + 30
d.line([(x2 - 15, y), (x2 - 15, y + 150)], fill=RULE, width=1)
e2 = col3f(x2, col3, "AFRICA",
           "G20 opens in Johannesburg",
           "The first G20 summit on African soil opens in South Africa.", y)
x3 = MX + 2 * col3 + 60
d.line([(x3 - 15, y), (x3 - 15, y + 150)], fill=RULE, width=1)
e3 = col3f(x3, col3, "MARKETS",
           "Bitcoin crashes to two-year low",
           "Crypto slides as Nvidia faces a US accounting probe amid deepening turmoil.", y)
y = max(e1, e2, e3) + 14
y = rule(y)
y += 14

# ---- also ----
d.text((MX, y), "ALSO IN THE NEWS", font=f_kick, fill=BLUE)
y += 25
f_also = font(SERIF, 17)
y = draw_wrapped(
    "Serbia\u2019s president resigns.  ·  Pentagon moves to restrict defence ties with Canada.  ·  "
    "Trump vows to work with Democrats to cap credit-card interest at 10%.  ·  Houthis launch "
    "revenge strikes on the Saudi capital.  ·  39 missing after a factory fire in Indonesia.  ·  "
    "24 dead as a boat capsizes in Nigeria.",
    f_also, MX, y, CW, BODY, spacing=3)
y += 12

# ---- numbers strip ----
nums = [("10,000", "Rohingya killed, per the court\u2019s evidence"),
        ("$48bn+", "US cost of the Iran war, Pentagon tally"),
        ("730,000+", "Rohingya fled to Bangladesh in 2017"),
        ("6th", "weekend of protests across France")]
box_w = (CW - 3 * 24) // 4
box_h = 92
top = y
for i, (n, t) in enumerate(nums):
    x0 = MX + i * (box_w + 24)
    d.rectangle([x0, top, x0 + box_w, top + box_h], outline=RULE, width=1)
    fn = font(SERIF_B, 28)
    d.text((x0 + (box_w - text_w(n, fn)) // 2, top + 10), n, font=fn, fill=RED)
    ft = font(SANS, 13)
    lines = wrap(t, ft, box_w - 16)
    yy = top + 48
    for ln in lines:
        d.text((x0 + (box_w - text_w(ln, ft)) // 2, yy), ln, font=ft, fill=BODY)
        yy += 17
y = top + box_h + 14

# ---- footer ----
d.line([(MX, y), (W - MX, y)], fill=INK, width=4)
y += 10
f_foot = font(SANS, 14)
d.text((MX, y), "THE WORLD  ·  SUNDAY 22 NOVEMBER 2026", font=f_foot, fill=GREY)
r = "ONE IMAGE  ·  ONE DAY"
d.text((W - MX - text_w(r, f_foot), y), r, font=f_foot, fill=GREY)
print("final y:", y, "canvas:", H)
import os
img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png"))
print("saved entry.png")
