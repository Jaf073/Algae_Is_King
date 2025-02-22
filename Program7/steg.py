from PIL import Image
import sys

#default vals
SENTINEL = [0, 1, 0, 0, 1, 0]
SENTINEL_Byte = ['0x0', '0xff', '0x0', '0x0', '0xff', '0x0']
s=True; b=True; offset=0; interval=1; w=''; h=''

#Convert bits to bytes
def toByte(data):
    Some=""
    count = 0
    Bytes = []
    
    #make data % by 4
    while len(data)%4 != 0:
        data.append(0)
    #print(data)
    
    for B in data:
        Some += str(B)
        count += 1
        if count == 8:
            #print(Some)
            Bytes.append(hex(int(Some,2)))
            Some = ""
            count = 0
    return(Bytes)

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
        bits = toByte(bits)
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

#get bits from pixels in image
def steg():
    global s; global b; global offset; global interval; global w; global h
    # Load image
    img = Image.open(w).convert('RGB')  # Convert to RGB mode
    
    # Calculate pixels in image and offset
    totalPixels = img.width * img.height
    if offset >= totalPixels:
        raise ValueError("offset too large")
    
    # Determine channel
    channelIndex = {'R': 0, 'G': 1, 'B': 2}.get(channel.upper())
   
    bits = []
    # Get LSBs
    if b:
        for i in range(offset, totalPixels):
            x = i % img.width
            y = i // img.width
            pixel = img.getpixel((x, y))
            lsb = pixel[channelIndex] & 1
            bits.append(lsb)
    
    else:
        # Convert to bytes
        bytes_list = []
        for i in range(0, len(bits), 8):
            byte_chunk = bits[i:i+8]
            if len(byte_chunk) < 8:
                byte_chunk += [0] * (8 - len(byte_chunk))
            byte_value = sum(bit << (7 - j) for j, bit in enumerate(byte_chunk))
            bytes_list.append(byte_value)
        return bytes(bytes_list)
    else:
        return bits

#get arguments from command line
def update(): #update values of global variables
    global s; global b; global offset; global interval; global w; global h
    
    for arg in sys.argv:
        print(arg)
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
            
#I wonder if anky is reading this code
def main():
    data = steg()
    print("Data retrieved:", data)
    print("Finding Data:")
    print(FIND(data))

main()
