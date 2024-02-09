import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Combo & spin")
window.geometry("300x300")

# combobox and Tkinter var
# objects used later in the creation of an object
# have to be defined first
items = ("ice cream", "pizza", "broccoli")
food_string = tk.StringVar(value = items[0])

combobox = ttk.Combobox(window, values = items, textvariable = food_string)
combobox.pack(side = "top", pady = 10)

# event
# combobox has a special event that calls a function
# everytime an item of the combobox is selected
combobox.bind('<<ComboboxSelected>>', lambda event: label.configure(text = f"{food_string.get()}. Yummy!"))

# frame and labels
frame = ttk.Frame(window)
frame.pack()

label_not_linked = ttk.Label(frame, text = "favorite food is: ")
label_not_linked.pack(side = "left", pady = 20)

label = ttk.Label(frame, text = "any food")
label.pack(side = "left")

# spinbox and its tkinter var
spin_int = tk.IntVar(value = 2)

# we can set values from a value to another.
# increment defines a pas.
# note that the spinbox has a "command" parameter.
spinbox = ttk.Spinbox(window, from_ = 0, to = 10, increment = 2, textvariable = spin_int)
spinbox.pack(pady = 30)

# events
spinbox.bind("<<Increment>>", lambda event : print("up"))
spinbox.bind("<<Decrement>>", lambda event : print("down"))

# run
window.mainloop()