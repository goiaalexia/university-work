import socket
import pickle

arr = [1, 10, 4, 5]
data = pickle.dumps(arr)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 7777))
s.send(data)
print(s.recv(4096))
s.close()
