import struct
import textwrap
from prettytable import PrettyTable
from PIL import Image
import numpy as np

# Function to format multi-line data
def format_multi_line(prefix, string, size=80):
    size -= len(prefix)
    if isinstance(string, bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
    return '\n'.join([prefix + line for line in textwrap.wrap(string, size)])

def encrypt_image(image_path, output_path):
    image = Image.open(image_path)
    np_image = np.array(image)
    encrypted = 255 - np_image  # Simple pixel inversion

    # Preserve format if possible
    format = image.format if image.format else output_path.split('.')[-1].upper()
    Image.fromarray(encrypted).save(output_path, format=format)
    print(f"[*] Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path):
    image = Image.open(image_path)
    np_image = np.array(image)
    decrypted = 255 - np_image  # Reverse inversion

    # Preserve format if possible
    format = image.format if image.format else output_path.split('.')[-1].upper()
    Image.fromarray(decrypted).save(output_path, format=format)
    print(f"[*] Decrypted image saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter your choice (1 or 2): ").strip()
    if choice not in ['1', '2']:
        print("Invalid choice! Exiting.")
        return

    input_path = input("Enter input image file path: ").strip()
    output_path = input("Enter output image file path: ").strip()

    try:
        if choice == '1':
            encrypt_image(input_path, output_path)
        else:
            decrypt_image(input_path, output_path)
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()

