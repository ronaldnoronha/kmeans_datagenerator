import socket #import socket module

s = socket.socket() #create a socket object
host = socket.gethostname() #Host i.p
port = 12397 #Reserve a port for your service

s.connect((host, port))

while True:
    data = s.recv(1024)
    print(repr(data))
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((host, port))
#     # s.sendall(b'Hello, world')
#     data = s.recv(1024)
#
# print('Received', repr(data))

