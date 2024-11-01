import sys

#default vals
SENTINEL = [0, 1, 0, 0, 1, 0]
SENTINEL_Byte = [0, 255, 0, 0, 255, 0]
s=True; b=False; offset=1024; interval=1; w=''; h=''

#Find sentinel in list of bits/bytes
def FIND(bits=[]):
    global s; global b; global offset; global interval; global w; global h
    ret = []
    i=0

    if b:
        for j in range(0, len(bits), interval):
            bit = bits[j]
            if bit == SENTINEL[i]:  # Check if sentinel
                i += 1
            else:  # Add message to list
                i = 0
            ret.append(bit)
            if i == len(SENTINEL):
                return ret[:len(ret) - len(SENTINEL)]
    else:
        for j in range(0, len(bits), interval):
            bit = bits[j]
            if bit == SENTINEL_Byte[i]:  # Check if sentinel
                i += 1
            else:  # Add message to list
                i = 0
            ret.append(bit)
            if i == len(SENTINEL_Byte):
                return ret[:len(ret) - len(SENTINEL_Byte)]
    return None

def main():
    # Open the file in binary mode
    with open('stegged-byte.bmp', 'rb') as file:
        # Read the entire file into a variable
        binary_data = file.read()
        array = bytearray(binary_data)

    print(array[offset:5000])
    print(FIND(array[offset:]))

main()
