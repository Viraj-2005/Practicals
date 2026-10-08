import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server started. Waiting for clients...")

def handle_client(conn, addr):
    print(f"Connected with {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break

        message = data.decode()
        if message.lower() == "exit":
            break

        print(f"Client {addr} says: {message}")
        conn.send(data)
    conn.close()
    print(f"Connection closed : {addr}")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target = handle_client, args = (conn, addr))
    thread.start()


