import cv2
import os
import numpy as np
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Function to open file dialog to select an image
def select_image():
    Tk().withdraw()  # Hide the root Tk window
    filename = askopenfilename(title="Select an image", 
                               filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff;*.webp;*.gif")])
    return filename

# Function to validate password
def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$"
    return bool(re.match(pattern, password))

# Function to encrypt a message into an image
def encrypt_message(img, msg):
    msg += "~"  # Add a delimiter to mark the end of the message
    msg_bin = ''.join(format(ord(char), '08b') for char in msg)  # Convert message to binary

    idx = 0
    img_height, img_width, _ = img.shape  # Get image dimensions

    for i in range(img_height):
        for j in range(img_width):
            for channel in range(3):  # Modify RGB channels
                if idx < len(msg_bin):
                    img[i, j, channel] = np.uint8((int(img[i, j, channel]) & 254) | int(msg_bin[idx]))
                    idx += 1
                else:
                    return img
    return img

# Function to decrypt message from an image
def decrypt_message(img):
    bin_str = ""
    for row in img:
        for pixel in row:
            for channel in range(3):
                bin_str += str(int(pixel[channel]) & 1)  # Extract LSB

    # Convert binary to text
    message = ""
    for i in range(0, len(bin_str), 8):
        char = chr(int(bin_str[i:i+8], 2))
        if char == "~":  # Stop at delimiter
            break
        message += char

    return message

# Allow user to select an image
img_path = select_image()

if img_path:
    img = cv2.imread(img_path)  # Read the selected image
    if img is None:
        print("Could not open or read the image file.")
        exit(1)

    msg = input("Enter secret message: ")

    # Get a valid password from the user
    while True:
        password = input("Enter a passcode (Min 6 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char): ")
        if is_valid_password(password):
            break
        else:
            print("Invalid password! Password must have at least 6 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")

    encrypted_img = encrypt_message(img, msg)

    # Save the encrypted image in the same directory as the script
    current_directory = os.path.dirname(os.path.abspath(__file__))
    encrypted_img_path = os.path.join(current_directory, "encryptedImage.png")

    cv2.imwrite(encrypted_img_path, encrypted_img)
    print(f"Encrypted image saved as {encrypted_img_path}")
    os.system(f"start {encrypted_img_path}")  # Open image on Windows

    # Decrypt the message
    pas = input("Enter passcode for Decryption: ")
    if password == pas:
        decrypted_message = decrypt_message(encrypted_img)
        print("Decrypted message:", decrypted_message)
    else:
        print("YOU ARE NOT AUTHORIZED.")
else:
    print("No image selected. Exiting.")
