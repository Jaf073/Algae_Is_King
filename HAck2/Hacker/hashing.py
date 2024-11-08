def pass_hash(password):
    length = len(password)
    string = ""
    
    while len(password) < 12:
        password = '\xbb' + password
        #print(password)

    #print(password)
    #for c in enumerate(password):
        #print (c)
        #print(str(ord(c[1])))
        #print(chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb)))
        #string += chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))
        #print(chr(29, x, 251))
    
    #print (string)
    #return (string)
    return "".join([chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))  for c in enumerate(password)])

def main():
    file_path = "bad_passwords.txt"
    binaryfile = "hashes.bin" 
    words_list = []
    ALL = []
    decoded_hashes = []

    with open(binaryfile, 'rb') as binary_file:
        # Read the entire binary file
        content = binary_file.read()
    
    for i in content:
       # print(ch# Split content by the stop byte (0xFF)
        hashes = content.split()

        # Decode bytes to string and filter out empty hashes
        for hash in hashes:
            decoded_hashes.append(hash.decode('utf-8'))
        
        newline = []
        for i in decoded_hashes:
            texx = ""
            for c in i:
                if c == 'ÿ':
                    newline.append(texx)
                else:
                    texx += c


    with open(file_path, 'r') as file:
            for line in file:
                # Strip leading/trailing whitespace and split line into words
                words = line.strip().split()
                words_list.extend(words)
    
    for i in words_list:
        new = pass_hash(i)
        ALL.append(new)
        if new in newline:
            print("FOUND: " + str(i))
        #print(new)

    print("HASHED")
    print(ALL)
    print("------------------------")
    print("Given")
    print(newline)
    print("Done")
    print()
    print()
    
main()
