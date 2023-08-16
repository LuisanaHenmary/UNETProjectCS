import tkinter as tkr
from tkinter import ttk
from components.observations_field import ObservationsField
from datetime import datetime
from views.utils import calculate_age

"""This module is to give details of a person."""


class Detail(ttk.Label):
    """This class is a label with a piece of information."""

    def __init__(self, container, text, style="TextLabel.TLabel", coordinates=(0, 0)):
        """Initialize the label

            Args:
                container (Widget): It is where the view will be contained.
                text (str): It is written information.
                style (str): It is the name of the label style.
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        super().__init__(container, text=text, style=style)
        x, y = coordinates
        self.place(x=x, y=y)


class DetailsPersonWindow(tkr.Toplevel):
    """Creates a secondary window with a person's information."""

    def __init__(self, info):
        """Initialize the window.

            Args:
                info (dict): It is a dictionary with the information of a person."""

        super().__init__(width=850, height=570)
        self.resizable(False, False)
        self.title(str(info['CI']))

        born = datetime(
            info['Birthday']['year'],
            info['Birthday']['month'],
            info['Birthday']['day']
        )

        age = calculate_age(born)

        frame = tkr.Frame(self, width=1210, height=570, background='#99CCFF')
        frame.place(x=0, y=0)

        Detail(
            frame,
            text=f"CI: {info['CI']}.",
            coordinates=(20, 20)
        )

        Detail(
            frame,
            text=f"Nro Manzana: {info['Street']}.",
            coordinates=(200, 20)
        )

        Detail(
            frame,
            text=f"Lider de calle" if info["IsLeaderStreet"] else "",
            style="BigLabel.TLabel",
            coordinates=(380, 20)
        )

        Detail(
            frame,
            text=f"Jefe de familia" if info["IsFamilyLeader"] else "",
            style="BigLabel.TLabel",
            coordinates=(560, 20)
        )

        fullname = f"{info['Names']} {info['Lastnames']}"

        Detail(
            frame,
            text=f"Nombre completo: {fullname}.",
            coordinates=(20, 60)
        )

        Detail(
            frame,
            text=f"Genero: {'Femenino' if info['Gender'] else 'Masculino'}.",
            coordinates=(20, 100)
        )

        Detail(
            frame,
            text=f"Cumpleaños: {born.strftime('%d/%m/%Y')}.",
            coordinates=(200, 100)
        )

        Detail(
            frame,
            text=f"Edad: {age}",
            coordinates=(440, 100)
        )

        Detail(
            frame,
            text=f"Nro. carnet de patria: {info['SerialCard']}",
            coordinates=(20, 140)
        )

        Detail(
            frame,
            text=f"Nro. Teléfono: {info['PhoneNumber']}",
            coordinates=(300, 140)
        )

        Detail(
            frame,
            text=f"Email: {info['Email']}",
            coordinates=(560, 140)
        )

        Detail(
            frame,
            text="Cantidad de bombonas de:",
            style="BigLabel.TLabel",
            coordinates=(20, 180)
        )

        pos_x = 20
        for kg in [10, 18, 27, 43]:
            key = f"Kg{kg}"
            Detail(
                frame,
                text=f"{kg} kg: {info['GasCounters'][key]}",
                coordinates=(pos_x, 220)
            )
            pos_x += 100

        Detail(
            frame,
            text=f"Dirección: {info['Address']}",
            coordinates=(20, 270)
        )

        text = ObservationsField(self, coordinates=(20, 320))
        text.set_text(info["Observations"])
        text.disabled()
