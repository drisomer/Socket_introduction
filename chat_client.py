#chat client side 
import socket
# define constant to be used 

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#create a client socket and connect the server, and specify the tuple i.e DESIp/port
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

while True:
    #receive the send message from the server and decode it
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    #quit if the connected server wants to quit else keep sending
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\Ending the chat....goodbye.....")
        break
    else:
        print(f"\n(message)")
        message = input("message")
        client_socket.send(message.encode(ENCODER))
 #close the client socket
client_socket.close()

       


