
from PIL import Image, ImageDraw, ImageFont
import calendar
import numpy as np

# Calendar settings
year = 2025
width, height = 3840, 2160  # 4K resolution
months = list(range(1, 13))
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Create a new image with a gradient background
def create_gradient_background(width, height):
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    
    # Gradient from light blue to light purple
    for y in range(height):
        t = y / height
        r = int(135 + t * (186 - 135))
        g = int(206 + t * (147 - 206))
        b = int(235 + t * (235 - 235))
        for x in range(width):
            pixels[x, y] = (r, g, b)
    return image

# Load font (replace with path to your .ttf font file, e.g., Roboto-Regular.ttf)
try:
    title_font = ImageFont.truetype("arial.ttf", 60)  # Adjust path if needed
    day_font = ImageFont.truetype("arial.ttf", 30)
    date_font = ImageFont.truetype("arial.ttf", 24)
except:
    title_font = ImageFont.load_default()
    day_font = ImageFont.load_default()
    date_font = ImageFont.load_default()

# Create the calendar image
image = create_gradient_background(width, height)
draw = ImageDraw.Draw(image)

# Calendar layout settings
month_width = width // 4
month_height = height // 3
padding = 50
cell_size = 70
day_names = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

# Colors
month_bg_color = (255, 255, 255, 200)  # Semi-transparent white
month_border_color = (50, 50, 50)  # Dark gray
text_color = (20, 20, 20)  # Near black
weekend_color = (200, 50, 50)  # Red for weekends
title_color = (0, 0, 128)  # Dark blue for month names

# Draw year title at the top
year_text = f"{year} Calendar"
year_bbox = draw.textbbox((0, 0), year_text, font=title_font)
year_text_width = year_bbox[2] - year_bbox[0]
draw.text(((width - year_text_width) // 2, 20), year_text, fill=title_color, font=title_font)

# Generate and draw each month
for month_idx, month in enumerate(months):
    # Calculate month position in 4x3 grid
    row = month_idx // 4
    col = month_idx % 4
    x_start = col * month_width + padding
    y_start = row * month_height + padding + 100  # Offset for year title

    # Draw semi-transparent background for the month
    draw.rectangle(
        [x_start, y_start, x_start + month_width - 2 * padding, y_start + month_height - 2 * padding],
        fill=month_bg_color,
        outline=month_border_color,
        width=2
    )

    # Draw month name
    month_name = month_names[month - 1]
    month_bbox = draw.textbbox((0, 0), month_name, font=title_font)
    month_text_width = month_bbox[2] - month_bbox[0]
    draw.text(
        (x_start + (month_width - 2 * padding - month_text_width) // 2, y_start + 20),
        month_name,
        fill=title_color,
        font=title_font
    )

    # Get calendar data for the month
    cal = calendar.monthcalendar(year, month)
    y_offset = y_start + 100

    # Draw day names
    for i, day in enumerate(day_names):
        x = x_start + i * cell_size + 20
        draw.text((x, y_offset), day, fill=text_color, font=day_font)

    # Draw dates
    y_offset += 50
    for week in cal:
        for i, day in enumerate(week):
            if day == 0:
                continue  # Skip empty days
            x = x_start + i * cell_size + 20
            y = y_offset
            color = weekend_color if i >= 5 else text_color  # Red for weekends
            draw.text((x, y), str(day), fill=color, font=date_font)
        y_offset += cell_size

# Save the image as JPEG
image.save("calendar_2025.jpg", "JPEG", quality=95)
print("Calendar saved as calendar_2025.jpg")
