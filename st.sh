#!/bin/bash
echo "Press Enter to start the stopwatch."
read
start_time=$(date +%s)

echo "Stopwatch started... Press Enter to stop."
read
end_time=$(date +%s)

elapsed=$(( end_time - start_time ))
echo "Elapsed time: $elapsed seconds"
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import math
import random
import os

class WallpaperGenerator:
    def __init__(self):
        # 4K mobile dimensions (portrait orientation)
        self.width = 2160
        self.height = 3840
        self.output_dir = "wallpapers"
        os.makedirs(self.output_dir, exist_ok=True)
    
    def save_wallpaper(self, image, filename):
        """Save wallpaper as high-quality JPEG"""
        filepath = os.path.join(self.output_dir, f"{filename}.jpg")
        image.save(filepath, "JPEG", quality=95, optimize=True)
        print(f"Saved: {filepath}")
    
    def create_gradient_wallpaper(self, color1, color2, direction="vertical", name="gradient"):
        """Create smooth gradient wallpaper"""
        image = Image.new("RGB", (self.width, self.height))
        draw = ImageDraw.Draw(image)
        
        if direction == "vertical":
            for y in range(self.height):
                ratio = y / self.height
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                draw.rectangle([(0, y), (self.width, y + 1)], fill=(r, g, b))
        else:  # horizontal
            for x in range(self.width):
                ratio = x / self.width
                r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
                g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
                b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
                draw.rectangle([(x, 0), (x + 1, self.height)], fill=(r, g, b))
        
        # Add subtle noise for texture
        noise = np.random.normal(0, 3, (self.height, self.width, 3))
        img_array = np.array(image)
        img_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        image = Image.fromarray(img_array)
        
        self.save_wallpaper(image, name)
        return image
    
    def create_geometric_pattern(self, name="geometric"):
        """Create abstract geometric pattern"""
        image = Image.new("RGB", (self.width, self.height), (20, 20, 30))
        draw = ImageDraw.Draw(image)
        
        # Background gradient
        for y in range(self.height):
            ratio = y / self.height
            color = (
                int(20 + 40 * ratio),
                int(20 + 60 * ratio),
                int(30 + 80 * ratio)
            )
            draw.rectangle([(0, y), (self.width, y + 1)], fill=color)
        
        # Add geometric shapes
        colors = [
            (255, 100, 150, 100),  # Semi-transparent pink
            (100, 255, 200, 120),  # Semi-transparent cyan
            (255, 200, 100, 80),   # Semi-transparent orange
            (150, 100, 255, 110),  # Semi-transparent purple
        ]
        
        # Create overlay for transparency
        overlay = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
        overlay_draw = ImageDraw.Draw(overlay)
        
        for _ in range(20):
            color = random.choice(colors)
            shape_type = random.choice(["circle", "rectangle", "triangle"])
            
            if shape_type == "circle":
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                radius = random.randint(100, 400)
                overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], fill=color)
            
            elif shape_type == "rectangle":
                x1 = random.randint(0, self.width//2)
                y1 = random.randint(0, self.height//2)
                x2 = x1 + random.randint(200, 600)
                y2 = y1 + random.randint(200, 800)
                overlay_draw.rectangle([x1, y1, x2, y2], fill=color)
            
            elif shape_type == "triangle":
                x1 = random.randint(0, self.width)
                y1 = random.randint(0, self.height)
                points = [
                    (x1, y1),
                    (x1 + random.randint(-300, 300), y1 + random.randint(-300, 300)),
                    (x1 + random.randint(-300, 300), y1 + random.randint(-300, 300))
                ]
                overlay_draw.polygon(points, fill=color)
        
        # Composite images
        image = image.convert("RGBA")
        image = Image.alpha_composite(image, overlay)
        image = image.convert("RGB")
        
        # Apply blur for smooth effect
        image = image.filter(ImageFilter.GaussianBlur(radius=2))
        
        self.save_wallpaper(image, name)
        return image
    
    def create_wave_pattern(self, name="waves"):
        """Create flowing wave pattern"""
        # Create base image
        img_array = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        # Generate wave pattern
        for y in range(self.height):
            for x in range(self.width):
                # Multiple wave frequencies
                wave1 = math.sin(x * 0.01 + y * 0.005) * 50
                wave2 = math.sin(x * 0.005 + y * 0.01) * 30
                wave3 = math.sin(x * 0.002 + y * 0.008) * 70
                
                # Combine waves
                combined = wave1 + wave2 + wave3
                
                # Create color based on wave
                r = int(100 + combined * 0.8)
                g = int(50 + combined * 1.2)
                b = int(150 + combined * 0.6)
                
                # Clamp values
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))
                
                img_array[y, x] = [r, g, b]
        
        # Apply Gaussian blur for smooth effect
        img_array = cv2.GaussianBlur(img_array, (15, 15), 0)
        
        # Convert to PIL and enhance
        image = Image.fromarray(img_array)
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.3)
        
        self.save_wallpaper(image, name)
        return image
    
    def create_abstract_art(self, name="abstract"):
        """Create abstract art wallpaper"""
        image = Image.new("RGB", (self.width, self.height), (10, 10, 20))
        
        # Convert to numpy for OpenCV operations
        img_array = np.array(image)
        
        # Create multiple color layers
        layers = []
        colors = [
            (255, 50, 100),   # Red-pink
            (50, 255, 150),   # Green-cyan
            (100, 50, 255),   # Blue-purple
            (255, 200, 50),   # Yellow-orange
        ]
        
        for color in colors:
            layer = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            
            # Create random blobs
            for _ in range(5):
                center_x = random.randint(0, self.width)
                center_y = random.randint(0, self.height)
                
                # Create blob using circles with varying radii
                for radius in range(50, 300, 20):
                    alpha = 1.0 - (radius / 300.0)
                    cv2.circle(layer, (center_x, center_y), radius, 
                             (int(color[0] * alpha), int(color[1] * alpha), int(color[2] * alpha)), -1)
            
            # Blur the layer
            layer = cv2.GaussianBlur(layer, (101, 101), 0)
            layers.append(layer)
        
        # Blend layers
        for layer in layers:
            img_array = cv2.addWeighted(img_array, 0.7, layer, 0.3, 0)
        
        # Convert back to PIL
        image = Image.fromarray(img_array)
        
        # Add final enhancement
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(1.4)
        
        self.save_wallpaper(image, name)
        return image
    
    def create_cosmic_wallpaper(self, name="cosmic"):
        """Create cosmic/space-themed wallpaper"""
        # Start with dark space background
        image = Image.new("RGB", (self.width, self.height), (5, 5, 15))
        img_array = np.array(image)
        
        # Add stars
        for _ in range(1000):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            brightness = random.randint(150, 255)
            img_array[y, x] = [brightness, brightness, brightness]
        
        # Add nebula-like clouds
        for _ in range(3):
            center_x = random.randint(200, self.width - 200)
            center_y = random.randint(200, self.height - 200)
            
            # Create nebula colors
            colors = [
                (255, 100, 150),  # Pink
                (100, 150, 255),  # Blue
                (150, 100, 255),  # Purple
                (255, 150, 100),  # Orange
            ]
            
            color = random.choice(colors)
            
            # Create nebula effect
            nebula = np.zeros((self.height, self.width, 3), dtype=np.uint8)
            
            for radius in range(100, 400, 30):
                alpha = 1.0 - (radius / 400.0)
                cv2.circle(nebula, (center_x, center_y), radius,
                         (int(color[0] * alpha), int(color[1] * alpha), int(color[2] * alpha)), -1)
            
            # Heavy blur for nebula effect
            nebula = cv2.GaussianBlur(nebula, (151, 151), 0)
            
            # Blend with main image
            img_array = cv2.addWeighted(img_array, 0.8, nebula, 0.2, 0)
        
        # Convert to PIL and enhance
        image = Image.fromarray(img_array)
        
        # Add some noise for texture
        noise = np.random.normal(0, 5, (self.height, self.width, 3))
        img_array = np.array(image)
        img_array = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        image = Image.fromarray(img_array)
        
        self.save_wallpaper(image, name)
        return image
    
    def generate_all_wallpapers(self):
        """Generate all wallpaper types"""
        print("Generating 4K mobile wallpapers...")
        
        # Gradient wallpapers
        self.create_gradient_wallpaper((255, 100, 150), (100, 50, 255), "vertical", "gradient_pink_purple")
        self.create_gradient_wallpaper((50, 255, 200), (255, 100, 50), "vertical", "gradient_cyan_orange")
        self.create_gradient_wallpaper((100, 100, 255), (255, 200, 100), "horizontal", "gradient_blue_yellow")
        
        # Geometric patterns
        self.create_geometric_pattern("geometric_abstract")
        
        # Wave patterns
        self.create_wave_pattern("fluid_waves")
        
        # Abstract art
        self.create_abstract_art("abstract_blend")
        
        # Cosmic wallpapers
        self.create_cosmic_wallpaper("cosmic_nebula")
        
        print(f"\nAll wallpapers generated successfully!")
        print(f"Location: {os.path.abspath(self.output_dir)}")
        print(f"Resolution: {self.width}x{self.height} (4K)")
        print("Format: JPEG (High Quality)")

# Usage example
if __name__ == "__main__":
    generator = WallpaperGenerator()
    generator.generate_all_wallpapers()
    
    # Generate custom wallpapers
    print("\nGenerating additional custom wallpapers...")
    
    # Custom gradient combinations
    generator.create_gradient_wallpaper((255, 0, 100), (0, 255, 200), "vertical", "gradient_magenta_cyan")
    generator.create_gradient_wallpaper((100, 0, 255), (255, 100, 0), "vertical", "gradient_purple_orange")
    
    # Additional abstract art
    generator.create_abstract_art("abstract_dream")
    generator.create_cosmic_wallpaper("cosmic_stars")
    
    print("\nCustom wallpapers generated!")
