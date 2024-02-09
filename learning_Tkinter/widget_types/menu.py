import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("300x250")
window.title("Menu")

# MENU
global_menu = tk.Menu(window)

# SUBMENUS
# FIRST SUBMENU
file_menu = tk.Menu(global_menu, tearoff = False, bg = "light blue", activebackground = "red")

# add items in the submenu
file_menu.add_command(label = "New", command = lambda: print("New file"))
file_menu.add_command(label = "Open", command = lambda: print("Open file"))

# add a bar to separate the entries in a menu
file_menu.add_separator()

# create an exit button
# pas besoin de lambda pour appeler cette fonction
file_menu.add_command(label = "Exit", command = window.destroy)

# method called on the menu that countains our submenu
global_menu.add_cascade(label = "File", menu = file_menu)

# SECOND SUBMENU
help_menu = tk.Menu(global_menu, tearoff = 0)

help_menu.add_command(label = "Help...", command = lambda: print(help_check_string.get()))

help_check_string = tk.StringVar(value = "off")
help_menu.add_checkbutton(label = "Check", onvalue = "on", offvalue = "off", variable = help_check_string)

global_menu.add_cascade(label = "Help", menu = help_menu)

# SUB-SUBMENUS
other_menu = tk.Menu(help_menu, tearoff = 0)

other_menu.add_command(label = "Call", command = lambda: print("Call assistance"))

help_menu.add_cascade(label = "Assistance", menu = other_menu)

# LAYOUT
# replaces the geometry manager
# it allows your submenus to be seen in the parent menu
window.configure(menu = global_menu)

# MENU BUTTON
menu_button = ttk.Menubutton(window, text = "Menu Button")
menu_button.pack()

# create a submenu in the button
button_sub_menu = tk.Menu(menu_button, tearoff = False)
button_sub_menu.add_command(label = "entry 1", command = lambda: print("test 1"))
button_sub_menu.add_checkbutton(label = "Check 1")

# == menu_button["menu"] = button_sub_menu
menu_button.configure(menu = button_sub_menu)

# run
window.mainloop()