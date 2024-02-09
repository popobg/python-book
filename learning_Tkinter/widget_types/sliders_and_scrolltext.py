import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# window
window = tk.Tk()
window.title("Scales and sliders")
window.geometry("600x500")

# Tkinter VAR
# DoubleVar store floatting values
# the slicer will be set initially at the value of the tkinter var
scale_var = tk.DoubleVar(value = 15)

# SLIDER
# set on vertical slider
scale = ttk.Scale(window,
                  # parameter "command value" is activated anytime
                  # we are clicking on the scale (like a button).
                  # progress.stop() : stop the motion of the progress bar
                  command = lambda value: progress.stop(),
                  # don't forget the underscore for from_
                  from_ = 0,
                  to = 25,
                  # determines the length of the slider
                  length = 300,
                  # by default, orient = "horizontal"
                  orient = "vertical",
                  variable = scale_var)
scale.pack()

# PROGRESS BAR
progress = ttk.Progressbar(window,
                           variable = scale_var,
                           maximum = 25,
                           orient = "horizontal",
                           # the progress bar is full.
                           # if set on "indeterminate",
                           # it is a slider
                           mode = "determinate",
                           length = 400)
progress.pack(side = "left", pady = 20)

# set the progress bar into motion
# the set value is the frequency of update in ms (1000ms = 1s)
progress.start(1000)

# SCROLLED TEXT
# we can also create our own scrolled text with a slider and a textbox
# this scrolled text is a particular widget already programed in tkinter
scrolled_text = scrolledtext.ScrolledText(window, width = 50, height = 5)
scrolled_text.pack()

# run
window.mainloop()