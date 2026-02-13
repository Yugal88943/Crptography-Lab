import string

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def encrypt(plain_text, key):
    cipher_text = ""
    key = key.lower()
    key_index = 0

    for char in plain_text.lower():
        if char in alphabet:
            text_pos = alphabet.index(char)
            key_pos = alphabet.index(key[key_index % len(key)])
            new_pos = (text_pos + key_pos) % 26
            cipher_text += alphabet[new_pos]
            key_index += 1
        else:
            cipher_text += char

    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    key = key.lower()
    key_index = 0

    for char in cipher_text.lower():
        if char in alphabet:
            text_pos = alphabet.index(char)
            key_pos = alphabet.index(key[key_index % len(key)])
            new_pos = (text_pos - key_pos) % 26
            plain_text += alphabet[new_pos]
            key_index += 1
        else:
            plain_text += char

    return plain_text


# -------- Main Program --------
while True:
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    text = input("Enter your message: ")
    key = input("Enter the key: ")

    if choice == "encrypt":
        result = encrypt(text, key)
        print("Encrypted text:", result)

    elif choice == "decrypt":
        result = decrypt(text, key)
        print("Decrypted text:", result)

    else:
        print("Invalid choice!")

    again = input("Continue? (yes/no): ").lower()
    if again == "no":
        print("Exiting program.")
        break
