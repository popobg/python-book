#! /usr/bin/env python3

"""Rock leaf scissors game app with Tkinter and original images."""

import os
from pathlib import Path
import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
import pygame
from screens import Title_screen, Choice_screen, Winner_screen
import paths
import items

# MAIN CLASS
class App(ctk.CTk):

    # class attributes
    round_passed = 0
    score = [0, 0]
    round_selected = None

    def __init__(self, name: str, size: tuple[int]):
        super().__init__()

        self.title(name)
        self.geometry(self.center_window(
            size[0],
            size[1],
            self._get_window_scaling()
            ))
        self.minsize(size[0], size[1])
        self.maxsize(1000, 900)

        # set the icon
        self.set_icon(ctk.get_appearance_mode())

        # track if the system changes theme and link the changing of icon to it
        ctk.AppearanceModeTracker.callback_list.append(self.set_icon)

        self.create_ctk_style()

        # initiate pygame to play music
        pygame.mixer.init()

        self.items = (items.Rock(), items.Leaf(), items.Scissors())

        self.title = Title_screen(self, self.items)

        self.mainloop()

    def set_icon(self, appearance_mode: str) -> None:
        """Convert any photo format into an icon and set it as the window's icon.
        Adapt the icon to the system appearance mode.
        """
        if appearance_mode == "Dark":
            path = os.path.join(Path(__file__).parent, paths.icon_dark)
        else:
            path = os.path.join(Path(__file__).parent, paths.icon_light)
        icon = ImageTk.PhotoImage(file=path)

        self.wm_iconbitmap()
        self.iconphoto(False, icon)

    def center_window(self, width: int, height: int, scale_factor: float = 1.0) -> str:
        """Center the window on the main monitor when executing the program."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def create_ctk_style(self) -> None:
        """Create different styles with ctk to be used by the widgets."""
        self.title_font = ctk.CTkFont(
            family="Georgia",
            size=45,
            slant="italic",
            )

        self.text_font = ctk.CTkFont(
            family="Georgia",
            size=23,
            weight="normal",
            )

        self.little_text_font = ctk.CTkFont(
            family="Georgia",
            size=18,
            weight="normal",
            slant="italic",
            )

        self.button_font = ctk.CTkFont(
            family="Georgia",
            size=20,
        )

    @staticmethod
    def set_round_selected(app, new_number: int) -> None:
        app.round_selected = new_number

    @staticmethod
    def set_round_passed(app, new_number: int) -> None:
        app.round_passed = new_number

    @staticmethod
    def set_score(app, user_score: int = 0, computer_score: int = 0, reset: bool = False) -> None:
        """Update the score; the reset option set the score to 0."""
        if reset:
            app.score = [0, 0]
            return None
        app.score = [user_score, computer_score]
        return None

    @staticmethod
    def clear_window(app) -> None:
        """Destroy all the widgets currently on the window."""
        for widget in app.winfo_children():
            widget.destroy()

    @staticmethod
    def create_canvas(app) -> tk.Canvas:
        """Create a canva and adjust the background to the system appearance mode."""
        # update is necessary to get the accurate size of the window via winfo
        app.update()
        canvas = tk.Canvas(
            app,
            width=app.winfo_width(),
            height=app.winfo_height() / 2,
            bd=0,
            highlightthickness=0,
            relief="ridge",
            )

        if ctk.get_appearance_mode() == "Light":
            canvas.configure(bg = app.cget("fg_color")[0])
        else:
            canvas.configure(bg = app.cget("fg_color")[1])

        return canvas

    @staticmethod
    def display_score(app, winner:bool = False) -> None:
        """Display the current score via a label."""
        label_score = ctk.CTkLabel(
                master=app,
                text=f"Joueur : {app.score[0]} ; ordinateur : {app.score[1]}",
                font=app.little_text_font
            )

        if winner:
            label_score.place(
                relx=0.5,
                rely=0.17,
                anchor="center"
            )
        else:
            label_score.place(
                relx=0.99,
                rely=0.05,
                anchor="ne"
            )

    @staticmethod
    def run_game(app, items: tuple, audio_path: str) -> None:
        """Manage the transition between different states of the game
        and play the sound button effect.
        """
        app.play_sound(audio_path)
        if app.round_passed < app.round_selected:
            Choice_screen(app, items)
        else:
            Winner_screen(app, items)

    @staticmethod
    def play_sound(path: str) -> None:
        """Play the sound at the given path"""
        pygame.mixer.music.load((os.path.join(Path(__file__).parent, path)))
        pygame.mixer.music.play(loops = 0)

# CLASSES
app = App("Pierre-feuille-ciseaux", (750, 750))