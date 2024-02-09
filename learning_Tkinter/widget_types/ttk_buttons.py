import tkinter as tk
from tkinter import ttk

# create window
window = tk.Tk()
window.title("Tkinter Variables")
window.geometry('600x600')

# basic solid button and its tkinter variable
def button_func():
    button_string.set('button pressed')
    # pressing the button inform you about the value of the radiobutton currently checked
    print(radio_var.get())

button_string = tk.StringVar(value = "start")

button = ttk.Button(window, text = "A simple button", command = button_func, textvariable = button_string)
button.pack()

# checkbutton and its tkinter variable
# the tkinter variable is necessary to store
# if the box is clicked (1 / True) or not (0 / False)
# we can use a StringVar, an IntVar or a BooleanVar
check_var = tk.IntVar(value = 10)

# parameter onvalue sets the value if the box is clicked
# parameter offvalue sets the value if the box is unclicked
check1 = ttk.Checkbutton(window, text = "checkbox 1", command = lambda: print(check_var.get()), variable = check_var, onvalue = 10, offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(window, text = "checkbox 2", command = lambda: print("test"))
check2.pack()

# radiobuttons and their tkinter variable
# without a different parameter in value (or no parameter at all = default value = 0), all the radiobutton are linked
radio_var = tk.StringVar(value = 2)

radio1 = ttk.Radiobutton(window, text = "Radiobutton 1", value = "radio 1", variable = radio_var, command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(window, text = "Radiobutton 2", value = 2, variable = radio_var)
radio2.pack()

def uncheck_checkbox():
    check_var2.set(False)

# checkbutton and its tkinter variable
check_var2 = tk.BooleanVar()

check3 = ttk.Checkbutton(window, text = "checkbox 3", command = lambda: print(radio_string.get()), variable = check_var2)
check3.pack()

# radiobuttons and their tkinter variable
radio_string = tk.StringVar()

radioA = ttk.Radiobutton(window, text = "Radio A", value = "A", variable = radio_string, command = uncheck_checkbox)
radioA.pack()

radioB = ttk.Radiobutton(window, text = "Radio B", value = "B", variable = radio_string, command = uncheck_checkbox)
radioB.pack()

# run the program
window.mainloop()