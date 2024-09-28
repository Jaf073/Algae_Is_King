
def generate_key(msg, key):
    #Force key into lowercase only
    key = key.lower()
    keyList = []
    buff = 0
    for i in range(len(msg)):
        if (ord(key[(i+buff)%len(key)]) >= 97 and ord(key[(i+buff)%len(key)]) <=122):
            keyList.append(key[((i+buff)%len(key))])
        else:
            buff += 1
            keyList.append(key[((i+buff)%len(key))])
    return "".join(keyList)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    buff = 0
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char.lower()) + ord(key[i+buff]) - 2 * 97) % 26 + 97).upper()
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i+buff]) - 2 * 97) % 26 + 97)
        else:
            encrypted_char = char
            buff -= 1
        #print(f"Char: {char}, KeyChar: {key[i]}, Encrypted: {encrypted_char}")
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def decrypt_vigenere(msg, key):
    decrypted_text = []
    buff = 0
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        tempChar = char.lower()
        if char.isupper():
            decrypted_char = chr((ord(tempChar) - ord(key[i+buff]) + 26) % 26 + 97).upper()
        elif char.islower():
            decrypted_char = chr((ord(tempChar) - ord(key[i+buff]) + 26) % 26 + 97)
        else:
            decrypted_char = char
            buff -= 1
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

# Example usage
msg = "Get ready for Cyber Storm! We’re going to turn your world upside down on November 8!"
key = "This is my key"

print("MSG: " + msg)
print("Key: " + key)
encrypted_text = encrypt_vigenere(msg, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = decrypt_vigenere(encrypted_text, key)
print(f"Decrypted Text: {decrypted_text}")

#previous code was only support the upper case letters
#this code can be apply on both
