import sys
import select

HOST = '127.0.0.1'
PORT = 8018
TIMEOUT = 5
BUF_SIZE = 1024


class WhatsUpClient():

    def __init__(self, host=HOST, port=PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        #print(" connecting to %s:%s " %(host,port))
        while 1:
            try:
                buf = self.sock.recv(BUF_SIZE)
                sys.stdout.write(buf)
                data = raw_input()
                if cmd.strip() == "KILL_SERVICE":
                    sys.exit(1)
                self.sock.send(data)
            except:
                self.sock.close()

        def run(self):
            pass







