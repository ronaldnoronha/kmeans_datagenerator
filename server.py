from sklearn.datasets import make_blobs
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
host = 'localhost'
# host = socket.gethostbyname_ex(socket.gethostname()) #Get the local machine name
print("Host: ", socket.get)
port = 9999 # Reserve a port for your service
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
