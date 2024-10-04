from ftplib import FTP

# some ftp details
IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/10/"
METHOD = 10
USE_PASSIVE = False  #set to False if the connection times out
DEBUG = False

###### Main #######

if (DEBUG):
    print("Logging in...")
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

if (DEBUG):
    print("Logged in.")
    print("Nagvigating...")

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the ftp server
ftp.quit()
if (DEBUG):
    print("Logged out.")

# display the folder contents
if (DEBUG):
    print("Printing the files in this directory: ")
    for f in files:
        print(f)

# split files into a list of only the permissions
filePerm = []
for f in files:
    x = f.split()
    filePerm.append(x[0])
if (DEBUG):
    print("These are the file permission of the files: ")
    print(filePerm)

# find the hidden message based on number of bits used to decode the message
if (METHOD == 7):
    if (DEBUG):
        print("Finding the message in the left most 7 bits of the file permissions: ")
   
    # filtering the files to only use the ones that hide the message
    filePermUsed = []
    for file in filePerm:
        if (file[0] == "-" and file[1] == "-" and file[2] == "-"):
            filePermUsed.append(file)
    if (DEBUG):
        print("These are the files used in hidding the message: ")
        print(filePermUsed)
 
    # converting the permissions into binary
    binary = ""
    for file in filePermUsed:
        for bit in file:
            if (bit == "-"):
                binary += "0"
            else:
                binary += "1"
        binary += " "
    
    # spliting the string binary into a list to then convert to ascii
    binaryList = binary.split()
    
    if (DEBUG):
        print("These are the file permissions in binary form: ")
        print(binaryList)
    
    # converting the binary to ascii to find the hidden message
    message = ""
    for b in binaryList:
       message += chr(int(b, 2))
    print(message)

elif (METHOD == 10):
    if (DEBUG):
        print("Finding the message in all 10 bits of the file permissions: ")
    
    # converting the permissions of the file into binary form
    binary = ""
    for file in filePerm:
        for bit in file:
            if (bit == "-"):
                binary += "0"
            else:
                binary += "1"
 
    # splitting the binary string into lists of 7 bit chuncks 
    n = 7
    binaryList = [binary[i:i+n] for i in range(0, len(binary), n)]
    if (DEBUG):
        print("These are the file permissions in binary form: ")
        print(binaryList)

    # decoding the binary into ascii characters to find the message
    message = ""
    for b in binaryList:
       message += chr(int(b, 2))
    print(message)



