import socket
import datetime

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# allow reuse of port
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind server
server.bind(("localhost", 12345))

# start listening
server.listen()

print("Server started...")
print("Waiting for connection...")

# accept connection
conn, addr = server.accept()

print("Connected to:", addr)

# receive username
username = conn.recv(1024).decode()
print(username, "joined the chat")

while True:
    message = conn.recv(1024).decode()

    if message.lower() == "exit":
        print(username, "left the chat")
        break

    # add timestamp
    time = datetime.datetime.now().strftime("%H:%M:%S")

    full_message = "[" + time + "] " + username + ": " + message

    print(full_message)

    # save chat history
    with open("chat_history.txt", "a") as file:
        file.write(full_message + "\n")

    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
server.close()