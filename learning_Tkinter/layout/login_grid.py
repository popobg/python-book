import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Login")

# configure the grid
window.columnconfigure((0, 1), weight = 1)
window.columnconfigure(2, weight = 2)

window.rowconfigure((0, 1, 2), weight = 1)

# widgets & layout
username = ttk.Label(window, text = "Username: ")
username.grid(column = 0, row = 0, padx = 5, pady = 5)

username_entry = ttk.Entry(window)
username_entry.grid(column = 1, row = 0, columnspan = 2, padx = 5, pady = 5)

password = ttk.Label(window, text = "Password: ")
password.grid(column = 0, row = 1, padx = 5, pady = 5)

password_entry = ttk.Entry(window, show = "*")
password_entry.grid(column = 1, row = 1, columnspan = 2, padx = 5, pady = 5)

login = ttk.Button(window, text = "Login", command = lambda: print("login..."))
login.grid(column = 2, row = 2, padx = 5, pady = 5, sticky = "e")

# run
window.mainloop()