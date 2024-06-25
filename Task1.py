def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Shift the character within its ASCII range (uppercase)
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Shift the character within its ASCII range (lowercase)
            elif char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def decrypt_caesar_cipher(text, shift):
    # Decryption is essentially encryption with a negative shift
    return caesar_cipher(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt (e) or decrypt (d) a message? (e/d): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value (an integer): ").strip())
        except ValueError:
            print("Shift value must be an integer.")
            continue
        
        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = decrypt_caesar_cipher(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        
        again = input("Do you want to encrypt/decrypt another message? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
