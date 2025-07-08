
from PIL import Image, ImageDraw
import numpy as np
import cv2
import os
import random

# 4K portrait dimensions for mobile
WIDTH, HEIGHT = 2160, 3840

# Output directory
os.makedirs("wallpapers", exist_ok=True)

def generate_base_gradient():
    """Create a vertical gradient background using NumPy and OpenCV."""
    top = np.array([random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)], dtype=np.uint8)
    bottom = np.array([random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)], dtype=np.uint8)

    gradient = np.linspace(top, bottom, HEIGHT).astype(np.uint8)
    gradient = np.tile(gradient[:, np.newaxis, :], (1, WIDTH, 1))

    return gradient

def draw_geometric_shapes(image_pil):
    """Overlay random geometric shapes using PIL."""
    draw = ImageDraw.Draw(image_pil)

    for _ in range(100):
        shape_type = random.choice(["circle", "rectangle", "triangle"])
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        size = random.randint(100, 500)
        x2, y2 = x1 + size, y1 + size
        color = tuple([random.randint(100, 255) for _ in range(3)] + [random.randint(40, 120)])

        if shape_type == "circle":
            draw.ellipse((x1, y1, x2, y2), fill=color)
        elif shape_type == "rectangle":
            draw.rectangle((x1, y1, x2, y2), fill=color)
        elif shape_type == "triangle":
            draw.polygon([(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)], fill=color)

    return image_pil

def generate_geometric_wallpaper():
    # Step 1: Create gradient background using NumPy + OpenCV
    gradient_np = generate_base_gradient()

    # Step 2: Convert NumPy image (BGR) to RGB for PIL
    rgb_image = cv2.cvtColor(gradient_np, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(rgb_image).convert("RGBA")

    # Step 3: Draw geometric shapes on top
    final_image = draw_geometric_shapes(pil_image)

    # Step 4: Convert back to RGB (remove alpha) and save as JPEG
    final_image_rgb = final_image.convert("RGB")
    output_path = "wallpapers/geometric_wallpaper_4k.jpg"
    final_image_rgb.save(output_path, format="JPEG", quality=95, optimize=True)

    print(f"Wallpaper saved at: {output_path}")

# Run the wallpaper generator
generate_geometric_wallpaper()
