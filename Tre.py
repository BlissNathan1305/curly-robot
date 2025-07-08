from PIL import Image, ImageDraw, ImageFilter
import random, os, math

WIDTH, HEIGHT = 2160, 3840
os.makedirs("wallpapers", exist_ok=True)

def save(img, name):
    img.save(f"wallpapers/{name}.jpg", "JPEG", quality=95)

def random_color(bright=True):
    return tuple(random.randint(128, 255) if bright else random.randint(0, 100) for _ in range(3))

# 1. Minimal Gradient
def minimal_gradient():
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        color = (
            int(100 + 155 * ratio),
            int(120 + 100 * ratio),
            int(180 + 75 * ratio)
        )
        draw.line([(0, y), (WIDTH, y)], fill=color)
    save(img, "1_minimal_gradient")

# 2. 3D Sphere Illusion
def sphere_illusion():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(30):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        r = random.randint(80, 300)
        c = random_color()
        draw.ellipse([x - r, y - r, x + r, y + r], fill=c)
    img = img.filter(ImageFilter.GaussianBlur(4))
    save(img, "2_sphere_illusion")

# 3. Cyberpunk Grid
def cyberpunk_grid():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for y in range(0, HEIGHT, 100):
        draw.line([(0, y), (WIDTH, y)], fill=(255, 0, 255), width=2)
    for x in range(0, WIDTH, 100):
        draw.line([(x, HEIGHT // 2), (x, HEIGHT)], fill=(0, 255, 255), width=2)
    save(img, "3_cyberpunk_grid")

# 4. Kawaii Pastel
def kawaii_pastel():
    img = Image.new("RGB", (WIDTH, HEIGHT), (255, 240, 250))
    draw = ImageDraw.Draw(img)
    pastel_colors = [(255, 182, 193), (255, 192, 203), (255, 222, 173)]
    for _ in range(100):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        r = random.randint(30, 80)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=random.choice(pastel_colors))
    save(img, "4_kawaii_pastel")

# 5. Synthwave Sun
def synthwave_sun():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    draw.ellipse([WIDTH//4, HEIGHT//3, 3*WIDTH//4, HEIGHT//2], fill=(255, 100, 0))
    for i in range(20):
        y = HEIGHT//2 + i * 50
        draw.line([(0, y), (WIDTH, y)], fill=(255, 0, 255), width=1)
    save(img, "5_synthwave_sun")

# 6. Neon Geometrics
def neon_geometrics():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    neon = [(255, 0, 255), (0, 255, 255), (255, 255, 0)]
    for _ in range(40):
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x2 = x1 + random.randint(-300, 300)
        y2 = y1 + random.randint(-300, 300)
        draw.line([x1, y1, x2, y2], fill=random.choice(neon), width=3)
    img = img.filter(ImageFilter.GaussianBlur(1))
    save(img, "6_neon_geometrics")

# 7. Abstract Nature Blend
def nature_blend():
    img = Image.new("RGB", (WIDTH, HEIGHT), random_color(False))
    draw = ImageDraw.Draw(img)
    for _ in range(100):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        r = random.randint(40, 120)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=random_color(False))
    img = img.filter(ImageFilter.BLUR)
    save(img, "7_nature_blend")

# 8. Tech Circuits
def tech_circuits():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(200):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        w, h = random.randint(30, 120), random.randint(10, 40)
        color = random.choice([(0,255,0), (0,200,255), (255,255,0)])
        draw.rectangle([x, y, x+w, y+h], outline=color, width=2)
    save(img, "8_tech_circuits")

# 9. Dark AMOLED Art
def amoled_art():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for _ in range(25):
        x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        r = random.randint(60, 200)
        draw.ellipse([x - r, y - r, x + r, y + r], outline=random_color(), width=3)
    img = img.filter(ImageFilter.GaussianBlur(0.5))
    save(img, "9_amoled_art")

# 10. Glitch Grid
def glitch_grid():
    img = Image.new("RGB", (WIDTH, HEIGHT), "black")
    draw = ImageDraw.Draw(img)
    for y in range(0, HEIGHT, 80):
        draw.line([(0, y), (WIDTH, y)], fill=random_color(), width=3)
    for x in range(0, WIDTH, 80):
        draw.line([(x, 0), (x, HEIGHT)], fill=random_color(), width=2)
    save(img, "10_glitch_grid")

# Generate all 10 wallpapers
minimal_gradient()
sphere_illusion()
cyberpunk_grid()
kawaii_pastel()
synthwave_sun()
neon_geometrics()
nature_blend()
tech_circuits()
amoled_art()
glitch_grid()
