import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("400x600")
window.title("Stacking order")

# widgets
# 1st to be defined, background widget
label1 = ttk.Label(window, text = "Label 1", background = "green")
# 2nd to be defined so on top of the previous one, middleground widget
label2 = ttk.Label(window, text = "Label 2", background = "red")
# last to be defined, foreground widget
label3 = ttk.Label(window, text = "Label 3", background = "purple")

# elevate the widget on top of the other widget
button1 = ttk.Button(window, text = "Raise label 1", command = lambda: label1.lift())
# get the widget behind the others
button2 = ttk.Button(window, text = "Lower label 1", command = lambda: label1.lower())
# same as lift
button3 = ttk.Button(window, text = "Raise label 3 above label 1", command = lambda: label3.tkraise(aboveThis = label1))

# layout
label1.place(x = 50, y = 100, width = 200, height = 150)
label2.place(x = 150, y = 60, width = 140, height = 100)
label3.place(x = 20, y = 80, width = 180, height = 100)

button1.place(rely = 1, relx = 0.75, anchor = "se")
button2.place(rely = 1, relx = 1, anchor = "se")
button3.place(rely = 1, relx = 0.5, anchor = "se")

# RUN
window.mainloop()