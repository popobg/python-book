import tkinter as tk
from tkinter import ttk

# WINDOW
window = tk.Tk()
window.geometry("500x600")
window.title("pack and frames")

# 1st level (window)
frame1 = ttk.Frame(window, relief = "groove")
# allows the frame to take all the place it can have
frame1.pack(expand = True, fill = "both")

label1 = ttk.Label(window, text = "Another label", background = "green", anchor = "center")
# without the fill option, the label will take only the space needed to display the text
label1.pack(expand = True)

frame2 = ttk.Frame(window, relief = "sunken")
frame2.pack(expand = True, fill = "both", padx = 20, pady = 20)

# 2nd level
# frame 1
label2 = ttk.Label(frame1, text = "First label", background = "red")
# without expand = True, the label will fill only the x axis (because side = "up")
label2.pack(expand = True, fill = "both")

label3 = ttk.Label(frame1, text = "Label 2", background = "blue")
label3.pack(expand = True, fill = "both")

# frame 2
button1 = ttk.Button(frame2, text = "Button 1")
button1.pack(side = "left", expand = True, fill = "both")

label4 = ttk.Label(frame2, text = "Last of the labels", background = "yellow")
label4.pack(side = "left", expand = True, fill = "both")

button2 = ttk.Button(frame2, text = "Button 2")
button2.pack(side = "left", expand = True, fill = "both")

frame3 = ttk.Frame(frame2)
frame3.pack(side = "left", expand = True, fill = "both")

# 3rd level (frame3)
button3 = ttk.Button(frame3, text = "Button 3")
button3.pack(expand = True, fill = "both")

button4 = ttk.Button(frame3, text = "Button 4")
button4.pack(expand = True, fill = "both")

button5 = ttk.Button(frame3, text = "Button 5")
button5.pack(expand = True, fill = "both")

# RUN
window.mainloop()