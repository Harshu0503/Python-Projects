import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))
    print("Connected to server.")

    while True:
        message = input("Your message: ")
        client_socket.send(message.encode('utf-8'))

        reply = client_socket.recv(1024).decode('utf-8')
        print(f"Received reply: {reply}")

if __name__ == "__main__":
    start_client()
