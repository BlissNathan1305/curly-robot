
from PIL import Image, ImageDraw
import cv2
import numpy as np
import os

# Mobile wallpaper dimensions (Portrait)
width, height = 2160, 3840
output_dir = "mobile_wallpapers"
os.makedirs(output_dir, exist_ok=True)

def create_gradient_image(start_color, end_color, style="radial"):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    xx, yy = np.meshgrid(x, y)

    if style == "radial":
        r = np.sqrt(xx**2 + yy**2)
        r = r / r.max()
    elif style == "linear":
        r = (yy + 1) / 2
    else:
        r = np.random.rand(height, width)

    red = start_color[0] * (1 - r) + end_color[0] * r
    green = start_color[1] * (1 - r) + end_color[1] * r
    blue = start_color[2] * (1 - r) + end_color[2] * r

    gradient = np.stack([red, green, blue], axis=-1).astype(np.uint8)
    return gradient

# Definitions of styles
styles = [
    ((30, 144, 255), (0, 0, 0), "radial"),        # DodgerBlue to black
    ((255, 140, 0), (75, 0, 130), "linear"),      # Sunset tones
    ((50, 205, 50), (255, 255, 255), "radial"),   # Lime to white
    ((255, 0, 150), (0, 0, 255), "linear"),       # Neon pink to blue
    ((255, 255, 200), (100, 149, 237), "radial"), # Pastel to cornflower
    ((0, 0, 0), (200, 200, 200), "linear"),       # Minimal dark to light
]

for i, (start, end, style) in enumerate(styles):
    gradient_img = create_gradient_image(start, end, style)
    img = Image.fromarray(gradient_img)

    draw = ImageDraw.Draw(img)

    # Add some abstract shapes (optional flair)
    for _ in range(12):
        radius = np.random.randint(80, 300)
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        color = tuple(np.random.randint(100, 255, size=3))
        draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color)

    # Convert to OpenCV for blur & save
    cv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv_img = cv2.GaussianBlur(cv_img, (17, 17), 0)
    filename = f"{output_dir}/mobile_wallpaper_{i+1}.jpg"
    cv2.imwrite(filename, cv_img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

print("✅ 6 stunning mobile wallpapers saved to:", output_dir)
