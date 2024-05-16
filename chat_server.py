#chat server side 

import socket
#define constant to be used 
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENDCODER = "utf-8"
BYTESIZE = 1024
#create a server socket for IPv4 AF_INET, and bind it to an ip/port 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


#accept incomming connection and let them know they are connected 
print("server is runing....\n")

cleint_socket, client_address = server_socket.accept()
#send information to client socket
cleint_socket.send("You are connected to the server...\n".encode(ENDCODER))

#send/recieve message
while True:
    #receive information from the client 
    message =cleint_socket.recv(BYTESIZE).decode(ENDCODER)

    #quit if client side wants to quit, else display a message 
    if meessage == "quit": 
        cleint_socket.send("quit".encode(ENNCODER))
        print("\n Ending the chat......Goodbye.....")
        break
    else:
        print (f"\n{message}")
        message =input ("Message:")
        cleint_socket.send(message.encode(ENDCODER))

#closing the socket
server_socket.close()




      
