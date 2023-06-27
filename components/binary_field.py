import tkinter as tkr
from tkinter import ttk


"""Binary Field module"""


class BinaryField:
    """It is a field with two 'Radio Button', where the first option has the value 'True'
    and the other has the value 'False'.

        Attributes:
            __selected (BooleanVar): The selected current value
    """
    def __init__(self, container, field_name, binary_options=("Si", "No"), coordinates=(0, 0)) -> None:
        """Initializes the object of type BinaryField.

                Args:
                    container (Widget): It is where the component will be contained
                    field_name (str): Is the name of the field in the form
                    binary_options (tuple): There are two options for every Radio Button
                    coordinates (tuple): The 'x' and 'y' locations in the container
        """
        pos_x, pos_y = coordinates
        op1, op2 = binary_options
        self.__selected = tkr.BooleanVar()

        label_field = ttk.Label(container, text=field_name, style="BigLabel.TLabel")
        label_field.place(x=pos_x, y=pos_y)

        style_radio = ttk.Style()
        style_radio.configure("BothRadio.TRadiobutton", font="Verdana 12", background="White")

        option1 = ttk.Radiobutton(
            container,
            text=op1,
            value=True,
            variable=self.__selected,
            style="BothRadio.TRadiobutton"
        )

        option2 = ttk.Radiobutton(
            container,
            text=op2,
            value=False,
            variable=self.__selected,
            style="BothRadio.TRadiobutton"
        )

        option1.place(x=pos_x, y=pos_y+30)
        option2.place(x=pos_x, y=pos_y+60)

        self.reboot_current_value()

    def get_binary_value(self) -> bool:
        """Returns the current selected value."""
        return self.__selected.get()

    def reboot_current_value(self) -> None:
        """Sets the current value to be 'False'."""
        self.__selected.set(False)
