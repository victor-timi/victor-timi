"""The also-built panel: six more products in a three-column grid."""
from vt.content import ALSO
from vt.svg import Svg, wrap


def also(theme):
    names = ", ".join(name for name, _, _ in ALSO)
    svg = Svg(1200, 476, f"Also built: {names}.")
    svg.add(f'<rect width="1200" height="476" rx="24" fill="{theme["surface"]}"/>')
    svg.text(48, 80, "Also built", "display", 700, 34, theme["ink"], track=-0.6)
    col = (1200 - 96) / 3
    for i, (name, line, stack) in enumerate(ALSO):
        x, y = 48 + (i % 3) * col, 136 + (i // 3) * 170
        svg.text(x, y, name, "display", 700, 22, theme["ink"], track=-0.3)
        ty = y + 28
        for text in wrap(line, "body", 15, col - 40, 3):
            svg.text(x, ty, text, "body", 400, 15, theme["soft"])
            ty += 21
        svg.text(x, y + 108, stack, "mono", 500, 12, theme["accent"])
    return svg
