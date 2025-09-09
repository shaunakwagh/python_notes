
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y



# Create an XML-RPC server instance
# Replace 'localhost' and '8000' with your desired host and port
server = SimpleXMLRPCServer(("localhost", 8000))

# Register the functions to be exposed as remote methods
server.register_function(add, "add")


print("XML-RPC server listening on port 8000...")
# Start serving requests
server.serve_forever()