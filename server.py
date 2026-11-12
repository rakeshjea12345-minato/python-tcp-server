import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set server IP and port
HOST = "127.0.0.1"
PORT = 5000

# Bind server to IP and port
server.bind((HOST, PORT))

# Start listening for clients
server.listen(5)

print("TCP Server is running...")
print(f"Waiting for connections on {HOST}:{PORT}")

while True:
    # Accept client connection
    conn, addr = server.accept()

    print("Connected by:", addr)

    # Receive message from client
    data = conn.recv(1024).decode()

    print("Client says:", data)

    # Send response
    response = "Hello Client! Message received."
    conn.send(response.encode())

    # Close client connection
    conn.close()