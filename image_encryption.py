from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR operation (swaps the values based on key)
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save("encrypted_image.png")
    print("Encryption Complete! Saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # XOR again reverses the change
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save("decrypted_image.png")
    print("Decryption Complete! Saved as 'decrypted_image.png'")

def main():
    print("--- Simple Image Encryption Tool ---")
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()
    path = input("Enter image filename (e.g., photo.jpg): ")
    key = int(input("Enter a secret number key (e.g., 123): "))

    if choice == 'e':
        encrypt_image(path, key)
    elif choice == 'd':
        decrypt_image(path, key)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()