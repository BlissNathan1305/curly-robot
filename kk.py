
from PIL import Image, ImageDraw, ImageFilter, ImageMath
import random
import math

def generate_geometric_wallpaper(width=2160, height=3840, filename="geometric_wallpaper.jpg", noise_level=0.1, pattern_density=0.05, pattern_shape="triangle"):
    """
    Generates a 4K geometric wallpaper with noise.

    Args:
        width: Width of the wallpaper (default: 2160, 4K mobile).
        height: Height of the wallpaper (default: 3840, 4K mobile).
        filename: Filename to save the wallpaper (default: "geometric_wallpaper.jpg").
        noise_level: Amount of noise (0.0 to 1.0, default: 0.1).
        pattern_density: Density of the geometric pattern (0.0 to 1.0, default: 0.05).  Higher = more shapes.
        pattern_shape: Shape of the pattern ("triangle", "circle", "square", "hexagon", default: "triangle").
    """

    # 1. Create a base image with a gradient background
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)

    # Define gradient colors (you can customize these)
    color1 = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))  # Darker base
    color2 = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255)) # Lighter top

    # Create a simple vertical gradient
    for i in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * i / height)
        g = int(color1[1] + (color2[1] - color1[1]) * i / height)
        b = int(color1[2] + (color2[2] - color1[2]) * i / height)
        draw.line((0, i, width, i), fill=(r, g, b))


    # 2. Add Geometric Pattern
    num_shapes = int(width * height * pattern_density)
    for _ in range(num_shapes):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(20, 150) # Adjust size range as needed
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        alpha = random.randint(50, 150) # Transparency

        # Create a transparent layer for the shape
        shape_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        shape_draw = ImageDraw.Draw(shape_img)

        if pattern_shape == "triangle":
            points = [(x, y - size // 2), (x - size // 2, y + size // 2), (x + size // 2, y + size // 2)]
            shape_draw.polygon(points, fill=color + (alpha,))
        elif pattern_shape == "circle":
            shape_draw.ellipse((x - size // 2, y - size // 2, x + size // 2, y + size // 2), fill=color + (alpha,))
        elif pattern_shape == "square":
            shape_draw.rectangle((x - size // 2, y - size // 2, x + size // 2, y + size // 2), fill=color + (alpha,))
        elif pattern_shape == "hexagon":
            # Calculate hexagon vertices
            vertices = []
            for i in range(6):
                angle = 2 * math.pi / 6 * i
                vertex_x = x + size // 2 * math.cos(angle)
                vertex_y = y + size // 2 * math.sin(angle)
                vertices.append((vertex_x, vertex_y))
            shape_draw.polygon(vertices, fill=color + (alpha,))
        else:
            print(f"Warning: Unknown pattern shape: {pattern_shape}.  Using triangle instead.")
            points = [(x, y - size // 2), (x - size // 2, y + size // 2), (x + size // 2, y + size // 2)]
            shape_draw.polygon(points, fill=color + (alpha,))

        # Overlay the transparent shape onto the base image
        img = Image.alpha_composite(img.convert("RGBA"), shape_img)  #Convert base image to RGBA



    # 3. Add Noise
    if noise_level > 0:
        noise_img = Image.new("L", (width, height))  # Grayscale noise
        for i in range(width):
            for j in range(height):
                noise = int(random.gauss(0, 255 * noise_level)) # Gaussian noise
                noise = max(0, min(255, noise))  # Clamp to 0-255
                noise_img.putpixel((i, j), noise)


        # Blend the noise with the image using ImageMath
        img = ImageMath.eval("a + b", a=img.convert("L"), b=noise_img).convert("RGB") # convert to grayscale then add noise then convert back to RGB

    # 4. Apply a subtle blur (optional) - can improve noise appearance
    img = img.filter(ImageFilter.GaussianBlur(radius=1))


    # 5. Save the image
    img.save(filename, "JPEG", quality=95)  # High quality JPEG

    print(f"Wallpaper generated and saved as {filename}")

if __name__ == "__main__":
    # Example usage:
    generate_geometric_wallpaper(filename="my_wallpaper.jpg", noise_level=0.08, pattern_density=0.03, pattern_shape="hexagon")
    #generate_geometric_wallpaper(filename="my_wallpaper2.jpg", noise_level=0.12, pattern_density=0.04, pattern_shape="circle")  # Try with different parameters!
    #generate_geometric_wallpaper(filename="my_wallpaper3.jpg", noise_level=0.05, pattern_density=0.06, pattern_shape="square")
    #generate_geometric_wallpaper(filename="my_wallpaper4.jpg", noise_level=0.1, pattern_density=0.02, pattern_shape="triangle")
