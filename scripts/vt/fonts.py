"""Google Fonts subsets, cached on disk and returned as base64 woff2."""
import base64
import hashlib
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

CACHE = Path(__file__).resolve().parents[2] / ".cache" / "fonts"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

FONTS = {
    "display": ("Bricolage Grotesque", "wght@{w}", "normal"),
    "body": ("Hanken Grotesk", "wght@{w}", "normal"),
    "mono": ("IBM Plex Mono", "wght@{w}", "normal"),
    "serif": ("Playfair Display", "ital,wght@1,{w}", "italic"),
    "hand": ("Caveat", "wght@{w}", "normal"),
}
def http_get(url, binary=False):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                data = r.read()
            return data if binary else data.decode()
        except OSError:
            if attempt == 4:
                raise
            time.sleep(2 * (attempt + 1))


def font_data(role, weight, chars):
    family, spec, _ = FONTS[role]
    key = hashlib.sha1(f"{role}{weight}{chars}".encode()).hexdigest()[:16]
    cached = CACHE / f"{role}-{weight}-{key}.woff2"
    if not cached.exists():
        query = f"family={family.replace(' ', '+')}:{spec.format(w=weight)}&text={urllib.parse.quote(chars)}"
        css = http_get(f"https://fonts.googleapis.com/css2?{query}")
        url = re.search(r"url\((https://[^)]+)\)", css).group(1)
        CACHE.mkdir(parents=True, exist_ok=True)
        cached.write_bytes(http_get(url, binary=True))
    return base64.b64encode(cached.read_bytes()).decode()
