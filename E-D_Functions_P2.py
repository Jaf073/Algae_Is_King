def generate_key(msg, key):
    #Force key into lowercase only
    key = list(key.lower())
    #If the msg is the same length as the key,
    #there is no need to expand the length of the key
    if len(msg) == len(key):
        return key
    else:
        #put key character for each char in msg
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    #return long key
    return "".join(key)

def Encrypt_Vig(msg, key):
    #initialize encrypted msg
    encrypted_text = []
    #make key the same length as msg
    key = generate_key(msg, key)
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

def Decrypt_Vig(msg, key):
    #initialize decrypted msg
    decrypted_text = []
    #make key the same length as msg
    key = generate_key(msg, key)
    #find character on chart using key and msg as coords for i in range(len(msg)):
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

#---------------------Enter input code------------------------#
# Example usage
Txt_t_Enc = "Hello, World!"
Dec_t_Txt = "Xijvs, Gmbpb!"
key = "KEY"

encrypted_text = Encrypt_Vig(Txt_t_Enc, key)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = Decrypt_Vig(Dec_t_Txt, key)
print(f"Decrypted Text: {decrypted_text}")
