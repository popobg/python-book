import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("600x600")
window.title("Combined layout")
# minimum size : the user can not reduce the window below this values
window.minsize(600, 600)

# main layout widgets (frames)
menu_frame = ttk.Frame(window, relief = "raised")
menu_frame.place(x = 0, y = 0, relwidth = 0.35, relheight = 1)

main_frame = ttk.Frame(window, relief = "groove")
main_frame.place(relx = 0.35, y = 0, relwidth = 0.65, relheight = 1)

# MENU
# first, widgets creation
menu_button1 = ttk.Button(menu_frame, text = "Button 1")
menu_button2 = ttk.Button(menu_frame, text = "Button 2")
menu_button3 = ttk.Button(menu_frame, text = "Button 3")

menu_slider1 = ttk.Scale(menu_frame, orient = "vertical")
menu_slider2 = ttk.Scale(menu_frame, orient = "vertical")

toggle_frame = ttk.Frame(menu_frame)
menu_toggle1 = ttk.Checkbutton(toggle_frame, text = "Check 1")
menu_toggle2 = ttk.Checkbutton(toggle_frame, text = "Check 2")

entry = ttk.Entry(menu_frame)

# then, the layout
# menu_frame grid
menu_frame.columnconfigure((0, 1, 2), weight = 1, uniform = "a")
menu_frame.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = "a")

# buttons layout
menu_button1.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
menu_button2.grid(row = 0, column = 2, sticky = "nsew")
menu_button3.grid(row = 1, column = 0, columnspan = 3, sticky = "nsew")

# sliders layout
menu_slider1.grid(row = 2, column = 0, rowspan = 2, sticky = "nsew", pady = 20, padx = 5)
menu_slider2.grid(row = 2, column = 2, rowspan = 2, sticky = "nsew", pady = 20, padx = 5)

# toggle_frame layout
toggle_frame.grid(row = 4, column = 0, columnspan = 3, sticky = "nsew")
menu_toggle1.pack(side = "left", expand = True)
menu_toggle2.pack(side = "left", expand = True)

# entry layout
entry.place(relx = 0.5, rely = 1, relwidth = 0.9, anchor = "s")

# MAIN
# creating widgets
entry_frame1 = ttk.Frame(main_frame)
main_label1 = ttk.Label(entry_frame1, text = "Label 1", background = "red", anchor = "center")
main_button1 = ttk.Button(entry_frame1, text = "Button 1", width = 15)

entry_frame2 = ttk.Frame(main_frame)
main_label2 = ttk.Label(entry_frame2, text = "Label 2", background = "blue", foreground = "white", anchor = "center")
main_button2 = ttk.Button(entry_frame2, text = "Button 2")

# frames layout
entry_frame1.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)
entry_frame2.pack(side = "left", expand = True, fill = "both", padx = 20, pady = 20)

# entry_frame1 layout
main_label1.pack(expand = True, fill = "both")
main_button1.pack(pady = 100)

# entry_frame2 layout
main_label2.pack(expand = True, fill = "both")
main_button2.pack(expand = True)

# RUN
window.mainloop()