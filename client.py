import socket

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect(("localhost", 12345))

print("Connected to server")

username = input("Enter your name: ")

client.send(username.encode())

while True:
    message = input("You: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    print("Server:", reply)

client.close()