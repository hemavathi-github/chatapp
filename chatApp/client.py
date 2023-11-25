import socket
from threading import Thread

name = input("enter your name ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5500
client.connect((ip, port))
print("connected")


def receive():
    while True:
        try:
           message = client.recv(2048).decode("utf-8")
           if message == "name":
               client.send(name.encode("utf-8"))
        except:
            print("error")
            client.close() 
            break

def details():
    while True:
        message = "{}:{}".format(name, input(""))
        client.send(message.encode("utf-8"))  
        print(message)  
thread1 = Thread(target = receive)
thread1.start()
thread2 = Thread(target = details)
thread2.start()


