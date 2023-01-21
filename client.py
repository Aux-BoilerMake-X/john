import socket
import random
HOST = "10.184.42.72"
PORT = 4010
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        print(data)
        if random.randint(0, 5) == 3:
            s.sendall(b"Hello from client")
            print("sending data to server")







