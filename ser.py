import sys
import socket
import select
import threading

class Server:

    connections=[]
    clients =[]
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # to reuse the same socket
        self.sock.bind(('0.0.0.0'),8018)
        self.sock.listen(10)
        while  True:
           conn,add_rs = self. sock.accept()
           Thread_s=threading.Thread(target=self.handle_sock, args=(conn,add_rs))
           Thread_s.daemon = True
           Thread_s.start()
           self.connections.append(conn)
           self.clients.append(add_rs[0])
           print(self.connections)

           #print("client: is connected)

    def handle_sock(self,conn,add_rs):
        while True:
            data =conn.recv(1024)
            print data
            for conns in self.connections:
                connections.send(data)
            if not data:

                #print("client_name",disconnected)
                self.connections.remove(conn)
                self.clients.remove(a[0])
                conn.close()
                self.send_clients()
                break
    def send_clients(self):
        cx= ""
        for cls in self.clients:
            cx= cx + "cls" +","

        for conns in self.connections:
            conns.send(b'\x12'+bytes(cx, "utf-8"))





server = Server()
server.go()













