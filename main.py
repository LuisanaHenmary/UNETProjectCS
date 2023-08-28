import os
import tkinter as tkr
from components.root_window import RootWindow
from views.app import App
from PIL import ImageTk, Image

"""This module runs everything."""


class StartupPresentation(tkr.Frame):
    """"""
    def __init__(self, container):
        """Initialize the startup presentation

            Args:
                container (Widget): It is where the view will be contained."""

        super().__init__(container, background="#EAEDED", width=1230, height=570)
        self.__notebook_pag = App(container)

        try:
            imagen = Image.open(os.path.join(os.getcwd(), "images", "SimbSur.jpeg"))
            imagen = imagen.resize((400, 400))
            test = ImageTk.PhotoImage(imagen)
            img = tkr.Label(self, image=test)
            img.image = test
            img.place(x=355, y=20)
        except Exception as e:
            print(e)
            tkr.Label(self, text="Imagen no encontrada").place(x=10, y=10)
        finally:
            tkr.Label(
                self,
                text="CONSEJO COMUNAL",
                font=("Arial", 50)
            ).place(x=250, y=420)
            self.place(x=0, y=0)

    def begin(self):
        """End the presentation and start the application"""

        self.destroy()
        self.__notebook_pag.place(x=0, y=0)


if __name__ == "__main__":
    root = RootWindow()
    startup_presentation = StartupPresentation(root)
    root.after(5000, startup_presentation.begin)
    root.mainloop()
