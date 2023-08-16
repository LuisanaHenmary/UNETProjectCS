import tkinter as tkr
import os


"""Root Window module"""


class RootWindow(tkr.Tk):
    """It is a child class of Tk that represents the main window of the application."""

    def __init__(self) -> None:
        """Initializes the object of type RootWindow."""

        super().__init__()
        super().title("AppName")
        self.iconbitmap(os.path.join(os.getcwd(), "images", "south.ico"))
        self.config(width=1230, height=570)
        self.resizable(False, False)
