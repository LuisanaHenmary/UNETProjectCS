import tkinter as tkr
from tkinter import ttk
from datetime import datetime
from components.table import Table
from components.select_field import SelectField
from components.text_field import TextField
from views.utils import search_index_person, update_file, calculate_age
from views.details_windows import DetailsPersonWindow
from views.update_window import UpdatePeople


"""This module has a class that has the records table and a filter panel."""


class RecordsTable(tkr.Frame):
    """Create the view that has the records table and the filter panel.

    Attributes:
        __all_records (list): It is to have all the records.
        __only_street_leader (BooleanVar): It is to establish if the street leader filter is active
        __only_family_leader (BooleanVar): It is to establish if the filter of heads of family is active.
        __min_age (StringVar): It is to enter the minimum age.
        __max_age (StringVar): It is to enter the maximum age.
        __only_nkg (IntVar): It is to establish which gas cylinder filter options are active.
        __records (Table): It is to manipulate the table of records.
        __number_results (Label): It is a label to display the number of results.
        __message (Label): It is a label to display a warning message.
        __street_filter (SelectField): It is a field to select the number of the block.
        __ci_filter (TextField): It is a field to enter the identification number."""

    def __init__(self, container) -> None:
        """Initializes the RecordsTable view.

            Args:
                container (Widget): It is where the view will be contained."""

        super().__init__(container)
        self.config(background="#99CCFF", height=370, width=1450)
        self.place(x=5, y=5)

        self.__all_records = []

        self.__only_street_leader = tkr.BooleanVar()
        self.__only_family_leader = tkr.BooleanVar()
        self.__only_committee_member = tkr.BooleanVar()
        self.__min_age = tkr.StringVar()
        self.__max_age = tkr.StringVar()
        self.__only_nkg = tkr.IntVar()

        self.__min_age.set("0")
        self.__max_age.set("150")
        self.__only_nkg.set(0)

        self.__records = Table(self, (10, 10))
        self.__number_results = ttk.Label(self, style="TextLabel.TLabel")
        self.__number_results.place(x=10, y=240)
        self.__message = ttk.Label(self, style="WarningLabel.TLabel")
        self.__message.place(x=250, y=240)

        filter_options = [x for x in range(25) if x not in [5, 22]]

        ttk.Label(
            self,
            text="Filtrar por:",
            style="BigLabel.TLabel"
        ).place(x=10, y=270)

        self.__street_filter = SelectField(
            self,
            "Nro.\nManzana:",
            filter_options,
            7,
            (10, 310)
        )

        self.__street_filter.changed_event(self.all_filter)

        self.__ci_filter = TextField(
            self,
            name_field="Nro. cedula:",
            coordinates=(10, 370)
        )

        self.__ci_filter.changed_event(self.all_filter)

        ttk.Label(
            self,
            text="Edad entre:",
            style="TextLabel.TLabel"
        ).place(x=10, y=415)

        age_min = tkr.Entry(
            self,
            textvariable=self.__min_age,
            width=5
        )

        age_min.bind("<KeyRelease>", self.all_filter)
        age_min.place(x=130, y=415)

        ttk.Label(
            self,
            text="y",
            style="TextLabel.TLabel"
        ).place(x=175, y=415)

        age_max = tkr.Entry(
            self,
            textvariable=self.__max_age,
            width=5
        )

        age_max.bind("<KeyRelease>", self.all_filter)
        age_max.place(x=200, y=415)

        checkbox_style = ttk.Style()
        checkbox_style.configure(
            "CheckboxLabel.TCheckbutton",
            font=('Helvetica', 14),
            background="#99CCFF"
        )

        ttk.Checkbutton(
            self,
            variable=self.__only_street_leader,
            text="Solo lideres de calle",
            style="CheckboxLabel.TCheckbutton",
            command=self.all_filter,
            onvalue=True,
            offvalue=False
        ).place(x=450, y=300)

        ttk.Checkbutton(
            self,
            variable=self.__only_family_leader,
            text="Solo jefes de familia",
            style="CheckboxLabel.TCheckbutton",
            command=self.all_filter,
            onvalue=True,
            offvalue=False
        ).place(x=450, y=350)

        ttk.Checkbutton(
            self,
            variable=self.__only_committee_member,
            text="Solo miembros de comité",
            style="CheckboxLabel.TCheckbutton",
            command=self.all_filter,
            onvalue=True,
            offvalue=False
        ).place(x=450, y=400)

        radio_button = ttk.Style()
        radio_button.configure(
            "RadioLabel.TRadiobutton",
            font=('Helvetica', 14),
            background="#99CCFF"
        )

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Sin filtro de bombona",
            value=0,
            style="RadioLabel.TRadiobutton"
        ).place(x=750, y=300)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 10kg",
            value=1,
            style="RadioLabel.TRadiobutton"
        ).place(x=750, y=350)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 18kg",
            value=2,
            style="RadioLabel.TRadiobutton"
        ).place(x=750, y=400)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 27kg",
            value=3,
            style="RadioLabel.TRadiobutton"
        ).place(x=750, y=450)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 43kg",
            value=4,
            style="RadioLabel.TRadiobutton"
        ).place(x=750, y=500)

        tkr.Button(
            self,
            text="Ver detalles",
            command=self.open_details_window,
            font=("Times", 14),
            background="yellow",
            padx=5,
            pady=5,
            bd=0
        ).place(x=10, y=470)

        tkr.Button(
            self,
            text="Actualizar",
            command=self.open_update_window,
            font=("Times", 14),
            background="blue",
            foreground="White",
            padx=5,
            pady=5,
            bd=0
        ).place(x=135, y=470)

        tkr.Button(
            self,
            text="Eliminar",
            command=self.eliminate,
            font=("Times", 14),
            background="#CC0000",
            foreground="White",
            padx=5,
            pady=5,
            bd=0
        ).place(x=250, y=470)

    def set_records(self, records) -> None:
        """Sets all registers.

            Args:
                records (list): It is a list with all the records."""

        self.__all_records = records

    def update_table(self, people) -> None:
        """Updates the table according to the values in the people list.

            Args:
                people (list): People records."""

        old_records = self.__records.get_children()

        for old_record in old_records:
            self.__records.delete(old_record)

        for person in people:
            formated_date = datetime(
                person['Birthday']['year'],
                person['Birthday']['month'],
                person['Birthday']['day']
            )

            fullname = f"{person['Names']} {person['Lastnames']}"

            mew_record = (
                person["CI"],
                person["Street"],
                fullname,
                "Si" if person["IsLeaderStreet"] else "No",
                "Si" if person["IsFamilyLeader"] else "No",
                "Femenino" if person["Gender"] else "Masculino",
                formated_date.strftime("%d/%m/%Y"),
                person["SerialCard"],
                person["GasCounters"]["Kg10"],
                person["GasCounters"]["Kg18"],
                person["GasCounters"]["Kg27"],
                person["GasCounters"]["Kg43"]
            )

            self.__records.insert('', tkr.END, values=mew_record)

        self.__number_results.configure(text=f"Numero de resultados: {len(people)}")

    def all_filter(self, event=None) -> None:
        """Filter the records in the table.

            Args:
                event: An event that occurs."""

        filter_records = self.__all_records

        if len(self.__ci_filter.get_text_value()) > 0:

            filter_records = [
                person for person in filter_records
                if person["CI"].find(self.__ci_filter.get_text_value()) == 0
            ]

        if self.__street_filter.get_choise_int() > 0:

            filter_records = [
                person for person in filter_records
                if person["Street"] == self.__street_filter.get_choise_int()
            ]

        if self.__only_street_leader.get():
            filter_records = [
                person for person in filter_records
                if person["IsLeaderStreet"]
            ]

        if self.__only_family_leader.get():
            filter_records = [
                person for person in filter_records
                if person["IsFamilyLeader"]
            ]

        if self.__only_committee_member.get():
            filter_records = [
                person for person in filter_records
                if person["IsCommitteeMember"]
            ]

        if (not self.__min_age.get() == "") and (not self.__max_age.get() == ""):
            min_age = int(self.__min_age.get())
            max_age = int(self.__max_age.get())
            filter_records = [
                person for person in filter_records
                if calculate_age(datetime(
                    person['Birthday']['year'],
                    person['Birthday']['month'],
                    person['Birthday']['day']
                )) in range(min_age, max_age + 1)
            ]

        if self.__only_nkg.get() == 1:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["Kg10"] > 0
            ]

        elif self.__only_nkg.get() == 2:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["Kg18"] > 0
            ]

        elif self.__only_nkg.get() == 3:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["Kg27"] > 0
            ]

        elif self.__only_nkg.get() == 4:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["Kg43"] > 0
            ]

        self.update_table(filter_records)

    def open_details_window(self) -> None:
        """Opens a new window to view the details of the selected record."""

        self.__message.configure(text="")

        try:
            selected_record = self.__records.selection()
            selected_ci = int(self.__records.item(selected_record[0])['values'][0])
            info = search_index_person(self.__all_records, selected_ci)[1]
            DetailsPersonWindow(info)
        except IndexError:
            self.__message.configure(text="Seleccione un registro de la tabla, por favor")
            return

    def open_update_window(self) -> None:
        """Opens a new window to update the selected record."""

        self.__message.configure(text="")

        try:
            selected_record = self.__records.selection()
            selected_ci = int(self.__records.item(selected_record[0])['values'][0])
            index, info = search_index_person(self.__all_records, selected_ci)
            update_window = UpdatePeople(index, info, self.__all_records)

            tkr.Button(
                update_window,
                text="Guardar",
                command=lambda: update_window.update_data(self.all_filter),
                font=("Times", 14),
                background="#00FF00",
                foreground="White",
                padx=5,
                pady=5,
                bd=0
            ).place(x=895, y=190)

        except IndexError:
            self.__message.configure(text="Seleccione un registro de la tabla, por favor")
            return

    def eliminate(self) -> None:
        """Delete the selected record."""

        self.__message.configure(text="")

        try:
            selected_record = self.__records.selection()
            selected_ci = int(self.__records.item(selected_record[0])['values'][0])
            index = search_index_person(self.__all_records, selected_ci)[0]
            self.__all_records.pop(index)
        except IndexError:
            self.__message.configure(text="Seleccione un registro de la tabla, por favor")
            return

        self.update_table(self.__all_records)
        self.all_filter()

        update_file(self.__all_records)
