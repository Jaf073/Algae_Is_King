        #print(str(ord(c[1])))
        #print(chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb)))
        #string += chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))
        #print(chr(29, x, 251))

    #print (string)
    #return (string)
    return "".join([chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))  for c in enumerate(password)])

def main():
    file_path = "bad_passwords.txt"
    words_list = []
    binaryfile = "hashes.bin"

    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and split line into words
            words = line.strip().split()
            words_list.extend(words)
    for i in words_list:
        print(pass_hash(i))

    with open(binaryfile, 'rb') as binary_file:
        # Read the entire binary file
        content = binary_file.read()
    print(content)
main()
"hashing.py" 33L, 949B                                        32,27         Bot

