import xmlrpc.client


with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    # Call a remote method named 'add' with arguments 5 and 3
    result = proxy.add(5, 3)
    print(f"Result of add(5, 3): {result}")