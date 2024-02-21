import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import random

# example function to illustrate
def update_btn():
    global button_x
    # layout
    button_x += 0.005
    button.place(relx = button_x, rely = 0.5, anchor = "center")

    # configure
    colors = ["red", "yellow", "green", "orange", "blue", "pink", "white"]
    color = random.choice(colors)
    style.configure("button.TButton", background = color)

    if button_x < 0.9:
        window.after(10, update_btn)

# class
class SlidePanel(ttk.Frame):
    """A sliding animated panel on the right side of the window"""

    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        # general attributes
        self.start_pos = start_pos + 0.02
        self.end_pos = end_pos - 0.02
        # the end_pos can be greater than the start_pos,
        # so we have to use absolute
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        # it is a switch : check if in a start-pos and move to the end
        # or the contrary
        self.in_start_pos = True

        # insert widgets
        self.create_widgets()

        # layout
        self.place(relx = self.start_pos, rely = 0.01, relwidth = self.width, relheight = 0.97)

    def animate(self):
        """check the position of the switch"""
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        """move the panel to the left"""
        if self.pos > self.end_pos:
            # decreases the position on x
            self.pos -= 0.008

            self.place(relx = self.pos, rely = 0.01, relwidth = self.width, relheight = 0.97)
            # call a function after some time (ms)
            self.after(3, self.animate_forward)

        else:
            self.in_start_pos = False

    def animate_backwards(self):
        """move the panel to the right"""
        if self.pos < self.start_pos:
            # increases the position on x
            self.pos += 0.008

            self.place(relx = self.pos, rely = 0.01, relwidth = self.width, relheight = 0.97)
            self.after(3, self.animate_backwards)

        else:
            self.in_start_pos = True

    def create_widgets(self):
        ttk.Button(self, text = "Button 1").pack(expand = True, anchor = "center")
        ttk.Button(self, text = "Button 2").pack(expand = True, anchor = "center")
        ttk.Label(self, text = "Label").pack(expand = True, anchor = "center")
        scrolledtext.ScrolledText(self, width = 20, height = 10).pack(anchor = "center", padx = 5, pady = 5)

# creating the window
window = tk.Tk()
window.title("Animated widgets")
window.geometry("400x350")
window.configure(bg = "#21334f")

# style
style = ttk.Style()
# this theme makes the bg of the button more visible
style.theme_use("clam")
style.configure("TFrame", background = "pink")

# create an instance of slide panel (master, start, end)
animated_panel = SlidePanel(window, 1, 0.7)

# var
button_x = 0.5

# widget
button = ttk.Button(window, text = "toggle sidebar", command = animated_panel.animate, style = "button.TButton")
button.place(relx = button_x, rely = 0.5, relheight = button_x, anchor = "center")

window.mainloop()