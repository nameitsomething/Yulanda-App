from Utils.School import School
from Utils.Student import Student
from Utils.Course import Course
from socket import socket
from threading import *
import struct

HOST = ''
PORT = 12345
server_soc = socket()
school = School()
running = True
clients = []


class Jetson(Thread):
    def __init__(self, conn: socket):
        Thread.__init__(self)
        self.conn = conn
        self.running = True

    def run(self):
        while self.running:
            self.wait_for_response()

    def wait_for_response(self):
        # In here put code for Jetson requests/Signals
        # Jetson can send information to the school in here

        pass


class User(Thread):
    def __init__(self, conn: socket):
        Thread.__init__(self)
        self.conn = conn
        self.running = True

    def run(self):
        while self.running:
            self.wait_for_request()

    def wait_for_request(self):
        # In here put code for user requests
        # User can request information from the School class through numerical commands

        pass


def login(conn: socket):
    conn.sendall(struct.pack("B", 1))
    data = conn.recv(128).decode().split(",")

    if data[0] == "jet123" and data[1] == "12345":
        temp = Jetson(conn)
        temp.start()
        return temp
    elif data[0] == "user123" and data[1] == "12346":
        temp = User(conn)
        temp.start()
        return temp


if __name__ == '__main__':
    server_soc.bind((HOST, PORT))
    server_soc.listen(4)

    while running:
        conn, addr = server_soc.accept()
        clients.append(login(conn))

