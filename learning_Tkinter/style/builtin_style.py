import tkinter as tk
from tkinter import ttk, font

# WINDOW
window = tk.Tk()
window.title("built-in style")
window.geometry("250x300")

# print all the font usable in tkinter (sorted)
print(sorted(font.families()))

# WIDGETS
label = ttk.Label(window,
                  text = "Label\nAnd then type on\nanother line",
                  anchor = "center",
                  background = "orange",
                  # font = ("style_name", size)
                  font = ("Jokerman", 12),
                  # anchro places the widget in the place available,
                  # justify places it in the area available after the anchor
                  justify = "right")
label.pack(expand = True, fill = "both")

# ttk.Button has no style options
btn1 = ttk.Button(window, text = "button")
btn1.pack()

# set the style name to use the style.configure for this style name
label2 = ttk.Label(window, text = "Label 2",  style = "label.TLabel")
label2.pack()

btn2 = ttk.Button(window, text = "Save", style = "btn.TButton")
btn2.pack(pady = 20)

# Frame
# no style options
frame = ttk.Frame(window)
frame.pack(expand = True, fill = "both")

# STYLE
# creating style object
style = ttk.Style()

# print the themes available in the OS
print(style.theme_names())

# global window style
style.theme_use("clam")

# Twidget = all of the widget in the app.
# "." = all the widgets in the app,
# but doesn't overwrite the options of a widget
style.configure("label.TLabel",
                font = ("Stencil", 11),
                # hexadecimal color
                background = "#b0e1c3",
                foreground = "#322933")

# map : ("Twidget", opt = [(), ()])
style.map("btn.TButton",
          background = [("pressed", "blue"), ("active", "green")],
          foreground = [("pressed", "white")])

style.configure("TFrame", background = "pink")

# RUN
window.mainloop()