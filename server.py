### Server to publish time

import socket
from datetime import datetime
import time

s = socket.socket() #Create a socket object
host = socket.gethostname() #Get the local machine name
port = 12397 # Reserve a port for your service
s.bind((host,port)) #Bind to the port
counter = 10**2

s.listen() #Wait for the client connection
while True:
    c,addr = s.accept() #Establish a connection with the client
    print("Got connection from"+ str(addr))
    for i in range(counter):
        message = str(datetime.now())
        print(f'Send: {message!r}')
        c.send(message.encode())
        time.sleep(1)
    c.close()


# import socket
# import time
#
# host = socket.gethostname()  # Standard loopback interface address (localhost)
# port = 12397        # Port to listen on (non-privileged ports are > 1023)
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((host, port))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         conn.send(b'Hello World')
#         while True:
#             time.sleep(1)
#             # data =  conn.recv(1024)
#             # if not data:
#             #     break
#             conn.sendall(b'Hello World')
