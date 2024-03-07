import os
from pathlib import Path
import customtkinter as ctk
from PIL import Image, ImageTk

class Image_tk:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.original = Image.open(os.path.join(Path(__file__).parent, self.file_name))
        self.image_tk = self._image_tk()
        self.image_ctk = self._ctk_image()

    def _image_tk(self):
        return ImageTk.PhotoImage(self.original)

    def _ctk_image(self):
        return ctk.CTkImage(
            dark_image=self.original,
            light_image=self.original,
            size=(215, 215),
            )