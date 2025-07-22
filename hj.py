
from PIL import Image, ImageDraw, ImageFont
import calendar

# Set up image properties
width, height = 3840, 2160  # 4K resolution
background_color = (255, 255, 255)  # white background
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Load fonts (fallback to default if unavailable)
try:
    font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 120)
    font_day = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    font_date = ImageFont.truetype("DejaVuSans.ttf", 50)
except IOError:
    font_title = font_day = font_date = ImageFont.load_default()

# Constants
margin = 100
calendar_spacing = 80
weekday_bg = (230, 230, 250)  # light purple
title_colors = [(255, 105, 180), (30, 144, 255)]  # pink, blue

def draw_calendar(year, month, x, y, title_color):
    # Draw month title
    title = f"{calendar.month_name[month]} {year}"
    draw.text((x, y), title, fill=title_color, font=font_title)

    # Draw weekday headers
    for i, day in enumerate(calendar.day_abbr):
        dx = x + i * 200
        dy = y + 140
        draw.rectangle([dx, dy, dx + 180, dy + 70], fill=weekday_bg)
        draw.text((dx + 20, dy + 10), day, fill="black", font=font_day)

    # Draw days
    cal = calendar.monthcalendar(year, month)
    for row, week in enumerate(cal):
        for col, date in enumerate(week):
            if date:
                dx = x + col * 200
                dy = y + 230 + row * 130
                draw.text((dx + 20, dy), str(date), fill="black", font=font_date)

# Draw both months
draw_calendar(2025, 7, 100, 100, title_colors[0])    # July
draw_calendar(2025, 8, 100, 1150, title_colors[1])   # August

# Save the image
image.save("july_august_calendar.jpeg", "JPEG")
print("Calendar saved as july_august_calendar.jpeg")
