# Name: Kaylee Matic
# Date: 10/16/2024
# A program that implements the XOR crpto method

import sys

# constants
DEBUG = False

# getting the plaintext/cipher text
message = sys.stdin.buffer.read()

# reading the key from a file
file = open("key", 'rb')
key = file.read()

# printing the plaintext/ciphertext and key
if (DEBUG):
    print(f"The message: {message}")
    print(f"The key: {key}")

# closing the file
file.close()

# converting the key and message to a bytearray
messageArray = bytearray(message)
keyArray = bytearray(key)

# printing the arrays
if (DEBUG):
    print(f"The array of the message: {messageArray}")
    print(f"The array of the key: {keyArray}")

# XOR each byte of the message with the key
outputArray = []
for x in range(len(messageArray)):
    output = messageArray[x] ^ keyArray[x]
    outputArray.append(output)

# printing the outputArray
for bit in outputArray:
    sys.stdout.write(chr(bit))