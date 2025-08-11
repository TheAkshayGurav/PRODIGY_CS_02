Pixel Manipulation for Image Encryption: Develop a simple image encryption tool using pixel manipulation in python. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images. How It Works Encryption → (pixel_value + key) % 256 Decryption → (pixel_value - key) % 256 Uses Pillow (PIL) for image handling and numpy for fast pixel manipulation. The key can be any integer, and the same key must be used for decryption.

--- Image Encryption Tool ---

Encrypt Image
Decrypt Image Enter choice (1/2): 

1 Enter input image path: input.jpg 

2 Enter output image path: encrypted.png 

Enter encryption/decryption key (integer): 50 

Image encrypted and saved as encrypted.png 

If you run decrypt with the same key 50, you’ll get back the original image.
