from components.gas_cylinders_counter import GasCylindersCounter
from tkinter import ttk


"""Gas Cylinders Form module"""


class GasCylindersForm:
    """Represents a form to determine the quantity of cylinders purchased, in different
    types depending on their content (Kg).

        Attributes:
            __cylinders_10kg (GasCylindersCounter): Quantity of gas cylinders (purchased) of 10 kg
            __cylinders_18kg (GasCylindersCounter): Quantity of gas cylinders (purchased) of 18 kg
            __cylinders_27kg (GasCylindersCounter): Quantity of gas cylinders (purchased) of 27 kg
            __cylinders_43kg (GasCylindersCounter): Quantity of gas cylinders (purchased) of 43 kg"""

    def __init__(self, container, coordinates=(0, 0)) -> None:
        """Initializes the object of type GasCylindersForm.

            Args:
                container (Widget): It is where the component will be contained
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates

        label_form = ttk.Label(
            container,
            text="Cantidad de bombonas de gas\ndomestico que posee de:",
            style="BigLabel.TLabel"
        )

        label_form.place(x=pos_x, y=pos_y)

        self.__cylinders_10kg = GasCylindersCounter(container, "10 Kg:", (pos_x + 20, pos_y + 70))
        self.__cylinders_18kg = GasCylindersCounter(container, "18 Kg:", (pos_x + 150, pos_y + 70))
        self.__cylinders_27kg = GasCylindersCounter(container, "27 Kg:", (pos_x + 20, pos_y + 123))
        self.__cylinders_43kg = GasCylindersCounter(container, "43 Kg:", (pos_x + 150, pos_y + 125))

    def get_counters(self) -> dict[str, int]:
        """Returns a dictionary with the number of cylinders purchased, with their respective type."""

        return {
            "Kg10": self.__cylinders_10kg.get_counter(),
            "Kg18": self.__cylinders_18kg.get_counter(),
            "Kg27": self.__cylinders_27kg.get_counter(),
            "Kg43": self.__cylinders_43kg.get_counter()
        }

    def set_fields(self, new_values) -> None:
        """Sets new integer numeric values.

            Args:
                new_values (dict): Are the new integer numeric values"""

        self.__cylinders_10kg.set_counter(new_values["Kg10"])
        self.__cylinders_18kg.set_counter(new_values["Kg18"])
        self.__cylinders_27kg.set_counter(new_values["Kg27"])
        self.__cylinders_43kg.set_counter(new_values["Kg43"])

    def reboot_all_fields(self) -> None:
        """Return each counter to 0"""

        self.__cylinders_10kg.reboot_counter()
        self.__cylinders_18kg.reboot_counter()
        self.__cylinders_27kg.reboot_counter()
        self.__cylinders_43kg.reboot_counter()
