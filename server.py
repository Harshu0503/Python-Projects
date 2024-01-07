import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(1)
    print("Server listening on port 5555...")

    client_socket, address = server.accept()
    print(f"Accepted connection from {address}")

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            print(f"Connection with {address} closed.")
            break
        print(f"Received message from {address}: {message}")

        reply = input("Your reply: ")
        client_socket.send(reply.encode('utf-8'))

    server.close()

if __name__ == "__main__":
    start_server()
