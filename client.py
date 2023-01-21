import socket

HOST = "172.20.10.7"  
PORT = 4006

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024)
        print(data)

print(f"Received {data!r}")