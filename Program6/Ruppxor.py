import sys

def xor():
    # Read key from key file as bineary
    f = open("key", 'r')
    key = f.read()
    # key = '0101'

    # Take message from stdin
    message = bytearray((input().encode('utf-8')))
    
    # xor the input with the key to create the output
    out = ''
    for i in range(len(key)):
        if (bool(key[i]) ^ bool(message[i])) == True:
            out += '1'
        else:
            out += '0'

    output = bytearray((out.encode('utf-8')))
    
    # return the output to stdout
    sys.stdout.buffer.write(output)
    
xor()
    