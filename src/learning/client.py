from socket import socket

HOST = "3.21.205.199"
PORT = 12345

sock = socket()
sock.connect((HOST, PORT))

data = "Hello from client"
data = str.encode(data)

sock.sendall(data)

data = sock.recv(1024)
data = data.decode()
print(data)

exit(0)