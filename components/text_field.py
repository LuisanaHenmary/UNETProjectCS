import tkinter as tkr
from tkinter import ttk


"""Text Field module"""


class TextField:
    """Represents a field, in the form, where an alphanumeric value is entered.

        Attributes:
            __text_value (StringVar): Is the value currently entered"""

    def __init__(self, container, name_field, coordinates=(0, 0)) -> None:
        """Initializes the object of type TextField.

            Args:
                container (Widget): It is where the component will be contained
                name_field (str): Is the name of the field in the form
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates
        self.__text_value = tkr.StringVar()
        text_label = ttk.Label(container, text=name_field, style="TextLabel.TLabel")
        text_label.place(x=pos_x, y=pos_y)
        self.__text_entry = ttk.Entry(container, textvariable=self.__text_value, width=28, font="Verdana 11")
        self.__text_entry.place(x=(pos_x+120), y=pos_y)

    def set_text_value(self, text) -> None:
        """Sets a new text.

            Args:
                text (str): It is the new established text."""

        self.__text_value.set(text)

    def get_text_value(self) -> str:
        """Return the value currently entered."""

        return self.__text_value.get()

    def reboot_field(self) -> None:
        """Converts the currently entered value to an empty string."""

        self.__text_value.set("")

    def changed_event(self, event_method) -> None:
        """Event that is executed when one of the options is selected.

            Args:
                event_method (method): It is an event"""

        self.__text_entry.bind('<KeyRelease>', event_method)
