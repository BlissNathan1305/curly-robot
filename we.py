
"""
wallpapers.py
Generate 4 K (2160×3840) portrait wallpapers with PIL only.
pip install Pillow
"""

from pathlib import Path
from random import randint, uniform
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math
import colorsys

# -----------------------------------------------------------
# Parameters you can play with
# -----------------------------------------------------------
OUTPUT_DIR   = Path(__file__).resolve().parent
QUALITY      = 95        # JPEG quality

# Aurora colours (HSV tuples)  <── FIXED
AURORA_HUES  = [(0.33, 0.9, 1.0), (0.55, 0.9, 1.0), (0.1, 0.8, 1.0)]
WAVELENGTHS  = [600, 400, 320]                         # horizontal wave lengths
AMPLITUDES   = [250, 180, 120]                         # vertical amplitudes
ALPHA        = 180                                      # layer transparency

# Nebula palette (RGB)
NEBULA_COLS  = [(43, 0, 85), (75, 0, 130), (137, 0, 149),
                (255, 65, 108), (255, 177, 153)]

# Minimal ocean
OCEAN_TOP    = (0, 30, 60)     # deep blue
OCEAN_BOTTOM = (0, 180, 220)   # cyan
# -----------------------------------------------------------


def hsv_to_rgb_f(h, s, v):
    return tuple(round(x * 255) for x in colorsys.hsv_to_rgb(h, s, v))


def make_aurora_wallpaper():
    W, H = 2160, 3840
    base = Image.new("RGB", (W, H), (5, 5, 15))

    for hue, wl, amp in zip(AURORA_HUES, WAVELENGTHS, AMPLITUDES):
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw  = ImageDraw.Draw(layer)
        y0 = H // 2 + randint(-200, 200)
        points = []
        for x in range(0, W + 50, 50):
            y = y0 + int(amp * math.sin(2 * math.pi * x / wl))
            points.append((x, y))
        # Draw a filled polygon extending to bottom
        points += [(W, H), (0, H)]
        colour = hsv_to_rgb_f(*hue) + (ALPHA,)
        draw.polygon(points, fill=colour)
        layer = layer.filter(ImageFilter.GaussianBlur(120))
        base = Image.alpha_composite(base.convert("RGBA"), layer).convert("RGB")

    # Add subtle reflection on water
    mirror = base.transpose(Image.FLIP_TOP_BOTTOM).crop((0, 0, W, H // 2))
    mirror = ImageEnhance.Brightness(mirror).enhance(0.35)
    base.paste(mirror, (0, H // 2))
    base.save(OUTPUT_DIR / "aurora_4k.jpg", quality=QUALITY)


def make_nebula_wallpaper():
    W, H = 2160, 3840
    img = Image.new("RGB", (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(img, "RGBA")

    # Soft background nebula
    for _ in range(150):
        x = randint(-200, W + 200)
        y = randint(-200, H + 200)
        radius = randint(300, 900)
        col = NEBULA_COLS[randint(0, len(NEBULA_COLS) - 1)]
        alpha = randint(20, 80)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius],
                     fill=col + (alpha,))

    # Bright gas filaments
    for _ in range(60):
        x0, y0 = randint(0, W), randint(0, H)
        angle = uniform(0, 2 * math.pi)
        length = randint(200, 1000)
        x1 = x0 + length * math.cos(angle)
        y1 = y0 + length * math.sin(angle)
        width = randint(2, 10)
        col = NEBULA_COLS[randint(2, 4)]
        alpha = randint(100, 180)
        draw.line([(x0, y0), (x1, y1)], fill=col + (alpha,), width=width)

    # Stars
    for _ in range(2000):
        x, y = randint(0, W), randint(0, H)
        size = randint(1, 3)
        brightness = randint(180, 255)
        draw.ellipse([x, y, x + size, y + size],
                     fill=(brightness, brightness, brightness))

    img = img.filter(ImageFilter.GaussianBlur(1))
    img.save(OUTPUT_DIR / "nebula_4k.jpg", quality=QUALITY)


def make_minimal_ocean():
    W, H = 2160, 3840
    base = Image.new("RGB", (W, H))
    top = OCEAN_TOP
    bottom = OCEAN_BOTTOM
    for y in range(H):
        ratio = y / H
        r = int(top[0] * (1 - ratio) + bottom[0] * ratio)
        g = int(top[1] * (1 - ratio) + bottom[1] * ratio)
        b = int(top[2] * (1 - ratio) + bottom[2] * ratio)
        draw = ImageDraw.Draw(base)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    # Soft sun glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    cx, cy = W // 2, int(H * 0.28)
    for radius in range(200, 50, -5):
        alpha = max(0, 30 - (200 - radius) // 5)
        gdraw.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                      fill=(255, 255, 230, alpha))
    base = Image.alpha_composite(base.convert("RGBA"), glow).convert("RGB")
    base.save(OUTPUT_DIR / "minimal_ocean_4k.jpg", quality=QUALITY)


if __name__ == "__main__":
    print("Generating aurora wallpaper …")
    make_aurora_wallpaper()

    print("Generating nebula wallpaper …")
    make_nebula_wallpaper()

    print("Generating minimal ocean wallpaper …")
    make_minimal_ocean()

    print(f"Done! Check {OUTPUT_DIR.resolve()}")
