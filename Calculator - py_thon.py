import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math
window = tk.Tk()
window.title("CALCULATOR")
frame = tk.Frame(master = window, bg = "Black", padx = 8)
frame.pack()
entry = tk.Entry(master = frame, relief = SUNKEN,borderwidth = 2,width = 25)
entry.grid(row = 0, column = 0,columnspan = 2,ipady = 2,pady = 2)
def myclick(number):
    entry.insert(tk.END,number)

def equal():
    try:
        y=str(eval(entry.get()))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

def clear():
    entry.delete(0,tk.END)

def square_root():
    try:
        x=float(entry.get())
        y=str(math.sqrt(x))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Invalid Input")

def percentage():
    try:
        x=float(entry.get())
        y=str(x/100)
        entry.delete(0,tk.END)
        entry.insert(o,y)
    except:
        tkinter.messagebox.showinfo("Error","Invalid Input")

def sin():
    try:
        x = float(entry.get())
        y = str(math.sin(math.radians(x)))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

def cos():
    try:
        x=float(entry.get())
        y=str(math.cos(math.radians(x)))
        entry.delete(0, tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Invalid Input")

              
def tan():
    try:
        x=float(entry.get())
        y=str(math.tan(math.radians(x)))
        entry.delete(0,tk.END)
        entry.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Invalid Input")

button_1 = tk.Button(master = frame,text ="1",padx=15,pady=5,width=3,command = lambda:myclick('1'))
button_1.grid(row=1,column =0,pady=2)

button_2 = tk.Button(master=frame, text='2', padx=15,pady=5, width=3, command=lambda: myclick('2'))
button_2.grid(row=1, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3', padx=15,pady=5, width=3, command=lambda: myclick('3'))
button_3.grid(row=1, column=2, pady=2)

button_4 = tk.Button(master=frame, text='4', padx=15,pady=5, width=3, command=lambda: myclick('4'))
button_4.grid(row=2, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5', padx=15,pady=5, width=3, command=lambda: myclick('5'))
button_5.grid(row=2, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6', padx=15,pady=5, width=3, command=lambda: myclick('6'))
button_6.grid(row=2, column=2, pady=2)

button_7 = tk.Button(master=frame, text='7', padx=15,pady=5, width=3, command=lambda: myclick('7'))
button_7.grid(row=3, column=0, pady=2)

button_8 = tk.Button(master=frame, text='8', padx=15,pady=5, width=3, command=lambda: myclick('8'))
button_8.grid(row=3, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9', padx=15,pady=5, width=3, command=lambda: myclick('9'))
button_9.grid(row=3, column=2, pady=2)

button_0 = tk.Button(master=frame, text='0', padx=15,pady=5, width=3, command=lambda: myclick('0'))
button_0.grid(row=4, column=1, pady=2)

button_add= tk.Button(master = frame,text ="+",padx=15,pady=5,width=3,command = lambda:myclick('+'))
button_add.grid(row=5,column =0,pady=2)

button_subtract = tk.Button(master = frame,text ="-",padx=15,pady=5,width=3,command = lambda:myclick('-'))
button_subtract.grid(row=5,column =1,pady=2)

button_multiply = tk.Button(master = frame,text ="*",padx=15,pady=5,width=3,command = lambda:myclick('*'))
button_multiply.grid(row=5,column =2,pady=2)

button_divide= tk.Button(master = frame,text ="/",padx=15,pady=5,width=3,command = lambda:myclick('/'))
button_divide.grid(row=6,column =0,pady=2)

button_clear = tk.Button(master = frame,text ="clear",padx=15,pady=5,width=14,command = clear)
button_clear.grid(row=6,column =1, columnspan = 2,pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,pady=5, width=9, command=equal)
button_equal.grid(row=8, column=0, columnspan=3, pady=2)

button_sqrt = tk.Button(master = frame,text='^',padx=15,pady=5,width=3,command = square_root)
button_sqrt.grid(row=4,column=2,pady =2)

button_percent = tk.Button(master = frame,text='%',padx=15,pady=3,width=3,command = percentage)
button_percent.grid(row=4,column=0,pady=2)

button_sin = tk.Button(master = frame, text='sin',padx =15,pady=3,width=3,command = sin)
button_sin.grid(row=7,column = 0,pady=2)

button_cos = tk.Button(master = frame, text='cos',padx =15,pady=3,width=3,command = cos)
button_cos.grid(row=7,column =1,pady=2)

button_tan = tk.Button(master = frame, text='tan',padx =15,pady=3,width=3,command = tan)
button_tan.grid(row=7,column = 2,pady=2)

window.mainloop()



