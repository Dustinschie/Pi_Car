#	import socket module
import socket

class Client:
	def __init__(self, host = "10.0.1.6", port = 12345):
		#	Create a socket object
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#	Define the port and host
		self.__host = host
		self.__port = port

		#	connect to the server on pi
		self.s.connect((host, port))
		self.s.sendall('Hello, world')

		#	recieve data from the server
		print self.s.recv(1024)

	def __del__(self):
		print("sending exit signal to to Server")
		self.s.send('exit')
		self.s.close()

	def send(self, controlCode):
		self.s.send(controlCode)

	def receive(self):
		return self.s.recv(1024)

# while True:
# 	temp = str(raw_input("Enter Something: "))
# 	if temp == "exit":
# 		break
# 	s.send(temp)
#	print s.recv(1024)
	
#	s.sendall('exit')
#	close the connection
#	s.close()


