# ---------- Create Playfair Matrix ----------
def create_matrix(key):
    key = key.lower().replace("j", "i")
    seen = set()
    matrix_list = []

    # Add key letters first
    for ch in key:
        if ch.isalpha() and ch not in seen:
            seen.add(ch)
            matrix_list.append(ch)

    # Add remaining alphabets (without j)
    for ch in "abcdefghiklmnopqrstuvwxyz":
        if ch not in seen:
            matrix_list.append(ch)

    # Convert into 5x5 matrix
    matrix = [matrix_list[i:i+5] for i in range(0, 25, 5)]
    return matrix


# ---------- Prepare Text ----------
def prepare_text(text):
    text = text.lower().replace("j", "i")
    text = ''.join([c for c in text if c.isalpha()])

    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = ""

        if i+1 < len(text):
            b = text[i+1]

        if a == b:         # same letters → add x
            pairs.append(a + "x")
            i += 1
        else:
            if b:
                pairs.append(a + b)
                i += 2
            else:          # odd length
                pairs.append(a + "x")
                i += 1

    return pairs


# ---------- Find Position ----------
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# ---------- Encrypt ----------
def encrypt(plain_text, key):
    matrix = create_matrix(key)
    pairs = prepare_text(plain_text)

    cipher_text = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:
            cipher_text += matrix[r1][(c1 + 1) % 5]
            cipher_text += matrix[r2][(c2 + 1) % 5]

        # Same column
        elif c1 == c2:
            cipher_text += matrix[(r1 + 1) % 5][c1]
            cipher_text += matrix[(r2 + 1) % 5][c2]

        # Rectangle rule
        else:
            cipher_text += matrix[r1][c2]
            cipher_text += matrix[r2][c1]

    return cipher_text


# ---------- Decrypt ----------
def decrypt(cipher_text, key):
    matrix = create_matrix(key)
    pairs = prepare_text(cipher_text)

    plain_text = ""

    for pair in pairs:
        a, b = pair[0], pair[1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:
            plain_text += matrix[r1][(c1 - 1) % 5]
            plain_text += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            plain_text += matrix[(r1 - 1) % 5][c1]
            plain_text += matrix[(r2 - 1) % 5][c2]

        # Rectangle rule
        else:
            plain_text += matrix[r1][c2]
            plain_text += matrix[r2][c1]

    return plain_text


# ---------- Main Program ----------
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
