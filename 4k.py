
from PIL import Image, ImageDraw
import numpy as np

# Define 4K resolution for portrait mobile wallpaper
width, height = 2160, 3840

# Create a vertical gradient background using NumPy
gradient = np.linspace(0, 255, height, dtype=np.uint8)
gradient = np.tile(gradient, (width, 1)).T

# Create an RGB image with a custom gradient
background = np.zeros((height, width, 3), dtype=np.uint8)
background[:, :, 0] = gradient  # Red channel
background[:, :, 1] = 100 + gradient // 2  # Green channel
background[:, :, 2] = 255 - gradient  # Blue channel

# Convert NumPy array to PIL Image
background_img = Image.fromarray(background)

# Draw abstract circles for a stunning effect
draw = ImageDraw.Draw(background_img)
for i in range(50, 1000, 100):
    draw.ellipse(
        (width//2 - i, height//2 - i, width//2 + i, height//2 + i),
        outline=(255, 255, 255)
    )

# Save as high-quality JPEG
background_img.save("stunning_wallpaper_4k.jpg", "JPEG", quality=95)

