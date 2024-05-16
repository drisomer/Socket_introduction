# Distributed System lab1 

import socket
import threading

client_id  = input("Choose a Client_ID >>>>>")

# creating socket and connection

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 59000))
#def for client recv
def client_receive():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message == "Enter your client ID: ":
                client_socket.send(client_id.encode("utf-8"))
            else:
                print(message)
        except:
            print("Error")
            client_socket.close()
            break
#def for client send
def client_send():
    while True:
        message = input("")
        client_socket.send(message.encode("utf-8"))

#client_id = alias
client_socket.send(client_id.encode())
#threading  for send and recv start
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()