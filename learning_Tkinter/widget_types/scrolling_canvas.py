import random
import tkinter as tk
from tkinter import ttk

# setup window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")
window.minsize(400, 300)
window.configure(bg = "black")

# CANVAS
# scrollregion = (left, top, right, bottom)
canvas = tk.Canvas(window, bg = "white", scrollregion = (0, 0, 2000, 5000))

# creating a line that go all the way through the canvas
# create_**(l, t, r, b, fill = color, width = size)
canvas.create_line(0, 0, 2000, 5000, fill = "green", width = 10)

# creating 100 rectangles
for i in range(1):
    # left side coordonates
    l = random.randint(0, 2000)
    # top side coordonates
    t = random.randint(0, 5000)
    # right side coordonates
    r = l + random.randint(10, 500)
    # bottom side coordonates
    b = t + random.randint(10, 500)
    color = random.choice(("red", "blue", "yellow", "green", "pink", "purple", "black", "orange"))

    canvas.create_rectangle(l, t, r, b, fill = color)

canvas.pack(expand = True, fill = "both")

# SCROLLBARS
# in the command, the scrollbar influences the canvas
scrollbar_y = ttk.Scrollbar(window, orient = "vertical", command = canvas.yview)
# here, we set the canvas to update the scrollbar too,
# so that we can see the update on the scrollbar.
# it tells the scrollbar how tall the canvas is, and where we are in it
canvas.configure(yscrollcommand = scrollbar_y.set)
scrollbar_y.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

scrollbar_x = ttk.Scrollbar(window, orient = "horizontal", command = canvas.xview)
canvas.configure(xscrollcommand = scrollbar_x.set)
scrollbar_x.place(relx = 0, rely = 1, relwidth = 1, anchor = "sw")

# FUNCTIONS
def scroll_y(event):
    # event(mousewheel).delta == 120 if scroll up
    if event.delta > 0:
        # yview(amount, "what")
        # scroll up
        canvas.yview_scroll(-1, "units")

    # event(mousewheel).delta == -120 if scroll down
    else:
        # scroll down
        canvas.yview_scroll(1, "units")

def scroll_x(event):
    # same as before, on the horizontal axis
    if event.delta > 0:
        canvas.xview_scroll(-1, "units")

    else:
        canvas.xview_scroll(1, "units")

# EVENT BIDING
# bind the vertical scrollbar to the mousewheel
# canvas.bind("<MouseWheel>", scroll_y)

# easier, with a lambda function
# -1 inverses the direction
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta/120), "units"))

# bind the horizontal scrollbar to shift + mousewheel
canvas.bind("<Shift-MouseWheel>", scroll_x)

# run
window.mainloop()