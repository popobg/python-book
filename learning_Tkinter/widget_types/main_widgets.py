import tkinter as tk
from tkinter import ttk

# create a variable for the window
window = tk.Tk()
window.title("Tkinter Variables")

# define the size of the window ('widthxheight' - pixels)
window.geometry('600x600')

# tk WIDGETS

# Text = basic text input box
# the master is the parent, which is the window for the first label
# without parameter, pack places the widget into the window
text = tk.Text(window)
text.pack()

# ttk WIDGETS

# Label
# font = 'font fontsize format'
title_label = ttk.Label(master = window, text = 'Miles to kilometers', font = 'Calibri 12 italic')
title_label.pack()

# input field
# creating the parent/master frame of other widgets
input_frame = ttk.Frame(master = window)

# widgets added in the input frame
# Entry = single line entry widget
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text = 'Convert')

# layouts
entry.pack()
button.pack()
input_frame.pack()

# run the program
window.mainloop()