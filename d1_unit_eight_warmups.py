
import tkinter

root = tkinter.Tk()

root.title("Temperature Converter")

fahrenheitLabel = tkinter.Label(root, text="Fahrenheit:")
fahrenheitLabel.grid(column=1, row=1)

fahrenheitValue = tkinter.StringVar()
celsiusValue = tkinter.StringVar()

celsiusLabel = tkinter.Label(root, text="Celsius:")
celsiusLabel.grid(column=1, row=2)

fahrenheitEntry = tkinter.Entry(root, textvariable=fahrenheitValue)
fahrenheitEntry.grid(column=2, row=1)

resultLabel = tkinter.Label(root, textvariable=celsiusValue)
resultLabel.grid(column=2, row=2)


root.mainloop()
