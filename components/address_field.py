import tkinter as tkr
from tkinter import ttk


"""Address Field module"""


class AddressField:

    """Represents a text field where you can enter the address.

        Attributes:
            __input_field (Text): Is the value currently entered"""

    def __init__(self, container, coordinates=(0, 0)) -> None:
        """Initializes the object of type AddressField.

            Args:
                container (Widget): It is where the component will be contained
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates
        address_label = ttk.Label(container, text="Dirección:", style="TextLabel.TLabel")
        address_label.place(x=pos_x, y=pos_y)

        self.__input_field = tkr.Text(container, height=9, width=50, background="#CCE5FF")
        self.__input_field.place(x=pos_x, y=pos_y+30)

    def get_address(self) -> str:
        """Return the value currently entered."""
        return self.__input_field.get(1.0, "end-1c")

    def set_address(self, text) -> None:
        """Sets a new text.

            Args:
                text (str): It is the new established text."""

        self.__input_field.insert(1.0, text)

    def reboot_text_field(self) -> None:
        """Converts the currently entered value to an empty string."""
        self.__input_field.delete(1.0, "end-1c")
