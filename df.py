
from PIL import Image, ImageDraw
import numpy as np
import random

# Image settings for mobile (portrait 4K)
width, height = 2160, 3840  # Optimized for mobile 9:16 aspect ratio
image = Image.new("RGB", (width, height), (0, 0, 0))
draw = ImageDraw.Draw(image, "RGBA")  # RGBA for translucent shapes

# Create a cosmic gradient background
def create_gradient_background():
    pixels = image.load()
    for y in range(height):
        t = y / height
        r = int(20 + t * (100 - 20))   # Indigo to purple
        g = int(10 + t * (50 - 10))
        b = int(50 + t * (200 - 50))
        for x in range(width):
            pixels[x, y] = (r, g, b)

# Add subtle noise texture for depth
def add_noise():
    noise = np.random.randint(-15, 15, (height, width, 3), dtype=np.int32)
    pixels = np.array(image)
    pixels = np.clip(pixels + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(pixels)

# Draw fluid wave patterns and glowing orbs
def draw_shapes():
    # Fluid waves
    for _ in range(8):
        points = []
        for x in range(0, width, 50):
            y = height // 2 + int(400 * np.sin(x / 150 + random.random() * 3))
            y += int(200 * np.cos(x / 200 + random.random() * 2))
            points.append((x, y))
        draw.line(points, fill=(100, 200, 255, 90), width=30, joint="curve")

    # Glowing orbs
    for _ in range(15):
        x = random.randint(100, width - 100)
        y = random.randint(200, height - 200)
        radius = random.randint(50, 150)
        # Inner glow (smaller, brighter)
        draw.ellipse(
            [x - radius // 2, y - radius // 2, x + radius // 2, y + radius // 2],
            fill=(255, 150, 200, 150)  # Neon pink glow
        )
        # Outer glow (larger, translucent)
        draw.ellipse(
            [x - radius, y - radius, x + radius, y + radius],
            fill=(100, 200, 255, 50)  # Neon blue outer glow
        )

# Generate the wallpaper
create_gradient_background()
image = add_noise()  # Reassign image after noise
draw = ImageDraw.Draw(image, "RGBA")  # Update draw object
draw_shapes()

# Save the image
image.save("mobile_wallpaper_4k.jpg", "JPEG", quality=95)
print("Wallpaper saved as mobile_wallpaper_4k.jpg")
