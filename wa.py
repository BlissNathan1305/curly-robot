
from PIL import Image, ImageDraw
import numpy as np
import cv2
import os

# Define 4K mobile dimensions (portrait)
WIDTH, HEIGHT = 2160, 3840

# Create output directory
os.makedirs("wallpapers", exist_ok=True)

def generate_gradient_background():
    """Create a vertical gradient using NumPy and OpenCV."""
    top_color = np.array([255, 100, 100], dtype=np.uint8)     # Light red
    bottom_color = np.array([50, 0, 100], dtype=np.uint8)     # Deep purple

    # Create a linear gradient between the two colors
    gradient = np.linspace(top_color, bottom_color, HEIGHT).astype(np.uint8)
    gradient = np.tile(gradient[:, np.newaxis, :], (1, WIDTH, 1))

    return gradient

def overlay_shapes(pil_img):
    """Draw some shapes on top using PIL."""
    draw = ImageDraw.Draw(pil_img)

    # Draw a few translucent circles
    for i in range(10):
        x = np.random.randint(0, WIDTH)
        y = np.random.randint(0, HEIGHT)
        radius = np.random.randint(200, 500)
        color = (255, 255, 255, 40)  # White translucent

        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)

    return pil_img

def save_wallpaper():
    # Step 1: Create gradient background
    background_np = generate_gradient_background()

    # Step 2: Convert NumPy to PIL image
    image_pil = Image.fromarray(background_np)

    # Step 3: Draw shapes using PIL
    final_image = overlay_shapes(image_pil)

    # Step 4: Save as high-quality JPEG
    output_path = "wallpapers/wallpaper_4k_mobile.jpg"
    final_image.save(output_path, format="JPEG", quality=95, optimize=True)

    print(f"Wallpaper saved at: {output_path}")

# Generate the wallpaper
save_wallpaper()
