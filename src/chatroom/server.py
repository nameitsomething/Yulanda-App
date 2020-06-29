from socket import socket
from threading import Thread

class server:

    class worker(Thread):
        def __init__(self, sock: socket):
            Thread.__init__(self)
            self.sock = sock

        def run(self):
            while True:
                data = self.sock.recv(1024)
                self.sock.sendall(data)

    def __init__(self):
        self.sock = socket()
        self.PORT = 12345

    def connect(self):
        self.sock.bind(("", self.PORT))
        self.sock.listen(3)

    def acceptNew(self):
        conn, addr = self.sock.accept()
        client = self.worker(conn)
        client.start()

serv = server()
serv.connect()
serv.acceptNew()
