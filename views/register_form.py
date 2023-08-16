import tkinter as tkr
from PIL import ImageTk, Image
import os
from components.text_field import TextField
from components.select_field import SelectField
from components.date_field import DateField
from components.binary_field import BinaryField
from components.address_field import AddressField
from components.gas_cylinders_form import GasCylindersForm
from components.observations_field import ObservationsField


"""This module is for the registration form view."""


class RegisterForm(tkr.Frame):
    """This class creates a form to register a person.

        Attributes:
            __street (SelectField): It is a field to select the number of the block.
            __person_ci (TextField): It is a field to enter the identity card.
            __first_names (TextField): It is a field to enter the first name.
            __last_names (TextField): It is a field to enter the last name.
            __phone_number (TextField): It is a field to enter the phone number.
            __email (TextField): It is a field to enter the email.
            __serial_card_country (TextField): It is a field to enter the country card number.
            __birthdate (DateField): It is a field to enter the date of birth.
            __gender (BinaryField): It is a field to select the genre.
            __gas_cylinders (GasCylindersForm): It is a field to establish the quantity of gas cylinders.
            __address (AddressField): It is a field to enter the address.
            __is_street_leader (BinaryField): It is a field to establish if it is a block leader or not
            __is_family_leader (BinaryField): It is a field to establish if he is a head of family or not
            __observations (ObservationsField): It is a field to enter some observations."""

    def __init__(self, container) -> None:
        """Initializes the RegisterForm view.

            Args:
                container (Widget): It is where the view will be contained"""

        super().__init__(container)
        self.config(background="#99CCFF", height=570, width=1390)
        self.place(x=5, y=5)

        self.__records = []

        try:
            imagen = Image.open(os.path.join(os.getcwd(), "images", "SimbSur.jpeg"))
            imagen = imagen.resize((150, 150))
            test = ImageTk.PhotoImage(imagen)
            img = tkr.Label(self, image=test)
            img.image = test
            img.place(x=10, y=10)
        except Exception as e:
            print(e)
            tkr.Label(self, text="Imagen no encontrada").place(x=10, y=10)

        self.__street = SelectField(
            self,
            "Nro.\nManzana:",
            [x for x in range(1, 25) if x not in [5, 22]],
            3,
            (200, 10)
        )

        self.__person_ci = TextField(self, "Cedula:", (10, 200))
        self.__first_names = TextField(self, "Nombres:", (10, 240))
        self.__last_names = TextField(self, "Apellidos:", (10, 280))
        self.__phone_number = TextField(self, "Nro. Telf:", (460, 200))
        self.__email = TextField(self, "Correo:", (460, 240))
        self.__serial_card_country = TextField(self, "Carnet de la\npatria serial:", (460, 280))

        self.__birthdate = DateField(self, min_year=1900, coordinates=(340, 10))

        self.__gender = BinaryField(self,
                                    "Genero:",
                                    binary_options=("Femenino", "Masculino"),
                                    coordinates=(200, 100)
                                    )

        self.__gas_cylinders = GasCylindersForm(self, (570, 10))

        self.__is_street_leader = BinaryField(self,
                                              "¿Es lider de calle?",
                                              coordinates=(900, 10)
                                              )

        self.__is_family_leader = BinaryField(self,
                                              "¿Es Jefe de familia?",
                                              coordinates=(900, 120)
                                              )

        self.__observations = ObservationsField(self, coordinates=(10, 350))
        self.__address = AddressField(self, (570, 350))

    def reset_all(self) -> None:
        """reset all fields"""

        self.__street.reboot_select()
        self.__person_ci.reboot_field()
        self.__first_names.reboot_field()
        self.__last_names.reboot_field()
        self.__phone_number.reboot_field()
        self.__email.reboot_field()
        self.__serial_card_country.reboot_field()
        self.__birthdate.reboot_fields()
        self.__gender.reboot_current_value()
        self.__gas_cylinders.reboot_all_fields()
        self.__address.reboot_text_field()
        self.__is_street_leader.reboot_current_value()
        self.__is_family_leader.reboot_current_value()
        self.__observations.reboot_text_field()

    def save_all(self) -> dict:
        """Returns a dictionary with the data of the registered person."""

        street_number = self.__street.get_choise_int()
        ci_person = self.__person_ci.get_text_value()
        names = self.__first_names.get_text_value()
        lastname = self.__last_names.get_text_value()
        phone_number = self.__phone_number.get_text_value()
        email_address = self.__email.get_text_value()
        serial_card = self.__serial_card_country.get_text_value()
        birthday = self.__birthdate.get_date()
        gender = self.__gender.get_binary_value()
        gas_counters = self.__gas_cylinders.get_counters()
        address_person = self.__address.get_address()
        is_leader = self.__is_street_leader.get_binary_value()
        is_family_leader = self.__is_family_leader.get_binary_value()
        observations_person = self.__observations.get_observations()

        return {
            "Street": street_number,
            "CI": ci_person,
            "Names": names,
            "Lastnames": lastname,
            "PhoneNumber": phone_number,
            "Email": email_address,
            "SerialCard": serial_card,
            "Birthday": birthday,
            "Gender": gender,
            "GasCounters": gas_counters,
            "Address": address_person,
            "IsLeaderStreet": is_leader,
            "IsFamilyLeader": is_family_leader,
            "Observations": observations_person
        }
