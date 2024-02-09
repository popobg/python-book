import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("buttons, functions and arguments")
window.geometry("300x150")

# functions
def outer_func(arg):
    def inner_func():
        print('a button was pressed')
        print(arg.get())
    return inner_func

# widgets
entry_string = tk.StringVar(value = "start")
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

# by default, the lambda function is not being code when the object is created
button = ttk.Button(window, text = "Button", command = outer_func(entry_string))
button.pack()

# run
window.mainloop()