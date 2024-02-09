import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("style test")
window.geometry("200x150")

# widgets
label = ttk.Label(window, text = "Label", style = "label.TLabel")
label.pack(side = "top")

btn1 = ttk.Button(window, text = "button")
btn1.pack()

label2 = ttk.Label(window, text = "Label 2")
label2.pack()

btn2 = ttk.Button(window, text = "Save", style = "btn.TButton")
btn2.pack(pady = 20)

# style
style = ttk.Style(window)
style.configure("label.TLabel", font = ("Helvetica", 11), background = "purple", foreground = "white")

style.map("btn.TButton", background = [("pressed", "blue"), ("active", "light blue")], foreground = [("pressed", "white")])

# run
window.mainloop()