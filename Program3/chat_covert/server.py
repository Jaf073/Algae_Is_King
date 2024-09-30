# this is a program to set up a chat server i.e. send text
# messages on a specific port to whoever connects to me.
import socket
from time import sleep

# constants
PORT = 7299

#create a socket object and connect it to the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", PORT))

# listen till someone connects
s.listen(0)
print("Server is listening")

try:
    c, addr = s.accept()
except KeyboardInterrupt:
    # print message and exit if someone hits Ctrl+C before
    # a connection is accepted
    print("Server stopped prematurely")
    exit(0)

# set the message
msg = "this is a bunch of random characters"

# send the message
for i in msg:
    c.send(i.encode())
    sleep(0.1)

# send end of message, and close the socket
c.send("EOF".encode())
print("Messae sent...")
c.close()