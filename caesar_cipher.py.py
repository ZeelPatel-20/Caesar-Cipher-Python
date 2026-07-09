"""
Caesar Cipher Encryption & Decryption Tool
Author: Zeel Patel
Description:
A Python program to encrypt and decrypt messages using the Caesar Cipher algorithm.
"""

def encrypt(text, shift):
    """Encrypt the given text using Caesar Cipher."""
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep spaces, numbers, and special characters unchanged
            result += char

    return result


def decrypt(text, shift):
    """Decrypt the given text using Caesar Cipher."""
    return encrypt(text, -shift)


def main():
    print("=" * 40)
    print("      Caesar Cipher Program")
    print("=" * 40)

    message = input("Enter your message: ")

    # Validate shift value
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                break
            else:
                print("Please enter a number between 0 and 25.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").strip().upper()

    if choice == 'E':
        encrypted = encrypt(message, shift)
        print("\nEncrypted Message:")
        print(encrypted)

    elif choice == 'D':
        decrypted = decrypt(message, shift)
        print("\nDecrypted Message:")
        print(decrypted)

    else:
        print("\nInvalid choice! Please enter E or D.")


if __name__ == "__main__":
    main()
