import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
# PIL = pillow image library
from PIL import Image, ImageTk
from pathlib import Path
import os

# setup
window = ctk.CTk()
window.title("Images with Tkinter")
window.geometry("500x350")
window.minsize(400, 300)

# functions
def fill_image(event):
    """comparing ratio of the canvas and the image
    to calculate the size of the image to resize it more smoothly"""
    # the image used in the canvas needs to be
    # in the same scop as the mainloop
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates of the image
    # if the canvas is wider than the image
    if canvas_ratio > image_ratio:
        width = int(event.width)
        height = int(width / image_ratio)

    # if the canvas is narrower than the image
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    # resize the already imported image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place the canvas
    # the x and y are the center of the canvas
    canvas.create_image(int(event.width / 2),
                        int(event.height / 2),
                        image = resized_tk,
                        anchor = "center")


def show_image(event):
    """comparing ratio of the canvas and the image
    to calculate the size of the image to always show full image"""
    # the image used in the canvas needs to be
    # in the same scop as the mainloop
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # get coordinates of the image
    if canvas_ratio > image_ratio:
        height = int(event.height)
        width = int(height * image_ratio)

    else:
        width = int(event.width)
        height = int(width/image_ratio)

    # resize the already imported image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place the canvas
    # the x and y are the center of the canvas
    canvas.create_image(int(event.width / 2),
                        int(event.height / 2),
                        image = resized_tk,
                        anchor = "center")


def change_theme():
    """update the window's theme"""

    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
        style.configure("TFrame", background = "#ede6e6")
        canvas.configure(bg = "#ede6e6")

    else:
        ctk.set_appearance_mode("dark")
        style.configure("TFrame", background = "#262222")
        canvas.configure(bg = "#262222")

# import images
# open(file_path)
image_original = Image.open(os.path.join(Path(__file__).parent, "raccoon.jpg"))
# know the ratio width/height of the image to resize it correctly
image_ratio = image_original.size[0] / image_original.size[1]
# needed to give the image to a tk or ttk widget
image_tk = ImageTk.PhotoImage(image_original)

# the button will not resize with the window, so it's fine to use resize
python_dark = Image.open(os.path.join(Path(__file__).parent, "python_dark.jpg")).resize((40, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

# for ctk, we always have to pass a light and a dark version of the image
# the two must have the same size
image_ctk = ctk.CTkImage(dark_image = Image.open(os.path.join(Path(__file__).parent,
                        "python_dark.jpg")).resize((40, 30)),
                         light_image = Image.open(os.path.join(Path(__file__).parent, "python_colored.jpg")).resize((40, 30)))

# grid layout
window.columnconfigure((0, 1, 2, 3), weight = 1, uniform = "a")
window.rowconfigure(0, weight = 1, uniform = "a")

# button frame
button_frame = ttk.Frame(window)
button_frame.grid(column = 0, row = 0, sticky = "nsew")

# buttons
button1 = ttk.Button(button_frame,
                    text = "A button",
                    image = python_dark_tk,
                    # indicates where the image must be placed
                    compound = "left")
button1.pack(expand = True)

button2 = ctk.CTkButton(button_frame,
                    text = "A second button",
                    bg_color = "white",
                    fg_color = "white",
                    hover_color = "#f7f1e4",
                    text_color = "black",
                    image = image_ctk,
                    # indicates where the image must be placed
                    compound = "left")
button2.pack(expand = True)

# canvas
# bd = 0 --> no broder
canvas = tk.Canvas(window, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.grid(column = 1, row = 0, columnspan = 3, sticky = "nsew")

# event binding canvas resizing
canvas.bind("<Configure>", fill_image)

# ctk switch
switch = ctk.CTkSwitch(window, text = "Change theme", progress_color = "pink", command = change_theme)
switch.place(relx = 1, rely = 1, anchor = "se")

# style
style = ttk.Style()

if ctk.get_appearance_mode() == "Dark":
    style.configure("TFrame", background = "#262222")
    canvas["bg"] = "#262222"

else:
    style.configure("TFrame", background = "#ede6e6")
    canvas["bg"] = "#ede6e6"


# run
window.mainloop()