def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption & Decryption")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (number): "))

    if choice == 'encrypt':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == 'decrypt':
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please select 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
