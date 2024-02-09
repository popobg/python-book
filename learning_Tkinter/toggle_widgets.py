import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("400x350")
window.title("Stacking order")

# PLACE
# function
def toggle_label_place():
    # var accessible from outside the function
    global glabel1_visible

    if glabel1_visible:
        label1.place_forget()
        glabel1_visible = False
    else:
        glabel1_visible = True
        label1.place(relx = 0.1, rely = 0.5, anchor = "center")

# button
button1 = ttk.Button(window, text = "toggle label 1", command = toggle_label_place)
button1.place(relx = 0, rely = 1, anchor = "sw")

# var
glabel1_visible = True
# label
label1 = ttk.Label(window, text = "Label 1")
label1.place(relx = 0.1, rely = 0.5, anchor = "center")

# GRID
window.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
window.rowconfigure(0, weight = 1, uniform = "a")

# function
def toggle_label_grid():
    global glabel2_visible

    if glabel2_visible:
            label2.grid_forget()
            glabel2_visible = False
    else:
        glabel2_visible = True
        label2.grid(row = 0, column = 1)

# button
button2 = ttk.Button(window, text = "toggle label 2", command = toggle_label_grid)
button2.grid(row = 0, column = 1, sticky = "s")

# var
glabel2_visible = True
# label
label2 = ttk.Label(window, text = "Label 2")
label2.grid(row = 0, column = 1)

# PACK
# function
def toggle_label_pack():
    global glabel3_visible

    if glabel3_visible:
            label3.pack_forget()
            glabel3_visible = False
    else:
        glabel3_visible = True
        label3.pack(expand = True)

# frame
frame = ttk.Frame(window)
frame.place(relx = 0.7, rely = 0, relwidth = 0.3, relheight = 1)

# var
glabel3_visible = True
# label
label3 = ttk.Label(frame, text = "Label 3")
label3.pack(expand = True)

# button
button3 = ttk.Button(frame, text = "toggle label 3", command = toggle_label_pack)
button3.pack(side = "bottom")

# RUN
window.mainloop()