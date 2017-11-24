import sys
import select
import socket
import threading

#HOST = '127.0.0.1'
#PORT = 8018
#TIMEOUT = 5
#BUF_SIZE = 1024
class Client():
    def chat(self,sock):
        while True:
            sock.send(bytes(inputs(""),'utf-8'))

    def __init__(self, add_rs):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.connect((host, port))
        #print(" connecting to %s:%s " %(host,port))
        sock.connect ((addr_s,8018))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        thread_v=Threading.thread(target=self.chat,args=(sock,))
        thread_v.daemon=True
        ithread.start()

        while True:
            data=sock.recieve(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                print("got clients")
            else:
                print(str(data, 'utf-8'))
if (len(sys.argv)>1):
    client=Client(sys.argv[1])




