import sys
import socket
import select

HOST = ''
SOCKET_LIST = []
RECV_BUFFER = 4096
PORT = 9009

class Serv_chat(Threading.thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.ip = self.addr[0]
        self.name = ''

    def Chatroom(self, room_name, msg):
        global rooms
        # if the group does not exist, create it
        rooms.setdefault(room_name, set())

        # if current user is a member of the group
        if (self.conn, self.addr) in rooms[room_name]:
            self.broadcast(msg, rooms[room_name])
        else:

               print("You are currently a member of group `%s`"% (room_name,))

    def join(self,room_name):
        global rooms
        rooms[group_name].add((self.conn, self.addr))
        print("## You have joined the group `%s`" %
                             (group_name,))





    def leave(self):





    def broadcast(self):


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(10)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(sock)
    while True:
        current_connection, address = sock.accept()
        while True:
            data = current_connection.recv(2048)

            if data == 'KILL_SERVICE\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                break

            elif data == 'stop\r\n':
                current_connection.shutdown(1)
                current_connection.close()
                exit()

            elif data:
                current_connection.send(data)
                print data



