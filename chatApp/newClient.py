import socket
from tkinter import *
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5500
client.connect((ip, port))
print("connected")

class Chatgui:
    def receive(self):
        while True:
            try:
                message = self.recv(2048).decode("utf-8")
                if message == "name":
                    self.send(self.name.encode("utf-8"))
            except:
                print("error")
                pass
                break
    def loginFunction(self,userName):
        self.name = userName
        # print(userName)
        thread1 = Thread(target=self.receive())
        thread1.start()
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()
        self.join = Toplevel()
        self.join.title("Chat app")
        self.join.configure(width=800, height=800)
        self.head = Label(self.join, text="Chat app login", font=("Arial", 20))
        self.head.place(relx=0.2, rely=0.1, relheight=0.2, relwidth=0.7)
        self.login = Label(self.join, text="enter your name", font=("Arial", 18))
        self.login.place(relx=0.2,rely=0.1, relheight=0.2, relwidth=0.7)
        self.loginname = Entry(self.join, font=("Arial", 17))
        self.loginname.place(relx=0.2, rely=0.3, relheight=0.06, relwidth=0.7)
        self.loginbutton = Button(self.join,text="Login" , font=("Arial", 17), command=lambda:self.loginFunction(self.loginname.get()))
        self.loginbutton.place(relx=0.2, rely=0.4, relheight=0.06, relwidth=0.3)
        self.window.mainloop()

    
chat = Chatgui()
        


