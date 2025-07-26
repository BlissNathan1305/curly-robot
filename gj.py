import qrcode

# Data to encode in the QR code
data = "https://www.example.com"

# Create a QR code instance
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a JPEG
img.save("qrcode.jpg")
