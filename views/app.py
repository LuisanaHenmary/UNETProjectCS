import tkinter as tkr
from tkinter import ttk
from views.utils import load_data, update_file
from views.records_table import RecordsTable
from views.register_form import RegisterForm


class App(ttk.Notebook):

    def __init__(self, container):

        self.__current_records = []

        super().__init__(container)
        self.place(x=0, y=0)
        self.__register_person = RegisterForm(self)
        self.__records_t = RecordsTable(self)

        save_button = tkr.Button(
            self.__register_person,
            text="Guardar",
            command=self.save_person,
            font=("Times", 14),
            background="#00FF00",
            foreground="White",
            padx=5,
            pady=5,
            bd=0
        )
        save_button.place(x=900, y=270)
        self.add(self.__register_person, text="Registo")
        self.add(self.__records_t, text="Registros actuales")

        self.load_records()

    def load_records(self):
        try:
            self.__current_records = load_data()

        except FileNotFoundError:
            update_file([])
            self.__current_records = load_data()

        self.__records_t.update_table(self.__current_records)
        self.__records_t.set_records(self.__current_records)

    def save_person(self):

        self.__current_records.append(self.__register_person.save_all())

        update_file(self.__current_records)

        self.__records_t.update_table(self.__current_records)
        self.__records_t.all_filter()
        self.__register_person.reset_all()
