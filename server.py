import socket
from threading import Thread
import threading
import time
HOST = "10.184.42.72"
PORT = 4010
lock  = threading.Lock()
conns = []

def listen_for_data(conn):
    while True:
        data = conn.recv(1024)
        print(data)

def listen_for_connections(socket):
    while True:
        conn, addr = socket.accept()
        lock.acquire()
        conns.append(conn)
        lock.release()

        t = Thread(target=listen_for_data, args=(conn, ))
        t.start()

def send_data_out(data):
    for i, conn in enumerate(conns):
        try:
            conn.send(data)
        except BrokenPipeError:
            print("[ERROR] BrokenPipeError")
            del conns[i]
        except ConnectionAbortedError:
            print("[ERROR] ConnectionAbortedError")
            del conns[i]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    t1 = Thread(target=listen_for_connections, args=(s, ))
    t1.start()
    
    while True:
        time.sleep(1)
        send_data_out(b"hello there")