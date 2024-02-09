import random
import tkinter as tk
from tkinter import ttk

# setup window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")
window.minsize(400, 300)
window.configure(bg = "black")

# TREEVIEW
table = ttk.Treeview(window, columns = (1, 2), show = "headings")
table.pack(expand = True, fill = "both")

table.heading(1, text = "First name")
table.heading(2, text = "Last name")

first_names = ["Bob", "Maria", "Alex", "James"]
last_names = ["Smith", "Sinclair", "Zouiten", "Bob"]

# generate random lines in the table
for i in range(100):
    table.insert(parent = "", index = tk.END, values = (random.choice(first_names), random.choice(last_names)))

# SCROLLBAR
scrollbar_table = ttk.Scrollbar(window, orient = "vertical", command = table.yview)
table.configure(yscrollcommand = scrollbar_table.set)
scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# run
window.mainloop()