import socket

Host = '127.0.0.1'
port = 4444  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((Host, port))
client.send(b'I am CLIENT2')
response = client.recv(1024)
print(f"[*] Server response: {response.decode('utf-8')}")
client.close()
