import socket
import threading
import time

messages = []
clients = []

class message():
    def __init__(self, msg, reciver, sender):
        self.reciver = reciver
        self.sender = sender
        self.msg = msg


class ServerData():
    def __init__(self, port):
        self.port = port
        self.IPv4 = socket.gethostbyname(socket.gethostname())

    def getAdrr(self):
        return (self.IPv4, self.port)

HEADER = 64
FORMAT = "utf-8"
DISCONNECT = "%COM=DISCONNECT%"

print("[PUI] Configuering Server...")

myServerData = ServerData(5050)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(myServerData.getAdrr())

def SendBack(msg, client):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

def handle_returns():
    while True:
        for client in clients:
            index = 0
            for message in messages:
                #print(message.reciver)
                #print(client["name"])
                if message.reciver == client["name"]:
                    SendBack(f"'{message.msg}' from {message.sender}", client["conn"])
                    messages.pop(index)
                index += 1

def handle_client(conn, addr):
    print(f"[SERVER_CONNECT] {addr} connected")
    connected = True
    nameRecived = False
    name = None
    while not nameRecived:
        try:
            name_length = conn.recv(HEADER).decode(FORMAT)
            if name_length:
                name = conn.recv(len(name_length)).decode(FORMAT)
            nameRecived = True
        except ConnectionResetError:
            print(f"[{addr}] Disconnected")
            break
    clients.append({"name" : name, "conn" : conn})
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            reciver_length = int(conn.recv(HEADER).decode(FORMAT))
            msg = conn.recv(msg_length).decode(FORMAT)
            reciver = conn.recv(reciver_length).decode(FORMAT)

            if msg == DISCONNECT:
                print(f"[{addr}] Disconnected")
                break
            else:
                print(f"[{addr}] {msg}")
                messages.append(message(msg, reciver, name))

    conn.close()

def start():
    returnThread = threading.Thread(target=handle_returns)
    returnThread.start()
    server.listen()
    print(f"[SERVER] Server Is Listening On {myServerData.IPv4}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER] Active Connections = {threading.active_count() - 2}")

print("[SERVER] Starting Server...")
start()


