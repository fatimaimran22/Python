import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(("127.0.0.1",8080))

client.send("Message from Client 2".encode())

data_from_server=client.recv(1024)
print(f"Data from server: {data_from_server}")