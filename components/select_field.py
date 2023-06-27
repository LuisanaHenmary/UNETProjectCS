import tkinter as tkr
from tkinter import ttk


"""Select Field module"""


class SelectField:
    """It represents a field that allows selecting one of the multiple options from a list.

        Attributes:
            __int_value (IntVar): The selected current value
            __select_value (Combobox): It is to manipulate the properties of the ComboBox
    """
    def __init__(self, container, name_field, options, max_leng, coordinates=(0, 0)) -> None:
        """Initializes the object of type SelectField.

        Args:
            container (Widget): It is where the component will be contained
            name_field (str): Is the name of the field in the form
            options (list): There are multiple options for the Combobox
            max_leng (int): To determine the size of the Combobox
            coordinates (tuple): The 'x' and 'y' locations in the container
        """
        pos_x, pos_y = coordinates
        self.__int_value = tkr.IntVar()

        text_label = ttk.Label(container, text=name_field, style="SelectLabel.TLabel")
        text_label.place(x=pos_x, y=pos_y)

        self.__select_value = ttk.Combobox(container, textvariable=self.__int_value, font="Verdana 10")
        self.__select_value['state'] = "readonly"
        self.__select_value.place(x=(pos_x+50), y=pos_y)
        self.__select_value['values'] = options
        self.reboot_select()
        self.__select_value.config(width=max_leng, height=26)

    def get_choise_int(self) -> int:
        """Returns the current selected value."""
        return self.__int_value.get()

    def reboot_select(self) -> None:
        """Makes the selected value the first option in the ComboBox."""
        self.__select_value.current(0)
