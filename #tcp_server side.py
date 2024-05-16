#TCP server side 
import socket

#create a server side socket using IPv4 (AF_INET) and TCP (SOCk_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# see how to get ip address dynamically

print(socket.gethostname()) #hostname
print(socket.gethostbyname(socket.gethostname())) #ip of the given host name

# Bind our new socket to a tuple... the tuple is two value (IP addr, and Port)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#put socket into listing mode
server_socket.listen()

#listen forever to accept any connection
while True:
    #accept evry single connection and store two piece of information
    client_socket, client_address = server_socket.accept()
    print(type(client_socket))
    print (client_socket)
    print(type(client_address))
    print(client_address)

    print(f"connected to {client_address}!\n")
    #send a message to the client that just connected
    client_socket.send ("You are connected...!".encode("utf-8"))
    #close server connection
    server_socket.close()
    break




