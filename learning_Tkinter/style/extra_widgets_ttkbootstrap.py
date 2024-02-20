import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge

# window with ttkbootstrat
window = ttk.Window(title = "Extra widgets",
                    themename = "superhero",
                    # only resizable in height
                    resizable = (False, True))
window.geometry("500x650")
# displays the window in the center of the screen monitor
# same as window.position_center()
window.place_window_center()

# scrollable frame
# autohide = when True, the scrollbars will hide
# when the mouse is not within the framebox
scroll_frame = ScrolledFrame(window, autohide = True)
scroll_frame.pack(fill = "both", expand = True, padx = 10, pady = 10)

for i in range(100):
    # hard to create a layout into a scrollable frame,
    # so insert a frame inside it
    frame = ttk.Frame(scroll_frame)
    frame.pack(expand = True, fill = "both")

    ttk.Label(frame, text = f"Label: {i}", anchor = "center").pack(side = "left", expand = True, fill = "x", padx = 5)
    ttk.Button(frame, text = f"Button: {i}").pack(side = "left", expand = True, padx = 5)

# toast = semi-transparent pop up window for temporary messages
toast = ToastNotification(title = "This is a message title",
                          message = "This is the actual message",
                          # duration = time to display the message in ms
                          # if not set, click on the window to close it
                          duration = 3000,
                          # outline is not supported
                          bootstyle = "dark",
                          # position = (x padding, y padding, start position)
                          # start position is a cardinal point
                          # and is the most important parameter
                          position = (50, 100, "nw"))

# hide_toast() exists too
ttk.Button(window, text = "show toast", command = lambda: toast.show_toast()).pack()

# tooltip = text displays pop up when the mouse is hovering a widget
button = ttk.Button(window, text = "tooltip button", bootstyle = "info")
button.pack()
# Tooltip(master)
ToolTip(button, text = "This does something", bootstyle = "success-inverse")

# calendar
calendar = DateEntry(window,
                     # this date format is the default one
                     dateformat = "%d-%m-%Y",
                     # default starting day = 6 (sunday)
                     firstweekday = 7,
                     bootstyle = "warning")
calendar.pack(pady = 10)

ttk.Button(window,
           text = "get calendar date",
           bootstyle = "light-link",
           command = lambda: print(calendar.entry.get())).pack()

# floodgauge (= progressbar tkinter)
progress_int = tk.IntVar(value = 50)
progress = ttk.Floodgauge(window,
                          text = "progress",
                          bootstyle = "danger",
                          variable = progress_int,
                          # overwriting a text into the bar
                          # {} displays the value of the progress
                          mask = "mask {}%")
progress.pack(pady = 10, fill = "x")

# autoincrement the gauge
# progress.stop() to stop it
progress.start(interval = 500)

# a scale that is linked to the progress bar
# and allows to control it
ttk.Scale(window, from_ = 0, to = 100, bootstyle = "light", variable = progress_int).pack(fill = "x")

# meter
# the diameter of the circle of the meter
meter = ttk.Meter(metersize = 180,
                  # space between the meter and the other widgets
                  padding = 10,
                  # value setted (default = 0)
                  amountused = 25,
                  # max value of the meter (default = 100)
                  amounttotal = 200,
                  # length of the indicator wedge
                  # 0 by default so the indicator goes from 0 to set value
                  wedgesize = 0,
                  # "full" or "semi" circle
                  metertype = "semi",
                  # thickness of the meter
                  # 10 by default
                  meterthickness = 20,
                  # by default = 0, so that the indicator is a solid bar
                  # when > 0, the indicator is made by striped wedges
                  stripethickness = 10,
                  # text under the value of the meter
                  subtext = "miles per hour",
                  # textright/left
                  textright = "mph",
                  # bootstyle color of the subtext and other text label defined
                  subtextstyle = "warning",
                  # if set to True, can be manually updated
                  interactive = True,
                  bootstyle = "info",
                  # indicates whether to show the left, center
                  # and right text labels on the meter;
                  # if set to False, only the subtext is visible
                  showtext = True,
                  # sets the amount by which to change the meter indicator
                  # when incremented by mouse interaction
                  stepsize = 10)
meter.pack()

meter.configure(amountused = 50)

# update the amount used with another widget
entry_meter = ttk.Entry(window, textvariable = meter.amountusedvar)
entry_meter.place(relx = 0.5, rely = 1, anchor = "s")

# increment the amount by 10 steps
meter.step(delta = -10)

# decrement the amount by 15 steps
meter.step(delta = 15)

# update the subtext
meter.configure(subtext = "loading...")

# run
window.mainloop()