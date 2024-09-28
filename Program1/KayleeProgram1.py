# Name: Kaylee Matic
# Date: 9/28/2024
# Write a program that decodes various messages in binary

import sys

# Function to decode binary and put into readable format
def decode(input): 
    inputArray = list(input)
    
    # need to check if the binary is encoded in 7 bit chunks or 8 bit chunks
    # the first if checks if it could be encoded by either 7 or 8 but won't be known until the message is fully decoded
    # the next elif checks by chunks of 7
    # and the last elif checks by chunks of 8
    if ((len(inputArray)-1) % 7 == 0 and (len(inputArray)-1) % 8 == 0):
        index = 0
        group = 0
        decrypted = ""
        temp = ""
        while (index < len(inputArray)):
            temp += inputArray[index]
            index += 1
            group += 1
            if (group >= 7):
                decrypted += chr(int(temp, 2))
                temp = ""
                group = 0
        print("This is the file decrypted by chunks of 7: ")
        print(decrypted)

        index = 0
        group = 0
        decrypted = ""
        temp = ""
        while (index < len(inputArray)):
            temp += inputArray[index]
            index += 1
            group += 1
            if (group >= 8):
                decrypted += chr(int(temp, 2))
                temp = ""
                group = 0
        print("This is the file decrypted by chunks of 8: ")
        print(decrypted)

    elif ((len(inputArray)-1) % 7 == 0):
        index = 0
        group = 0
        decrypted = ""
        temp = ""
        while (index < len(inputArray)):
            temp += inputArray[index]
            index += 1
            group += 1
            if (group >= 7):
                decrypted += chr(int(temp, 2))
                temp = ""
                group = 0
        print("This is the file decrypted by chunks of 7: ")
        print(decrypted)

    elif ((len(inputArray)-1) % 8 == 0):
        index = 0
        group = 0
        decrypted = ""
        temp = ""
        while (index < len(inputArray)):
            temp += inputArray[index]
            index += 1
            group += 1
            if (group >= 8):
                decrypted += chr(int(temp, 2))
                temp = ""
                group = 0
        print("This is the file decrypted by chunks of 8: ")
        print(decrypted)


##### MAIN ######
inputFile = sys.stdin.read()
decode(inputFile)