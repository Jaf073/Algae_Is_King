import sys

#default vals
SENTINEL = [0, 1, 0, 0, 1, 0]
SENTINEL_Byte = [0, 255, 0, 0, 255, 0]
s=True; b=True; offset=1024; interval=1; w=''; h=''

def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


#Find sentinel in list of bits/bytes
def FIND(data=[]):
    global s; global b; global offset; global interval; global w; global h
    ret = []
    x=0

    if b:
        for info in data:
            if str(info) == str(SENTINEL[x]):
                x += 1
            elif x == 1 and info == '0':
                x = 1        
            elif x == 4 and info == '0':
                x = 1                          
            else:
                x = 0
                
            ret.append(info)
            if x >= len(SENTINEL):
                thing = ret[:len(ret) - len(SENTINEL)] #get list of bits
                goodName = bin(int(''.join(map(str, thing)), 2) << 1) #convert to binary string
                bitsPlz = bitstring_to_bytes(goodName) #convert to byte array
                #return (thing)
                #return (goodName)
                return bitsPlz
    else:
        for info in data:
            if info == SENTINEL_Byte[x]:
                x += 1
            elif x == 1 and info == 0:
                x = 1        
            elif x == 4 and info == 0:
                x = 1                          
            else:
                x = 0
                
            ret.append(info)
            if x >= len(SENTINEL_Byte):
                return bytearray(ret[:len(ret) - len(SENTINEL_Byte)])
    return None

#get arguments from command line
def update(): #update values of global variables
    global s; global b; global offset; global interval; global w; global h
    
    for arg in sys.argv:
        #(-sr)
        if arg == "-s":
            s = True
        elif arg == "-r":
            s = False
            
        #(-bB)
        elif arg == '-b':
            b = True
        elif arg == '-B':
            b = False
        
        #(-o)
        elif '-o' in arg:
            offset = int(arg[2:])

        #([-i])
        elif '-i' in arg:
            interval = int(arg[2:])

        #(-w)
        elif '-w' in arg:
            w = arg[2:]

        #([-h])
        elif '-h' in arg:
            h = arg[2:]  

def main():
    global s; global b; global offset; global interval; global w; global h
    # Open the file in binary mode
    with open('stegged-bit.bmp', 'rb') as file:
        # Read the entire file into a variable
        binary_data = file.read()
        data = bytearray(binary_data)

    update()
    if b:
        binary_string = ''.join(format(byte, '08b') for byte in data)
        data = list(binary_string)
        
    print("Data retrieved:", data[:15])
    print("Finding Data:")
    print(FIND(data[:15]))

main()

