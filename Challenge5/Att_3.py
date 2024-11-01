import sys
import os
from math import floor

#default vals
SENTINEL = [0, 1, 0, 0, 1, 0]
SENTINEL_Byte = [0, 255, 0, 0, 255, 0]
s=True; b=False; offset=1024; interval=1; w=''; h=''; error = False; msg = ""

#Optimal Interval
def optInterval(Sw=0, o=0, Sh=0, s=1):
    return floor((Sw-o)/(Sh+s))

#Store data in bytes
def StoreBytes(offset=0, interval=1, wB=[], hB=[]): 
    i=0
    while i < len(hB): #store data
        wB[offset] = H[i]
        offset += interval
        i += 1

    i=0
    while i < len(SENTINEL): #store sentinel
        wB[offset] = SENTINEL[i]
        offset += interval
        i += 1
        
    return wB


#Get Bytes from data
def ExtractBytes(offset=0, interval=1, wB=[]):
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
                return bytearray(ret[:len(ret) - len(SENTINEL_Byte)])
            
        offset += interval
    return None

#Test cases
o=1024
w = 'stegged-byte.bmp'
h = 'stegged-byte.bmp'
Sw = os.path.getsize(w)
Sh = os.path.getsize(h)
s = len(SENTINEL)

#test interval
#print(optInterval(19334874, 1024, 15827, 6))

#I = optInterval(Sw, o, Sh, w)
