
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

# Set image dimensions (1440x2560 for 4K mobile)
width, height = 1440, 2560

# Create a new image with white background
image = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(image)

# Load a font (download a TTF font like DejaVuSans if needed, or use a default one)
try:
    font = ImageFont.truetype("DejaVuSans.ttf", 30)  # Adjust path and size as needed
except:
    font = ImageFont.load_default()  # Fallback if no TTF font is available

# Title
title = "2025 Calendar (July - December)"
draw.text((width // 2 - len(title) * 10, 20), title, fill="black", font=font)

# Function to get days in a month
def get_days_in_month(year, month):
    return (datetime(year, month % 12 + 1, 1) - timedelta(days=1)).day

# Start date: July 1, 2025
start_date = datetime(2025, 7, 1)
end_date = datetime(2025, 12, 31)

# Calculate position for each month
month_height = (height - 100) // 6  # Divide space for 6 months
x_offset = 50
y_offset = 100

current_date = start_date
while current_date <= end_date:
    month = current_date.month
    year = current_date.year
    days = get_days_in_month(year, month)
    month_name = current_date.strftime("%B %Y")

    # Draw month title
    draw.text((x_offset, y_offset), month_name, fill="blue", font=font)
    y_offset += 40

    # Draw days of the week header
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, day in enumerate(days_of_week):
        draw.text((x_offset + i * 100, y_offset), day, fill="black", font=font)
    y_offset += 40

    # Get first day of the month (0 = Monday, 6 = Sunday)
    first_day = datetime(year, month, 1).weekday()
    max_rows = (days + first_day + 6) // 7  # Calculate rows needed

    # Draw calendar grid
    day_num = 1
    for row in range(max_rows):
        for col in range(7):
            if row == 0 and col < first_day or day_num > days:
                draw.text((x_offset + col * 100, y_offset), "", fill="black", font=font)
            else:
                draw.text((x_offset + col * 100, y_offset), str(day_num), fill="black", font=font)
                day_num += 1
            if day_num > days:
                break
        y_offset += 40
        if day_num > days:
            break

    # Move to next month
    y_offset += 20
    current_date = current_date.replace(day=1) + timedelta(days=32)
    current_date = current_date.replace(day=1)

# Save the image as JPEG
image.save("calendar_2025_jul_dec.jpg", "JPEG", quality=95)

print("Calendar saved as 'calendar_2025_jul_dec.jpg'")
