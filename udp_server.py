#udp server side
import socket
#create a server side socket IPv4 and udp 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#binding our new socket to a tuple (addr and port)

server_socket.bind((socket.gethostbyname(socket.gethostname()),12345))

#we are not listing or accepting connection since upd is connectionless
message, address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
