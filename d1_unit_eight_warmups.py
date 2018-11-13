
import tkinter

root = tkinter.Tk()
root.title("Temperature Converter")


def f_to_c():
    f_value = int(fahrenheitValue.get())
    c_value = 5/9 * (f_value - 32)
    celsiusValue.set(str(c_value))


fahrenheitLabel = tkinter.Label(root, text="Fahrenheit:")
fahrenheitLabel.grid(column=1, row=1)

fahrenheitValue = tkinter.StringVar()
celsiusValue = tkinter.StringVar()

celsiusLabel = tkinter.Label(root, text="Celsius:")
celsiusLabel.grid(column=1, row=2)

fahrenheitEntry = tkinter.Entry(root, textvariable=fahrenheitValue)
fahrenheitEntry.grid(column=2, row=1)

resultLabel = tkinter.Label(root, textvariable=celsiusValue)
resultLabel.grid(column=2, row=2, sticky="W")


convert_botton = tkinter.Botton(root, text="Convert", command=f_to_c())
convert_botton.grid(row=3, column=1, colunmspan=2)


root.mainloop()
