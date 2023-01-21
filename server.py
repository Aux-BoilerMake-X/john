import socket
from queue import Queue
from threading import Thread
import threading
import time

HOST = "172.20.10.7"
PORT = 4006

lock  = threading.Lock()
conns = []

def producer(out_q, socket):
    while True:
        conn, addr = s.accept()

        lock.acquire()
        conns.append(conn)
        lock.release()
        
def consumer(in_q, socket):
    while True:
        time.sleep(1)
        for conn in conns:
            try:
                conn.send(b"hello")
            except BrokenPipeError:
                print("[ERROR] BrokenPipeError")
          
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    q = Queue()
    t1 = Thread(target=consumer, args=(q, s))
    t2 = Thread(target=producer, args=(q, s))
    t1.start()
    t2.start()

    while True:
        pass
