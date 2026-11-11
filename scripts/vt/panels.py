"""Themed panels: proof strip, work cards and the how-I-build panel."""
from vt.content import CHECKS, PRINCIPLES, PROOF
from vt.contributions import load_contributions
from vt.svg import Svg, badge, chip, mosaic, wrap
from vt.theme import CREAM, EMBER


def proof(theme):
    total = f"{load_contributions()['total']:,}"
    svg = Svg(1200, 184, f"14 products built. 5+ years independent. {total} contributions in the last 12 months. 1,000+ test files across five client codebases.")
    svg.add(f'<rect width="1200" height="184" rx="24" fill="{theme["surface"]}"/>')
    col = (1200 - 96) / 4
    for i, (number, line1, line2) in enumerate(PROOF):
        x = 48 + i * col
        svg.text(x, 92, number.format(total=total), "display", 700, 54, theme["accent"], track=-1)
        svg.text(x, 126, line1, "body", 400, 16, theme["soft"])
        svg.text(x, 148, line2, "body", 400, 16, theme["soft"])
    return svg


# ---------- work cards ----------

def card(item, index, theme, mode):
    colour = item[mode]
    svg = Svg(590, 344, f"{item['name']}: {item['outcome']} {item['detail']}")
    svg.add(f'<rect width="590" height="344" rx="24" fill="{theme["surface"]}"/>')
    chip(svg, 32, 30, item["chip"], colour, theme)
    mosaic(svg, 590 - 32 - 50, 28, colour, index)
    svg.text(32, 116, item["name"], "display", 700, 40, theme["ink"], track=-0.8)
    y = 152
    for line in wrap(item["outcome"], "body", 19, 526, 2):
        svg.text(32, y, line, "body", 500, 19, theme["ink"])
        y += 26
    svg.text(32, 226, item["label"].upper(), "body", 600, 11.5, colour, track=1.8)
    y = 252
    for line in wrap(item["detail"], "body", 16, 526, 2):
        svg.text(32, y, line, "body", 400, 16, theme["soft"])
        y += 23
    svg.text(32, 316, item["stack"], "mono", 500, 13, theme["faint"])
    badge(svg, 558, 297, item["badge"], colour, theme)
    return svg


# ---------- how I build ----------

def how(theme):
    svg = Svg(1200, 476, "How I build: standards a script enforces. Guard checks for tokens, copy, errors, types, env, secrets, length, tests and migrations.")
    svg.add(f'<rect width="1200" height="476" rx="24" fill="{theme["surface"]}"/>')
    svg.text(48, 100, "How I build", "display", 700, 44, theme["ink"], track=-1)
    svg.text(48, 140, "Standards a script enforces, not a style guide.", "serif", 400, 22, theme["accent"])
    y = 206
    for label, body in PRINCIPLES:
        svg.text(48, y, label.upper(), "body", 600, 12, theme["accent"], track=2)
        ty = y + 28
        for line in wrap(body, "body", 17, 480, 2):
            svg.text(48, ty, line, "body", 400, 17, theme["soft"])
            ty += 25
        y += 92

    px, py, pw, ph = 600, 48, 552, 380
    svg.add(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#0A1416"/>')
    for i in range(3):
        svg.add(f'<circle cx="{px + 24 + i * 16}" cy="{py + 24}" r="4.5" fill="#33454A"/>')
    svg.text(px + 28, py + 70, "$", "mono", 500, 15, EMBER)
    svg.text(px + 46, py + 70, "make guards", "mono", 500, 15, CREAM)
    y = py + 106
    for name, desc in CHECKS:
        svg.add(f'<path d="M{px + 28} {y - 5} l4 4 l8 -9" fill="none" stroke="#6CC08B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
        svg.text(px + 50, y, name, "mono", 500, 14, CREAM)
        svg.text(px + 160, y, desc, "body", 400, 14, "#93A3A1")
        y += 28
    svg.text(px + 28, y + 12, f"{len(CHECKS)} checks passed", "mono", 500, 13, "#6CC08B")
    return svg
