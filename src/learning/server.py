from socket import socket

sock = socket()

PORT = 12345

sock.bind(("", PORT))

sock.listen(2)
client, addr = sock.accept()

data = client.recv(1024)
data = data.decode()

print(data)

data = "Hello from server"
data = str.encode(data)

client.sendall(data)
exit(0)