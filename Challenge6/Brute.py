def make():
    need = "bf767" 
    salt = "salt"

    #lowercase
    for q in range(48, 123):
        for w in range(48, 123):
            for e in range(48, 123):
                for r in range(48, 123):
                    for t in range(48, 123):
                        salt+= str(chr(q)) + str(chr(w)) + str(chr(e)) + str(chr(r)) + str(chr(t))
                        print(salt)
                        salt = "salt"
        

make()
