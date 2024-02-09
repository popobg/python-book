import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Event binding")
window.geometry("600x500")

# functions
def return_pressed(event):
    print("Return key pressed.")

def log(event):
    print(event)

# widget
btn = ttk.Button(window, text = "Save")

# binding
# <Return> is the <Entrée> button in french
# it calls 2 functions when it is pressed when focusing the button
btn.bind("<Return>", return_pressed)
btn.bind("<Return>", log, add = "+")

# layout
# the method focus bind the cursor on the widget
btn.focus()
btn.pack()

window.mainloop()