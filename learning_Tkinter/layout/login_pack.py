import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Login")

fields = {}

# widgets
fields["username"] = ttk.Label(window, text = "Username: ")

fields["username_entry"] = ttk.Entry(window)

fields["password"] = ttk.Label(window, text = "Password: ")

fields["password_entry"] = ttk.Entry(window, show = "*")

# layout
for field in fields.values():
    field.pack(anchor = "w", padx = 10, pady = 5, fill = "x")

# widget button and its geometry manager
ttk.Button(window, text = "Login").pack(anchor = "w", padx = 10, pady = 5, fill = "x")

# run
window.mainloop()