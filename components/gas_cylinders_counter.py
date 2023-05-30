import tkinter as tkr


"""Gas Cylinders Counter module"""


class GasCylindersCounter:
    """Represents a counter of purchased gas cylinders.

        Attributes:
            __cylinder_counter (IntVar): Quantity of gas cylinders

    """
    def __init__(self, container, cylinder_kg, coordinates=(0, 0)) -> None:
        """Initializes the object of type GasCylindersCounter.

                Args:
                    container (Widget): It is where the component will be contained
                    cylinder_kg (str): To indicate how many kilograms the cylinders are
                    coordinates (tuple): The 'x' and 'y' locations in the container
        """
        pos_x, pos_y = coordinates
        self.__cylinder_counter = tkr.IntVar()
        self.reboot_counter()
        kg_label = tkr.Label(container, text=cylinder_kg, background="White")
        kg_label.place(x=pos_x, y=pos_y)
        gas_count = tkr.Spinbox(container, from_=0, to=10, textvariable=self.__cylinder_counter, width=4)
        gas_count.place(x=(pos_x+40), y=pos_y)

    def get_counter(self) -> int:
        """Returns the number of cylinders, of n Kg, purchased."""
        return self.__cylinder_counter.get()

    def reboot_counter(self) -> None:
        """Returns the counter to 0"""
        self.__cylinder_counter.set(0)
