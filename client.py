import socket
import time
from datetime import datetime

s = socket.socket() #create a socket object
# host = socket.gethostname() #Host i.p
host = 'localhost'
port = 9999 #Reserve a port for your service

s.connect((host, port))

input = []

while True:
    data = s.recv(1024)
    # print(data.decode("utf-8"))
    if data == b"":
        break
    input.append(data.decode("utf-8")+','+str(datetime.now()))
    print(data.decode("utf-8")+','+str(datetime.now()))
s.close()
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((host, port))
#     # s.sendall(b'Hello, world')
#     data = s.recv(1024)
#
# print('Received', repr(data))

