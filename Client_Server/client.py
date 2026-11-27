import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def riceviMessaggi(sock):
    # stampa tutto cio che manda il server
    while True:
        try:

            messaggio = sock.recv(1024).decode()
            if not messaggio:
                break
            print(messaggio)

        except:
            print("\003[91mConnessione persa con il server.\003[0m")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( (HOST, PORT) )

    # il target all'interno della Threading e' una callback, cioe non serve inserire le () dopo il richiamo della funzione
    threading.Thread(target=riceviMessaggi, args=(s,), daemon=true).start()