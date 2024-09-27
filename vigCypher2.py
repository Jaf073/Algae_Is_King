import sys

# mostly from mr feet
def genKey(msg):
    key = sys.argv[2]

    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key += (key[i % len(key)])
    
    return "".join(key)

# Function to Encrypt using the Vigenère cipher.
def eVig(msg, key):
   #initialize encrypted msg
    encrypted_text = []
    
    #find character on chart using key and msg as coords
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    #return encrypted message
    return "".join(encrypted_text)

# Decryption function for the Vigenère cipher
def dVig(msg, key):
    #initialize decrypted msg
    decrypted_text = []

    #find character on chart using key and msg as coords 
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    #return decrypted char
    return "".join(decrypted_text)



def main():
    intent = sys.argv[1]

    while True:
        message = input("")
        key = genKey(message)
        if intent == "-e":
                print(f"encryption: {eVig(message, key)}")
        if intent == "-d":
            print(f"decryption: {dVig(message, key)}")

main()
