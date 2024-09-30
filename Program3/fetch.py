from ftplib import FTP

# some ftp details
IP = "localhost"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
USE_PASSIVE = True # set this to False if the connection times out
DEBUG = False

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

