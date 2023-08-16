from tkinter import ttk, scrolledtext


"""Address Field module"""


class ObservationsField:

    """Represents a text field where you can enter the address.

        Attributes:
            __input_field (Text): Is the value currently entered"""

    def __init__(self, container, coordinates=(0, 0)) -> None:
        """Initializes the object of type AddressField.

            Args:
                container (Widget): It is where the component will be contained
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates

        observations_label = ttk.Label(
            container,
            text="Observaciones:",
            style="TextLabel.TLabel"
        )

        observations_label.place(x=pos_x, y=pos_y)

        self.__input_field = scrolledtext.ScrolledText(
            container,
            height=9,
            width=65,
            background="#CCE5FF"
        )

        self.__input_field.place(x=pos_x, y=pos_y+30)

    def get_observations(self) -> str:
        """Return the value currently entered."""

        return self.__input_field.get(1.0, "end-1c")

    def set_text(self, text) -> None:
        """Sets a new text.

            Args:
                text (str): It is the new established text."""

        self.__input_field.insert(1.0, text)

    def disabled(self) -> None:
        """Disable text editing."""

        self.__input_field["state"] = 'disabled'

    def reboot_text_field(self) -> None:
        """Converts the currently entered value to an empty string."""

        self.__input_field.delete(1.0, "end-1c")
