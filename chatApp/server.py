import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipAdress = "127.0.0.1"
portNum = 5500
server.bind((ipAdress, portNum))
server.listen()
print("server started")
clients = []
names = []

def remove(connections):
    if connections in clients:
        clients.remove(connections)
    if connections in names:
        names.remove(connections)

def broadcast(message, connections):
    for i in clients:
        if i != connections:
            try:
                i.send(message.encode("utf-8"))
            except:
                remove(i)

def clientThread(socketObject, adress):
    socketObject.send("welcome to chat".encode("utf-8"))
    while True:
        try:
           message = socketObject.recv(2048).decode("utf-8")
           if message:
                messageSent = "<" + adress[0] + ">" + message
                print(message)
                broadcast(messageSent, socketObject)
           else:
               remove(socketObject)
               remove(names)
        except:
            continue

while True:
    socketObject, adress = server.accept()
    socketObject.send("name".encode("utf-8"))
    name = socketObject.recv(2048).decode("utf-8")
    names.append(name)
    clients.append(socketObject)
    broadcast(name, socketObject)
    print(names)
    newThread = Thread(target = clientThread, args = (socketObject, adress))
    newThread.start()

