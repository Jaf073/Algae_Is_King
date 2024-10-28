SENTINEL = [0, 16, 0, 0, 16, 0]

def FIND(bits, offset=0, interval=1):
    i=0
    ret = []
    for j in range(offset,len(bits),interval):
        bit = bits[j]
        if bit == SENTINEL[i]: #check if sentinal
            i+=1
        else: #add message to list
            i = 0
        ret.append(bit)
        if i == len(SENTINEL): return(ret[:len(ret)-len(SENTINEL)])
    return(None)

if __name__=='__main__':
    print("Normal")
    bits = [0,0,2,4,5,0,16,0,1,0,16,0,0,16,0,3,5,7]
    print(bits)
    print(FIND(bits))
    print("--None--")
    bits = [0,0,2,4,5,0]
    print(bits)
    print(FIND(bits))
    print("--interval=2--")
    bits = [3,3,3,3,3,3,0,1,16,1,0,1,0,1,16,1,0]
    print(bits)
    print(FIND(bits,0,2))
    print("--interval=1,offset=2--")
    bits = [3,3,3,3,3,0,1,16,1,0,1,0,1,16,1,0]
    print(bits)
    print(FIND(bits,1,2))



    
