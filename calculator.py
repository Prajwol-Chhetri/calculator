from tkinter import *

root = Tk()
root.title("Calculator")

# setting the dimensions and adding the entry box to the window.
e = Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# defining the functions of the calculator
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def decimal():
    current = e.get()
    if '.' not in current:
        e.insert(END, str('.'))


def button_clear():
    e.delete(0, END)


def add():
    global first_number
    global math
    math = "addition"
    first_number = float(e.get())
    e.delete(0, END)


def subtract():
    global first_number
    global math
    math = "subtraction"
    first_number = float(e.get())
    e.delete(0, END)


def multiply():
    global first_number
    global math
    math = "multiplication"
    first_number = float(e.get())
    e.delete(0, END)


def divide():
    global first_number
    global math
    math = "division"
    first_number = float(e.get())
    e.delete(0, END)


def equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, first_number + float(second_number))
    elif math == "subtraction":
        e.insert(0, first_number - float(second_number))
    elif math == "multiplication":
        e.insert(0, first_number * float(second_number))
    elif math == "division":
        e.insert(0, first_number / float(second_number))


# defining the buttons

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_divide = Button(root, text="/", padx=40, pady=20, command=divide)

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_multiply = Button(root, text="*", padx=40, pady=20, command=multiply)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_subtract = Button(root, text="-", padx=40, pady=20, command=subtract)

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_decimal = Button(root, text=".", padx=41, pady=20, command=decimal)
button_add = Button(root, text="+", padx=40, pady=20, command=add)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear)

button_equal = Button(root, text="=", padx=183, pady=20, command=equal)

# Putting the buttons on the screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_decimal.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_add.grid(row=4, column=2)
button_clear.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
