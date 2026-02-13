def rail_fence_encrypt(text, rails):
    if rails == 1:
        return text

    result = ""
    gap = 2 * (rails - 1)

    for r in range(rails):
        i = r
        down = True
        step1 = gap - 2 * r
        step2 = 2 * r

        while i < len(text):
            result += text[i]

            if r == 0 or r == rails - 1:
                i += gap
            else:
                if down:
                    i += step1
                else:
                    i += step2
                down = not down

    return result

def rail_fence_decrypt(cipher, rails):
    if rails == 1:
        return cipher

    n = len(cipher)
    result = [''] * n
    gap = 2 * (rails - 1)
    idx = 0

    for r in range(rails):
        i = r
        down = True
        step1 = gap - 2 * r
        step2 = 2 * r

        while i < n and idx < n:
            result[i] = cipher[idx]
            idx += 1

            if r == 0 or r == rails - 1:
                i += gap
            else:
                if down:
                    i += step1
                else:
                    i += step2
                down = not down

    return "".join(result)

# -------- Main Program --------
while True:
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    text = input("Enter your message: ")
    rails = int(input("Enter number of rails: "))

    if choice == "encrypt":
        result = rail_fence_encrypt(text, rails)
        print("Encrypted text:", result)

    elif choice == "decrypt":
        result = rail_fence_decrypt(text, rails)
        print("Decrypted text:", result)

    else:
        print("Invalid choice!")

    again = input("Continue? (yes/no): ").lower()
    if again == "no":
        print("Exiting program.")
        break
