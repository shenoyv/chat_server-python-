import sys
import select
import socket

HOST = '127.0.0.1'
PORT = 8888
BUF_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(" connecting to %s:%s " %(HOST,PORT))
sock.connect ((HOST,PORT))
print(" connected to %s:%s " %(HOST,PORT))
while True:
        sockets_list = [sys.stdin, sock]
        read_sock, write_sock, error_sock = select.select(sockets_list, [], [])
        for read in read_sock:
            if read == sock:
                message = read.recv(BUF_SIZE).decode()
                print(message)
            else:
                message = sys.stdin.readline()
                sock.send(message.encode())
                sys.stdout.write("-->>")
                sys.stdout.write(message)
                sys.stdout.flush()
        if message.lower().strip() == 'exit':
            break
print("closing the connection")
sock.close()


