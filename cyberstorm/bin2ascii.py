import sys

def BinaryDecode(code, bit):
    # We first convert the string to an array and remove the newline character
    ar = list(code)
    del ar[-1]
    
    # variable setup #
    decrypted = [] # we will store solved elements of the message here
    tempstr = "" # we will store binary characters here until they are ready to be solved
    group = 0 # this will keep track of if we've reached the bit size
    index = 0 # iterates through the entire array once

    # iterates through the entire array while 
    # repeatedly building chunks of size bit
    while index < len(ar):
        tempstr += ar[index]
        index += 1
        group += 1
        if group >= bit: # this means tempstr is ready to convert
            decrypted += "".join([chr(int(tempstr, 2))]) # we cast the string to an int, then the int to it's respective char
            
            # we clear temstr and group to start again
            tempstr = ""
            group = 0
    
    # we merge the array to a string and print it
    printstr = "".join(decrypted)
    print(printstr)

def main():
    inp = sys.stdin.read()
    print("Seven bit output: ")
    BinaryDecode(inp, 7)
    print()
    print("Eight bit output: ")
    BinaryDecode(inp, 8)

main()