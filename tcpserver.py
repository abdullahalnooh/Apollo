import socket
import threading

ServerIP = "0.0.0.0"
ServerPort = 4444 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ServerIP, ServerPort))
server.listen(3)
print(f"[*] Listening on [any]:{ServerPort} ...")

def handle(client_socket):
    try:
        while True:
            syn = client_socket.recv(1024)
            if not syn:
                break
            print(f"[*] Received: {syn.decode('utf-8')}")
            client_socket.send(b"Message received")
    except ConnectionResetError:
        print("Connection was reset.")
    finally:
        client_socket.close()

while True:
    client, addr = server.accept()
    print(f"[*] Accepted connection from: {addr}")
    clientT = threading.Thread(target=handle, args=(client,))
    clientT.start()
