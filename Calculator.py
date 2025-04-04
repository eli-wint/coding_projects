import tkinter as tk
root = tk.Tk()

# Math variables
displayNumber = 0
currentValue = 0
result = 0
pastResult = 0

numericalEntry = tk.Entry(root, justify = 'center')
numericalEntry.pack()
equalsButton = tk.Button(root, text = "=", width = 17)
displayAnswer = tk.Label(root, text = f"{displayNumber}", font = ("HELVETICA", 20))
additionButton = tk.Button(root, text = "+", width = 17)
subtractionButton = tk.Button(root, text = "-", width = 17)
multiplicationButton = tk.Button(root, text = "x", width = 17)
divisionButton = tk.Button(root, text = "%", width = 17)
clearButton = tk.Button(root, text = "CLEAR ALL")
oneButton = tk.Button(root, text = "1", width = 17)
twoButton = tk.Button(root, text = "2", width = 17)
threeButton = tk.Button(root, text = "3", width = 17)
fourButton = tk.Button(root, text = "4", width = 17)
fiveButton = tk.Button(root, text = "5", width = 17)
sixButton = tk.Button(root, text = "6", width = 17)
sevenButton = tk.Button(root, text = "7", width = 17)
eightButton = tk.Button(root, text = "8", width = 17)
nineButton = tk.Button(root, text = "9", width = 17)
zeroButton = tk.Button(root, text = "0", width = 17)

# Putting variables into the grid
numericalEntry.grid(column = 1, row = 0)
displayAnswer.grid(column = 1, row = 1)
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
multiplicationButton.grid(column = 2, row = 5, sticky="w")
subtractionButton.grid(column = 0, row = 6, sticky = "w")
equalsButton.grid(column = 1, row = 6, sticky = "w")
divisionButton.grid(column = 2, row = 6, sticky = "w")
clearButton.grid(column = 1, row = 7)

def CalculateEntry():
    global displayNumber, currentValue, result, pastResult

    if (pastResult != 0):
        currentValue = (str(pastResult) + numericalEntry.get())
    else:
        currentValue = numericalEntry.get()

    numericalEntry.delete(0, tk.END)

    result = eval(currentValue)

    displayAnswer.config(text = f"{result}")

    pastResult = result

def InsertButtonInput(selectedButton):
    global numericalEntry, oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton, zeroButton, additionButton
    # (variable).insert(num, text)
    numericalEntry.insert(tk.END, selectedButton)

def ClearAllCommand():
    global numericalEntry, displayAnswer, pastResult
    numericalEntry.delete(0, tk.END)
    displayAnswer.config(text = "0")
    pastResult = 0

equalsButton.config(command= lambda: CalculateEntry())
oneButton.config(command=lambda: InsertButtonInput("1"))
twoButton.config(command=lambda: InsertButtonInput("2"))
threeButton.config(command=lambda: InsertButtonInput("3"))
fourButton.config(command=lambda: InsertButtonInput("4"))
fiveButton.config(command=lambda: InsertButtonInput("5"))
sixButton.config(command=lambda: InsertButtonInput("6"))
sevenButton.config(command=lambda: InsertButtonInput("7"))
eightButton.config(command=lambda: InsertButtonInput("8"))
nineButton.config(command=lambda: InsertButtonInput("9"))
zeroButton.config(command=lambda: InsertButtonInput("0"))
additionButton.config(command= lambda: InsertButtonInput("+"))
subtractionButton.config(command= lambda: InsertButtonInput("-"))
multiplicationButton.config(command= lambda: InsertButtonInput("*"))
divisionButton.config(command= lambda: InsertButtonInput("/"))
clearButton.config(command= lambda: ClearAllCommand())

root.mainloop()