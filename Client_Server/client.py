import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def riceviMessaggi():
    ...

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( (HOST, PORT) )

    # il target all'interno della Threading è una callback, cioe non serve inserire le () dopo il richiamo della funzione
    threading.Thread(target=riceviMessaggi, args=(s,), daemon=true).start()