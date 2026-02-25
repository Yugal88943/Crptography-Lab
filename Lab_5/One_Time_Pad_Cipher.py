# A substitution cipher
# Uses random key
# Key length = PLaintext length
# Each letter is shifted using modular arithmetic
# -----------------------------------------------
# Encryption: C = (P + K) mod 26
# Decryption: P = (C - K) mod 26
# -----------------------------------------------

# Prepare Text
def prepare_text(text):
    clean_text = ""
    for c in text:
        if c.isalpha():
            clean_text += c.upper()
    return clean_text

# Encryption
def encrypt(plain_text, key):
    plain_text = prepare_text(plain_text)
    key = prepare_text(key)

    if(len(plain_text) != len(key)):
        return "Error: Key length must be equal to plaintext length."
    cipher_text = ""

    for i in range(len(plain_text)):
        p = ord(plain_text[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        
        c = (p + k) % 26
        cipher_text += chr(c + ord('A'))
    return cipher_text 

# Decryption 
def decrypt(cipher_text, key):
    cipher_text = prepare_text(cipher_text)
    key = prepare_text(key)

    if(len(cipher_text) != len(key)):
        return"Error: Key length must be equal to ciphertext length."
    plain_text = "" 
    for i in range(len(cipher_text)):
        c = ord(cipher_text[i]) - ord('A')
        k = ord(key[i]) - ord('A')

        p = (c - k) % 26
        plain_text += chr(p + ord('A'))
    return plain_text
    

# Main Program
while True:
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    text = input("Enter your message: ")
    key = input("Enter the key (same length as message): ")

    if choice == "encrypt":
        result = encrypt(text, key)
        print("Encrypted Text: ",result)
    elif choice == "decrypt":
        result = decrypt(text, key)
        print("Decrypted Text: ", result)
    else:
        print("Invalid Choice!")
    
    again = input("Continue? (yes/no): ")
    if again == "no":
        print("Exiting Program")
        break