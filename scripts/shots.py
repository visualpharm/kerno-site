"""Capture live screenshots of Kerno projects (desktop + phone) into site/shots/."""
import io
import sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

OUT = Path(__file__).resolve().parent.parent / "site" / "shots"
SITES = {"bruno": "https://usabruno.com/", "turnos": "https://demo.humanrounds.org/"}
SIZES = {"desktop": dict(viewport={"width": 1440, "height": 900}, device_scale_factor=1),
         "phone": dict(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, url in SITES.items():
            for size, opts in SIZES.items():
                ctx = b.new_context(locale="es-AR", **opts)
                pg = ctx.new_page()
                pg.goto(url, wait_until="load", timeout=60000)
                pg.wait_for_timeout(2500)
                pg.wait_for_timeout(1500)
                f = OUT / f"{name}-{size}.webp"
                Image.open(io.BytesIO(pg.screenshot())).convert("RGB").save(f, "WEBP", quality=82)
                print(f)
                ctx.close()
        b.close()

if __name__ == "__main__":
    sys.exit(main())
