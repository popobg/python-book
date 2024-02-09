import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("400x600")
window.title("place")

# widgets and layout

label1 = ttk.Label(window, text = "Label 1", background = "red", anchor = "center")
# the two types (relative and absolute) can be combined
label1.place(x = 300, y = 100, relwidth = 0.1, height = 200)

label2 = ttk.Label(window, text = "Label 2", background = "blue", foreground = "white", anchor = "w")
# relative positioning is much more flexible because it updates itself when the size of the window changes
label2.place(relx = 0.5, rely = 0.5, relwidth = 0.3, relheight = 0.5, anchor = "center")

label3 = ttk.Label(window, text = "Label 3", background = "green", anchor = "center")
label3.place(x = 80, y = 60, width = 160, height = 300)

button1 = ttk.Button(window, text = "Button 1")
# without the anchor set to "se", the widget will not be visible
button1.place(relx = 1, rely = 1, anchor = "se")

# frame and layout
frame = ttk.Frame(window)
frame.place(relx = 0, rely = 0, relwidth = 0.3, relheight = 1)

frame_label = ttk.Label(frame, text = "Frame label", background = "yellow")
# here the relative positions are related to the size of the countainer, which is the frame
frame_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.5)

frame_button = ttk.Button(frame, text = "Frame button")
frame_button.place(relx = 0, rely = 0.5, relwidth = 1, relheight = 0.5)

# RUN
window.mainloop()