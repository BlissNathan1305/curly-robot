import qrcode
from PIL import Image

# Data to encode in the QR code
data = "https://x.ai"  # Replace with your desired URL or text

# Create a QR code object with custom settings
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # Size of each box in pixels
    border=4,  # Border thickness (in boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image with a custom color scheme
img = qr.make_image(fill_color="darkblue", back_color="lightgray")

# Optionally add a logo (e.g., a small image in the center)
try:
    logo = Image.open("logo.png")  # Replace with path to a small logo image (e.g., 100x100 pixels)
    logo_size = 100
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
    pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
    img.paste(logo, pos)
except:
    pass  # Skip logo if not available

# Save the QR code as a JPEG
img.save("qrcode_custom.jpg", "JPEG", quality=95)

print("QR code saved as 'qrcode_custom.jpg'")
