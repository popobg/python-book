#! /usr/bin/env python3

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, size: tuple[int]):
        super().__init__()

        self.title("Responsive layouts")
        self.geometry(f"{size[0]}x{size[1]}")

        # necessary for the first time the methods will be executed
        # for the forget method to work
        self.frame = ttk.Frame(self)
        self.frame.pack()

        # dict : {window_width: window.method_appropriate_to_the_size}
        # don't call the method, just passing the name (no ())
        Size_notifier(self,
                      {
                        300: self.create_small_layout,
                        600: self.create_medium_layout,
                        1200: self.create_large_layout
                        })

        self.mainloop()

    def create_small_layout(self):
        # necessary to erase the already displayed layout
        self.frame.forget()

        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = "both")

        ttk.Label(self.frame, text = "Label 1", background = "red", anchor = "center").pack(expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 2", background = "green", anchor = "center").pack(expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 3", background = "light blue", anchor = "center").pack(expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 4", background = "yellow", anchor = "center").pack(expand = True, fill= "both", padx = 5, pady = 5)

    def create_medium_layout(self):
        self.frame.forget()

        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = "both")

        self.frame.columnconfigure((0, 1), weight = 1, uniform = "a")
        self.frame.rowconfigure((0, 1), weight = 1, uniform = "a")

        # there is no efficient way in Tkinter to copy one master to another,
        # so we have to reimplement all the labels
        ttk.Label(self.frame, text = "Label 1", background = "red", anchor = "center").grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 2", background = "green", anchor = "center").grid(row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 3", background = "light blue", anchor = "center").grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 4", background = "yellow", anchor = "center").grid(row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)

    def create_large_layout(self):
        self.frame.forget()

        self.frame = ttk.Frame(self)
        self.frame.pack(expand = True, fill = "both")

        ttk.Label(self.frame, text = "Label 1", background = "red", anchor = "center").pack(side = "left", expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 2", background = "green", anchor = "center").pack(side = "left", expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 3", background = "light blue", anchor = "center").pack(side = "left", expand = True, fill= "both", padx = 5, pady = 5)
        ttk.Label(self.frame, text = "Label 4", background = "yellow", anchor = "center").pack(side = "left", expand = True, fill= "both", padx = 5, pady = 5)

class Size_notifier:
    """Check if we are crossing the breaking points of width of the window"""

    def __init__(self, window, size_dict: dict):
        self.window = window
        # before storing it, we are making sure that the dict is sorted
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}
        self.current_min_size = None

        # event = when the widget (here the window/app) is resized
        self.window.bind("<Configure>", self.check_size)

        # place the elements in the window to get the right values
        # have to do the event binding BEFORE updating
        self.window.update()

        # winfo_width get the height of the window, after update
        min_height = self.window.winfo_height()
        # turn the keys into a list
        min_width = list(self.size_dict)[0]

        # disable the resize under 300 width/height
        # that way, we will never have a smaller size than the smaller threshold
        # (doesn't work on wsl)
        self.window.minsize(min_width, min_height)

    def check_size(self, event):

        # check only the resize of the window, not the frame
        if event.widget == self.window:
            # current window width
            window_width = event.width
            checked_size = None

            for threshold_size in self.size_dict:
                # for each positive number, we have exceeded a breaking point
                delta = window_width - threshold_size

                if delta >= 0:
                    checked_size = threshold_size

            # check if the current size is different from the last overtaked threshold
            if checked_size != self.current_min_size:
                self.current_min_size = checked_size

                # [key] is replaced by the value (the function self.create_*_layout)
                # then () call the method on the window (because the self above refers to the app)
                self.size_dict[self.current_min_size]()

app = App((300, 300))