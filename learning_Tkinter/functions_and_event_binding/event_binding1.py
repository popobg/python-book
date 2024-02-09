import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Event binding")
window.geometry("600x500")

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = "a button")
btn.pack()

# function
# the function binding take event as an argument
def get_pos(event):
    print(f"x: {event.x}, y: {event.y}")

# events
# we can bind an event to a widget or to the top-level window

# when we are using a lambda function to catch an event,
# we have to write "lambda event" before the fuction
window.bind("<Alt-KeyPress>", lambda event: print(event.char))

# don't work on the wsl
entry.bind("<FocusIn>", print("the entry field was selected"))
entry.bind("<FocusOut>", print("the entry field was unselected"))

# print the position of the cursor on the window anytime the mouse moves
window.bind("<Motion>", get_pos)

# run
window.mainloop()