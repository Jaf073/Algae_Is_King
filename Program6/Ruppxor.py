import sys

def xor():
    # Read key from key file as bineary
    # f = open("key", 'r')
    # key = f.read()
    key = '0101'
    # Take message from stdin
    m = sys.stdin
    b = bytearray()
    message = b.extend(m)
    
    # xor the input with the key to create the output
    output = ''
    for i in range(len(key)):
        output.append(bool(key[i]) ^ bool(message[i]))
    
    # return the output to stdout
    print(message)
    
xor()
    