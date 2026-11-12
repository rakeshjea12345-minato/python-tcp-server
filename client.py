import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect(("127.0.0.1", 5000))

# Send message
message = "Hello Server!"
client.send(message.encode())

# Receive server response
response = client.recv(1024).decode()

print("Server says:", response)

# Close connection
client.close()