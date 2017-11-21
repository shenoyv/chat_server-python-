import sys
import socket
import select


def chat_client():
    if (len(sys.argv) < 3):
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    def chat_client():
        if (len(sys.argv) < 3):
            print 'Usage : python chat_client.py hostname port'
            sys.exit()

        host = sys.argv[1]
        port = int(sys.argv[2])

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        while 1:
            socket_list = [sys.stdin, s]

