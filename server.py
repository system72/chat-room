#!/usr/bin/env python 

""" 
A sorta simple echo server
""" 

import msvcrt
import socket
import time

p = """Please use the pass code (close) to close the program"""
print(p)

User = socket.gethostbyname('localhost')

host = '' 
port = 41509
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
client, address = s.accept()
while 1: 
    data = client.recv(size)
    print(data)
    packet = raw_input(User + ":")
    if(packet == "close"):
        break
    client.send(packet)


client.close()
s.close()
time.sleep(5)





