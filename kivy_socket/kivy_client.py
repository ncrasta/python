import socket
import json
from json import JSONEncoder
import numpy as np
import time


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


class NumpyArrayEncoder(JSONEncoder):
	# To sereialize the dictionary for the socket
	def default(self, obj):
		if isinstance(obj, np.ndarray):
			return obj.tolist()
		return JSONEncoder.default(self, obj)


try:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)
	print(f"Connected to server {SERVER}")
except IOError:
	print("Undefined Connection Error Encountered")
	input("Press Enter to exit, then restart the script")
	sys.exit()


def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))


if __name__ == "__main__":
	# Later data will be sent from SORT algo
	for i in range(np.random.randint(10)):
		data = {'ID':{0:1,1:2,2:3,3:4},
	            'Position [m]':{0:(1, 0, 0),1:(0, 1, 0),2:(0,0,1),3:(1,1,1)},
	            'Velocity [m/s]':{0:(0, 0, 0),1:(0, 0, 0),2:(0, 0, 0),3:(0, 0, 0)},
	            'Distance [m]':{0:1,1:1,2:1,3:round(np.linalg.norm([1,1,1]),2)},
	            'Warning':{0:'close',1:'fast',2:'None',3:'close and fast'},
	            }
		data_string = json.dumps(data, cls=NumpyArrayEncoder)
		send(data_string)
		time.sleep(1)
