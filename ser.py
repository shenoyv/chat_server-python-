import sys
import socket
import select
import threading

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#to reuse the same socket
    connections=[]
    def __init__(self):
        self.sock.bind(('0.0.0.0'),8018)
        self.sock.listen(10)
    def handle_sock(self,conn,add_rs):
        while True:
            data =conn.recv(1024)
            print data
            for conns in self.connections:
                connections.send(data)
            if not data:
               break
    












