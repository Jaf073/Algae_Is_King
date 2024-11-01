import argparse
import sys

# Define sentinel
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])

def store_byte_method(wrapper, hidden, offset, interval):
    i = 0
    while i < len(hidden):
        wrapper[offset] = hidden[i]
        offset += interval
        i += 1

    for byte in SENTINEL:
        wrapper[offset] = byte
        offset += interval

def retrieve_byte_method(wrapper, offset, interval):
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

def store_bit_method(wrapper, hidden, offset):
    for byte in hidden + SENTINEL:
        for bit in range(8):
            wrapper[offset] &= 0b11111110
            wrapper[offset] |= (byte >> (7 - bit)) & 0b00000001
            offset += 1

def retrieve_bit_method(wrapper, offset):
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true", help="Store data")
    parser.add_argument("-r", action="store_true", help="Retrieve data")
    parser.add_argument("-b", action="store_true", help="Bit mode")
    parser.add_argument("-B", action="store_true", help="Byte mode")
    parser.add_argument("-o", type=int, default=0, help="Offset (default 0)")
    parser.add_argument("-i", type=int, default=1, help="Interval (default 1)")
    parser.add_argument("-w", required=True, help="Wrapper file")
    #parser.add_argument("-h", help="Hidden file")

    args = parser.parse_args()

    with open(args.w, "rb") as f:
        wrapper = bytearray(f.read())

    if args.s:
        with open(args.h, "rb") as f:
            hidden = bytearray(f.read())
        if args.B:
            store_byte_method(wrapper, hidden, args.o, args.i)
        elif args.b:
            store_bit_method(wrapper, hidden, args.o)
        sys.stdout.buffer.write(wrapper)

    elif args.r:
        if args.B:
            hidden = retrieve_byte_method(wrapper, args.o, args.i)
        elif args.b:
            hidden = retrieve_bit_method(wrapper, args.o)
        sys.stdout.buffer.write(hidden)
main()
