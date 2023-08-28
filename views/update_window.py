import tkinter as tkr
from components.gas_cylinders_form import GasCylindersForm
from components.binary_field import BinaryField
from components.select_field import SelectField
from components.text_field import TextField
from components.observations_field import ObservationsField
from components.address_field import AddressField
from views.utils import update_file

"""It is to update the information of a person."""


class UpdatePeople(tkr.Toplevel):
    """Creates a secondary window to update information.

        Attributes:
            __current_people (list): People list.
            __index (int): Position in the list.
            __data (dict): A dictionary with the person's information.
            __street (SelectField): It is a field to select the number of the block.
            __last_names (TextField): It is a field to enter the last name.
            __phone_number (TextField): It is a field to enter the phone number.
            __email (TextField): It is a field to enter the email.
            __gas_cylinders (GasCylindersForm): It is a field to establish the quantity of gas cylinders.
            __is_street_leader (BinaryField): It is a field to establish if it is a block leader or not.
            __is_family_leader (BinaryField): It is a field to establish if he is a head of family or not.
            __is_community_spokesperson (BinaryField): It is a field to establish if it is a community spokesperson.
            __observations (ObservationsField): It is a field to enter some observations.
            __address (AddressField): It is a field to enter the address."""

    def __init__(self, index, info, people):
        """Initialize the window

            Args:
                index (int): Position in the list.
                info (dict): A dictionary with the person's information.
                people (list): People list."""

        super().__init__(width=1210, height=415, background="#99CCFF")
        self.resizable(False, False)
        self.title(f"Actualizando datos de {info['CI']}")
        self.__current_people = people
        self.__index = index
        self.__data = info

        streets = [x for x in range(1, 25) if x not in [5, 22]]

        self.__street = SelectField(
            self,
            "Nro.\nManzana:",
            streets,
            3,
            (10, 10)
        )
        self.__street.set_selected(streets.index(info['Street']))

        self.__last_names = TextField(self, "Apellidos:", (10, 70))
        self.__last_names.set_text_value(info["Lastnames"])

        self.__phone_number = TextField(self, "Nro. Telf:", (10, 120))
        self.__phone_number.set_text_value(info["PhoneNumber"])

        self.__email = TextField(self, "Correo:", (10, 170))
        self.__email.set_text_value(info["Email"])

        self.__gas_cylinders = GasCylindersForm(self, (450, 10))
        self.__gas_cylinders.set_fields(info['GasCounters'])

        self.__is_street_leader = BinaryField(
            self,
            "¿Es lider de calle?",
            coordinates=(770, 10)
        )
        self.__is_street_leader.set_binary_value(info['IsLeaderStreet'])

        self.__is_family_leader = BinaryField(
            self,
            "¿Es Jefe de familia?",
            coordinates=(980, 10)
        )

        self.__is_family_leader.set_binary_value(info['IsFamilyLeader'])

        self.__is_community_spokesperson = BinaryField(
            self,
            "¿Es vocero comunal?",
            coordinates=(770, 120)
        )

        self.__is_community_spokesperson.set_binary_value(info['IsCommunitySpokesperson'])

        self.__observations = ObservationsField(self, coordinates=(10, 220))
        self.__observations.set_text(info['Observations'])

        self.__address = AddressField(self, (570, 220))
        self.__address.set_address(info["Address"])

    def update_data(self, update_table):
        """Update the data and the table.

            Args:
                update_table (function): It is a function to update the table."""

        self.__data['Street'] = self.__street.get_choise_int()
        self.__data["PhoneNumber"] = self.__phone_number.get_text_value()
        self.__data["Email"] = self.__email.get_text_value()
        self.__data['GasCounters'] = self.__gas_cylinders.get_counters()
        self.__data['IsLeaderStreet'] = self.__is_street_leader.get_binary_value()
        self.__data['IsFamilyLeader'] = self.__is_family_leader.get_binary_value()
        self.__data['IsCommunitySpokesperson'] = self.__is_community_spokesperson.get_binary_value()
        self.__data['Observations'] = self.__observations.get_observations()
        self.__data['Address'] = self.__address.get_address()

        self.__current_people.pop(self.__index)
        self.__current_people.insert(self.__index, self.__data)
        update_table(self.__current_people)
        update_file(self.__current_people)
        self.destroy()
