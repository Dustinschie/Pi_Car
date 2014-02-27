import os

clientIP = raw_input("Enter client's IP address: ")

command = ["raspivid -t 999999 -fps 15  -w 480 -h 272 -o - | nc",  "5001"]

os.system(command[0] + " " + clientIP + " " + command[1])
