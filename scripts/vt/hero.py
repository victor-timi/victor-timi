"""The hero banner: name, positioning and the contributions ribbon."""
import calendar
import json
import math
from pathlib import Path

from vt.svg import Svg
from vt.theme import AMBER, CREAM, EMBER

CONTRIB = Path(__file__).resolve().parents[2] / "data" / "contributions.json"


def hero():
    data = json.loads(CONTRIB.read_text())
    months = list(data["months"].items())[-13:]
    svg = Svg(1200, 620, f"Victor Timi, senior AI and full-stack engineer. {data['total']:,} contributions in the last 12 months.")
    svg.defs.append(
        '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#0A1D21"/><stop offset=".55" stop-color="#113539"/>'
        '<stop offset="1" stop-color="#1D514E"/></linearGradient>'
        '<radialGradient id="glow" cx="0" cy="0" r="1" gradientTransform="translate(0 0) scale(760 520)" gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#F2C27A" stop-opacity=".24"/><stop offset="1" stop-color="#F2C27A" stop-opacity="0"/></radialGradient>'
        '<clipPath id="card"><rect width="1200" height="620" rx="28"/></clipPath>')
    svg.add('<g clip-path="url(#card)"><rect width="1200" height="620" fill="url(#bg)"/>'
            '<rect width="1200" height="620" fill="url(#glow)"/>')
    for r in (170, 250, 330, 410, 490):
        svg.add(f'<circle cx="1200" cy="0" r="{r}" fill="none" stroke="{CREAM}" stroke-opacity=".07"/>')
    for i in range(14):
        angle = 1.62 + i * 0.077
        x2, y2 = 1200 + 720 * math.cos(angle), 720 * math.sin(angle)
        svg.add(f'<line x1="1200" y1="0" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{CREAM}" stroke-opacity=".05"/>')
    svg.add('</g>')

    svg.text(64, 78, "SENIOR AI & FULL-STACK ENGINEER", "body", 600, 13, CREAM, track=3.6, opacity=.82)
    svg.text(1136, 78, "OPEN TO CONTRACTS AND REMOTE ROLES", "body", 600, 13, CREAM, "end", track=3.6, opacity=.82)
    svg.text(58, 236, "Victor Timi", "display", 700, 124, CREAM, track=-2.5)
    svg.text(64, 298, "builds software that holds up after launch.", "serif", 400, 40, AMBER)
    svg.text(64, 354, "AI systems, SaaS platforms and the design systems under them.", "body", 400, 21, CREAM, opacity=.84)
    svg.text(64, 384, "Architecture, backend, interface and infrastructure, owned end to end.", "body", 400, 21, CREAM, opacity=.84)

    svg.text(64, 452, f"{data['total']:,} contributions in the last 12 months", "mono", 500, 14, CREAM, opacity=.9)
    svg.text(1136, 452, "most of them in private client repositories", "body", 400, 14, CREAM, "end", opacity=.62)
    base, top, x0, x1, gap = 560, 476, 64, 1136, 10
    bar = (x1 - x0 - gap * (len(months) - 1)) / len(months)
    peak = max(v for _, v in months)
    for i, (month, value) in enumerate(months):
        h = max(4, (base - top) * value / peak)
        x = x0 + i * (bar + gap)
        is_peak = value == peak
        fill = f'fill="{EMBER}"' if is_peak else f'fill="{CREAM}" fill-opacity=".26"'
        svg.add(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bar:.1f}" height="{h:.1f}" rx="3" {fill}/>')
        if is_peak:
            svg.text(x + bar / 2, base - h - 8, str(value), "mono", 500, 13, EMBER, "middle")
        label = calendar.month_abbr[int(month[5:])]
        svg.text(x + bar / 2, base + 24, label, "mono", 500, 12, CREAM, "middle", opacity=.55)
    return svg
