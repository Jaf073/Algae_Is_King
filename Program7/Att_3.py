import sys
import os
from math import floor

#default vals
SENTINEL = [0, 1, 0, 0, 1, 0]
SENTINEL_Byte = [0, 255, 0, 0, 255, 0]
s=True; b=False; offset=0; interval=1; w=''; h=''; error = False; msg = ""

#Optimal Interval
def optInterval(Sw=0, o=0, Sh=0, s=1):
    return floor((Sw-o)/(Sh+s))

#Store data in bytes
def StoreBytes(wB=[], hB=[]): 
    i=0
    while i < len(hB): #store data
        wB[offset] = hB[i]
        offset += interval
        i += 1

    i=0
    while i < len(SENTINEL): #store sentinel
        wB[offset] = SENTINEL[i]
        offset += interval
        i += 1
        
    return wB


#Get Bytes from data
def ExtractBytes(wB=[]):
    global s; global b; global offset; global interval; global w; global h
    H = []
    x=0
    
    while offset<len(wB):
        Byte = wB[offset]

        #Check if Sentinel
        if Byte == SENTINEL_Byte[x]: x += 1
        elif Byte == 0: x = 1                                 
        else: x = 0

        #Check if Sentinel Complete
        if x >= len(SENTINEL_Byte):
                return bytearray(H[:len(H) - len(SENTINEL_Byte)])
        H.append(Byte)
        offset += interval
    return None

def StoreBits(wB=[], hB=[]): 
    i=0
    while i < len(hB): #store data
        for j in range(0,7):
            W[offset] &= 11111110
            W[offset] |= ((hB[i] & 10000000) >> 7)
            hB[i] <<= 1
            offset += interval
        i += 1
        
    i=0
    while i < len(SENTINEL): #store sentinel
        for j in range(0,7):
            W[offset] &= 11111110
            W[offset] |= ((SENTINEL[i] & 10000000) >> 7)
            SENTINEL[i] <<= 1
            offset += interval
        i += 1
    return wB

def ExtractBits(wB=[]):
    H = []
    x=0
    
    while offset<len(wB):
        Byte = 0

        for j in range(0,7):
            Byte |= (wB[offset] &  00000001)
            if j < 7:
                Byte <<= 1
                offset += interval
        
        #Check if Sentinel
        if Byte == SENTINEL_Byte[x]: x += 1
        elif Byte == 0: x = 1                                 
        else: x = 0

        #Check if Sentinel Complete
        if x >= len(SENTINEL_Byte):
                return bytearray(H[:len(H) - len(SENTINEL_Byte)])

        H.append(Byte)
        offset += interval
    return None

#get arguments from command line
def update(): #update values of global variables
    global s; global b; global offset; global interval; global w; global h; global error; global msg

    #check for each arg (yes ik this is inefficient)
    hasO = False
    hasW = False   
    
    for arg in sys.argv:
        #(-sr)
        if arg == "-s":
            s = True
        elif arg == "-r":
            s = False
            
        #(-bB)
        elif arg == '-b':
            b = True
        elif arg == '-B':
            b = False
        
        #(-o)
        elif '-o' in arg:
            offset = int(arg[2:])
            hasO = True

        #([-i])
        elif '-i' in arg:
            interval = int(arg[2:])

        #(-w)
        elif '-w' in arg:
            w = arg[2:]
            hasW = True

        #([-h])
        elif '-h' in arg:
            h = arg[2:]

    #Check for errors
    if "-s" not in sys.argv and "-r" not in sys.argv:
        return (True, "no -s or -r")
    elif "-b" not in sys.argv and "-B" not in sys.argv:
        return (True, "no -b or -B") 
    elif not hasO:
        return (True, "no offset")
    elif not hasW:
        return (True, "no wrapper file")
    #No errors
    else: return (False, "")

def main():
    global s; global b; global offset; global interval; global w; global h; global error; global msg
    
    error, msg = update()

    if error:#break function and return error msg
        print(msg)
        return(False)

    #No Error    
    else:
        # Open the file in binary mode
        with open(w, 'rb') as file:
        # Read the entire file into a variable
            someData = file.read()
            data = bytearray(someData)

        if len(h) > 3:
            #Get Sizes
            Sw = os.path.getsize(w)
            Sh = os.path.getsize(h)
            s = len(SENTINEL)
            optInterval(Sw, o, Sh, s)
            

        if b and s:
            StoreBit(w, h)
        elif b and not s:
            ExtractBit(w)
        elif s and not b:
            StoreByte(w, h)
        else:
            ExtractByte(w)
