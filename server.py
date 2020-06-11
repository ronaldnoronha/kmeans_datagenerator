from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import time
from datetime import datetime
import socket #import socket module

def create_data(n_samples, n_features, centers, std):
    features, target = make_blobs(n_samples = n_samples,
                                  # two feature variables,
                                  n_features = n_features,
                                  # four clusters,
                                  centers = centers,
                                  # with .65 cluster standard deviation,
                                  cluster_std = std,
                                  # shuffled,
                                  shuffle = True)
    return features, target

features, target = create_data(100,3,8,0.65)

s = socket.socket() #Create a socket object
host = socket.gethostname() #Get the local machine name
port = 12397 # Reserve a port for your service
s.bind((host,port)) #Bind to the port

s.listen() #Wait for the client connection
while True:
    c,addr = s.accept() #Establish a connection with the client
    print("Got connection from"+ str(addr))
    for i in range(len(features)):
        message = str(datetime.now())+','+ str(features[i])+','+str(target[i])
        print(f'Send: {message!r}')
        c.send(message.encode())
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
