from socket import socket

HOST = ""
PORT = 12345

conn = socket()
conn.connect((HOST,PORT))

test_counter = 0

if __name__ == "__main__":

    # --- Login Sequence ---
    temp = int.from_bytes(conn.recv(64))
    if temp == 1:
        temp = str.encode("jet123,12345")
        conn.sendall(temp)
        temp = conn.recv(128)
        if temp.decode() == "posak":  # ---- End Login Sequence ----
            pass
