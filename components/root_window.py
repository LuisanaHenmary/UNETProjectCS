import tkinter as tkr


"""Root Window module"""


class RootWindow(tkr.Tk):
    """It is a child class of Tk that represents the main window of the application."""
    def __init__(self) -> None:
        """Initializes the object of type RootWindow."""
        super().__init__()
        super().title("AppName")
        self.config(width=1390, height=570)
        self.resizable(False, False)
