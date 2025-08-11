
'''
Task # 02
Pixel Manipulation for Image Encryption
'''

from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Load image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Encrypt: Add key to each pixel (mod 256)
    encrypted_array = (img_array + key) % 256

    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Load encrypted image
    img = Image.open(input_path)
    img_array = np.array(img)

    # Decrypt: Subtract key from each pixel (mod 256)
    decrypted_array = (img_array - key) % 256

    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("\n--- Image Encryption Tool ---")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter choice (1/2): ")

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter encryption/decryption key (integer): "))

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()