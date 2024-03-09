import random
import customtkinter as ctk
from image import Image_tk
import paths
import items


class Title_screen:
    """Display the title screen with a menu to select the number of rounds
    and a button to launch the game.
    """

    def __init__(self, parent, items: tuple) -> None:
        self.window = parent
        self.items = items
        self.set_rounds("3")
        self.create_widgets()

    def create_widgets(self) -> None:
        """Create the widgets of the window then call the layout method."""
        self.window.clear_window(self.window)

        self.label_title = ctk.CTkLabel(
            self.window,
            text="Pierre-feuille-ciseaux",
            font=self.window.title_font,
            )

        self.canvas = self.window.create_canvas(self.window)

        self.frame = ctk.CTkFrame(self.window, fg_color="transparent")
        self.label_option = ctk.CTkLabel(
            self.frame,
            text="Combien de manches voulez-vous jouer ?",
            font=self.window.text_font,
            )

        self.optionmenu = ctk.CTkOptionMenu(
            self.frame,
            font=self.window.button_font,
            values=["1 manche", "3 manches", "5 manches", "10 manches", "15 manches"],
            command=self.set_rounds,
            )
        # set the start value
        self.optionmenu.set("3 manches")

        self.button = ctk.CTkButton(
            self.window,
            text="Lancer le jeu",
            font=self.window.button_font,
            command=lambda: self.window.run_game(self.window, self.items, paths.button_sound),
            )

        self.create_layout()

    def insert_images(self, event) -> None:
        """Clear the canva and place the images widgets into it.
        Images are in the center of each third part of the canva.
        """
        self.canvas.delete("all")

        for i, image in enumerate(self.items):
            # the first one is at the (1/3 * width of the canva) / 2,
            # so it is at the 1/6 of the canva width;
            # the second image is at the 1/2 of the canva (2/3 - (1/3 / 2)), so 2/3 - 1/6;
            # the last one is at the width at the canva - 1/3 / 2, so at 5/6 of the width.
            self.canvas.create_image(
                event.width * (2 * i + 1) / 6,
                int(event.height / 2),
                image=image.neutral.image_tk,
                anchor="center",
                )

    def create_layout(self) -> None:
        """Manage the position of the widgets into the window
        with the place and pack methods.
        """
        self.label_title.place(
            relx=0.5,
            rely=0.1,
            relwidth=1,
            anchor="center",
            )

        self.canvas.place(
            relx=0,
            rely=0.2,
            relwidth=1,
            anchor="nw",
            )

        # The function is called every time the size of the canva changes,
        # including at the creation of the window when executing the script.
        self.canvas.bind("<Configure>", self.insert_images)

        self.frame.place(
            relx=0,
            rely=0.7,
            anchor="nw",
            relwidth=1,
            relheight=0.2,
            )

        self.button.place(
            relx=0.5,
            rely=0.93,
            anchor="center",
            )

        self.label_option.pack(
            side="left",
            expand=True,
            fill="both",
            pady=10,
            )

        self.optionmenu.pack(
            side="left",
            expand=True,
            )

    def set_rounds(self, choice: str) -> None:
        numb_round = []
        for char in choice:
            if char.isdigit():
                numb_round.append(char)
            else:
                break
        self.window.set_round_selected(self.window, int("".join(numb_round)))


class Choice_screen:
    """Display choices and allow the user to choose an item."""

    def __init__(self, parent, items: tuple) -> None:
        self.window = parent
        self.items = items
        self.create_widgets()

    def create_widgets(self) -> None:
        self.window.clear_window(self.window)

        self.label = ctk.CTkLabel(
            self.window,
            text="C'est le moment de choisir quoi jouer...",
            font=self.window.text_font,
            )

        self.button_frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent",
            )

        self.button_rock = ctk.CTkButton(
            self.button_frame,
            text="",
            image=self.items[0].neutral.image_ctk,
            compound="top",
            command=lambda choice = self.items[0]: self.start_duel(choice, paths.rock_sound),
            )

        self.button_leaf = ctk.CTkButton(
            self.button_frame,
            text="",
            image=self.items[1].neutral.image_ctk,
            compound="top",
            command=lambda choice = self.items[1]: self.start_duel(choice, paths.leaf_sound),
            )

        self.button_scissors = ctk.CTkButton(
            self.button_frame,
            text="",
            image=self.items[2].neutral.image_ctk,
            compound="top",
            command=lambda choice = self.items[2]: self.start_duel(choice, paths.scissors_sound),
            )

        self.window.display_score(self.window)
        self.create_layout()

    def create_layout(self) -> None:
        self.label.pack(
            side="top",
            fill="x",
            pady=100,
            ipady=30,
            )

        self.button_frame.pack(
            side="top",
            expand=True,
            fill="both",
            )

        self.button_scissors.pack(
            side="left",
            expand=True,
            padx=10,
            pady=20,
            )

        self.button_leaf.pack(
            side="left",
            expand=True,
            padx=10,
            pady=20,
            )

        self.button_rock.pack(
            side="left",
            expand=True,
            padx=10,
            pady=20,
            )

    def start_duel(self, choice: items, audio_path: str) -> None:
        self.window.play_sound(audio_path)
        Duel_screen(self.window, choice, self.items)


class Duel_screen:
    """Display the user and the computer choices"""

    def __init__(self, parent, user_choice: str, items: tuple) -> None:
        self.window = parent
        self.user_choice = user_choice
        self.items = items

        self.computer_choice = random.choice(items)

        self.win_text = "Vous avez gagné cette manche ! Bravo !"
        self.lose_text = "Vous avez perdu cette manche... Dommage."
        self.draw_text = "Egalité. La manche ne compte pas."

        self.button_draw_text = "Rejouer la manche"
        self.button_text = "Suivant"

        self.create_widgets()

    def create_widgets(self) -> None:
        self.window.clear_window(self.window)
        match_score = self.match()

        self.canvas = self.window.create_canvas(self.window)

        self.label_user = ctk.CTkLabel(
            self.window,
            text="Joueur",
            font=self.window.text_font
            )

        self.label_computer = ctk.CTkLabel(
            self.window,
            text="Ordinateur",
            font=self.window.text_font
            )

        self.label_vs = ctk.CTkLabel(
            self.window,
            text="VS",
            font=self.window.text_font
            )

        self.label = ctk.CTkLabel(
            self.window,
            text=match_score[2],
            font=self.window.text_font
            )

        self.button = ctk.CTkButton(
            self.window,
            text=match_score[3],
            font = self.window.button_font,
            command=lambda: self.window.run_game(self.window, self.items, paths.button_sound),
        )

        self.window.display_score(self.window)
        self.create_layout(match_score)

    def insert_images(self, event, match: tuple) -> None:
        """Clear the canva and place the images widgets into it.
        Images are in the center of each third part of the canva.
        """
        self.canvas.delete("all")

        for i, image in enumerate((match[0], match[1])):
            self.canvas.create_image(
                event.width * (2 * i + 1) / 4,
                int(event.height / 2),
                image=image.image_tk,
                anchor="center",
                )

    def create_layout(self, match: tuple) -> None:
        self.canvas.place(
            relx=0,
            rely=0.2,
            relwidth=1,
            anchor="nw",
            )
        self.canvas.bind("<Configure>", lambda event: self.insert_images(event, match))

        self.label_vs.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
        )

        self.label_user.place(
            relx=0.2,
            rely=0.25,
            anchor="nw",
        )

        self.label_computer.place(
            relx=0.7,
            rely=0.25,
            anchor="nw",
        )

        self.label.place(
            relx=0,
            rely=0.7,
            relwidth=1,
            anchor="nw",
        )

        self.button.place(
            relx=0.5,
            rely=0.9,
            anchor="center"
        )

    def match(self) -> tuple:
        if self.user_choice == self.computer_choice:
            return (self.user_choice.neutral, self.computer_choice.neutral, self.draw_text, self.button_draw_text)
        elif self.user_choice > self.computer_choice:
            self.window.set_round_passed(self.window, self.window.round_passed + 1)
            self.window.set_score(self.window, (self.window.score[0] + 1), self.window.score[1])
            return (self.user_choice.win, self.computer_choice.lose, self.win_text, self.button_text)
        elif self.user_choice < self.computer_choice:
            self.window.set_round_passed(self.window, self.window.round_passed + 1)
            self.window.set_score(self.window, self.window.score[0], (self.window.score[1] + 1))
            return (self.user_choice.lose, self.computer_choice.win, self.lose_text, self.button_text)


class Winner_screen:
    """Display the winner of the game"""

    def __init__(self, parent, items: tuple):
        self.window = parent
        self.items = items

        self.end_sentence, self.sound = self.determine_winner()

        self.thumb_up = Image_tk(paths.thumb_up)
        self.thumb_down = Image_tk(paths.thumb_down)

        self.window.play_sound(self.sound)
        self.create_widgets()

    def determine_winner(self):
        if self.window.score[0] > self.window.score[1]:
            return ("Bien joué, vous êtes le gagnant !", paths.success_sound)
        else:
            return ("L'ordinateur a gagné,\nvous aurez plus de chance la prochaine fois !", paths.fail_sound)

    def new_game(self):
        self.window.play_sound(paths.button_sound)
        self.window.set_round_passed(self.window, 0)
        self.window.set_score(self.window, reset=True)
        self.window.title = Title_screen(self.window, self.items)

    def create_widgets(self):
        self.window.clear_window(self.window)

        self.canvas = self.window.create_canvas(self.window)

        self.win_lose_sentence = ctk.CTkLabel(
            self.window,
            text=self.end_sentence,
            font=self.window.text_font,
            compound="center",
        )

        self.frame = ctk.CTkFrame(
            self.window,
            fg_color="transparent",
        )

        self.button_new = ctk.CTkButton(
            self.frame,
            text="Rejouer",
            font=self.window.button_font,
            command=self.new_game,
        )

        self.button_exit = ctk.CTkButton(
            self.frame,
            text="Quitter le jeu",
            font=self.window.button_font,
            command=quit,
        )

        self.window.display_score(self.window, True)
        self.create_layout()

    def insert_image(self, event):
        self.canvas.delete("all")

        if self.window.score[0] > self.window.score[1]:
            self.canvas.create_image(
                int(event.width / 2),
                int(event.height / 2),
                image=self.thumb_up.image_tk,
                anchor="center",
                )
        else:
            self.canvas.create_image(
                int(event.width / 2),
                int(event.height / 2),
                image=self.thumb_down.image_tk,
                anchor="center",
                )

    def create_layout(self):
        self.canvas.pack(
            side="top",
            expand= True,
            fill="both",
            pady = 50,
        )

        self.canvas.bind("<Configure>", lambda event: self.insert_image(event))

        self.win_lose_sentence.place(
            relx=0.5,
            rely=0.6,
            anchor="center",
        )

        self.frame.pack(
            side="top",
            pady=50,
        )

        self.button_new.pack(
            side="left",
            expand=True,
            padx=20,
            pady=30,
        )

        self.button_exit.pack(
            side="left",
            expand=True,
            padx = 20,
            pady=30,
        )

