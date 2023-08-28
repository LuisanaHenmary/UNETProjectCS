import tkinter as tkr
from tkinter import ttk
from views.utils import load_data, update_file
from views.records_table import RecordsTable
from views.register_form import RegisterForm
from styles.labels_style import (
    TextFieldLabel,
    SelectFieldLabel,
    CounterFieldLabel,
    BigLabel,
    WarningMessage
)

"""It is the application module"""


class App(ttk.Notebook):
    """It is the application.

        Attributes:
            __current_records (list): A list with all the records.
            __register_person (RegisterForm): The view of the records form.
            __records_t (RecordsTable): The record table view."""

    def __init__(self, container):
        """Initialize the application.

            Args:
                container (Widget): It is where the view will be contained."""

        super().__init__(container)
        self.place(x=0, y=0)

        self.__current_records = []
        self.__register_person = RegisterForm(self)
        self.__records_t = RecordsTable(self)

        TextFieldLabel()
        SelectFieldLabel()
        CounterFieldLabel()
        BigLabel()
        WarningMessage()

        tkr.Button(
            self.__register_person,
            text="Guardar",
            command=self.save_person,
            font=("Times", 14),
            background="#00FF00",
            foreground="White",
            padx=5,
            pady=5,
            bd=0
        ).place(x=1130, y=480)

        self.add(self.__register_person, text="Registo")
        self.add(self.__records_t, text="Registros actuales")

        self.load_records()

    def load_records(self):
        """Loads the records from json files, if it doesn't exist it creates it."""

        try:
            self.__current_records = load_data()

        except FileNotFoundError:
            update_file([])
            self.__current_records = load_data()

        self.__records_t.update_table(self.__current_records)
        self.__records_t.set_records(self.__current_records)

    def save_person(self):
        """Saves the person's registered information and updates the table."""

        self.__current_records.append(self.__register_person.save_all())

        update_file(self.__current_records)

        self.__records_t.update_table(self.__current_records)
        self.__records_t.all_filter()
        self.__register_person.reset_all()
