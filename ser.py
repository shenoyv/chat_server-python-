import socket
from _thread import *

HOST = '127.0.0.1'
PORT = 8888
BUF_SIZE = 2048
list_of_clients = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # to reuse the same socket
print("starting up on %s port %s" % (HOST, PORT))
sock.bind((HOST, PORT))
sock.listen(10)

def clientthread(conn, addr):
	conn.send("chatroom started".encode())
	while True:
			try:
				message = conn.recv(BUF_SIZE).decode()
				if message:
					print ("<" + addr[0]+":"+ str(addr[1]) + "> " + message)

					# Calls broadcast function to send message to all
					message_to_send = "<" + addr[0]+":"+ str(addr[1])  + "> " + message
					broadcast(message_to_send, conn)

				else:
					remove(conn)

			except:
				continue
while True:
    conn, addr = sock.accept()
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print(addr[0] + ":" + str(addr[1]) + " connected")

    # creates and individual thread for every user that connects
    start_new_thread(clientthread, (conn, addr))



def broadcast(message, connection):
	for clients in list_of_clients:
		if clients!=connection:
			try:
				clients.send(message.encode())
			except:
				clients.close()

				# if the link is broken, we remove the client
				remove(clients)

def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

conn.close()
server.close()