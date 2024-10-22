import sys

# Read key from key file as bineary
f = open('key2-1', 'rb')
key = f.read()
f.close()

# Read input
message = sys.stdin.buffer.read()

# Take message from stdin
messageArray = bytearray(message)
# Make keyArray
keyArray = bytearray(key)


# xor the input with the key to create the output
output = []
for i in range(len(messageArray)):
    output.append(messageArray[i] ^ keyArray[i])


# return the output to stdout
sys.stdout.buffer.write(output)
