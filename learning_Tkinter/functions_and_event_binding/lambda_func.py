import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("buttons, functions and arguments")
window.geometry("300x150")

# functions
def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())

# widgets
entry_string = tk.StringVar(value = "start")
entry = ttk.Entry(window, textvariable = entry_string)
entry.pack()

# by default, the lambda function is not being call when the object is created
button = ttk.Button(window, text = "Button", command = lambda: button_func(entry_string))
button.pack()

# run
window.mainloop()