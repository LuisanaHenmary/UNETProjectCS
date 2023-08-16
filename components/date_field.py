from components.select_field import (SelectField, ttk)
import datetime


"""Date Field module"""


class DateField:
    """It is a field, in the form, that allows selecting the day, month and year of a specific date.

        Attributes:
            __day (SelectField): The selected day of the month
            __month (SelectField): The selected month
            __year (SelectField): The selected year"""

    def __init__(self, container, min_year=1900, coordinates=(0, 0)) -> None:
        """Initializes the object of type BinaryField.

            Args:
                container (Widget): It is where the component will be contained
                min_year (int): First choice for the year
                coordinates (tuple): The 'x' and 'y' locations in the container"""

        pos_x, pos_y = coordinates
        days = [x for x in range(1, 32)]
        months = [x for x in range(1, 13)]
        current_year = datetime.date.today().year
        years = [x for x in range(min_year, current_year + 1)]

        main_label = ttk.Label(container, text="Fecha de nacimiento", style="BigLabel.TLabel")
        main_label.place(x=pos_x, y=pos_y)

        self.__day = SelectField(container, "Día:", days, 5, (pos_x, pos_y+40))
        self.__month = SelectField(container, "Mes:", months, 5, (pos_x, pos_y + 80))
        self.__year = SelectField(container, "Año:", years, 5, (pos_x, pos_y + 120))

    def get_date(self) -> dict[str, int]:
        """Returns a dictionary with the values of the currently
        selected day, month, and year."""

        return {
            "day": self.__day.get_choise_int(),
            "month": self.__month.get_choise_int(),
            "year": self.__year.get_choise_int()
        }

    def reboot_fields(self) -> None:
        """Restarts all ComboBoxes."""

        self.__day.reboot_select()
        self.__month.reboot_select()
        self.__year.reboot_select()
