
from PIL import Image, ImageDraw, ImageFont
import calendar
import datetime

# Set the year and months
year = datetime.date.today().year
months = [7, 8, 9, 10, 11, 12]

# Create a new image with a white background
img_width = 1000
img_height = 1500
img = Image.new('RGB', (img_width, img_height), color = (240, 230, 140)) # Light yellow background

# Set the font
font = ImageFont.load_default()

# Draw the calendar for each month
y = 50
for month in months:
    # Draw the month name
    draw = ImageDraw.Draw(img)
    draw.text((50, y), calendar.month_name[month] + ' ' + str(year), font=font, fill=(0, 0, 255)) # Blue text
    
    # Draw the calendar
    cal = calendar.monthcalendar(year, month)
    x = 50
    y += 50
    for week in cal:
        for day in week:
            if day == 0:
                draw.text((x, y), '', font=font, fill=(0, 0, 0)) # Black text
            else:
                draw.text((x, y), str(day), font=font, fill=(0, 0, 0)) # Black text
            x += 50
        x = 50
        y += 50
    
    # Add some space between months
    y += 20

# Save the image
img.save('calendar.jpg')
