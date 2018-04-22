#!/bin/python2
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((sys.argv[1], 1337))

while 1:
    user_input = raw_input("Please enter a string: ")
    sock.send(user_input)
    print sock.recv(1024)

sock.close()