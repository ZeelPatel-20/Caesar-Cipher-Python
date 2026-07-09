# Caesar Cipher Program

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Handle lowercase letters
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep spaces and symbols unchanged
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
print("=== Caesar Cipher Program ===")

message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

choice = input("Type 'E' for Encrypt or 'D' for Decrypt: ").upper()

if choice == 'E':
    encrypted = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted)

elif choice == 'D':
    decrypted = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted)

else:
    print("Invalid choice! Please select E or D.")
