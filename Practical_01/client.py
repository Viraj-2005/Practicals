import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server. Type 'exit' to quit.")

while True:
    message = input("You: ")
    client.send(message.encode())
    
    if message.lower() == "exit":
        break
    
    response = client.recv(1024).decode()
    print(f"Server: {response}")

client.close()
print("Connection closed.")