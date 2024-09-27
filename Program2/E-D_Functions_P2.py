chart = [
    ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
    ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'],
    ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b'],
    ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c'],
    ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],
    ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e'],
    ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f'],
    ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g'],
    ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h'],
    ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i'],
    ['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j'],
    ['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k'],
    ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l'],
    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m'],
    ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n'],
    ['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'],
    ['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p'],
    ['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'],
    ['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r'],
    ['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],
    ['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'],
    ['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],
    ['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'],
    ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'],
    ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'],
    ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y'],
    ]

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
        tempChar= char.lower()
        if (ord(tempChar) >= 97 and ord(tempChar) <=122):
            encrypted_char = chart[ord(tempChar)-97][ord(key[i])-97]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
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
    #find character on chart using key and msg as coords
    for i in range(len(msg)):
        char = msg[i]
        tempChar= char.lower()
        if (ord(tempChar) >= 97 and ord(tempChar) <=122):
            decrypted_char = chart[0][chart[ord(key[i])-97].index(tempChar)]
            if char.isupper():
                decrypted_char = decrypted_char.upper()
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    #return decrypted char
    return "".join(decrypted_text)
    

#---------------------Enter input code------------------------#
# Example usage
Txt_t_Enc = "Hello, World!"
Dec_t_Txt = "Rijvs, Ambpb!"
key = "KEY"

encrypted_text = Encrypt_Vig(Txt_t_Enc, key)
print(f"Encrypted Text: {encrypted_text}")
decrypted_text = Decrypt_Vig(Dec_t_Txt, key)
print(f"Decrypted Text: {decrypted_text}")

'''
key = input("Enter Key: ")
print(key)
encrypted_text = Encrypt_Vig(Txt_t_Enc, key)


while True:
    text = input("Enter Text: ")
    if text[:2] == "-e":
        encrypted_text = Encrypt_Vig(text[2:], key)
        print(f"Encrypted Text: {encrypted_text}")

    elif text[:2] == "-d":
        decrypted_text = Decrypt_Vig(text[2:], key)
        print(f"Decrypted Text: {decrypted_text}")
        '''
