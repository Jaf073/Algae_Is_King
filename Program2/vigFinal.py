import sys


def generate_key(msg):
    # get the key from the command line
    key = sys.argv[2]
    #Force key into lowercase only
    key = key.lower()
    keyList = []
    buff = 0 #make a buffer to keep iteration on track if we encounter some char not a-z
    for i in range(len(msg)):
        #Skip any character that is not a-z
        if (ord(key[(i+buff)%len(key)]) >= 97 and ord(key[(i+buff)%len(key)]) <=122):
            #add char to keylist the same length as the msg
            keyList.append(key[((i+buff)%len(key))]) 
        else:
            buff += 1
            #add char to keylist the same length as the msg
            keyList.append(key[((i+buff)%len(key))])
    return "".join(keyList)

def Encrypt_Vig(msg, key):
    encrypted_text = []
    #make a buffer to keep iteration on track if we encounter some char not a-z
    buff = 0

    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            #Fun math to find char w/o using a chart
            encrypted_char = chr((ord(char.lower()) + ord(key[i+buff]) - 2 * 97) % 26 + 97).upper()
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i+buff]) - 2 * 97) % 26 + 97)
        else:
            encrypted_char = char
            buff -= 1
        #print(f"Char: {char}, KeyChar: {key[i]}, Encrypted: {encrypted_char}")
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

def Decrypt_Vig(msg, key):
    decrypted_text = []
    #make a buffer to keep iteration on track if we encounter some char not a-z
    buff = 0
    for i in range(len(msg)):
        char = msg[i]
        #force char to be in lowercase for math but keep origional to determine if it is capitalized later
        tempChar = char.lower()
        if char.isupper(): #Fun math to find char w/o using a chart
            decrypted_char = chr((ord(tempChar) - ord(key[i+buff]) + 26) % 26 + 97).upper()
        elif char.islower():
            decrypted_char = chr((ord(tempChar) - ord(key[i+buff]) + 26) % 26 + 97)
        else:
            decrypted_char = char
            buff -= 1
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

    
def main(): 
    # find out if user wants to encrypt or decrypt
    intent = sys.argv[1]

    # runs the code until keyboard interrupt and encrypts/decrypts anything the user types
    while True:
        message = input("")
        key = generate_key(message)
        
        if intent == "-e":
            print(Encrypt_Vig(message, key))
        if intent == "-d":
            print(Decrypt_Vig(message, key))

main()
