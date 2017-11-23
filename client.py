import sys
import select
import socket
import threading

#HOST = '127.0.0.1'
#PORT = 8018
#TIMEOUT = 5
#BUF_SIZE = 1024
class Client():

    def __init__(self, host=HOST, port=PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.connect((host, port))
        #print(" connecting to %s:%s " %(host,port))
        while True:

