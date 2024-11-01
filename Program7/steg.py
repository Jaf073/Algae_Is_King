from PIL import Image
import argparse

SENTINEL_hex = [0, 0, 0, 0, 0, 0]
SENTINEL_bin = [0, 1, 0, 0, 1, 0]

def FIND(bits=[], interval=1):
    i = 0
    ret = []
    for j in range(0, len(bits), interval):
        bit = bits[j]
        if bit == SENTINEL_hex[i]:  # Check if sentinel
            i += 1
        else:  # Add message to list
            i = 0
        ret.append(bit)
        if i == len(SENTINEL_hex):
            return ret[:len(ret) - len(SENTINEL_hex)]
    return None

def steg(b, offset, file, channel='R'):
    # Load image
    img = Image.open(file).convert('RGB')  # Convert to RGB mode
    
    # Calculate pixels in image and offset
    totalPixels = img.width * img.height
    if offset >= totalPixels:
        raise ValueError("offset too large")
    
    # Determine channel
    channelIndex = {'R': 0, 'G': 1, 'B': 2}.get(channel.upper())
   
    bits = []
    # Get LSBs
    if b == "-b":
        for i in range(offset, totalPixels):
            x = i % img.width
            y = i // img.width
            pixel = img.getpixel((x, y))
            lsb = pixel[channelIndex] & 1
            bits.append(lsb)
    
    if b == "-B":
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

def main():
    parser = argparse.ArgumentParser(description="Steganography tool using LSB extraction")
    
    # Define positional and optional arguments
    parser.add_argument("-s", "--store", action="store_true", help="Store data")
    parser.add_argument("-r", "--retrieve", action="store_true", help="Retrieve data")
    parser.add_argument("-b", action="store_true", help="Bit mode")
    parser.add_argument("-B", action="store_true", help="Byte mode")
    parser.add_argument("-o", "--offset", type=int, default=0, help="Set offset (default: 0)")
    parser.add_argument("-i", "--interval", type=int, default=1, help="Set interval (default: 1)")
    parser.add_argument("-w", "--wrapper", required=True, help="Set wrapper file")

    args = parser.parse_args()
    
    # Validate mode and bit/byte flags
    if not (args.store or args.retrieve):
        parser.error("One of -s (store) or -r (retrieve) must be specified.")
    if not (args.b or args.B):
        parser.error("One of -b (bit mode) or -B (byte mode) must be specified.")
    
    # Validate hidden file requirement only if storing
    if args.store and not args.hidden:
        parser.error("The -s (store) mode requires -h (hidden file) to be specified.")

    mode = "-b" if args.b else "-B"
    offset = args.offset
    interval = args.interval
    wrapper_file = args.wrapper

    if args.retrieve:
        data = steg(mode, offset, wrapper_file, channel='R')
        print("Data retrieved:", data)
        print("Finding Data:")
        print(FIND(data, interval))

main()