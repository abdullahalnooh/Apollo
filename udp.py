import socket

Host = '127.0.0.1'
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'hello', (Host, port))

data, addr = client.recvfrom(4096)  
print(f"Received from server: {data.decode()}")
print(f"Server address: {addr}")
