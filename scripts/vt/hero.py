"""The hero banner: the LinkedIn banner's scene, positioning and the contributions ribbon."""
import calendar

from vt.contributions import load_contributions
from vt.hero_scene import defs, devices, footprint_trail, notes, orbits, private_badge, wall
from vt.svg import Svg
from vt.theme import AMBER, CREAM, DEEP, EMBER, INK, WARM

W, H = 1200, 690
LEFT = 64


def background(svg):
    svg.defs.append(
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{INK}"/>'
        f'<stop offset=".5" stop-color="{DEEP}"/><stop offset="1" stop-color="{WARM}"/></linearGradient>'
        '<radialGradient id="glowA" cx="0" cy="0" r="1" gradientTransform="translate(60 0) scale(620 420)" gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#FF6A28" stop-opacity=".26"/><stop offset="1" stop-color="#FF6A28" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="glowB" cx="0" cy="0" r="1" gradientTransform="translate(980 520) scale(560 300)" gradientUnits="userSpaceOnUse">'
        '<stop offset="0" stop-color="#FF4D2E" stop-opacity=".16"/><stop offset="1" stop-color="#FF4D2E" stop-opacity="0"/></radialGradient>'
        f'<linearGradient id="word" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{AMBER}"/><stop offset="1" stop-color="{EMBER}"/></linearGradient>'
        f'<linearGradient id="peak" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="{EMBER}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>'
        f'<clipPath id="card"><rect width="{W}" height="{H}" rx="28"/></clipPath>' + defs())
    svg.add(f'<g clip-path="url(#card)"><rect width="{W}" height="{H}" fill="url(#bg)"/>'
            f'<rect width="{W}" height="{H}" fill="url(#glowA)"/><rect width="{W}" height="{H}" fill="url(#glowB)"/>')


def copy(svg):
    svg.text(LEFT, 84, "SENIOR AI & FULL-STACK ENGINEER", "body", 600, 13, AMBER, track=3.6)
    svg.text(LEFT - 3, 186, "Victor Timi", "display", 700, 92, CREAM, track=-2)
    svg.text(LEFT, 246, "Atomic steps make a giant", "display", 700, 38, CREAM, track=-1)
    svg.text(LEFT, 296, "footprint.", "mono", 700, 40, "url(#word)", track=-1)
    footprint_trail(svg, LEFT + 262, 282)
    svg.text(LEFT, 346, "AI agents, RAG and computer vision.", "body", 400, 20, CREAM, opacity=.84)
    svg.text(LEFT, 374, "Web and mobile, from first commit to production.", "body", 400, 20, CREAM, opacity=.84)


def chart(svg, data):
    months = list(data["months"].items())[-13:]
    svg.text(LEFT, 512, f"{data['total']:,} contributions in the last 12 months", "mono", 500, 14, CREAM, opacity=.9)
    private_badge(svg, 1136, 494)
    base, top, x0, x1, gap = 626, 548, 64, 1136, 10
    bar = (x1 - x0 - gap * (len(months) - 1)) / len(months)
    peak = max(v for _, v in months)
    for i, (month, value) in enumerate(months):
        h = max(4, (base - top) * value / peak)
        x = x0 + i * (bar + gap)
        is_peak = value == peak
        fill = 'fill="url(#peak)"' if is_peak else f'fill="{CREAM}" fill-opacity=".16"'
        svg.add(f'<rect x="{x:.1f}" y="{base - h:.1f}" width="{bar:.1f}" height="{h:.1f}" rx="3" {fill}/>')
        svg.text(x + bar / 2, base - h - 8, str(value), "mono", 500, 13,
                 AMBER if is_peak else CREAM, "middle", opacity=1 if is_peak else .62)
        label = calendar.month_abbr[int(month[5:])]
        if i in (0, len(months) - 1):
            label = f"{label} ’{month[2:4]}"
        svg.text(x + bar / 2, base + 24, label, "mono", 500, 12, CREAM, "middle", opacity=.5)


def hero():
    data = load_contributions()
    svg = Svg(W, H, f"Victor Timi, senior AI and full-stack engineer. Atomic steps make a giant footprint. "
                    f"{data['total']:,} contributions in the last 12 months.")
    background(svg)
    wall(svg)
    orbits(svg)
    devices(svg)
    svg.add('</g>')
    copy(svg)
    notes(svg)
    chart(svg, data)
    return svg
