#	import Modules
import socket, re
from Car import Car
import pygame
import time


#	create socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "socket successfully created"

# reserve port and host
host = '' #	host is self; "server"
port = 12345

#	bind port
s.bind((host, port))
print "socket binded to %s" %(port)

#	put socket into listening mode
s.listen(5)
print "socket is listening"

#	Create Instance of Car
car = Car()

#	 endless loop
while True:
	#	establish connection with client
	c, addr = s.accept()
	print 'Got connection from', addr
	data = c.recv(1024)
	if not data or str(data) == "exit": 
		break

	else:
		print str(data)
	#	send a thank you message to the client
	c.send('thank you for connecting ')
	temp = ""
	while True:
		temp = str(c.recv(1024))
		if temp == "exit" or not temp or temp == "":
			break
		temp = ''.join(str(x) for x in set(temp))
		print temp
		car.move(temp)

	#	Close the connection with the client
	c.close()
	if temp == "exit":
		break