import math
import numexpr
import tkinter
from tkinter import *
from tkinter import messagebox


window = tkinter.Tk()
window.geometry("350x350")
window.resizable(False, False)
window.title("Calculator")
window.config(bg="#daf8ff")

var = StringVar()


def clear():
    var.set("0")


def write_zero():
    if var.get() == "0":
        var.set("0")
    else:
        var.set(var.get() + "0")


def write_one():
    if var.get() == "0":
        var.set("1")
    else:
        var.set(var.get() + "1")


def write_two():
    if var.get() == "0":
        var.set("2")
    else:
        var.set(var.get() + "2")


def write_three():
    if var.get() == "0":
        var.set("3")
    else:
        var.set(var.get() + "3")


def write_four():
    if var.get() == "0":
        var.set("4")
    else:
        var.set(var.get() + "4")


def write_five():
    if var.get() == "0":
        var.set("5")
    else:
        var.set(var.get() + "5")


def write_six():
    if var.get() == "0":
        var.set("6")
    else:
        var.set(var.get() + "6")


def write_seven():
    if var.get() == "0":
        var.set("7")
    else:
        var.set(var.get() + "7")


def write_eight():
    if var.get() == "0":
        var.set("8")
    else:
        var.set(var.get() + "8")


def write_nine():
    if var.get() == "0":
        var.set("9")
    else:
        var.set(var.get() + "9")


def write_multi():
    a = var.get()
    b = a[-1]
    if b != "*" and b != "/" and b != "+" and b != "-" and b != ".":
        var.set(var.get() + "*")


def write_divide():
    a = var.get()
    b = a[-1]
    if b != "*" and b != "/" and b != "+" and b != "-" and b != ".":
        var.set(var.get() + "/")


def write_plus():
    var.set(var.get() + "+")


def write_minus():
    var.set(var.get() + "-")


def write_dot():
    a = var.get()
    b = a[-1]
    if b != "*" and b != "/" and b != "+" and b != "-" and b != ".":
        var.set(var.get() + ".")


def back():
    a = var.get()
    if len(a) > 1:
        var.set(var.get()[:-1])
    else:
        var.set("0")


def result():
    try:
        var.set(numexpr.evaluate(var.get()))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero")
    except SyntaxError:
        messagebox.showerror("Error", "Invalid syntax")


def get_invert():
    try:
        var.set(numexpr.evaluate(var.get()) * -1)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero")
    except SyntaxError:
        messagebox.showerror("Error", "Invalid syntax")


label = Label(window, font=("Arial", 20), width=19, height=1, textvariable=var, anchor=E,
              bg="White", highlightthickness=2, highlightbackground="#6fa8dc")
label.grid(row=0, column=0, padx=5, pady=10, columnspan=4)

clean = tkinter.Button(window, text="С", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=clear)
clean.grid(row=2, column=0, padx=10, pady=10)

seven = tkinter.Button(window, text="7", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=write_seven)
seven.grid(row=3, column=0, padx=10, pady=10)

four = tkinter.Button(window, text="4", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                      command=write_four)
four.grid(row=4, column=0, padx=10, pady=10)

one = tkinter.Button(window, text="1", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                     command=write_one)
one.grid(row=5, column=0, padx=10, pady=10)

invert = tkinter.Button(window, text="-/=", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                        command=get_invert)
invert.grid(row=6, column=0, padx=10, pady=10)

backspace = tkinter.Button(window, text="⟵", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                           command=back)
backspace.grid(row=2, column=1, padx=10, pady=10)

eight = tkinter.Button(window, text="8", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=write_eight)
eight.grid(row=3, column=1, padx=10, pady=10)

five = tkinter.Button(window, text="5", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                      command=write_five)
five.grid(row=4, column=1, padx=10, pady=10)

two = tkinter.Button(window, text="2", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                     command=write_two)
two.grid(row=5, column=1, padx=10, pady=10)

zero = tkinter.Button(window, text="0", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                      command=write_zero)
zero.grid(row=6, column=1, padx=10, pady=10)

dot = tkinter.Button(window, text=",", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                     command=write_dot)
dot.grid(row=2, column=2, padx=10, pady=10)

nine = tkinter.Button(window, text="9", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                      command=write_nine)
nine.grid(row=3, column=2, padx=10, pady=10)

six = tkinter.Button(window, text="6", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                     command=write_six)
six.grid(row=4, column=2, padx=10, pady=10)

three = tkinter.Button(window, text="3", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=write_three)
three.grid(row=5, column=2, padx=10, pady=10)

equal = tkinter.Button(window, text="=", font=("Arial", 14), width=13, relief="ridge", bg="white", borderwidth=1,
                       command=result)
equal.grid(row=6, column=2, padx=10, pady=10, columnspan=5)

multi = tkinter.Button(window, text="*", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=write_multi)
multi.grid(row=2, column=3, padx=10, pady=10)

divide = tkinter.Button(window, text="/", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                        command=write_divide)
divide.grid(row=3, column=3, padx=10, pady=10)

plus = tkinter.Button(window, text="+", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                      command=write_plus)
plus.grid(row=4, column=3, padx=10, pady=10)

minus = tkinter.Button(window, text="-", font=("Arial", 14), width=5, relief="ridge", bg="white", borderwidth=1,
                       command=write_minus)
minus.grid(row=5, column=3, padx=10, pady=10)

var.set("0")

window.mainloop()
