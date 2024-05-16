#tcp_client side

import socket
#create a client side IPv4 socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect the socket to a server located at a given IP and port 
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))
#received a message from the server...and specify the max number of byte to recive
message = client_socket.recv(1024)

print(message.decode("utf-8"))
print (type(message))

#close connection
client_socket.close()

