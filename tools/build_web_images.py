#!/usr/bin/env python3
"""Build website-sized WebP copies of a tour's PNG images.

Usage: python3 tools/build_web_images.py tour-images/01_Christmas_in_Rome

Writes <tour>/web/<subdir>/<name>-<width>.webp for each width below and
<tour>/web/images.json listing the files, alt text and review verdict, so a
web page can use <img srcset> without shipping the 2-3 MB source PNGs.
"""
import json
import sys
from pathlib import Path

from PIL import Image

WIDTHS = (1600, 800)
QUALITY = 82


def main(tour_dir):
    tour = Path(tour_dir)
    manifest = json.loads((tour / "manifest.json").read_text())
    out_root = tour / "web"
    entries = []
    for asset in manifest["assets"]:
        src = tour / asset["filename"]
        img = Image.open(src).convert("RGB")
        variants = []
        for width in WIDTHS:
            width = min(width, img.width)
            height = round(img.height * width / img.width)
            dest = out_root / src.parent.name / f"{src.stem}-{width}.webp"
            dest.parent.mkdir(parents=True, exist_ok=True)
            img.resize((width, height), Image.LANCZOS).save(dest, "WEBP", quality=QUALITY, method=6)
            variants.append({"path": dest.relative_to(tour).as_posix(), "width": width,
                             "height": height, "bytes": dest.stat().st_size})
        entries.append({
            "source": asset["filename"],
            "placement": asset["placement"],
            "date": asset.get("date"),
            "alt_text": asset.get("alt_text"),
            "verdict": asset.get("landmark_review", {}).get("verdict"),
            "website_ready": asset.get("website_ready", False),
            "variants": variants,
        })
        print(f"{asset['filename']}: " + ", ".join(f"{v['width']}w {v['bytes'] // 1024} KB" for v in variants))
    (out_root / "images.json").write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "tour-images/01_Christmas_in_Rome")
