SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])

def Check(ByteArr):
    new = bytearray([])
    i=0
    for B in ByteArr:
        new.append(B)
        
        if B == SENTINEL[i]:  # Check if sentinel
            i += 1
        elif B==0x0: i=1 #0+0 --go back to pos 1
        elif i==3 and B==SENTINEL[1]: i=2 #0F0+F --go back to OF
        else: i=0 #restart counter
        
        if i==6:
            return(new[:(len(new)-len(SENTINEL))])
        
    return(None)

#Test 1: Normal
BR = bytearray([0x0d, 0x2f, 0x10, 0x30, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00])
print("Given: " + str(BR))
print("Goten: " + str(Check(BR)))
print("")

#Test 2: Sent in middle
BR = bytearray([0x50, 0x2f, 0x10, 0x0a, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00, 0x50, 0x2f, 0x10, 0x020])
print("Given: " + str(BR))
print("Goten: " + str(Check(BR)))
print("")

#Test 3: Part of sent in msg
BR = bytearray([0x00, 0xff, 0x00, 0x00, 0x00, 0xff, 0x00, 0x00, 0xff, 0x00])
print("Given: " + str(BR))
print("Goten: " + str(Check(BR)))
print("")

#Test 4: no sent
BR = bytearray([0x50, 0x2f, 0x10, 0x020, 0x00, 0x00, 0xff, 0x00, 0x50, 0x2f, 0x10, 0x020])
print("Given: " + str(BR))
print("Goten: " + str(Check(BR)))
print("")
            
