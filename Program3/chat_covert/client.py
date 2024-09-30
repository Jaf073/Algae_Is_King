import socket
from sys import stdout
from time import time

# constants
DEBUG = False
PORT = 7299
IPADDRESS = "localhost"

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
s.connect((IPADDRESS, PORT))

# reveive data
data = s.recv(4096).decode()

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()

    # starting timer
    start = time()
    data = s.recv(4096).decode()
    stop = time()

    delta = round(stop - start, 3)

    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

# close the connection
s.close()