import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2

# Define the resolution for 4K
width, height = 3840, 2160

# Create a blank image with a gradient background
def create_gradient_background(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            img[y, x] = (x % 256, y % 256, 255 - (x + y) % 256)
    return img

# Add some text to the image
def add_text_to_image(image, text, font_path, font_size, text_color, position):
    img_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=text_color)
    return np.array(img_pil)

# Create the gradient background
background = create_gradient_background(width, height)

# Add text to the image
font_path = "arial.ttf"  # You can use any TrueType font file available on your system
text = "Beautiful Wallpaper"
font_size = 100
text_color = (255, 255, 255)
position = (100, 100)
wallpaper = add_text_to_image(background, text, font_path, font_size, text_color, position)

# Save the wallpaper as a 4K JPEG
output_path = "beautiful_wallpaper_4k.jpg"
cv2.imwrite(output_path, wallpaper)

print(f"Wallpaper saved as {output_path}")
