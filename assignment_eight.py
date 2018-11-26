# Thenea Sun
# Nov. 8th
# This program is a simulator of calculators. It used the program of Graphical User Interfaces, in order to create a
# real calculator.

import tkinter

root = tkinter.Tk()

root.title("Thenea's Calculator")

Label_calculator = tkinter.Label(root, text="Thenea's Calculator")
Label_calculator.grid(row=1, column=1, columnspan=4)


def one():
    one = answer.get()
    answer.set(one + "1")


def two():
    two = answer.get()
    answer.set(two + "2")


def three():
    three = answer.get()
    answer.set(three + "3")


def four():
    four = answer.get()
    answer.set(four + "4")


def five():
    five = answer.get()
    answer.set(five + "5")


def six():
    six = answer.get()
    answer.set(six + "6")


def seven():
    seven = answer.get()
    answer.set(seven + "7")


def eight():
    eight = answer.get()
    answer.set(eight + "8")


def nine():
    nine = answer.get()
    answer.set(nine + "9")


def zero():
    zero = answer.get()
    answer.set(zero + "0")


def plus():
    plus = answer.get()
    answer.set(plus + "+")


def minus():
    minus = answer.get()
    answer.set(minus + "-")


def times():
    time = answer.get()
    answer.set(time + "*")


def divide():
    divides = answer.get()
    answer.set(divides + "/")


def equal():
    equal = answer.get()
    answer.set(eval(equal))
# tried to make equal work, and I got the function above to create this whole progress


def AC():
    answer.set("")


def dots():
    dot = answer.get()
    answer.set(dot + ".")


def square():
    squares = answer.get()
    answer.set(int(squares) * int(squares))


def triple():
    triples = answer.get()
    answer.set(int(triples) * int(triples) * int(triples))


answer = tkinter.StringVar()

LabelEntry = tkinter.Entry(root, textvariable=answer)
LabelEntry.grid(row=2, column=1, columnspan=4)

Label1 = tkinter.Button(root, text="   1   ", command=one)
Label1.grid(row=4, column=1)

Label2 = tkinter.Button(root, text="   2   ", command=two)
Label2.grid(row=4, column=2)

Label3 = tkinter.Button(root, text="   3   ", command=three)
Label3.grid(row=4, column=3)

Label4 = tkinter.Button(root, text="   4   ", command=four)
Label4.grid(row=5, column=1)

Label5 = tkinter.Button(root, text="   5   ", command=five)
Label5.grid(row=5, column=2)

Label6 = tkinter.Button(root, text="   6   ", command=six)
Label6.grid(row=5, column=3)

Label7 = tkinter.Button(root, text="   7   ", command=seven)
Label7.grid(row=6, column=1)

Label8 = tkinter.Button(root, text="   8   ", command=eight)
Label8.grid(row=6, column=2)

Label9 = tkinter.Button(root, text="   9   ", command=nine)
Label9.grid(row=6, column=3)

Label0 = tkinter.Button(root, text="         0          ", command=zero)
Label0.grid(row=7, column=1, columnspan=2)

Label_clear = tkinter.Button(root, text="AC/C", command=AC)
Label_clear.grid(row=3, column=1)

Label_equal = tkinter.Button(root, text="  =  ", command=equal)
Label_equal.grid(row=7, column=4)

Label_divide = tkinter.Button(root, text="  /  ", comman=divide)
Label_divide.grid(row=6, column=4)

Label_times = tkinter.Button(root, text="  *  ", command=times)
Label_times.grid(row=5, column=4)

Label_plus = tkinter.Button(root, text="  +  ", command=plus)
Label_plus.grid(row=3, column=4)

Label_minus = tkinter.Button(root, text="  -  ", command=minus)
Label_minus.grid(row=4, column=4)

Label_dots = tkinter.Button(root, text="    .   ", command=dots)
Label_dots.grid(row=7, column=3)

Label_square = tkinter.Button(root, text="  ^2  ", command=square)
Label_square.grid(row=3, column=2)

Label_triple = tkinter.Button(root, text="  ^3  ", command=triple)
Label_triple.grid(row=3, column=3)

root.mainloop()
