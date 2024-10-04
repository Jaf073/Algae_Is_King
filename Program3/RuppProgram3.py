from ftplib import FTP

# some ftp details
IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set this to False if the connection times out
DEBUG = False
METHOD = 7

if METHOD == 7:
    FOLDER = "/7/"
if METHOD == 10:
    FOLDER = "/10/"

# main
if (DEBUG):
    print("Logging in...")
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

if (DEBUG):
    print("Logged int.")
    print("Navigating...")

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the ftp server
ftp.quit()

# display the folder contents
for f in files:
    print(f)

# create a new list that contains just the permissions
perms = []
for f in files:
    perms.append(files.split()[0])
    
# print out perms if needed
if (DEBUG):
    print("File perms: ")
    print(perms + "\n")

if METHOD == 7:
    # create a list of files used in secret message
    secret = []
    # determine the files used in the secret message
    for p in perms:    
        secret.append[p]
    
    # print out secret files if needed
    if (DEBUG):
        print(secret)
    
    # create a list for the binary 
    binary = []
    # convert the permissions into binary
    for p in perms:
        # temp variable to store the binary as a string
        temp = ''
        for i in p:
            if p == '-':
                temp += '0'
            else:
                temp += '1'
        binary.append(temp)
    
    # print out binary if needed
    if (DEBUG):
        print(binary)
        
    # make string for decoded secret message
    message = ''
    
    # convert binary to ascii and add to message
    for b in binary:
        message += chr(b)
    
    # print secret message
    print(message)
    

if METHOD == 10:
    # create a list of files used in secret message
    secret = []
    # determine the files used in the secret message
    for p in perms:
        if p[0] == '-' and p[1] == '-' and p[2] == '-':
            secret.append[p[3:]]
    
    # print out secret files if needed
    if (DEBUG):
        print(secret)
    
    # create a list for the binary 
    binary = []
    # convert the permissions into binary
    for p in perms:
        # temp variable to store the binary as a string
        temp = ''
        for i in p:
            if p == '-':
                temp += '0'
            else:
                temp += '1'
        binary.append(temp)
    
    # print out binary if needed
    if (DEBUG):
        print(binary)
        
    # make string for decoded secret message
    message = ''
    
    # convert binary to ascii and add to message
    for b in binary:
        message += chr(b)
    
    # print secret message
    print(message)
    
