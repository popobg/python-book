import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.title("Option menu")
window.geometry("350x150")
window.minsize(350, 100)

# FUNCTIONS
def option_changed(window):
    output_label["text"] = f"You selected {string_var.get()}"

# VARIABLES
# values
languages = ("Python", "Javascript", "Java", "Swift", "GoLang", "C#", "C++", "Scala")

# tkinter variable
string_var = tk.StringVar()

# WIDGETS
# label
label = ttk.Label(window, text = "Select your favorite language:")

# option menu
option_menu = ttk.OptionMenu(window,
                             string_var,
                             languages[0],
                             *languages,
                             command = option_changed)

# output label
output_label = ttk.Label(window, foreground = "red")

# grid layout
window.columnconfigure((0, 1), weight = 1, uniform = "a")
window.rowconfigure((0, 1), weight = 1, uniform = "a")

# paddings for layout
paddings = {"padx" : 5, "pady" : 5}

# **paddings report the values of the set
label.grid(column = 0, row = 0, sticky = "w", **paddings)
option_menu.grid(column = 1, row = 0, **paddings)
output_label.grid(column = 0, row = 1, columnspan = 2, ** paddings)

# RUN
window.mainloop()