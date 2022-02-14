import socket
from sys import argv
import threading

HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "%COM=DISCONNECT%"
PORT = 5050
SERVER = socket.gethostbyname(argv[1])
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = True

def handle_server():
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)

            print(f"message recived : {msg}")

def ssend(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

def send(msg, recv):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    reciver = recv.encode(FORMAT)
    reciver_length = len(reciver)
    rsend_length = str(reciver_length).encode(FORMAT)
    rsend_length += b' ' * (HEADER - len(rsend_length))

    client.send(send_length)
    client.send(rsend_length)

    client.send(message)
    client.send(reciver)

ssend(input("Enter Name $>"))
print("")

hsr = threading.Thread(target=handle_server)
hsr.start()

while True:
    a = input()
    if a == ".end":
        send(DISCONNECT, ":o")
        connected = False
        break
    b = input("reciver: ")
    send(a, b)
