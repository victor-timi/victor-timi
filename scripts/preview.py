#!/usr/bin/env python3
"""Write preview.html: the README as GitHub shows it, light and dark side by side."""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GITHUB = {
    "light": dict(bg="#ffffff", fg="#1f2328", muted="#59636e", link="#0969da", rule="#d1d9e0"),
    "dark": dict(bg="#0d1117", fg="#f0f6fc", muted="#9198a1", link="#4493f8", rule="#3d444d"),
}


def to_html(markdown, mode):
    body = re.sub(r'<picture><source[^>]*srcset="([^"]+)-dark\.svg">(<img[^>]*?)src="[^"]+"([^>]*>)</picture>',
                  lambda m: f'{m.group(2)}src="{m.group(1)}-{mode}.svg"{m.group(3)}', markdown)
    blocks = []
    for block in body.strip().split("\n\n"):
        if block.startswith("## "):
            blocks.append(f"<h2>{html.escape(block[3:])}</h2>")
        elif block.startswith("<"):
            blocks.append(block)
        else:
            text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', html.escape(block))
            blocks.append(f"<p>{text}</p>")
    return "\n".join(blocks)


def pane(markdown, mode):
    c = GITHUB[mode]
    return (f'<section style="--bg:{c["bg"]};--fg:{c["fg"]};--muted:{c["muted"]};--link:{c["link"]};--rule:{c["rule"]}">'
            f'<div class="label">GitHub {mode} theme</div><article>{to_html(markdown, mode)}</article></section>')


def main():
    markdown = (ROOT / "README.md").read_text()
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Profile preview</title>
<style>
body {{ margin: 0; font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif; background: #f6f8fa; }}
main {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 900px), 1fr)); }}
section {{ background: var(--bg); color: var(--fg); padding: 32px 16px 64px; }}
.label {{ max-width: 838px; margin: 0 auto 16px; font-size: 14px; color: var(--muted); }}
article {{ max-width: 838px; margin: 0 auto; }}
article h2 {{ font-size: 24px; font-weight: 600; padding-bottom: .3em; border-bottom: 1px solid var(--rule); margin: 24px 0 16px; }}
article p {{ margin: 0 0 16px; }}
article a {{ color: var(--link); text-decoration: none; }}
article img {{ max-width: 100%; vertical-align: top; }}
</style></head><body><main>{pane(markdown, "light")}{pane(markdown, "dark")}</main></body></html>
"""
    (ROOT / "preview.html").write_text(page)
    print(ROOT / "preview.html")


if __name__ == "__main__":
    main()
