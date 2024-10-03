from ftplib import FTP

METHOD = 7

# some ftp details
IP = "localhost"
#IP = "138.47.99.83"
PORT = 21
USER = "anonymous"
PASSWORD = ""

# determines folder based on METHOD
if METHOD == 7:
    FOLDER = "/7/"
elif METHOD == 10:
    FOLDER = "/10/"
    
USE_PASSIVE = True # set this to false if the connection times out
DEBUG = False

# main
if (DEBUG):
    print("Logging in...")

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

if (DEBUG):
    print("Logged in.")
    print("Navigating...")

ftp.cwd(FOLDER)
files = []
ftp.retrlines("LIST", files.append) # gets all the files including permissions and appends them to files

# exit the FTP server
ftp.quit()

perms = []
bits = []

def decode(perms):
    for permission in perms:

        # gets rid of the first three bits if the METHOD is 7-bit
        if METHOD == 7:
            permission = permission[3:]

        # dashes (-) are 0 and anything else (r, w, x) is 1
        for c in permission:
            if c == '-':
                bits.append(0)
            else:
                bits.append(1)

    index = 0 # counts every bit
    group = 0 # counts a grouping of bits (7 or 10)
    decrypted = [] # holds the ASCII value after being converted
    temp = "" # holds binary characters until converted

    # iterates through the list and decodes the bits based on METHOD
    while index < len(bits):
        temp += str(bits[index])
        index += 1
        group += 1

        # these decrypt the bits based on the METHOD and grouping
        if METHOD == 7 and group >= 7:
            decrypted += "".join([chr(int(temp, 2))]) # the string is casted to an int, then to a char and added to the list
            temp = "" # resets the string to hold a new group
            group = 0 # resets the group

        if METHOD == 10 and group >= 10:
            decrypted += "".join([chr(int(temp, 2))])
            temp = ""
            group = 0

    # convert the list into a string and print it
    printstr = "".join(decrypted)
    print(printstr)

# iterates through each file in the directory and sorts them
for f in files:
    parts = f.split() # splits up each file line by spaces and puts each part in a list

    permissions = parts[0] # the first element is the permissions

    # these append permissions based on METHOD and whether the first three bits are set or not
    if METHOD == 7 and (permissions[0] == "-" and permissions[1] == "-" and permissions[2] == "-"):
        perms.append(permissions)

    if METHOD == 10:
        perms.append(permissions)

decode(perms)