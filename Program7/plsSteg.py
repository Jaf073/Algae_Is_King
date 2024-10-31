from PIL import Image
import sys

def steg(b, offset, file, channel='R'):
    # load image
    img = Image.open(file).convert('RGB')  # Convert to RGB mode
    
    # calculate pixels in image and offset
    totalPixels = img.width * img.height
    if offset >= totalPixels:
        raise ValueError("offset too large")
    
    # determine channel
    channelIndex = {'R': 0, 'G': 1, 'B': 2}.get(channel.upper())
   
    bits = []
    # get lsbs
    if b == "-b":
        for i in range(offset, totalPixels):
            x = i % img.width
            y = i // img.width
            pixel = img.getpixel((x, y))
            lsb = pixel[channelIndex] & 1
            bits.append(lsb)
    
    if b == "-B":
        # convert to bytes
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

def main():
    b = sys.argv[1]
    file = 'stegged-bit.bmp'
    offset = 1024
    if b == "-b":
        data = steg(b, offset, file, channel='R')
    elif b == "-B":
        data = steg(b, offset, file, channel='R')
    
    print(data)

main()
