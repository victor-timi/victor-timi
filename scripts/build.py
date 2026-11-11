#!/usr/bin/env python3
"""Build the profile SVGs in assets/ with subset fonts embedded.

    python3 scripts/build.py            build from data/
    python3 scripts/build.py --refresh LOGIN  refetch LOGIN's contributions with gh first
"""
import sys
from pathlib import Path

from vt.content import WORK
from vt.contributions import refresh_contributions
from vt.hero import hero
from vt.panels import card, how, proof
from vt.theme import THEMES

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def main():
    if "--refresh" in sys.argv:
        refresh_contributions(sys.argv[sys.argv.index("--refresh") + 1])
    ASSETS.mkdir(exist_ok=True)
    outputs = {"hero.svg": hero()}
    for mode, theme in THEMES.items():
        outputs[f"proof-{mode}.svg"] = proof(theme)
        outputs[f"how-{mode}.svg"] = how(theme)
        for i, item in enumerate(WORK):
            outputs[f"work-{item['slug']}-{mode}.svg"] = card(item, i, theme, mode)
    for name, svg in outputs.items():
        (ASSETS / name).write_text(svg.render())
        print(f"{name:32} {(ASSETS / name).stat().st_size / 1024:6.1f} KB")


if __name__ == "__main__":
    main()
