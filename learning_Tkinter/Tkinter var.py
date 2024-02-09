import tkinter as tk
from tkinter import ttk

# if we press the button, the text in StringVar (so the one in label and entry)
# is printed in the terminal output
def button_func():
    print(string_var.get())
    # we update the text of the StringVar after pulling off the button
    string_var.set('button pressed')

window = tk.Tk()
window.title('Tkinter variables')

# tkinter variable
# the argument given in StringVar() is the text we will see in label and entry
# by running the program
string_var = tk.StringVar(value = 'start value')
# to change it later, we can do string_var.set('start value')

# widgets
label = ttk.Label(master = window, text = 'label', textvariable = string_var)
label.pack()

entry = ttk.Entry(master = window, textvariable = string_var)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

window.mainloop()