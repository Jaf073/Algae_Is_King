import sys

# Read key from key file as bineary
f = open('8d1a2ecbe851db4c448fd5360797db84', 'rb')
key = f.read()
f.close()

# Read input
message = sys.stdin.buffer.read()

# Take message from stdin
messageArray = bytearray(message)
# Make keyArray
keyArray = bytearray(key)

# xor the input with the key to create the output
initialoutput = bytearray()
for i in range(len(messageArray)):
    initialoutput.append(messageArray[i] ^ keyArray[i])

# return the output to stdout
for i in initialoutput:
    sys.stdout.buffer.write(int.to_bytes(i))
