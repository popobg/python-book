import tkinter as tk
import ttkbootstrap as ttk

# window with ttkbootstrat
window = ttk.Window(themename = "minty")
window.title("ttk bootstrap intro")
window.geometry("400x300")

# function
def change_theme_menubutton():
    if selected_theme.get() == "dark theme":
        ttk.Style("superhero")

    if selected_theme.get() == "light theme":
        ttk.Style("minty")

def change_theme_combobox(event):
    if selected_theme.get() == "dark theme":
        ttk.Style("superhero")

    if selected_theme.get() == "light theme":
        ttk.Style("minty")

# widgets & layout
label = ttk.Label(window, text = "Label", anchor = "center")
label.pack(pady = 10)

button1 = ttk.Button(window, text = "Red", bootstyle = "danger-link")
button1.pack(pady = 10)

# by default, the buttons are solid
button2 = ttk.Button(window, text = "Yellow", bootstyle = "warning-solid")
button2.pack(pady = 10)

# with outline, the background is transparent
# the background turn into the full color when hovering above the widget
# bootstyle = "color-outline"
button3 = ttk.Button(window, text = "Green", bootstyle = "success-outline")
button3.pack(pady = 10)

checkbutton = ttk.Checkbutton(window, text = "square toggle checkbutton", bootstyle = "info-square-toggle")
checkbutton.pack(pady = 10)

# separator
ttk.Separator(window, bootstyle = "dark").pack(fill = "x")

# frame
frame = ttk.Frame(window)
frame.pack(expand = True, fill = "both")

# menubutton
selected_theme = tk.StringVar(value = "light theme")

menu_button = ttk.Menubutton(frame, text = "Select a theme:")
menu_button.pack(side = "left", expand = True)

button_submenu = tk.Menu(menu_button, tearoff = False)
button_submenu.add_radiobutton(label = "dark theme", command = change_theme_menubutton, variable = selected_theme)
button_submenu.add_radiobutton(label = "light theme", command = change_theme_menubutton, variable = selected_theme)

menu_button.configure(menu = button_submenu)

# combobox
combobox = ttk.Combobox(frame, values = ("dark theme", "light theme"), textvariable = selected_theme)
combobox.pack(side = "left", expand = True)

combobox.bind('<<ComboboxSelected>>', change_theme_combobox)

# Sizegrip
ttk.Sizegrip(window, bootstyle = "success").place(relx = 1, rely = 1, anchor = "se")

# run
window.mainloop()