from xmlrpc.server import SimpleXMLRPCServer

class RMIService:

    def say_hello(self, name):
        return f"Hello {name},  Remote Method Executed Successfully"

    def add_numbers(self, a, b):
        return a + b

if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("RMI Server running on Port 8000")
    server.register_instance(RMIService())
    server.serve_forever()
