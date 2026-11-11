"""Write README.md: the panels in order, light and dark, with card links."""
from pathlib import Path

from vt.content import CONTACT, WORK
from vt.contributions import load_contributions

README = Path(__file__).resolve().parents[2] / "README.md"


def picture(name, alt, width="100%", href=None):
    img = (f'<picture><source media="(prefers-color-scheme: dark)" srcset="assets/{name}-dark.svg">'
           f'<img alt="{alt}" src="assets/{name}-light.svg" width="{width}"></picture>')
    return f'<a href="{href}">{img}</a>' if href else img


def work_rows():
    rows = []
    for i in range(0, len(WORK), 2):
        cells = [picture(f"work-{w['slug']}", f"{w['name']}: {w['outcome']}", "49%", w.get("link"))
                 for w in WORK[i:i + 2]]
        rows.append("<p>\n" + "\n".join(cells) + "\n</p>")
    return "\n\n".join(rows)


def write_readme():
    total = f"{load_contributions()['total']:,}"
    contact = " · ".join(f"[{label}]({url})" for label, url in CONTACT)
    README.write_text(f"""<img alt="Victor Timi, senior AI and full-stack engineer. Builds software that holds up after launch." src="assets/hero.svg" width="100%">

{picture("proof", f"14 products built. 5+ years independent. {total} contributions in the last 12 months. 1,000+ test files across five client codebases.")}

## Selected work

Most of what I build lives in private client repositories. These are the products, what they do and the call that shaped each one.

{work_rows()}

{picture("also", "Also built: ISM, Job Sniper, Plan With a Pro, Vespucci, Flexecution and voice, email and social automation.")}

{picture("how", "How I build: standards a script enforces, from design tokens to migrations.")}

## Work with me

Open to contract work, consulting and remote roles in AI systems engineering, LLM architecture and full-stack development.

{contact}
""")
