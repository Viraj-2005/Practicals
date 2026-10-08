from xmlrpc.server import SimpleXMLRPCServer

messages = []

def send_message(name, msg):
    messages.append(f"{name}: {msg}")
    return "Message sent!"

def get_messages():
    return messages

server = SimpleXMLRPCServer(("127.0.0.1", 8000), allow_none=True)

server.register_function(send_message)
server.register_function(get_messages)

print("RPC Chat Server Started...")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer Stopped")