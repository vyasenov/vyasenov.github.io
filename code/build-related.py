#!/usr/bin/env python3
"""Scan blog/*.qmd front matter and write code/related-posts.json.

Output is consumed at runtime by code/related-posts.js to render a
"Related posts" section at the bottom of each blog post.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
BLOG_DIR = ROOT / "blog"
OUT = ROOT / "code" / "related-posts.json"


def parse_front_matter(text: str) -> dict | None:
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return None
    fm = m.group(1)

    def grab(field: str) -> str | None:
        match = re.search(rf'^{field}:\s*"?([^"\n]+?)"?\s*$', fm, re.MULTILINE)
        return match.group(1).strip() if match else None

    categories: list[str] = []
    inline = re.search(r'^categories:\s*\[([^\]]+)\]\s*$', fm, re.MULTILINE)
    if inline:
        categories = [c.strip().strip('"').strip("'") for c in inline.group(1).split(",")]
    else:
        block = re.search(r'^categories:\s*\n((?:\s+-\s+[^\n]+\n?)+)', fm, re.MULTILINE)
        if block:
            categories = [
                re.sub(r'^\s*-\s*', '', line).strip().strip('"').strip("'")
                for line in block.group(1).splitlines()
                if line.strip()
            ]

    return {"title": grab("title"), "date": grab("date"), "categories": categories}


posts = []
for qmd in sorted(BLOG_DIR.glob("*.qmd")):
    if qmd.name.startswith("_") or qmd.name == "index.qmd":
        continue
    fm = parse_front_matter(qmd.read_text())
    if not fm or not fm["title"]:
        continue
    posts.append({
        "slug": qmd.stem,
        "title": fm["title"],
        "date": fm["date"],
        "categories": fm["categories"],
        "href": qmd.stem + ".html",
    })

payload = json.dumps(posts, indent=2) + "\n"
existing = OUT.read_text() if OUT.exists() else None
if existing == payload:
    print(f"build-related: {len(posts)} posts, unchanged")
else:
    OUT.write_text(payload)
    print(f"build-related: wrote {len(posts)} posts to {OUT.relative_to(ROOT)}")
