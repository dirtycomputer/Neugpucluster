# import socket
# import json

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect(('localhost', 8003))

# data = {}
# data['DockerFileName'] = 'Django'
# data['DockerBuildPath'] = '../Web'
# data['Port'] = '8000'

# json_data = json.dumps(data)
# s.send(bytes(json_data,encoding="utf8"))
# s.close()

import json
import sys
import ClusterAPI
import time

# task_name = "testTask"
# batch_size = 200
# learning_rate = 0.01
# dataset_url = "http://localhost"
# with open("./test.json","r") as json_file:
# 	json_obj = json.load(json_file)
# network = json.dump(json_obj)

# param = {}
# param['batch_size'] = batch_size
# param['learning_rate'] = learning_rate
# param['dataset_url'] = dataset_url
# param['network'] = network

connect_url = ["localhost:27017"]
cluster = ClusterAPI.Cluster(connect_url)
# cluster.UpdateTaskParam(task_name,param)

cluster.release_lock()
print(cluster.get_lock())
print(cluster.get_lock())
time.sleep(120)
print(cluster.get_lock())