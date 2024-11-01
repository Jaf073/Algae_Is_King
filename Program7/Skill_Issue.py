from PIL import Image
import sys

SENTINEL_hex = [0x0, 0xFF, 0x0, 0x0, 0xFF, 0x0]
SENTINEL_bin = [0b00000000, 0b11111111, 0b00000000, 0b00000000, 0b11111111, 0b00000000]

def FIND(bits=[], interval=1):
    i=0
    ret = []
    for j in range(0,len(bits),interval):
        bit = bits[j]
        if bit == SENTINEL_hex[i]: #check if sentinal
            i+=1
        else: #add message to list
            i = 0
        ret.append(bit)
        if i == len(SENTINEL_hex): return(ret[:len(ret)-len(SENTINEL_hex)])
    return(None)

def toList(dataType, offset, file):
    # open image in grayscale
    image = Image.open(file)#.convert("L")
    width, height = image.size
    # set offset
    startY = offset // width
    startX = offset % width
    data = []

    # chatgpt helped with some of this
    # iterates over image
    for y in range(startY, height):
        for x in range(startX if y == startY else 0, width):
            #byte_value = image.getpixel((x, y))
            #get rgb value of pixel
            R, G, B = image.getpixel((x, y))
            
            if dataType == 'byte':
                #data.append(hex(byte_value))
                data.append(hex(R))
                data.append(hex(G))
                data.append(hex(B))
                
            elif dataType == 'bit':
                #data.append(bin(byte_value))
                data.append(bin(R))
                data.append(bin(G))
                data.append(bin(B))

        # reset x after first row
        startX = 0

    # display data collected
    if dataType == 'byte':
        print(f"byte after offset: {data[:10]}")
    elif dataType == 'bit':
        print(f"bit after offset: {data[:10]}")

    return data

def main():
    # takes command line arguments
    dataType = sys.argv[1]
    offset = int(sys.argv[2])
    file = "stegged-bit.bmp"

    print(FIND(toList(dataType, offset, file)))
    
main()
