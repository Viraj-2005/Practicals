import xmlrpc.client

if __name__ == "__main__":
    remote_object = xmlrpc.client.ServerProxy("http://localhost:8000/")

    response_msg = remote_object.say_hello("Viraj")
    print(f"Response from Server: {response_msg}")

    response_msg = remote_object.add_numbers(50, 25)
    print(f"Sum from Server: {response_msg}")

