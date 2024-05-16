#udp client side
import socket
#create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#send some information via a connectionless protocol
client_socket.sendto("hello server world".encode("utf-8"),(socket.gethostbyname(socket.gethostname()),12345))
