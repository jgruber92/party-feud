#!/usr/bin/env python3
"""Build index.html (the playable page) from src/game.html.

src/game.html is written without <!doctype>, <html>, <head> or <body> so it can also be
published as a Claude artifact, which adds those itself. This script adds them back so the
game runs as a normal web page (GitHub Pages, or double-clicking index.html).

Run after editing src/game.html:  python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src" / "game.html"
OUT = ROOT / "index.html"
SPLIT = "<!-- ============ BOARD (TV) ============ -->"

src = SRC.read_text(encoding="utf-8")
if SPLIT not in src:
    raise SystemExit(f"Could not find the marker {SPLIT!r} in {SRC}")
head, body = src.split(SPLIT, 1)

page = (
    "<!doctype html>\n"
    '<html lang="en">\n'
    "<head>\n"
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    f"{head.strip()}\n"
    "</head>\n"
    "<body>\n"
    f"{SPLIT}{body.rstrip()}\n"
    "</body>\n"
    "</html>\n"
)
OUT.write_text(page, encoding="utf-8")
print(f"Wrote {OUT.name} ({len(page):,} bytes)")
