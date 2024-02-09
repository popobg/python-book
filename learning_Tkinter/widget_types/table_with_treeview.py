import random
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Tables with treeview")
window.geometry("600x400")

# data
first_names = ["Bob", "Maria", "Alex", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Walker", "Clark"]

# treeview
# the parameter show = "headings" is necessary so we can see the text in it
table = ttk.Treeview(window, columns = ("first", "last", "email"), show = "headings")

# the headings are necessary to see the name of the columns
table.heading("first", text = "First name")
table.heading("last", text = "Last name")
table.heading("email", text = "Email")

# layout
# fill in the x and y directions in all the extra space available
table.pack(fill = "both", expand = True)

# insert values into a table
for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first}{last}@email.com"

    data = (first, last, email)

    # parent is usually a blank string
    table.insert(parent = "", index = 0, values = data)

# index (0 by default) determines where the values will be put in the table
# to place the item in the end, index = tk.END
table.insert(parent = "", index = tk.END, values = ("Bob", "Bob", "BobBob@email.com"))

# functions
def item_select(_):
    # table.selection returns the specific ID of the item
    # (placed in a specific space in the table) on a tuple
    for i in table.selection():
        # get the item from the tuple
        print(table.item(i)["values"])

def delete_items(_):
    # delete the selected item by pressing the delete key (suppr)
    for i in table.selection():
        table.delete(i)

# events
# specific treeview event binding
# calls the function when a line is selected
table.bind("<<TreeviewSelect>>", item_select)

table.bind("<Delete>", delete_items)

# run
window.mainloop()