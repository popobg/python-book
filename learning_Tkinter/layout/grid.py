import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("600x400")
window.title("grid")

# define a grid
# at least one row and one column must be created to use grid as geometry manager
window.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
window.columnconfigure(3, weight = 3, uniform = "a")

window.rowconfigure((0, 1, 2), weight = 1, uniform = "a")
window.rowconfigure(3, weight = 3, uniform = "a")

# widgets and layout

label1 = ttk.Label(window, text = "Label 1", background = "red", anchor = "center")
# widget.grid(index_row, index_column)
label1.grid(row = 0, column = 0, sticky = "new")

label2 = ttk.Label(window, text = "Label 2", background = "blue", foreground = "white", anchor = "w")
label2.grid(row = 1, column = 1, rowspan = 3, sticky = "ns")

label3 = ttk.Label(window, text = "Label 3", background = "green", anchor = "center")
label3.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", padx = 10)

label4 = ttk.Label(window, text = "Label 4", background = "yellow")
label4.grid(row = 3, column = 3, sticky = "se")

button1 = ttk.Button(window, text = "Button 1")
button1.grid(row = 0, column = 3, sticky = "nsew")

button2 = ttk.Button(window, text = "Button 2")
button2.grid(row = 2, column = 2, sticky = "nsew")

entry = ttk.Entry(window)
entry.grid(row = 2, rowspan = 2, column = 3)

# RUN
window.mainloop()