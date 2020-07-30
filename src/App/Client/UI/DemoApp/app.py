import struct
from tkinter import *
from socket import socket, error, timeout
from threading import *


HOST = ""
PORT = 12345

running = True
conn = socket()

class Window:

    def __init__(self, tk: Tk, conn: socket):
        self.tk = tk
        self.conn = conn

    def get_student_info(self):
        pass

    def update_student_present(self):
        pass

if __name__ == "__main__":
    conn.connect((HOST, PORT))
    root = Tk()
    temp = int.from_bytes(conn.recv(64))
    if temp == 1:
        temp = str.encode(f"user123,12346")
        conn.sendall(temp)
        win = Window(root, conn)
        while running:
            root.update()
            root.update_idletasks()
    else:
        print("oopsie")
        exit(0)


