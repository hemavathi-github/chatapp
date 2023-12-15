import socket
from tkinter import *
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 5500
client.connect((ip, port))
print("connected")

class Chatgui:
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
    def loginFunction(self,userName):
        # self.name = userName
        self.join.destroy()
        self.chatPage(userName)
        # print(userName)
        thread1 = Thread(target=self.receive)
        thread1.start()
    def chatPage(self, username):
        self.name = username
        self.window.deiconify()
        self.window.title("chat app")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=800, height=800)
        # self.user = Label(self.window, text=self.name, font=("Arial", 15))
        # self.user.place(relx=0.5, rely=0.2)
        self.window.configure(width=800, height=800, bg="red")  
        self.text = Label(self.window, text="Chat app", font=("Arial", 20))
        self.text.place(relx=0.2, rely=0.1)
        self.username1 = Label(self.window, text=self.name, font=("Arial", 14))
        self.username1.place(relx = 0.2, rely=0.2)
        print(self.name)
        self.txt = Text(self.window, width=50, height=5, font=("Arial", 14))
        self.txt.place(relx = 0.1, rely=0.3, relwidth = 0.4, relheight=0.2)
        self.msg = Entry(self.txt, font=("Arial", 12))
        self.msg.place(relx = 0.05, rely=0.8, relwidth = 0.9, relheight=0.35)
        self.sndbutton = Button(self.window, text="send", font=("Arial", 18), border=3, command= lambda: self.sendMsg(self.msg.get()))
        self.sndbutton.place(relx = 0.1, rely=0.7, relwidth = 0.3, relheight=0.1)
        scrollbar=Scrollbar(self.txt)
        scrollbar.place(relheight=1,relx=0.9)
        scrollbar.config(command=self.txt.yview)
    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode("utf-8")
                if message == "NAME":
                    client.send(self.name.encode("utf-8"))
                else:
                   self.displayMsg(message)
            except:
                print("error")
                client.close()
                break

    def displayMsg(self, msg):
        self.txt.insert(END, msg + "\n")

    def sendMsg(self, msg):
        self.message = msg
        self.msg.delete("0","end")
        thread2 = Thread(target = self.details)
        thread2.start()


    def details(self):
        while True:
            message = (f"{self.name}:{self.message}")
            client.send(message.encode("utf-8"))  
            print(message)  
            self.displayMsg(message)
            break
   
    
chat = Chatgui()
        


