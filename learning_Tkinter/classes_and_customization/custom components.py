#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk

# FUNCTION
def create_segment(parent, label_text: str, button_text: str) -> ttk.Frame:
    frame = ttk.Frame(parent, relief = "groove")

    # creating the grid
    frame.rowconfigure(0, weight = 1)
    frame.columnconfigure((0, 1, 2), weight = 1, uniform = "a")

    # widgets
    ttk.Label(frame, text = label_text, anchor = "center").grid(row = 0, column = 0)
    ttk.Button(frame, text = button_text).grid(row = 0, column = 1, sticky = "nsew")

    return frame

# CLASS
class Segment(ttk.Frame):

    def __init__(self, parent, label_text: str, button_text:str, btn: str = "button"):
        # creating the frame and placing it
        super().__init__(parent, relief = "sunken")
        self.pack(expand = True, fill = "both", padx = 10, pady = 5)

        # creating the layout grid
        self.create_grid()

        # layout and widgets
        ttk.Label(self, text = label_text, anchor = "center").grid(row = 0, column = 0)
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = "nsew")

        # example of function inside a class
        self.create_subframe(btn).grid(row = 0, column = 2, sticky = "nsew")

    def create_grid(self):
        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0, 1, 2), weight = 1, uniform = "a")

    def create_subframe(self, btn: str):
        frame = ttk.Frame(self)

        ttk.Entry(frame).pack(expand = True, fill = "both", padx = 5)
        ttk.Button(frame, text = btn).pack(pady = 10)

        return frame


# MAIN
window = tk.Tk()
window.title("Custom components")
window.geometry("300x400")

# class-based approach
Segment(window, "label", "button", "click me")
Segment(window, "test", "click")
Segment(window, "hello", "text")

# functionnal approach
# don't forget the layout method of the frame
frame3 = create_segment(window, "saving", "launch").pack(expand = True, fill = "both", padx = 10, pady = 5)
frame3 = create_segment(window, "bye", "exit").pack(expand = True, fill = "both", padx = 10, pady = 5)

window.mainloop()