alphabet = list('abcdefghijklmnopqrstuvwxyz')

print("Enter 4 numbers for the key matrix (2*2): ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

key_matrix = [[a,b],
              [c,d]]

# modular inverse of number mod 26
def mod_inverse(num):
    num = num%26
    for i in range(26):
        if(num * i) % 26 == 1:
            return i
    return -1 

# inverse key matrix
def inverse_key_matrix():
    a = key_matrix[0][0]
    b = key_matrix[0][1]
    c = key_matrix[1][0]
    d = key_matrix[1][1]

    # determinant
    det = (a*d - b*c)%26

    inv_det = mod_inverse(det)
    if inv_det == -1:
        print("Invalid key!")
        return None
    
    # inverse matix 
    inv_a = (d*inv_det)%26
    inv_b = (-b*inv_det)%26
    inv_c = (-c*inv_det)%26
    inv_d = (a*inv_det)%26

    return [[inv_a, inv_b],
            [inv_c, inv_d]]

def encrypt(plain_text):
    plain_text = plain_text.replace(" ","").lower()

    # if odd, use x
    if len(plain_text)%2 != 0:
        plain_text += 'x'

    cipher_text = ""

    # process letter in pair 
    for i in range(0, len(plain_text), 2):
        p1 = alphabet.index(plain_text[i])
        p2 = alphabet.index(plain_text[i+1])

        # matrix muliplication
        c1 = (key_matrix[0][0] * p1 + key_matrix[0][1] * p2) % 26
        c2 = (key_matrix[1][0] * p1 + key_matrix[1][1] * p2) % 26

        cipher_text += alphabet[c1] + alphabet[c2]
    print("Encrypted text : ", cipher_text)

def decrypt(cipher_text):
    inv_matix = inverse_key_matrix()
    if inv_matix is None:
        return
    plain_text = ""

    for i in range(0, len(cipher_text), 2):
        c1 = alphabet.index(cipher_text[i])
        c2 = alphabet.index(cipher_text[i+1])

        # multiply by inverse key
        p1 = (inv_matix[0][0] * c1 + inv_matix[0][1] * c2) % 26
        p2 = (inv_matix[1][0] * c1 + inv_matix[1][1] * c2) % 26

        plain_text += alphabet[p1] + alphabet[p2]
    print("Decrypted text: ", plain_text)

choice = input("Type 'encrypt' or 'decrypt': ")
message = input("Type your message: ")

if choice == "encrypt":
    encrypt(message)
elif choice == "decrypt":
    decrypt(message)
else:
    print("Invalid option")