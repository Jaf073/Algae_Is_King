# we create an array equivalent to an ascii table

#we must first take in input from the command line

# we then split the string into 8 char arrays

# we convert the eight character array into a value using a binary conversion 

# we add the corresponded element of the ascii array to a blank string
# IF the value is equal to 8 (backspace), we subtract from the array

# we output the string using stdout

# repeat the process using 7 char arrays

# to this end, we'll build the functionality into a function that takes the amount of characters as an argument

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

    # we need to split into chunks of size bit
    while index < len(ar):
        tempstr += ar[index]
        index += 1
        group += 1
        if group >= bit: # this means tempstring has the character in binary
            # FIXME: I don't know if this works with backspace, we can hardcode an if statement if it doesn't
            decrypted += "".join([chr(int(tempstr, 2))]) # we cast the string to an int, then the int to it's respective char
            
            tempstr = ""
            group = 0
    printstr = "".join(decrypted)
    print(printstr)

def main():
    inp = sys.stdin.read()
    BinaryDecode(inp, 7)
    BinaryDecode(inp, 8)


main()

