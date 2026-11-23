import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def riceviMessaggi():
    ...

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( (HOST, PORT) )
    threading.Thread().start()