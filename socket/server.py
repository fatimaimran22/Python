import socket

#internet socket-> internet communication ->IPv4 (AF_INET)
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #STREAM ->connection , TCP 
#return socket object
print(f"Socket Object created for server.")

address_tuple=("0.0.0.0",8080)
server.bind(address_tuple)  #tells OS to reserve this IP address+ port combo for this socket

server.listen(5)    #tells OS kernet to start listening for reserve address traffic and maximum of 5 connections allowed in a queue

while True:
    conn_to_client, address_of_client=server.accept()
    print(f"\nSocket Object created for client.")

    data=conn_to_client.recv(1024)  #receive upto 1024 bytes of data from the client
    print(f"\nData received from client: {address_of_client} is: {data.decode()}")  #decode byte->string
    
    conn_to_client.send("\nMessage from server".encode())   #encode string->byte

    conn_to_client.close()

   

