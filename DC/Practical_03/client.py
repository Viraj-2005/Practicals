import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://127.0.0.1:8000")
print(client.send_message("MCA STUDENTS", "Parul University"))
print(client.send_message("Rahul", "BCA Students"))

print("\nChat Messages:")
for msg in client.get_messages():
    print(msg)