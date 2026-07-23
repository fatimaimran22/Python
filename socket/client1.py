import socket
import sys

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except OSError as e:
        print(f"Failed to create socket: {e}")
        sys.exit(1)

    server_address = ("127.0.0.1", 8080)

    try:
        client.connect(server_address)
    except ConnectionRefusedError:
        print(f"Connection refused — is the server running on {server_address}?")
        client.close()
        sys.exit(1)
    except OSError as e:
        print(f"Failed to connect to {server_address}: {e}")
        client.close()
        sys.exit(1)

    try:
        message = "Message from Client 1"
        client.send(message.encode())
    except OSError as e:
        print(f"Error sending data: {e}")
        client.close()
        sys.exit(1)

    try:
        data_from_server = client.recv(1024)

        if not data_from_server:
            print("Server closed the connection without sending data.")
        else:
            try:
                print(f"Data from server: {data_from_server.decode()}")
            except UnicodeDecodeError as e:
                print(f"Could not decode server data: {e}")
                print(f"Raw bytes: {data_from_server}")

    except OSError as e:
        print(f"Error receiving data: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()