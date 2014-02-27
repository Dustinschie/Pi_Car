# import io
# import socket
# import struct
# from PIL import Image

# # Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
# # all interfaces)
# server_socket = socket.socket()
# server_socket.bind(('', 8000))
# server_socket.listen(0)

# # Accept a single connection and make a file-like object out of it
# connection = server_socket.accept()[0].makefile('rb')
# try:
#     while True:
#         # Read the length of the image as a 32-bit unsigned int. If the
#         # length is zero, quit the loop
#         image_len = struct.unpack('<L', connection.read(4))[0]
#         if not image_len:
#         	print 'hello'
#            	break
#         # Construct a stream to hold the image data and read the image
#         # data from the connection
#         image_stream = io.BytesIO()
#         image_stream.write(connection.read(image_len))
#         # Rewind the stream, open it as an image with PIL and do some
#         # processing on it
#         image_stream.seek(0)
#         image = Image.open(image_stream)
#         print('Image is %dx%d' % image.size)
#         image.verify()
#         print('Image is verified')
# finally:
#     connection.close()
#     server_socket.close()


                
#   import socket module
import socket, cv2, numpy as np, cPickle as pickle

class Client:
    def __init__(self, host = "10.0.1.6", port = 12345):
        #   Create a socket object
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #   Define the port and host
        self.__host = host
        self.__port = port

        #   connect to the server on pi
        self.s.connect((host, port))
        self.s.sendall('Hello, world')

        #   recieve data from the server
        # print pickle.loads(self.receive())

    def __del__(self):
        print("sending exit signal to to Server")
        self.s.send('exit')
        self.s.close()

    def send(self, controlCode):
        self.s.send(controlCode)

    def receive(self):
        size = int(self.s.recv(1024))
        print size
        data = self.s.recv(size)

        return data

    def showImage(self):
        # cv2.imshow('temp', pickle.loads(self.receive()))
        # print pickle.loads(self.receive())
        print pickle.loads(self.receive())


# while True:
#   temp = str(raw_input("Enter Something: "))
#   if temp == "exit":
#       break
#   s.send(temp)
#   print s.recv(1024)
    
#   s.sendall('exit')
#   close the connection
#   s.close()


temp = Client()
temp.showImage()