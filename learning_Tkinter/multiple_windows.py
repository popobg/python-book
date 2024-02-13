import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# FUNCTIONS
def ask_yes_no():
    messagebox.showinfo(title = "Info title", message = "Here is some information", detail = "How interesting!")

def create_window():
    global extra_window

    extra_window = Extra_window()

def destroy_window():
    # acessible because global variable
    extra_window.destroy()

# CLASS
class Extra_window(tk.Toplevel):

    def __init__(self):
        super().__init__()

        # set up
        self.title("Extra_window")
        self.geometry("250x300")

        self.create_widgets()

    def create_widgets(self):
        label1 = ttk.Label(self, text = "A label")
        label1.pack()

        button1 = ttk.Button(self, text = "A button")
        button1.pack(pady = 50)

        label2 = ttk.Label(self, text = "Another label")
        label2.pack(expand = True)

# MAIN
# setup window
window = tk.Tk()
window.title("Multiple windows")
window.geometry("600x400")
window.minsize(400, 300)

# widgets
create_window_button = ttk.Button(window, text = "Open main window", command = create_window)
create_window_button.pack(expand = True)

destroy_window_button = ttk.Button(window, text = "Close main window", command = destroy_window)
destroy_window_button.pack(expand = True)

info_box_button = ttk.Button(window, text = "Create yes/no window", command = ask_yes_no)
info_box_button.pack(expand = True)

# run
window.mainloop()