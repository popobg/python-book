import tkinter as tk
from tkinter import ttk
from tkinter import font

# WINDOW
window = tk.Tk()
window.geometry("600x450")
window.title("Pack")
window.configure(bg = "black")

# get the default font of the text
my_font = font.nametofont("TkDefaultFont")

# WIDGETS
label1 = ttk.Label(window, text = "First label", background = "red", font = (my_font.actual(), 10, "bold", "underline"), anchor = "center")
label2 = ttk.Label(window, text = "Label 2", background = "#6fa8dc")
label3 = ttk.Label(window, text = "Last of the label", background = "light green", anchor = "e")
button = ttk.Button(window, text = "Button")

# pack LAYOUT
label1.pack(side = "top", expand = True, fill = "both", pady = 10, padx = 10)
label2.pack(side = "left", expand = True, fill = "both")
label3.pack(side = "top", fill = "both", pady = 10)
button.pack(side = "top", expand = True, fill = "y")

# RUN
window.mainloop()