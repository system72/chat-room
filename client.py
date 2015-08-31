#!/usr/bin/env python 

""" 
A sorta simple echo client 
"""

import msvcrt
import socket
import time
import shutil
import sys

User = ([(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])

p = """Please use the pass code (close) to close the program"""
print(p)

host = '10.20.1.99'   #will need to change
port = 41509
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port))
while 1:
    data = raw_input(User + ":")
    if(data == "close"):
        break
    s.send(User + ": " + data) 
    data = s.recv(size)
    print(data)
    

s.close()
client.close()
time.sleep(5)




