# Name: Tommy Wallace
# Date: 9/28/24
# Description: My version of Program 1 for CSC 442

import fileinput

# Converts a list of binary numbers into ascii values into a string
def convert(bList, x):
    tempList = []
    tempStr = ''
    asciiStr = ''       # final string of chars
    # for each binary number
    for bit in bList:
        tempList.append(bit)
        if len(tempList) == x:
            tempStr = ''.join(tempList)         # moves the contents from tempList into tempStr
            asciiStr += chr(int(tempStr, 2))    # converts the binary from tempStr into chars and appends them to asciiStr
            tempStr = ''
            tempList = []
    return asciiStr

count = 0

# Sends binary from stdin into a list
binList = []
for line in list(fileinput.input()):
    binList = line

binList = binList[:-1] # removes newline from binList

# count the number of bits
for num in binList:
    count += 1

# if count is divisible by 7 then convert from 7-bit, else if count is divisble by 8 then convert from 8-bit
if count % 7 == 0:
    print(convert(binList, 7))
elif count % 8 == 0:
    print(convert (binList, 8))
