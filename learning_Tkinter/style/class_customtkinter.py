#! /usr/bin/env python3

"""same as classes_tkinter but with customtkinter"""

import customtkinter as ctk

# App will be the main window and inherits from ctk.CTk
class App(ctk.CTk):

    def __init__(self, name: str, size: tuple[int]):

        # MAIN SETUP
        # we are calling the function from tk.Tk to create the window
        super().__init__()

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


# new object, inherits from ctk.CtkFrame
class Menu(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color = "transparent")
        # place the created frame
        self.place(x = 0, y = 0, relwidth = 0.35, relheight = 1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        """create the widgets as attributes of the class so they become accessible outside of the function"""
        self.menu_button1 = ctk.CTkButton(self, text = "Button 1")
        self.menu_button2 = ctk.CTkButton(self, text = "Button 2")
        self.menu_button3 = ctk.CTkButton(self, text = "Button 3")

        # standard orientation = "horizontal"
        self.menu_slider1 = ctk.CTkSlider(self, orientation = "vertical", width = 20)
        self.menu_slider2 = ctk.CTkSlider(self, orientation = "vertical", width = 20)

        self.toggle_frame = ctk.CTkFrame(self)
        self.menu_toggle1 = ctk.CTkCheckBox(self.toggle_frame, text = "Check 1")
        self.menu_toggle2 = ctk.CTkCheckBox(self.toggle_frame, text = "Check 2")

        self.entry = ctk.CTkEntry(self)

    def create_layout(self):
        # create the grid
        self.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
        self.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = "a")

        # place the widgets
        # buttons layout
        self.menu_button1.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew", padx = 4, pady = 4)
        self.menu_button2.grid(row = 0, column = 2, sticky = "nsew", padx = 4, pady = 4)
        self.menu_button3.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew", padx = 4, pady = 4)

        # sliders layout
        self.menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = "ns", pady = 20, padx = 5)
        self.menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = "ns", pady = 20, padx = 5)

        # toggle_frame layout
        self.toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew")
        self.menu_toggle1.pack(side = "left", expand = True)
        self.menu_toggle2.pack(side = "left", expand = True)

        # entry layout
        self.entry.place(relx = 0.5, rely = 1, relwidth = 0.9, anchor = "s")


class Main(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx = 0.35, y = 0, relwidth = 0.65, relheight = 1)

        self.frame1 = Main_frame(self, "Label 1", "Button 1", "red")
        self.frame2 = Main_frame(self, "Label 2", "Button 2", "blue", foreground_color = "white")


class Main_frame(ctk.CTkFrame):

    def __init__(self, parent, label_text: str, button_text: str, background_color: str, foreground_color: str = "black"):
        super().__init__(parent)

        self.create_widgets(background_color, foreground_color, label_text, button_text)
        self.create_layout()

    def create_widgets(self, background_color, foreground_color, label_text, button_text):
        self.label = ctk.CTkLabel(self, text = label_text, bg_color = background_color, text_color = foreground_color, anchor = "center")
        self.button = ctk.CTkButton(self, text = button_text, width = 15, border_color = "pink", border_width = 25)

    def create_layout(self):
        self.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)
        self.label.pack(expand = True, fill = "both")
        self.button.pack(pady = 100)


# MAIN
# creates an instance of the class App
App("Class based app with ctk", (600, 600))