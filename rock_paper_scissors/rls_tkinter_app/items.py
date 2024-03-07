import tkinter as tk
import paths
from image import Image_tk

class Item:
    def __init__(self, win_image_path: str, lost_image_path: str, neutral_image_path: str):
        self.win = Image_tk(win_image_path)
        self.lose = Image_tk(lost_image_path)
        self.neutral = Image_tk(neutral_image_path)

class Rock(Item):
    def __init__(self):
        super().__init__(
            paths.rock_win_image_path,
            paths.rock_lose_image_path,
            paths.rock_neutral_image_path,
        )

    def __gt__(self, other: Item) -> bool:
        """a > b"""
        return True if type(other) == Scissors else False

    def __lt__(self, other: Item) -> bool:
        """a < b"""
        return True if type(other) == Leaf else False

    def __eq__(self, other: Item) -> bool:
        """a == b"""
        return True if type(other) == Rock else False

    def __str__(self) -> str:
        return f"rock item"

class Leaf(Item):
    def __init__(self):
        super().__init__(
            paths.leaf_win_image_path,
            paths.leaf_lose_image_path,
            paths.leaf_neutral_image_path,
        )

    def __gt__(self, other: Item) -> bool:
        """a > b"""
        return True if type(other) == Rock else False

    def __lt__(self, other: Item) -> bool:
        """a < b"""
        return True if type(other) == Scissors else False

    def __eq__(self, other: Item) -> bool:
        """a == b"""
        return True if type(other) == Leaf else False

    def __str__(self) -> str:
        return f"leaf item"

class Scissors(Item):
    def __init__(self):
        super().__init__(
            paths.scissors_win_image_path,
            paths.scissors_lose_image_path,
            paths.scissors_neutral_image_path,
        )

    def __gt__(self, other: Item) -> bool:
        """a > b"""
        return True if type(other) == Leaf else False

    def __lt__(self, other: Item) -> bool:
        """a < b"""
        return True if type(other) == Rock else False

    def __eq__(self, other: Item) -> bool:
        """a == b"""
        return True if type(other) == Scissors else False

    def __str__(self) -> str:
        return f"scissors item"


if __name__ == "__main__":
    window = tk.Tk()

    rock = Rock()
    rock2 = Rock()
    leaf = Leaf()
    scissors = Scissors()

    canvas = tk.Canvas(window)
    canvas.pack(expand = True, fill = "both")
    canvas.create_image(0, 0, image=rock.neutral.image_tk, anchor="nw")

    print(scissors > leaf)

    window.mainloop()