import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import time, math

def interpolate(animation_duration: float, start_pos: float, end_pos: float, t: float):
    """interpolate the position between start_pos and end_pos at a moment t from time 0 to animation_duration"""
    if t > animation_duration:
        t = animation_duration
    # 0 = starting_time
    # return one position (on the x axis in our case)
    # this position is somewhere between the start and the end pos
    return ((end_pos - start_pos) * t + animation_duration * start_pos - 0 * end_pos) / (animation_duration - 0)


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

        self.animate_start_t = 0
        # duration in sec (we can call it animation_duration_s)
        self.animation_duration = 0.1
        # set the fps we want to have for the animation
        self.fps = 60
        # time (fps = 1/time, in sec) given to the after func (*1000 to convert it in ms),
        # so this is the time between two calls of the animated func;
        # the less time there is between two calls, the more position we have
        # so the more smoother it gets
        self.animation_delay = int(1.0 / self.fps * 1000.0)

        # insert widgets
        self.create_widgets()

        # layout
        self.place(relx = self.start_pos, rely = 0.01, relwidth = self.width, relheight = 0.97)

    def animate(self):
        """check the position of the switch"""
        # start time for the animation
        self.animate_start_t = time.time()
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        """move the panel to the left (decrease x)"""
        # it is quasi impossible to have two float strictly equal;
        # so isclose makes sure the two float numbers are nearly equal
        if not math.isclose(self.pos, self.end_pos):
            # the last arg t is the only arg changing between two calls, because the time increases
            self.pos = interpolate(self.animation_duration, self.start_pos, self.end_pos, time.time() - self.animate_start_t)

            self.place(relx = self.pos, rely = 0.01, relwidth = self.width, relheight = 0.97)
            # call a function after some time (ms)
            self.after(self.animation_delay, self.animate_forward)

        else:
            self.in_start_pos = False

    def animate_backwards(self):
        """move the panel to the right (increase x)"""
        if not math.isclose(self.pos, self.start_pos):
            self.pos = interpolate(self.animation_duration, self.end_pos, self.start_pos, time.time() - self.animate_start_t)

            self.place(relx = self.pos, rely = 0.01, relwidth = self.width, relheight = 0.97)
            self.after(self.animation_delay, self.animate_backwards)

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
window.geometry("600x550")
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