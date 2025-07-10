
from PIL import Image, ImageDraw
import cv2
import numpy as np

# Create a blank 4K canvas
width, height = 3840, 2160
image = Image.new("RGB", (width, height), "#000000")
draw = ImageDraw.Draw(image)

# Create a radial gradient using numpy
def radial_gradient(center_color, edge_color):
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    xx, yy = np.meshgrid(x, y)
    radius = np.sqrt(xx**2 + yy**2)
    radius = radius / radius.max()

    r = center_color[0] * (1 - radius) + edge_color[0] * radius
    g = center_color[1] * (1 - radius) + edge_color[1] * radius
    b = center_color[2] * (1 - radius) + edge_color[2] * radius

    gradient = np.stack([r, g, b], axis=-1).astype(np.uint8)
    return gradient

# Apply gradient
gradient = radial_gradient((30, 144, 255), (0, 0, 0))  # DodgerBlue to black
gradient_img = Image.fromarray(gradient, 'RGB')

# Overlay some abstract circles for flair
draw = ImageDraw.Draw(gradient_img)
for i in range(10):
    radius = np.random.randint(100, 400)
    x = np.random.randint(0, width)
    y = np.random.randint(0, height)
    color = tuple(np.random.randint(100, 255, size=3))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline=None)

# Convert to OpenCV format for final touches
final_img = cv2.cvtColor(np.array(gradient_img), cv2.COLOR_RGB2BGR)

# Optionally apply Gaussian Blur for a smooth feel
final_img = cv2.GaussianBlur(final_img, (21, 21), 0)

# Save in HD JPEG format
cv2.imwrite("stunning_wallpaper_4k.jpg", final_img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
