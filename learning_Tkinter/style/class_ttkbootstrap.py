#! /usr/bin/env python3

"""same as classes_tkinter but with ttkbootstrap"""

import ttkbootstrap as ttk

# App will be the main window and inherits from ttk.ttk
class App(ttk.Window):

    def __init__(self, name: str, size: tuple[int], theme:str = "superhero"):

        # MAIN SETUP
        # we are calling the function from tk.Tk to create the window
        super().__init__(themename = theme)

        # title is a method of tk.Tk, so we can use it
        self.title(name)
        # width x height
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # WIDGETS
        self.menu = Menu(self)
        self.main = Main(self)

        # RUN
        self.mainloop()


# new object, inherits from ttk.ttkFrame
class Menu(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        # place the created frame
        self.place(x = 0, y = 0, relwidth = 0.35, relheight = 1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        """create the widgets as attributes of the class so they become accessible outside of the function"""
        self.menu_button1 = ttk.Button(self, text = "Button 1", bootstyle = "light")
        self.menu_button2 = ttk.Button(self, text = "Button 2", bootstyle = "secondary")
        self.menu_button3 = ttk.Button(self, text = "Button 3", bootstyle = "dark")

        # standard orientation = "horizontal"
        self.menu_scale1 = ttk.Scale(self, orient = "vertical")
        self.menu_scale2 = ttk.Scale(self, orient = "vertical")

        self.toggle_frame = ttk.Frame(self)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text = "Check 1")
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text = "Check 2")

        self.entry = ttk.Entry(self)

    def create_layout(self):
        # create the grid
        self.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = "a")

        # place the widgets
        # buttons layout
        self.menu_button1.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = 4, pady = 4)
        self.menu_button2.grid(row = 0, column = 2, sticky = "nsew", padx = 4, pady = 4)
        self.menu_button3.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", padx = 4, pady = 4)

        # Scales layout
        self.menu_scale1.grid(row = 2, column = 0, rowspan = 2, sticky = "ns", pady = 20, padx = 5)
        self.menu_scale2.grid(row = 2, column = 2, rowspan = 2, sticky = "ns", pady = 20, padx = 5)

        # toggle_frame layout
        self.toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew")
        self.menu_toggle1.pack(side = "left", expand = True)
        self.menu_toggle2.pack(side = "left", expand = True)

        # entry layout
        self.entry.place(relx = 0.5, rely = 0.99, relwidth = 0.9, anchor = "s")


class Main(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.35, y = 0, relwidth = 0.65, relheight = 1)

        self.frame1 = Main_frame(self, "Label 1", "Button 1", "danger", "warning")
        self.frame2 = Main_frame(self, "Label 2", "Button 2", "info", "success")


class Main_frame(ttk.Frame):

    def __init__(self, parent, label_text: str, button_text: str, label_color: str, button_color: str):
        super().__init__(parent)

        self.create_widgets(label_color, button_color, label_text, button_text)
        self.create_layout()

    def create_widgets(self, label_color, button_color, label_text, button_text):
        self.label = ttk.Label(self, text = label_text, bootstyle = f"{label_color}-inverse", anchor = "center")
        self.button = ttk.Button(self, text = button_text, bootstyle = f"{button_color}-outline", width = 15)

    def create_layout(self):
        self.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)
        self.label.pack(expand = True, fill = "both")
        self.button.pack(pady = 100)


# MAIN
# creates an instance of the class App
App("Class based app with ttkbootstrap", (600, 600))