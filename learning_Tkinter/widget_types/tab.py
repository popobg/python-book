import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Frames and parenting")
window.geometry("300x200")

# notebook widget
notebook = ttk.Notebook(window)

# tab 1
tab1 = ttk.Frame(notebook, relief = "groove")

label1 = ttk.Label(tab1, text = "Label in tab 1")
label1.pack()

entry1 = ttk.Entry(tab1)
entry1.pack(pady = 20, padx = 10)

# tab2
# less space occupied but same size as tab1
tab2 = ttk.Frame(notebook, relief = tk.GROOVE)

button1 = ttk.Button(tab2, text = "Button in tab 2")
button1.pack()

# add to notebook
notebook.add(tab1, text = "first tab")
notebook.add(tab2, text = "second tab")

# pack everything
notebook.pack()

# run
window.mainloop()