import tkinter as tk
root = tk.Tk()

# Math variables
displayNumber = 0
currentValue = 0
result = 0

numericalEntry = tk.Entry(root)
equalsButton = tk.Button(root, text = "=")
displayAnswer = tk.Label(root, text = f"{displayNumber}")
additionButton = tk.Button(root, text = "+")
oneButton = tk.Button(root, text = "1")
twoButton = tk.Button(root, text = "2")
threeButton = tk.Button(root, text = "3")
fourButton = tk.Button(root, text = "4")
fiveButton = tk.Button(root, text = "5")
sixButton = tk.Button(root, text = "6")
sevenButton = tk.Button(root, text = "7")
eightButton = tk.Button(root, text = "8")
nineButton = tk.Button(root, text = "9")
zeroButton = tk.Button(root, text = "0")

# Putting variables into the grid
numericalEntry.grid(column = 0, row = 0)
displayAnswer.grid(column = 0, row = 1)
oneButton.grid(column = 0, row = 2, sticky="w")
twoButton.grid(column = 1, row = 2, sticky="w")
threeButton.grid(column = 2, row = 2, sticky="w")
fourButton.grid(column = 0, row = 3, sticky="w")
fiveButton.grid(column = 1, row = 3, sticky="w")
sixButton.grid(column = 2, row = 3, sticky="w")
sevenButton.grid(column = 0, row = 4, sticky="w")
eightButton.grid(column = 1, row = 4, sticky="w")
nineButton.grid(column = 2, row = 4, sticky="w")
additionButton.grid(column = 0, row = 5, sticky="w")
zeroButton.grid(column = 1, row = 5, sticky="w")
equalsButton.grid(column = 2, row = 5, sticky="w")

def CalculateEntry():
    global displayNumber, currentValue, result

    currentValue = numericalEntry.get()

    numericalEntry.delete(0, tk.END)

    result = eval(currentValue)

    displayAnswer.config(text = f"{result}")

def InsertButtonInput(selectedButton):
    global numericalEntry
    # (variable).insert(num, text)


equalsButton.config(command= lambda: CalculateEntry())
additionButton.config()


root.mainloop()