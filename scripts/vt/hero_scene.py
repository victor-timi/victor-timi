"""The banner scene for the hero: a curved wall of product screens, devices, orbits and notes."""
import base64
import math
from functools import lru_cache
from pathlib import Path

from vt.svg import text_width
from vt.theme import AMBER, CREAM

SCREENS = Path(__file__).resolve().parents[2] / "assets" / "screens"

WALL = [
    ["ism-hero-dark", "s6", "vespucci-planner-page", "campusreels-home", "qnotix-hero-section", "en-dashboard"],
    ["call-management", "s3", "conde-home", "trellis-welcome", "work-orders-with-map", "cimpl3-demo"],
    ["sdg-home", "cimpl3-landing", "s2", "conde-color-ring", "trellis-dark", "ism-hero-dark"],
]
FOOT = ('<ellipse cx="20" cy="40" rx="11" ry="18"/><circle cx="9" cy="14" r="4"/><circle cx="17" cy="9" r="4.4"/>'
        '<circle cx="25.5" cy="9.5" r="3.8"/><circle cx="32" cy="14" r="3.2"/><circle cx="35" cy="21" r="2.6"/>')


@lru_cache(maxsize=None)
def image(name):
    data = base64.b64encode((SCREENS / f"{name}.jpg").read_bytes()).decode()
    return f"data:image/jpeg;base64,{data}"


def defs():
    return ('<clipPath id="tile"><rect width="124" height="78" rx="7"/></clipPath>'
            '<clipPath id="shot"><rect width="330" height="200" rx="4"/></clipPath>'
            '<clipPath id="phoneScreen"><rect width="68" height="146" rx="11"/></clipPath>'
            '<linearGradient id="wallFade" x1="0" y1="0" x2="1" y2="0">'
            '<stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".22" stop-color="#fff" stop-opacity="1"/>'
            '<stop offset=".92" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>'
            '<mask id="wallMask"><rect x="540" y="0" width="660" height="470" fill="url(#wallFade)"/></mask>'
            '<radialGradient id="spark"><stop offset="0" stop-color="#FFE4CC"/><stop offset=".35" stop-color="#FFB067" stop-opacity=".7"/>'
            '<stop offset="1" stop-color="#FF5A36" stop-opacity="0"/></radialGradient>')


def wall(svg):
    """Three rows of screens, sheared and dimmed toward the edges so the wall reads as curved."""
    svg.add('<g mask="url(#wallMask)">')
    for r, row in enumerate(WALL):
        for c, name in enumerate(row):
            t = (c - (len(row) - 1) / 2) / ((len(row) - 1) / 2)
            x = 900 + t * 300 + (22 if r % 2 else 0)
            y = 70 + r * 98
            sx = 0.86 - abs(t) * 0.22
            shear = t * 0.14
            fade = 0.55 - abs(t) * 0.22
            svg.add(f'<g transform="matrix({sx:.3f} {shear:.3f} 0 1 {x - 62 * sx:.1f} {y - 62 * shear:.1f})" opacity="{fade:.2f}">'
                    f'<g clip-path="url(#tile)"><rect width="124" height="78" fill="#18181B"/>'
                    f'<image href="{image(name)}" width="124" height="78" preserveAspectRatio="xMidYMin slice"/></g>'
                    f'<rect width="124" height="78" rx="7" fill="none" stroke="{CREAM}" stroke-opacity=".1"/></g>')
    svg.add('</g>')


def orbits(svg):
    for rx, ry, alpha, width in ((330, 76, .42, 1.4), (262, 56, .18, 1)):
        svg.add(f'<ellipse cx="935" cy="300" rx="{rx}" ry="{ry}" fill="none" stroke="{AMBER}" stroke-opacity="{alpha}" '
                f'stroke-width="{width}" transform="rotate(-8 935 300)"/>')
    a = math.radians(-62)
    sx, sy = 935 + 330 * math.cos(a), 300 + 76 * math.sin(a)
    rot = math.radians(-8)
    px = 935 + (sx - 935) * math.cos(rot) - (sy - 300) * math.sin(rot)
    py = 300 + (sx - 935) * math.sin(rot) + (sy - 300) * math.cos(rot)
    svg.add(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="16" fill="url(#spark)"/><circle cx="{px:.1f}" cy="{py:.1f}" r="2.6" fill="#FFE4CC"/>')


def devices(svg):
    """The featured browser window and two phones in front of the wall."""
    svg.add('<g transform="matrix(1 -0.05 0 1 742 156)">'
            '<rect x="-8" y="-8" width="346" height="232" rx="12" fill="#000" fill-opacity=".45"/>'
            '<rect width="330" height="216" rx="9" fill="#18181B" stroke="#FAFAF9" stroke-opacity=".16"/>'
            f'<circle cx="14" cy="8" r="3" fill="{AMBER}"/><circle cx="25" cy="8" r="3" fill="#52525B"/><circle cx="36" cy="8" r="3" fill="#52525B"/>'
            f'<g transform="translate(0 16)" clip-path="url(#shot)"><image href="{image("trellis-home")}" width="330" height="200" '
            'preserveAspectRatio="xMidYMin slice"/></g></g>')
    for x, y, shear, name in ((1062, 196, -0.09, "trellis-phone"), (1128, 168, -0.12, "conde-color-ring")):
        svg.add(f'<g transform="matrix(1 {shear} 0 1 {x} {y})">'
                '<rect x="-4" y="-4" width="76" height="154" rx="14" fill="#050505" stroke="#FAFAF9" stroke-opacity=".2"/>'
                f'<g clip-path="url(#phoneScreen)"><image href="{image(name)}" width="68" height="146" preserveAspectRatio="xMidYMin slice"/></g></g>')


def notes(svg):
    """The five skills as handwritten notes with small arrows, as on the banner."""
    items = [
        (596, 46, "system design", "M110 -6 C 126 -2, 136 8, 140 22", -4),
        (900, 40, "cloud & DevOps", "M120 -4 C 138 0, 148 12, 152 26", -3),
        (584, 448, "product architecture", "M150 -18 C 162 -30, 172 -40, 186 -48", -4),
        (842, 456, "agentic engineering", "M64 -22 C 64 -36, 70 -48, 80 -60", -3),
        (1052, 440, "UI/UX craft", "M-8 -14 C -20 -26, -24 -38, -22 -52", -4),
    ]
    for x, y, label, arrow, angle in items:
        svg.add(f'<g transform="rotate({angle} {x} {y})">')
        svg.text(x, y, label, "hand", 600, 22, CREAM, opacity=.92)
        svg.add(f'<path d="{arrow}" transform="translate({x} {y})" fill="none" stroke="{AMBER}" stroke-width="1.8" stroke-linecap="round"/>')
        svg.add('</g>')


def footprint_trail(svg, x, y):
    """Five prints in an even left-right step, centred on the line at y, growing toward the end."""
    for i in range(5):
        side = -1 if i % 2 == 0 else 1
        scale = 0.34 + i * 0.05
        svg.add(f'<g transform="translate({x + i * 30} {y + side * 4}) rotate({90 + side * 8}) scale({scale:.2f}) translate(-20 -36)" '
                f'fill="{AMBER}" fill-opacity="{0.32 + i * 0.12:.2f}">{FOOT}</g>')


LOCK = ('<rect x="0" y="5" width="11" height="8" rx="2"/>'
        '<path d="M2.5 5V3.5a3 3 0 0 1 6 0V5" fill="none" stroke-width="1.6"/>')


def private_badge(svg, x_right, y):
    """An amber pill with a lock: most contributions live in private client repositories."""
    label = "Most in private client repositories"
    width = text_width(label, "body", 13) + 52
    x = x_right - width
    svg.add(f'<rect x="{x:.1f}" y="{y}" width="{width:.1f}" height="28" rx="14" fill="{AMBER}" fill-opacity=".12" '
            f'stroke="{AMBER}" stroke-opacity=".32"/>')
    svg.add(f'<g transform="translate({x + 15:.1f} {y + 7})" fill="{AMBER}" stroke="{AMBER}">{LOCK}</g>')
    svg.text(x + 36, y + 18.5, label, "body", 600, 13, CREAM, opacity=.88)
