from PIL import Image, ImageDraw, ImageFilter
import random, math, os

WIDTH, HEIGHT = 2160, 3840
OUTPUT_DIR = "wallpapers"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def random_color(bright=True):
    if bright:
        return tuple(random.randint(100, 255) for _ in range(3))
    return tuple(random.randint(0, 150) for _ in range(3))

def save_image(img, name):
    img.save(f"{OUTPUT_DIR}/{name}.jpg", "JPEG", quality=95)

# 1. Minimal Gradient
def wallpaper_minimal_gradient():
    img = Image.new("RGB", (WIDTH, HEIGHT), "white")
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        r = int(100 + 100 * y / HEIGHT)
        g = int(150 + 50 * y / HEIGHT)
        b = 255
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))
    save_image(img, "minimal_gradient")

# 2. 3D Spheres
def wallpaper_3d_spheres():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(25):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        r = random.randint(100, 300)
        base_color = random_color()
        draw.ellipse([x - r, y - r, x + r, y + r], fill=base_color)
    img = img.filter(ImageFilter.GaussianBlur(4))
    save_image(img, "3d_spheres")

# 3. Cyberpunk Grid
def wallpaper_cyberpunk_grid():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for y in range(0, HEIGHT, 120):
        draw.line([(0, y), (WIDTH, y)], fill=(0, 255, 255), width=2)
    for x in range(0, WIDTH, 120):
        draw.line([(x, HEIGHT // 2), (x, HEIGHT)], fill=(255, 0, 255), width=2)
    save_image(img, "cyberpunk_grid")

# 4. Kawaii Pastel
def wallpaper_kawaii_pastel():
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 240, 250))
    draw = ImageDraw.Draw(img)
    for _ in range(100):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        r = random.randint(20, 100)
        color = random.choice([(255, 182, 193), (255, 192, 203), (255, 222, 173)])
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)
    save_image(img, "kawaii_pastel")

# 5. Synthwave Sun
def wallpaper_synthwave_sun():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    # Sun
    draw.ellipse([WIDTH//4, HEIGHT//3, 3*WIDTH//4, 3*HEIGHT//5], fill=(255, 100, 0))
    # Lines
    for i in range(20):
        y = HEIGHT//2 + i * 50
        draw.line([(0, y), (WIDTH, y)], fill=(255, 0, 255), width=1)
    save_image(img, "synthwave_sun")

# 6. Neon Geometrics
def wallpaper_neon_geometrics():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(40):
        x1 = random.randint(0, WIDTH)
        y1 = random.randint(0, HEIGHT)
        x2 = x1 + random.randint(-300, 300)
        y2 = y1 + random.randint(-300, 300)
        draw.line([(x1, y1), (x2, y2)], fill=random_color(), width=3)
    img = img.filter(ImageFilter.GaussianBlur(1))
    save_image(img, "neon_geometrics")

# 7. Abstract Nature Blend
def wallpaper_nature_blend():
    img = Image.new("RGB", (WIDTH, HEIGHT), random_color(False))
    draw = ImageDraw.Draw(img)
    for i in range(100):
        r = random.randint(20, 200)
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        color = random.choice([(50, 150, 50), (100, 200, 150), (50, 200, 100)])
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)
    img = img.filter(ImageFilter.BLUR)
    save_image(img, "abstract_nature_blend")

# 8. Tech Circuits
def wallpaper_tech_circuits():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        w = random.randint(40, 120)
        h = random.randint(10, 40)
        color = random.choice([(0,255,0), (0,200,255), (255,255,0)])
        draw.rectangle([x, y, x+w, y+h], outline=color, width=2)
    save_image(img, "tech_circuits")

# 9. AMOLED Art
def wallpaper_amoled_art():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(30):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        r = random.randint(50, 200)
        color = random_color()
        draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=3)
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    save_image(img, "amoled_art")

# 10. Glitch Grid
def wallpaper_glitch_grid():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for y in range(0, HEIGHT, 100):
        glitch_color = random_color()
        draw.line([(0, y), (WIDTH, y)], fill=glitch_color, width=3)
    for x in range(0, WIDTH, 100):
        draw.line([(x, 0), (x, HEIGHT)], fill=random_color(), width=2)
    save_image(img, "glitch_grid")

# Generate all wallpapers
wallpaper_minimal_gradient()
wallpaper_3d_spheres()
wallpaper_cyberpunk_grid()
wallpaper_kawaii_pastel()
wallpaper_synthwave_sun()
wallpaper_neon_geometrics()
wallpaper_nature_blend()
wallpaper_tech_circuits()
wallpaper_amoled_art()
wallpaper_glitch_grid()
