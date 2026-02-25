# We write plaintext row-wise in a gird
# The number of rows = length of the key
# Then we rearrange columns based on the alphabetical order of the key
# Read columns one by one - Ciphertext

import math

# Create Order
def get_key_order(key):
    key_list = list(key)
    sorted_key = sorted(key_list)
    order = []

    for ch in sorted_key:
        index = key_list.index(ch)
        order.append(index)
        key_list[index] = None # Avoid duplicate issues
    return order

# Encrypt
def encrypt(plain_text,key):
    plain_text = plain_text.replace(" ", "")
    cols = len(key)
    rows = math.ceil(len(plain_text)/cols)

    # Fill matrix row-wise
    matrix = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            if index < len(plain_text):
                row.append(plain_text[index])
                index += 1
            else:
                row.append('x') #padding
        matrix.append(row)
    order = get_key_order(key)

    cipher_text = ""
    for col_index in order:
        for r in range(rows):
            cipher_text += matrix[r][col_index]
    return cipher_text

# Decrypt
def decrypt(cipher_text, key):
    cols = len(key)
    rows = math.ceil(len(cipher_text)/cols)

    order = get_key_order(key)

    # Create empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)] #list comprehension
    index = 0
    for col_index in order:
        for r in range(rows):
            matrix[r][col_index] = cipher_text[index]
            index += 1

    plain_text = ""
    for r in range(rows):
        for c in range(cols):
            plain_text += matrix[r][c]

    return plain_text.rstrip('x')

# Main Program
while True:
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    text = input("Enter your message: ")
    key = input("Enter your key: ")

    if choice == "encrypt":
        result = encrypt(text,key)
        print("Encrypted Result: ",result)
    
    elif choice == "decrypt":
        result = decrypt(text, key)
        print("Decryted Result: ",result)
    
    else:
        print("Invalid choice!")

    again = input("Continue? (yes/no): ").lower()
    if again == "no":
        print("Exiting Program.")
        break