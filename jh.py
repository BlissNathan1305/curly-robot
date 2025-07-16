
from PIL import Image, ImageDraw, ImageFilter
import random

# Set dimensions for 4K wallpaper (3840 x 2160)
width, height = 3840, 2160

# Create a new image with a black background
img = Image.new('RGB', (width, height), (0, 0, 0))

# Draw stars
draw = ImageDraw.Draw(img)
for _ in range(1000):
    x = random.randint(0, width)
    y = random.randint(0, height)
    draw.point((x, y), fill=(255, 255, 255))

# Add a nebula
nebula = Image.new('RGB', (width, height), (0, 0, 0))
nebula_draw = ImageDraw.Draw(nebula)
nebula_draw.ellipse([(width // 2 - 500, height // 2 - 500), (width // 2 + 500, height // 2 + 500)], fill=(255, 0, 255))
nebula = nebula.filter(ImageFilter.GaussianBlur(radius=100))
img = Image.blend(img, nebula, 0.2)

# Save the image in 4K JPEG format
img.save('galaxy_wallpaper.jpg', 'JPEG', quality=95)
