import socket
import sys

def main():
    #internet socket-> internet communication ->IPv4 (AF_INET)
    try:
        server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #STREAM ->connection , TCP 
    except OSError as e:
        print(f"Failed to create socket: {e}")
        sys.exit(1)
    #return socket object
    print(f"Socket Object created for server.")

    address_tuple=("0.0.0.0",8080)
    try:
        server.bind(address_tuple)  #tells OS to reserve this IP address+ port combo for this socket
    except OSError as e:
        print(f"Bind failed on {address_tuple}: {e}")
        server.close()
        sys.exit(1)

    try:
        server.listen(5)  # kernel starts listening, max 5 queued connections
    except OSError as e:
        print(f"Listen failed: {e}")
        server.close()
        sys.exit(1)

    print("Server is listening on port 8080...")    #tells OS kernet to start listening for reserve address traffic and maximum of 5 connections allowed in a queue

    try:
        while True:
            try:
                conn_to_client, address_of_client = server.accept()
            except OSError as e:
                print(f"Error accepting connection: {e}")
                continue  # don't crash the whole server over one bad accept

            print(f"\nConnection accepted from client: {address_of_client}")
            
            try:
                data = conn_to_client.recv(1024)  # up to 1024 bytes from the client

                if not data:
                    print(f"Client {address_of_client} disconnected without sending data.")
                else:
                    try:
                        print(f"Data received from client {address_of_client}: {data.decode()}")
                    except UnicodeDecodeError as e:
                        print(f"Could not decode data from {address_of_client}: {e}")

                    try:
                        conn_to_client.send("\nMessage from server".encode())
                    except OSError as e:
                        print(f"Error sending to {address_of_client}: {e}")

            except OSError as e:
                print(f"Error communicating with {address_of_client}: {e}")

            finally:
                conn_to_client.close()  # always close, even if recv/send failed
    except KeyboardInterrupt:
        print("\nServer shutting down (Ctrl+C received).")

    finally:
        server.close()

if __name__ == "__main__":
    main()

    
   

