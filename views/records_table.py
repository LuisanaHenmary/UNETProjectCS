import tkinter as tkr
from tkinter import ttk
from components.table import Table
from components.select_field import SelectField
from views.utils import search_index_person, update_file


"""Documentation coming soon."""

class RecordsTable(tkr.Frame):

    def __init__(self, container) -> None:

        super().__init__(container)
        self.config(background="#99CCFF", height=370, width=1450)
        self.place(x=5, y=5)
        self.__only_street_leader = tkr.BooleanVar()
        self.__only_family_leader = tkr.BooleanVar()
        self.__only_nkg = tkr.IntVar()
        self.__ci_filter = tkr.StringVar()
        self.__only_nkg.set(0)
        self.__all_records = []
        self.__records = Table(self, (10, 10))
        filter_options = [x for x in range(25) if x not in [5, 22]]

        ttk.Label(
            self,
            text="Buscar por cedula:",
            style="TextLabel.TLabel"
        ).place(x=10, y=250)

        ci = tkr.Entry(
            self,
            textvariable=self.__ci_filter,
            width=28
        )

        ci.bind('<KeyRelease>', self.all_filter)

        ci.place(x=170, y=250)

        self.__street_filter = SelectField(
            self,
            "Por\nManzana:",
            filter_options,
            7,
            (400, 250)
        )

        self.__street_filter.changed_event(self.all_filter)

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
        ).place(x=10, y=310)

        ttk.Checkbutton(
            self,
            variable=self.__only_family_leader,
            text="Solo lideres de familia",
            style="CheckboxLabel.TCheckbutton",
            command=self.all_filter,
            onvalue=True,
            offvalue=False
        ).place(x=250, y=310)

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
        ).place(x=800, y=250)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 10kg",
            value=1,
            style="RadioLabel.TRadiobutton"
        ).place(x=800, y=300)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 18kg",
            value=2,
            style="RadioLabel.TRadiobutton"
        ).place(x=800, y=350)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 27kg",
            value=3,
            style="RadioLabel.TRadiobutton"
        ).place(x=800, y=400)

        ttk.Radiobutton(
            self,
            variable=self.__only_nkg,
            command=self.all_filter,
            text="Solo quienes tienen bombonas de 43kg",
            value=4,
            style="RadioLabel.TRadiobutton"
        ).place(x=800, y=450)

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
        ).place(x=110, y=400)

    def set_records(self, records):
        self.__all_records = records

    def update_table(self, people):

        old_records = self.__records.get_children()

        for old_record in old_records:
            self.__records.delete(old_record)

        for person in people:
            mew_record = (
                person["CI"],
                person["Street"],
                person["FullName"],
                "Si" if person["IsLeaderStreet"] else "No",
                "Si" if person["IsFamilyLeader"] else "No",
                "Femenino" if person["Gender"] else "Masculino",
                f"{person['Birthday']['day']}/{person['Birthday']['month']}/{person['Birthday']['year']}",
                person["SerialCard"],
                person["GasCounters"]["10 Kg"],
                person["GasCounters"]["18 Kg"],
                person["GasCounters"]["27 Kg"],
                person["GasCounters"]["43 Kg"]
            )

            self.__records.insert('', tkr.END, values=mew_record)

    def all_filter(self, event=None):

        filter_records = self.__all_records

        if len(self.__ci_filter.get()) > 0:

            filter_records = [
                person for person in filter_records
                if person["CI"].find(self.__ci_filter.get()) == 0
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

        if self.__only_nkg.get() == 1:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["10 Kg"] > 0
            ]

        elif self.__only_nkg.get() == 2:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["18 Kg"] > 0
            ]

        elif self.__only_nkg.get() == 3:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["27 Kg"] > 0
            ]

        elif self.__only_nkg.get() == 4:
            filter_records = [
                person for person in filter_records
                if person["GasCounters"]["43 Kg"] > 0
            ]

        self.update_table(filter_records)

    def eliminate(self):

        try:
            selected_record = self.__records.selection()
            selected_ci = int(self.__records.item(selected_record[0])['values'][0])
            index = search_index_person(self.__all_records, selected_ci)[0]
            self.__all_records.pop(index)
        except IndexError:
            print("Please Select a Record")
            return

        self.update_table(self.__all_records)
        self.all_filter()

        update_file(self.__all_records)
