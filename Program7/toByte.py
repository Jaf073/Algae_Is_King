def toByte(data):
    Some=""
    count = 0
    Bytes = []
    #make data % by 4
    while len(data)%4 != 0:
        data.append(0)
    #print(data)
    
    for B in data:
        Some += str(B)
        count += 1
        if count == 8:
            #print(Some)
            Bytes.append(hex(int(Some,2)))
            Some = ""
            count = 0
    return(Bytes)

print(toByte([1,1,1,1,1,0,0,1,0,1,0,1,1]))
        
