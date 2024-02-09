import tkinter as tk
from tkinter import ttk

# setup window
window = tk.Tk()
window.title("Scrolling")
window.geometry("600x400")
window.minsize(400, 300)
window.configure(bg = "black")

# TEXT
text = tk.Text(window)
text.pack(expand = True, fill = "both")

# add contents to the text box
# default behavior: mousewheel scrolls the doc
# there is no scrollbar
for i in range(1, 200):
    # text.insert(index, text),
    # with index = '1.0', 1 = strating line, 0 = char on that line
    text.insert(f'{i}.0', f'text: {i}\n')

# SCROLLBAR
scrollbar_text = ttk.Scrollbar(window, orient = "vertical", command = text.yview)
text.configure(yscrollcommand = scrollbar_text.set)
scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

# run
window.mainloop()