import qrcode

# Data to encode
data = "https://example.com"  # You can replace this with any text or URL

# Create QR code instance
qr = qrcode.QRCode(
        version=1,  # Controls size of the QR Code (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save("my_qr_code.png")

print("QR code saved as 'my_qr_code.png'")
