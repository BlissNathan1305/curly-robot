from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from random import randint, uniform, choice
import math, colorsys

OUTPUT_DIR = Path(__file__).resolve().parent
QUALITY    = 95

# 4-sand-dunes at dawn
# -----------------------------------------------------------
def make_dunes_wallpaper():
    W, H = 2160, 3840
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)

    # sky gradient (night → dawn)
    for y in range(H // 2):
        ratio = y / (H // 2)
        r = int(20 * (1 - ratio) + 255 * ratio)
        g = int(10 * (1 - ratio) + 180 * ratio)
        b = int(40 * (1 - ratio) + 120 * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # sand dunes with soft curves
    base_y = H * 0.55
    for i in range(6):
        amp = 180 - i * 25
        wl = 700 + i * 120
        y_shift = i * 70
        ridge = []
        for x in range(0, W + 50, 50):
            y = base_y + y_shift + int(amp * math.sin(2 * math.pi * x / wl))
            ridge.append((x, y))
        ridge += [(W, H), (0, H)]
        shade = 200 - i * 30
        draw.polygon(ridge, fill=(shade, int(shade * 0.75), int(shade * 0.55)))

    # low sun disc
    sun = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(sun)
    cx, cy = W // 2, int(H * 0.42)
    for r in range(120, 0, -2):
        alpha = max(0, 90 - r)
        sdraw.ellipse([cx - r, cy - r, cx + r, cy + r],
                      fill=(255, 220, 180, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), sun).convert("RGB")
    img.save(OUTPUT_DIR / "sand_dunes_dawn_4k.jpg", quality=QUALITY)


# -----------------------------------------------------------
# 5. Crystal geode macro
# -----------------------------------------------------------
def make_geode_wallpaper():
    W, H = 2160, 3840
    img = Image.new("RGB", (W, H), (25, 15, 45))
    draw = ImageDraw.Draw(img, "RGBA")

    # outer rock shell
    margin = 400
    shell = [(margin, margin), (W - margin, H - margin)]
    draw.ellipse(shell, fill=(45, 40, 55))

    # inner cavity
    cavity = [(margin + 200, margin + 200), (W - margin - 200, H - margin - 200)]
    draw.ellipse(cavity, fill=(65, 55, 100))

    # crystal facets
    hues = [0.75, 0.82, 0.9]  # purple → violet → magenta
    for _ in range(300):
        x = randint(margin + 250, W - margin - 250)
        y = randint(margin + 250, H - margin - 250)
        size = randint(8, 35)
        angle = uniform(0, 2 * math.pi)
        dx = size * math.cos(angle)
        dy = size * math.sin(angle)
        rgb = colorsys.hsv_to_rgb(choice(hues), uniform(0.7, 1), uniform(0.8, 1))
        col = tuple(round(c * 255) for c in rgb) + (randint(150, 255),)
        draw.polygon([(x, y), (x + dx, y + dy),
                      (x - dy, y + dx), (x + dy, y - dx)], fill=col)

    img = img.filter(ImageFilter.GaussianBlur(0.8))
    img.save(OUTPUT_DIR / "crystal_geode_4k.jpg", quality=QUALITY)


# -----------------------------------------------------------
# 6. Northern-lights lake mirror
# -----------------------------------------------------------
def make_lights_lake_wallpaper():
    W, H = 2160, 3840
    img = Image.new("RGB", (W, H), (5, 5, 15))
    draw = ImageDraw.Draw(img, "RGBA")

    # starfield
    for _ in range(2500):
        x, y = randint(0, W), randint(0, H // 2)
        size = randint(1, 2)
        b = randint(200, 255)
        draw.ellipse([x, y, x + size, y + size], fill=(b, b, b))

    # aurora arcs
    cols = [(0.50, 1.0, 1.0), (0.55, 1.0, 1.0), (0.10, 0.9, 1.0)]
    for hue, wl, amp in zip(cols, [500, 350, 250], [300, 220, 150]):
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ldraw = ImageDraw.Draw(layer)
        y0 = H * 0.25
        pts = []
        for x in range(0, W + 50, 50):
            y = y0 + int(amp * math.sin(2 * math.pi * x / wl))
            pts.append((x, y))
        pts += [(W, H // 2), (0, H // 2)]
        rgb = tuple(round(c * 255) for c in colorsys.hsv_to_rgb(*hue)) + (100,)
        ldraw.polygon(pts, fill=rgb)
        layer = layer.filter(ImageFilter.GaussianBlur(90))
        img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")

    # perfect lake mirror
    lake = img.crop((0, 0, W, H // 2)).transpose(Image.FLIP_TOP_BOTTOM)
    lake = ImageEnhance.Brightness(lake).enhance(0.6)
    img.paste(lake, (0, H // 2))
    img.save(OUTPUT_DIR / "northern_lights_lake_4k.jpg", quality=QUALITY)


# -----------------------------------------------------------
# Add these calls to __main__ if you want them in the same run
# -----------------------------------------------------------
if __name__ == "__main__":
    print("Generating sand-dunes wallpaper …")
    make_dunes_wallpaper()

    print("Generating crystal geode wallpaper …")
    make_geode_wallpaper()

    print("Generating northern-lights lake wallpaper …")
    make_lights_lake_wallpaper()

    print(f"Done! Check {OUTPUT_DIR.resolve()}")
