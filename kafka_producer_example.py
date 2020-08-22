from time import sleep
from json import dumps
from kafka import KafkaProducer
from sklearn.datasets import make_blobs
from datetime import datetime
import sys


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

features, target = create_data(10000,3,8,0.65)


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = lambda x: dumps(x).encode('utf-8'))



for i in range(len(features)):
    message = str(datetime.now()) + ','
    for j in features[i]:
        message += str(j)+' '
    message = message.strip()
    message += ','+str(target[i])

    # message = str(datetime.now()) + ',' + str(features[i]) + ',' + str(target[i])
    print(message)
    producer.send('test',value=message)
    sleep(1)



#
# for e in range(1000):
#     data = {'number':e}
#     producer.send('test', value=data)
#     sleep(1)
