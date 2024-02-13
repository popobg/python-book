import tkinter as tk
from tkinter import ttk

# CLASS
class List_frames(ttk.Frame):

    # item_height = height of one frame
    def __init__(self, parent, text_data: list, item_height: int):
        self.parent = parent

        super().__init__(master = self.parent)
        self.pack(expand = True, fill = "both")

        # attributes - widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        # how many space in the y axis is going to be used
        self.list_height = self.item_number * item_height

        # canvas
        # the canvas has to be larger than the window to be scrollable
        # for our use here, we need it to be at the same width as the window
        self.canvas = tk.Canvas(self, background = "white", scrollregion = (0, 0, self.winfo_width(), self.list_height))
        self.canvas.pack(expand = True, fill = "both")

        # display frame
        self.frame = ttk.Frame(self)

        # placing the widgets into the frame
        for index, item in enumerate(self.text_data):
            self.create_widgets(index, item).pack(side = "top", expand = True, fill = "both", pady = 5, padx = 10)

        # scrollbar
        self.create_scrollbar()

        # events binding
        # bind_all binds the event at the widget and its children
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-1 * int(event.delta/120), "units"))

        # Configure is lauched everytime the window is resized
        # (including when the window is created)
        self.bind("<Configure>", self.update_size)


    def create_widgets(self, index: int, item: list[str]):
        """create a frame with two labels and one button horizontally aligned"""
        # subframe into frame
        subframe = ttk.Frame(self.frame)

        # grid
        subframe.columnconfigure((0, 1, 2, 3), weight = 1, uniform = "a")
        subframe.rowconfigure(0, weight = 1, uniform = "a")

        # widgets into the subframe
        ttk.Label(subframe, text = f"#{index}", border = 10, anchor = "center").grid(row = 0, column = 0, padx = 10)
        ttk.Label(subframe, text = item[0], border = 10, anchor = "center").grid(row = 0, column = 1, padx = 10)
        ttk.Button(subframe, text = item[1]).grid(row = 0, column = 2, columnspan = 2, sticky = "nsew")

        # avoid creating an attribute self.subframe that will last outside of the function
        return subframe


    def create_scrollbar(self):
        """create a vertical scrollbar linked to the canvas"""
        self.scrollbar = ttk.Scrollbar(self.parent, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")


    def update_size(self, event):
        """placing the frame into the canvas
        and adjusting the size of the canvas and the display in it
        to the size of the window"""

        if self.list_height >= self.winfo_height():
            # the height of the canvas is the height of the data list.
            height = self.list_height
            # re-bind the scrolling
            self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-1 * int(event.delta/120), "units"))
            # re-place the scrollbar
            self.scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = "ne")

        else:
            # the height of the canvas is the height of the window.
            height = self.winfo_height()
            # to avoid weird scrolling in fullscreen,
            # we unbind the event binding of scrolling
            self.canvas.unbind_all("<MouseWheel>")
            # no scrollbar if it is not needed
            self.scrollbar.place_forget()

        # create_window(**mandatories arguments**: position, window = a widget)
        self.canvas.create_window((0, 0),
                                  window = self.frame,
                                  # "center" by default
                                  anchor = "nw",
                                  # the length of the widget defined in "window" by default
                                  # here, it is the width of the window itself
                                  width = self.winfo_width(),
                                  height = height)


# MAIN
# setup window
window = tk.Tk()
window.title("Scrollable canvas")
window.geometry("600x400")
window.minsize(400, 300)
window.configure(bg = "black")

text_list = [("label", "button"), ("thing", "click"), ("third", "something"), ("label1", "button"), ("label2", "button1")]
list_frame = List_frames(window, text_list, 100)

# run
window.mainloop()