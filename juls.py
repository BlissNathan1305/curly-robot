import calendar
from PIL import Image, ImageDraw, ImageFont

# ?? Calendar settings
year = 2025
month = 7
cal = calendar.month(year, month)

# ??️ Image settings
img_width, img_height = 500, 400
background_color = (0, 0, 255)  # Blue
text_color = (255, 255, 255)    # White

# ?? Create image
img = Image.new('RGB', (img_width, img_height), background_color)
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# ✍️ Draw calendar text
x, y = 20, 20
for line in cal.split('\n'):
    draw.text((x, y), line, fill=text_color, font=font)
    y += 20

# ?? Save image
img.save('calendar_july_2025.jpg')
print("Calendar image saved as 'calendar_july_2025.jpg'")
