import argparse
import sys

# sentinel to look for
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])

# storing hidden bytes in image
def storeByte(wrapper, hidden, offset, interval):
    i = 0
    while i < len(hidden):
        wrapper[offset] = hidden[i]
        offset += interval
        i += 1

    # hides sentinel in message
    for byte in SENTINEL:
        wrapper[offset] = byte
        offset += interval
        
    return(wrapper)

# get bytes from image
def retrieveByte(wrapper, offset, interval):
    hidden = bytearray()
    sentinel_index = 0

    while offset < len(wrapper):
        byte = wrapper[offset]
        hidden.append(byte)
        offset += interval
        
        if byte == SENTINEL[sentinel_index]:
            sentinel_index += 1
            if sentinel_index == len(SENTINEL):
                break
        else:
            sentinel_index = 0

    return hidden[:-len(SENTINEL)]

# store hidden bits in image
def storeBit(wrapper, hidden, offset):
    for byte in hidden + SENTINEL: #combine hidden message and sentinel
        for bit in range(8):
            wrapper[offset] &= 0b11111110 #make sure msg is 8 bits
            wrapper[offset] |= (byte >> (7 - bit)) & 0b00000001
            offset += 1
    return(wrapper)

# get bits from image
def retrieveBit(wrapper, offset):
    hidden = bytearray()
    sentinel_index = 0

    while offset < len(wrapper):
        byte = 0
        for bit in range(8):
            byte = (byte << 1) | (wrapper[offset] & 0b00000001)
            offset += 1

        hidden.append(byte)

        if byte == SENTINEL[sentinel_index]:
            sentinel_index += 1
            if sentinel_index == len(SENTINEL):
                return hidden[:-len(SENTINEL)]
        else:
            sentinel_index = 0

    return hidden

def main():
    # get arguments from command line
    # chatgpt helped here
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true", help="Store data")
    parser.add_argument("-r", action="store_true", help="Retrieve data")
    parser.add_argument("-b", action="store_true", help="Bit mode")
    parser.add_argument("-B", action="store_true", help="Byte mode")
    parser.add_argument("-o", type=int, default=0, help="Offset (default 0)")
    parser.add_argument("-i", type=int, default=1, help="Interval (default 1)")
    parser.add_argument("-w", required=True, help="Wrapper file")
    parser.add_argument("-H", required=False, help="Hidden file")

    args = parser.parse_args()

    # opens file and get bytes
    with open(args.w, "rb") as f:
        wrapper = bytearray(f.read())

    # if store then it stores bytes or bits
    if args.s:
        with open(args.h, "rb") as f:
            hidden = bytearray(f.read())
        if args.B: # bytes
            storeByte(wrapper, hidden, args.o, args.i)
        elif args.b: # bits
            storeBit(wrapper, hidden, args.o)
        # output new file
        sys.stdout.buffer.write(wrapper)

    # retrieve data
    elif args.r:
        if args.B: # bytes
            hidden = retrieveByte(wrapper, args.o, args.i)
        elif args.b: # bits
            hidden = retrieveBit(wrapper, args.o)
        # output retrieved data
        sys.stdout.buffer.write(hidden)

main()
