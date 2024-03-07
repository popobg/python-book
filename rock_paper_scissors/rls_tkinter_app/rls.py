#! /usr/bin/env python3

"""Rock paper scissors game app with Tkinter and original images."""

import os
from pathlib import Path
import random
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

class Rock:
    def __init__(self):
        self.neutral = Image_tk("rock.png")
        self.win = Image_tk("rock_win.png")
        self.lose = Image_tk("rock_lose.png")


# gérer le nombre de rounds (while ?), créer les widgets pour le choice et le duel screen.

class App(ctk.CTk):

    def __init__(self, name: str, size: tuple[int]):
        super().__init__()

        self.title(name)
        self.geometry(self.center_window(
            size[0],
            size[1],
            self._get_window_scaling()
            ))
        self.minsize(size[0], size[1])
        self.maxsize(1000, 700)

        # set the icon
        appearance_mode = ctk.get_appearance_mode()
        self.set_icon(appearance_mode)

        # track if the system changes theme and link the changing of icon to it
        ctk.AppearanceModeTracker.callback_list.append(self.set_icon)

        self.create_ctk_style()

        # reminder: the images used in a canva
        # needs to be in the same scop as the mainloop
        self.basic_rock = Image_tk("rock.png")
        self.win_rock = Image_tk("rock_win.png")
        self.lose_rock = Image_tk("rock_lose.png")
        self.basic_leaf = Image_tk("leaf.png")
        self.win_leaf = Image_tk("leaf_win.png")
        self.lose_leaf = Image_tk("leaf_lose.png")
        self.basic_scissors = Image_tk("scissors.png")
        self.win_scissors = Image_tk("scissors_win.png")
        self.lose_scissors = Image_tk("scissors_lose.png")

        self.title = Title_screen(self)

        self.score = (0, 0)
        self.round_passed = 0
        # for i in range(self.round + 1):
        #     choice = Choice_screen()
        #     Duel_screen(choice.user_choice)


        self.mainloop()

    def set_icon(self, appearance_mode: str) -> None:
        """Convert any photo format into an icon and set it as the window's icon.
        Adapt the icon to the system appearance mode.
        """
        if appearance_mode == "Dark":
            path = os.path.join(Path(__file__).parent, "icon_dark.png")
        else:
            path = os.path.join(Path(__file__).parent, "icon_light.png")
        icon = ImageTk.PhotoImage(file = path)

        self.wm_iconbitmap()
        self.iconphoto(False, icon)

    def center_window(self, width: int, height: int, scale_factor: float = 1.0) -> str:
        """Center the window on the main monitor when executing the program."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.5)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def create_ctk_style(self):
        """Create different styles with ctk to be used by the widgets."""
        self.title_font = ctk.CTkFont(
            family = "Georgia",
            size = 45,
            slant = "italic",
            )

        self.text_font = ctk.CTkFont(
            family = "Georgia",
            size = 23,
            weight = "normal",
            )

        self.button_font = ctk.CTkFont(
            family = "Georgia",
            size = 20,
        )

    def clear_window(self):
        """Destroy all the widgets currently on the window."""
        for widget in self.winfo_children():
            widget.destroy()

    def start_game(self):
        if self.round_passed < int(self.title.round[0]):
            self.round_passed += 1
            self.choice = Choice_screen(self)
            print(self.round_passed)
        else:
            self.winner_display = Winner_screen(self)


class Title_screen:
    """Display the title screen with a menu to select the number of rounds
    and a button to launch the game.
    """

    def __init__(self, parent: App) -> None:
        self.window = parent
        self.round = "3 manches"
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create the widgets of the window then call the layout method."""
        self.label_title = ctk.CTkLabel(
            self.window,
            text = "Pierre-feuille-ciseaux",
            font = self.window.title_font,
            )

        self.create_canvas()

        self.frame = ctk.CTkFrame(self.window, fg_color = "transparent")
        self.label_option = ctk.CTkLabel(
            self.frame,
            text = "Combien de manches voulez-vous jouer ?",
            font = self.window.text_font,
            )

        self.optionmenu = ctk.CTkOptionMenu(
            self.frame,
            font = self.window.button_font,
            values = ["1 manche", "3 manches", "5 manches", "10 manches", "15 manches"],
            command = self.set_rounds,
            )
        self.optionmenu.set("3 manches")

        self.button = ctk.CTkButton(
            self.window,
            text = "Lancer le jeu",
            font = self.window.button_font,
            command = self.window.start_game,
            )

        self.create_layout()

    def create_canvas(self) -> None:
        """Create a canva and adjust the background to the system appearance mode."""
        # update is necessary to get the accurate size of the window via winfo
        self.window.update()
        self.canvas = tk.Canvas(
            self.window,
            width = self.window.winfo_width(),
            height = self.window.winfo_height() / 2,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge",
            )

        if ctk.get_appearance_mode() == "Light":
            self.canvas.configure(bg = self.window.cget("fg_color")[0])
        else:
            self.canvas.configure(bg = self.window.cget("fg_color")[1])

    def insert_images(self, event):
        """Clear the canva and place the images widgets into it.
        Images are in the center of each third part of the canva.
        """
        self.canvas.delete("all")

        for i, image in enumerate((self.window.basic_rock, self.window.basic_leaf, self.window.basic_scissors)):
            # the first one is at the (1/3 * width of the canva) / 2,
            # so it is at the 1/6 of the canva width;
            # the second image is at the 1/2 of the canva (2/3 - (1/3 / 2)), so 2/3 - 1/6;
            # the last one is at the width at the canva - 1/3 / 2, so at 5/6 of the width.
            self.canvas.create_image(event.width * (2 * i + 1) / 6, int(event.height / 2), image = image.image_tk, anchor = "center")

    def create_layout(self):
        """Manage the position of the widgets into the window
        with the place and pack methods.
        """
        self.label_title.place(
            relx = 0.5,
            rely = 0.1,
            relwidth = 1,
            anchor = "center",
            )
        self.canvas.place(
            relx = 0,
            rely = 0.2,
            relwidth = 1,
            anchor = "nw",
            )

        # The function is called every time the size of the canva changes,
        # including at the creation of the window when executing the script.
        self.canvas.bind("<Configure>", self.insert_images)

        self.frame.place(
            relx = 0,
            rely = 0.7,
            anchor = "nw",
            relwidth = 1,
            relheight = 0.2,
            )
        self.button.place(
            relx = 0.5,
            rely = 0.93,
            anchor = "center",
            )

        self.label_option.pack(
            side = "left",
            expand = True,
            fill= "both",
            pady = 10,
            )
        self.optionmenu.pack(
            side = "left",
            expand = True,
            )

    def set_rounds(self, choice) -> None:
        self.round = choice


class Choice_screen:
    """Display choices and allow the user to choose an item."""

    def __init__(self, parent: App) -> None:
        self.window = parent
        self.create_widgets()

    def create_widgets(self) -> None:
        self.window.clear_window()

        self.label = ctk.CTkLabel(
            self.window,
            text = "C'est le moment de choisir quoi jouer...",
            font = self.window.text_font,
            )
        self.button_frame = ctk.CTkFrame(
            self.window,
            fg_color = "transparent",
            )

        self.button_scissors = ctk.CTkButton(
            self.button_frame,
            text = "",
            image = self.window.basic_scissors.image_ctk,
            compound = "top",
            command = lambda choice = "scissors": self.start_duel(choice),
            )
        self.button_leaf = ctk.CTkButton(
            self.button_frame,
            text = "",
            image = self.window.basic_leaf.image_ctk,
            compound = "top",
            command = lambda choice = "leaf": self.start_duel(choice),
            )
        self.button_rock = ctk.CTkButton(
            self.button_frame,
            text = "",
            image = self.window.basic_rock.image_ctk,
            compound = "top",
            command = lambda choice = "rock": self.start_duel(choice),
            )

        self.create_layout()

    def create_layout(self) -> None:
        self.label.pack(side = "top", fill = "x", pady = 20, ipady = 30)
        self.button_frame.pack(side = "top", expand = True, fill = "both")

        self.button_scissors.pack(side = "left", expand = True, padx = 10, pady = 20)
        self.button_leaf.pack(side = "left", expand = True, padx = 10, pady = 20)
        self.button_rock.pack(side = "left", expand = True, padx = 10, pady = 20)

    def start_duel(self, choice: str) -> None:
        duel = Duel_screen(self.window, choice)


class Duel_screen:
    """Display the user and the computer choices"""

    def __init__(self, parent: App, user_choice: str) -> None:
        self.window = parent
        self.user_choice = user_choice
        self.computer_choice = random.choice(["scissors", "leaf", "rock"])
        self.win_text = "Vous avez gagné cette manche ! Bravo !"
        self.lose_text = "Vous avez perdu cette manche... Dommage."
        self.draw_text = "Egalité. La manche ne compte pas."
        # self.create_widgets()

    # def create_widgets(self):
    #     self.window.clear_window()

    #     self.match()

    # def match(self) -> tuple:
    #     if self.user_choice == self.computer_choice:
            

    #     elif self.user_choice == "rock":
    #         if self.computer_choice == "scissors":
    #             return ()
    #         else:
    #             pass

    #     elif self.user_choice == "leaf" and self.computer_choice == "":
    #         pass


class Winner_screen:
    """Display the winner of the game"""

    def __init__(self, parent: App):

        print("end of the game")

class Image_tk:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.original = self.open_image()
        self.image_tk = self.set_image_tk()
        self.image_ctk = self.set_ctk_image()

    def open_image(self) -> str:
        return Image.open(os.path.join(Path(__file__).parent, self.file_name))

    def set_image_tk(self):
        return ImageTk.PhotoImage(self.original)

    # def resize_image(self, size: tuple):
    #     # resize with the values given : (width, height)
    #     self.original = self.original.resize(size)
    #     self.image_tk = self.set_image_tk()

    def set_ctk_image(self):
        return ctk.CTkImage(
            dark_image = self.original,
            light_image = self.original,
            size = (215, 215),
            )


app = App("Pierre-feuille-ciseaux", (750, 550))