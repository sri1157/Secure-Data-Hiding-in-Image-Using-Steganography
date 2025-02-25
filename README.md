# Secure-Data-Hiding-in-Image-Using-Steganography


🚀 Overview
This project implements Image Steganography using Python and OpenCV. It allows users to hide a secret message inside an image by modifying the least significant bit (LSB) of pixel values. A password is required to retrieve the hidden message.

✨ Features
🔏 Embed a secret message inside an image.
🔓 Retrieve the hidden message using a correct password.
✅ Password validation with security rules:
At least 6 characters
1 uppercase letter
1 lowercase letter
1 digit
1 special character (@$!%*?&)
🖼️ Supports multiple image formats: .jpg, .jpeg, .png, .bmp, .tiff, .webp, .gif
📂 Graphical file selection via a file dialog.
💾 Automatic encrypted image saving to the script directory.

📥 Installation
Prerequisites
Ensure you have Python installed. Then, install the required dependencies:
pip install opencv-python numpy

▶️ Usage
Running the Script
python stg.py

Steps:
📂 Select an image via the file dialog.
📝 Enter the secret message to hide.
🔐 Enter a secure password (must meet validation rules).
💾 Encrypted image is saved in the script directory as encryptedImage.png.
🔍 To decrypt, enter the correct password.

🤝 Contributing
Feel free to submit issues or pull requests to improve this project

✍️ Author
[SRIVALLIKA]
