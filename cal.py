import calendar

# Set year and month
year = 2025
month = 7  # July

# Create a plain text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)

# Generate the calendar
july_calendar = cal.formatmonth(year, month)

# Print the calendar
print(july_calendar)
