"""SVG canvas with tracked font usage, plus shared marks: chip, badge, mosaic."""
import collections
from xml.sax.saxutils import escape

from vt.fonts import FONTS, font_data

WIDTH_FACTOR = {"display": 0.56, "body": 0.53, "mono": 0.6, "serif": 0.47}

def text_width(s, role, size):
    return len(s) * size * WIDTH_FACTOR[role]


def wrap(s, role, size, max_width, max_lines):
    lines, line = [], ""
    for word in s.split():
        trial = f"{line} {word}".strip()
        if text_width(trial, role, size) > max_width and line:
            lines.append(line)
            line = word
        else:
            line = trial
    lines.append(line)
    if len(lines) > max_lines:
        raise ValueError(f"Copy too long for {max_lines} lines: {s!r}")
    return lines


class Svg:
    def __init__(self, width, height, title):
        self.width, self.height, self.title = width, height, title
        self.defs, self.parts = [], []
        self.used = collections.defaultdict(set)

    def add(self, markup):
        self.parts.append(markup)

    def text(self, x, y, s, role, weight, size, fill, anchor="start", track=0, opacity=1.0):
        self.used[(role, weight)].update(s)
        attrs = [f'x="{x:g}"', f'y="{y:g}"', f'font-family="vt-{role}"', f'font-weight="{weight}"',
                 f'font-size="{size}"', f'fill="{fill}"', f'text-anchor="{anchor}"']
        if FONTS[role][2] == "italic":
            attrs.append('font-style="italic"')
        if track:
            attrs.append(f'letter-spacing="{track}"')
        if opacity != 1:
            attrs.append(f'fill-opacity="{opacity}"')
        self.add(f'<text {" ".join(attrs)}>{escape(s)}</text>')

    def render(self):
        faces = []
        for (role, weight), chars in sorted(self.used.items()):
            data = font_data(role, weight, "".join(sorted(chars)))
            faces.append(f"@font-face{{font-family:'vt-{role}';font-style:{FONTS[role][2]};"
                         f"font-weight:{weight};src:url(data:font/woff2;base64,{data}) format('woff2')}}")
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
                f'viewBox="0 0 {self.width} {self.height}" role="img" aria-labelledby="title">'
                f'<title id="title">{escape(self.title)}</title>'
                f'<defs><style>{"".join(faces)}</style>{"".join(self.defs)}</defs>'
                f'{"".join(self.parts)}</svg>\n')


def tint(hex_colour, alpha):
    return f'fill="{hex_colour}" fill-opacity="{alpha}"'


def badge(svg, x_right, y, label, colour, theme):
    width = text_width(label, "body", 12.5) + 40
    x = x_right - width
    svg.add(f'<rect x="{x:g}" y="{y}" width="{width:g}" height="28" rx="14" {tint(colour, theme["tint_alpha"])}/>')
    svg.add(f'<circle cx="{x + 15:g}" cy="{y + 14}" r="4" fill="{colour}"/>')
    svg.add(f'<circle cx="{x + 15:g}" cy="{y + 14}" r="7" fill="none" stroke="{colour}" stroke-opacity="0.35"/>')
    svg.text(x + 28, y + 18.5, label, "body", 600, 12.5, colour)


def chip(svg, x, y, label, colour, theme):
    label = label.upper()
    width = text_width(label, "body", 11.5) + 11.5 * 0.16 * len(label) + 28
    svg.add(f'<rect x="{x}" y="{y}" width="{width:g}" height="28" rx="14" {tint(colour, theme["tint_alpha"])}/>')
    svg.text(x + 14, y + 18.5, label, "body", 600, 11.5, colour, track=1.8)


def mosaic(svg, x, y, colour, seed):
    pattern = [1, .55, .25, .55, .25, .12, .25, .12, .06]
    shift = seed % len(pattern)
    pattern = pattern[shift:] + pattern[:shift]
    for i, alpha in enumerate(pattern):
        cx, cy = x + (i % 3) * 18, y + (i // 3) * 18
        svg.add(f'<rect x="{cx}" y="{cy}" width="14" height="14" rx="3.5" {tint(colour, alpha)}/>')
