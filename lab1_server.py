# Distributed System lab1 

import socket
import threading

host_ip = "127.0.0.1"
host_port = 59000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host_ip, host_port))
server_socket.listen()

print("Server is listening on {}: {}".format(host_ip, host_port))

clients = [] #creating array to hold list of clients
client_ids = {}  # Dictionary to store client IDs
chat_history = {}  # Dictionary to store chat history

# Function to broadcast a message to all connected clients
def chat_handler_message(message):
    for client in clients:
        client.send(message)

# Function to handle a client
def handle_client(client, client_id):
    while True:
        try:
            message = client.recv(1024).decode("utf-8")
            if not message:
                break

            if message == "list":
                client.send(str(client_ids).encode("utf-8"))
            elif message.startswith("history"):
                target_id = message.split()[1]
                if target_id in chat_history:
                    #client.sendall('client_id already exist.'.encode())#added now
                #elif '' in client_id:
                    #client.sendall("".encode())
                    #chat_history[client_id] = client
                    #client.sendall(f"Login as {client_id}.".encode())# added down to here
                    history = chat_history[target_id]#
                    for entry in history:             #
                        client.send(entry.encode("utf-8"))
                else:
                    client.send("Chat history not found.".encode("utf-8"))
            elif message.startswith("exit"):
                client.send("Goodbye".encode("utf-8"))
                break
            elif " " in message:
                target_id, content = message.split(" ", 1)
                if target_id in client_ids:
                    target_client = client_ids[target_id]
                    forward_message = f"{client_id}:{content}"
                    target_client.send(forward_message.encode("utf-8"))
                    # Store the message in chat history
                    if target_id not in chat_history:
                        chat_history[target_id] = []
                    chat_history[target_id].append(forward_message)
                else:
                    client.send("Target client not found.".encode("utf-8"))
            else:
                client.send("Type Client ID space followed by message.".encode("utf-8"))
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    client.close()
    if client_id in clients:
        clients.remove(client)
        del client_ids[client_id]

def receive():
    while True:
        print("Server is up and running listening to connections...")
        client, address = server_socket.accept()
        print(f"Connection now established with {str(address)}")
        client.send("Enter your client ID: ".encode("utf-8"))
        client_id = client.recv(1024).decode("utf-8")
        clients.append(client)
        client_ids[client_id] = client
        print(f"Client {client_id} has connected to the chat.")
        thread = threading.Thread(target=handle_client, args=(client, client_id))
        thread.start()

if __name__ == "__main__":
    receive()
