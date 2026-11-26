#!/usr/bin/env python3
"""Build the profile SVGs in assets/ with subset fonts embedded.

    python3 scripts/build.py            build from data/
    python3 scripts/build.py --refresh LOGIN  refetch LOGIN's contributions with gh first

The banner source goes to .cache/hero-banner.svg; make banner turns it into assets/hero.webp.
"""
import sys
from pathlib import Path

from vt.also import also
from vt.content import WORK
from vt.contributions import refresh_contributions
from vt.hero import hero, ribbon
from vt.panels import card, how, proof
from vt.readme import write_readme
from vt.theme import THEMES

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
CACHE = ROOT / ".cache"


def main():
    if "--refresh" in sys.argv:
        refresh_contributions(sys.argv[sys.argv.index("--refresh") + 1])
    ASSETS.mkdir(exist_ok=True)
    CACHE.mkdir(exist_ok=True)
    (CACHE / "hero-banner.svg").write_text(hero().render())
    outputs = {"hero-ribbon.svg": ribbon()}
    for mode, theme in THEMES.items():
        outputs[f"proof-{mode}.svg"] = proof(theme)
        outputs[f"how-{mode}.svg"] = how(theme)
        outputs[f"also-{mode}.svg"] = also(theme)
        for i, item in enumerate(WORK):
            outputs[f"work-{item['slug']}-{mode}.svg"] = card(item, i, theme, mode)
    for name, svg in outputs.items():
        (ASSETS / name).write_text(svg.render())
        print(f"{name:32} {(ASSETS / name).stat().st_size / 1024:6.1f} KB")

    write_readme()


if __name__ == "__main__":
    main()
