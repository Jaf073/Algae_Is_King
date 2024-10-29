from PIL import Image
import sys


def toList(dataType, offset, file):
    # open image in grayscale
    image = Image.open(file).convert("L")
    width, height = image.size
    # set offset
    startY = offset // width
    startX = offset % width
    data = []

    # chatgpt helped with some of this
    # iterates over image
    for y in range(startY, height):
        for x in range(startX if y == startY else 0, width):
            byte_value = image.getpixel((x, y))
    
            if dataType == 'byte':
                data.append(byte_value)
            elif dataType == 'bit':
                bit_value = format(byte_value, '08b')
                data.append(bit_value)

        # reset x after first row
        startX = 0

    # display data collected
    if dataType == 'byte':
        print("byte after offset:", data[:10])
    elif dataType == 'bit':
        print("bit after offset:", data[:10])

    return data


def main():
    # takes command line arguments
    dataType = sys.argv[1]
    offset = int(sys.argv[2])
    file = "stegged-bit.bmp"

    toList(dataType, offset, file)

main()
