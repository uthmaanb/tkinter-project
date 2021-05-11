import tkinter as tk  # import as tkinter or as whatever you would like to call it
from tkinter import *  # import from tkinter whatever you are going to use or * to import everything
root = tk.Tk()  # root is parent window

# Code to add widgets will go here...
root.geometry("800x800")  # window size
root.title("temperature converter")  # title of window

answer1 = StringVar()
answer2 = StringVar()
celsius = StringVar()
fahrenheit = StringVar()

temp_in_cel = Label(root, text="temperature in celsius: ").place(x=10, y=10)
entry1 = Entry(root, textvariable=celsius).place(x=200, y=10)
cel_convtd = Label(root, text="Answer: ").place(x=10, y=50)
cel_convtd_ans = Entry(root, textvariable=answer1, state="readonly").place(x=200, y=50)

temp_in_fahr = Label(root, text="temperature in fahrenheit: ").place(x=10, y=150)
entry2 = Entry(root, textvariable=fahrenheit).place(x=200, y=150)
fah_convtd = Label(root, text="Answer: ").place(x=10, y=200)
fah_convtd_ans = Entry(root, textvariable=answer2, state="readonly").place(x=200, y=200)


def conv_cel():
    fahr = float(celsius.get()) * (9/5) + 32
    answer1.set(fahr)


def conv_fahr():
    cels = (float(fahrenheit.get()) - 32) * 5/9
    answer2.set(cels)


def clear():  # defining function for clearing the program
    entry1.delete(0, END)
    entry2.delete(0, END)
    cel_convtd_ans.config(state=NORMAL)  # because the clear function doesn't clear the readonly, change state to normal
    cel_convtd_ans.delete(0, END)
    cel_convtd_ans.config(state="readonly")


# kill program
def kill():
    return root.destroy()


convert_c = Button(root, text="Convert", command=conv_cel).place(x=150, y=80)
convert_f = Button(root, text="Convert", command=conv_fahr).place(x=50, y=250)
clr_btn = Button(root, text="clear", command=clear).place(x=150, y=250)
kill_btn = Button(root, text="kill", command=kill).place(x=150, y=350)


root.mainloop()  # continuously runs program in window
