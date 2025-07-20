import qrcode

# Data to encode in the QR code
data = "https://example.com"  # Replace with your URL or text

# Create a QR code object
qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border thickness (in boxes)
    )

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("qrcode.png")
