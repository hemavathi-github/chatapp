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
        names.remove(connections)

def broadcast(message, connections):
    for i in clients:
        if i != connections:
            try:
                i.send(message.encode("utf-8"))
            except:
                remove(connections)


def clientThread(socketObject, adress):
    socketObject.send("welcome to chat".encode("utf-8"))
    while True:
        try:
           message = socketObject.recv(2048).decode("utf-8")
           if message:
                # messageSent = "<" + adress[0] + ">" + message
                print(message,adress)
                broadcast(message, socketObject)
           else:
               remove(socketObject)
               remove(adress)
        except:
            continue


while True:
    socketObject, adress = server.accept()
    socketObject.send("NAME".encode("utf-8"))
    clientname = socketObject.recv(2048).decode("utf-8")
    names.append(clientname)
    clients.append(socketObject)
    msg = "{}, join the session".format(clientname)
    broadcast(msg, socketObject)
    print(msg)
    newThread = Thread(target = clientThread, args = (socketObject, clientname))
    newThread.start()

