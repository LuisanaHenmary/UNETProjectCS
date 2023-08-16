import tkinter as tkr
from tkinter import ttk

"""This module has the table of records."""


class Table(ttk.Treeview):
    """This class creates a table with the columns already set."""

    def __init__(self, container, coordinates=(0, 0)) -> None:
        """Initializes the object of type Table.

        Args:
            container (Widget): It is where the component will be containe
            coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates
        head_columns = tuple(f"#{x}" for x in range(1, 13))

        super().__init__(container, columns=head_columns, show="headings")

        self.heading("#1", text="CI", anchor=tkr.CENTER)
        self.heading("#2", text="Nro.manz", anchor=tkr.CENTER)
        self.heading("#3", text="Nombre completo", anchor=tkr.CENTER)
        self.heading("#4", text="¿Lider de calle?", anchor=tkr.CENTER)
        self.heading("#5", text="¿Jefe de familia?", anchor=tkr.CENTER)
        self.heading("#6", text="Genero", anchor=tkr.CENTER)
        self.heading("#7", text="Fecha nacimiento", anchor=tkr.CENTER)
        self.heading("#8", text="Carnet de la patria serial", anchor=tkr.CENTER)
        self.heading("#9", text="10kg", anchor=tkr.CENTER)
        self.heading("#10", text="18kg", anchor=tkr.CENTER)
        self.heading("#11", text="27kg", anchor=tkr.CENTER)
        self.heading("#12", text="43kg", anchor=tkr.CENTER)

        self.column("#1", width=99, anchor='c')
        self.column("#2", width=55, anchor='c')
        self.column("#3", width=205, anchor='c')
        self.column("#4", width=100, anchor='c')
        self.column("#5", width=100, anchor='c')
        self.column("#6", width=110, anchor='c')
        self.column("#7", width=150, anchor='c')
        self.column("#8", width=150, anchor='c')
        self.column("#9", width=55, anchor='c')
        self.column("#10", width=55, anchor='c')
        self.column("#11", width=55, anchor='c')
        self.column("#12", width=55, anchor='c')
        self.place(x=pos_x, y=pos_y)
