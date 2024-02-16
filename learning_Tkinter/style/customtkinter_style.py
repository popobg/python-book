import customtkinter as ctk

# window
window = ctk.CTk()
window.title("Customtkinter app")
window.geometry("400x350")
window.minsize(300, 250)

# functions
def segmented_button_callback(value):
    print("segmented button clicked:", value)

def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

# widgets
label = ctk.CTkLabel(window,
                     text = "A ctk label",
                    fg_color = ("red", "blue"),
                    text_color = ("black", "white"),
                    font = ("Helvetica", 25, "italic", "underline"),
                    # round corner
                    corner_radius = 10)
label.pack()

button = ctk.CTkButton(window,
                       text = "A ctk button",
                       fg_color = "#ff0",
                       text_color = "black",
                       # when the cursor passes above the widget
                       hover_color = "#880",
                       font = ("Gill Sans", 13, "bold"),
                       # clicking the button set the mode theme in black
                       command = change_theme)
button.pack(pady = 50)

# frame
frame = ctk.CTkFrame(window, fg_color = "transparent")
frame.pack(expand = True, fill = "both")

# grid
frame.columnconfigure((0, 1), weight = 1, uniform = "a")
frame.rowconfigure((0, 1), weight = 1, uniform = "a")

# segmented button et tkinter var
segemented_button_var = ctk.StringVar(value = "Value 1")
segemented_button = ctk.CTkSegmentedButton(frame,
                                           values = ["Value 1", "Value 2", "Value 3"],
                                           command = segmented_button_callback,
                                           variable = segemented_button_var)
segemented_button.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")

# slider
slider = ctk.CTkSlider(frame, orientation = "vertical", button_color = "#10e0a9", button_hover_color = "#3474eb", progress_color = "#0c5270")
slider.grid(row = 1, column = 0, pady = 10)

# switch
switch = ctk.CTkSwitch(frame,
                       text = "A ctk switch",
                       fg_color = "red",
                       progress_color = "pink",
                       border_color = "blue",
                       button_color = "green",
                       button_hover_color = "yellow",
                       switch_width = 60,
                       switch_height = 30,
                       # very thin slider + rounded background
                       corner_radius = 2)
switch.grid(row = 1, column = 1)

# run
window.mainloop()