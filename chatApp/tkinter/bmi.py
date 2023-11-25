from tkinter import *
from tkinter import ttk
window = Tk()
window.title("BMI calculator")
window.geometry("500x500")
window.configure(bg="white")
def calculate():
    health = ""
    bmi = 0
    weight = int(userweight.get())
    height = (int(userheight.get()))/100
    bmi = weight/(height*height)
    if bmi < 18.5:
        health = "underweight"
    elif bmi > 18.5 and bmi < 25:
        health = "healthy"
    elif bmi > 25 and bmi <35:
        health = "overweight"
    elif bmi >35:
        health = "obese" 
    BMI = Label(window, text=bmi)
    result = Label(window, text=health)
    BMI.place(x=150, y=230)
    result.place(x=150, y=250)
heading = Label(window, text="BMI calculator", fg="black", font=("Arial", 20))
heading.place(x=150, y=0)
name = Label(window, text="name: ", font=("Arial", 16))
name.place(x=40, y=60)
username = Entry(window, text="", bd=3)
username.place(x=175, y=60)
height = Label(window, text="height(in cm): ", font=("Arial", 16))
height.place(x=40, y=90)
userheight = Entry(window, text="", bd=3)
userheight.place(x=175, y=90)
weight = Label(window, text="mass (in kg):", font=("Arial", 16))
weight.place(x=40, y=120)
userweight = Entry(window, text="", bd=3)
userweight.place(x=175, y=120)
calc = Button(window, text="calculate", fg="white", bg="green", bd=3, command=calculate)
calc.place(x=200, y=200)
window.mainloop()


