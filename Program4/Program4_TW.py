# Name: Tommy Wallace
# Date: 10/5/24
# Description: My version of Program 4 for CSC 442
import socket
from sys import stdout
from time import time

# My convert function pulled from my version of Program 1
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


# constants
DEBUG = False
PORT = 31337
IPADDRESS = "138.47.99.83"

# list of delay times in between each character sent
delayTimes = []

# list of binary numbers based on delay times
binList = []

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
print("[connect to the chat server]\n...")
s.connect((IPADDRESS, PORT))

# receive data
data = s.recv(4096).decode()

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()

    # starting timer
    start = time()
    data = s.recv(4096).decode()
    stop = time()

    delta = round(stop - start, 3)
    delayTimes.append(delta)

    if (DEBUG):
        stdout.write(" {}\n" .format(delta))
        stdout.flush()

# close the connection
print("...\n[disconnect from the chat server]")
s.close()

# for each short delay time add a 0 to binry List or for each long delay time add a 1
for t in delayTimes:
    if t < 0.05:
        binList.append("0")
    else:
        binList.append("1")

# delete EOF\n from the binary list
binList = binList[:-28]

# decode and print binList
print("Covert message:", convert(binList,8))
