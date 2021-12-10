# Maak een object auto, een auto heeft een merk, kleur, model, nummerplaat
# Maak een programma dat dit als input komt vragen
# Exporteer dit naar een json formaat, keys in de json “brand”, “color”,
# “license_plate”, “fuel” Maak ook een unit test
import json

class Car:
    __brand = ''
    __color = ''
    __fuel = ''
    __license_plate = ''

    def __init__(self, brand: str, color: str, license_plate: str, fuel: str):
        """constructor
        """
        self.__brand = brand
        self.__color = color
        self.__license_plate = license_plate
        self.__fuel = fuel

    def __str__(self):
        return f'{self.__brand} - {self.__color} - {self.__license_plate} - {self.__fuel}'

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value: str):
        self.__color = value

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, value: str):
        self.__license_plate = value

    @property
    def fuel(self):
        return self.__fuel

    @property
    def to_dict(self) -> dict:
        return dict(
            firstname=self.firstname,
            lastname=self.lastname,
            birth_day=self.birthdate.day,
            birth_month=self.birthdate.month,
            birth_year=self.birthdate.year,
            email=self.email,
            id=self.id
        )

    @property
    def to_json(self):
        return json.dumps(self.to_dict)

    def from_dict(self, value):
        self.firstname = value["firstname"]
        self.lastname = value["lastname"]
        birth_day = value["birth_day"]
        birth_month = value["birth_month"]
        birth_year = value["birth_year"]
        self.set_birthday(birth_year, birth_month, birth_day)
        self.email = value["email"]
        self.id = value["id"]

    def from_json(self, value):
        d = json.loads(value)
        self.from_dict(d)


def create_person(firstname: str, lastname: str, year: int, month: int, day: int, email: str) -> Person:
    """firstname
        create a, lastname: str person based on his
         attributes
    Args:
        firstname (str): firstname of the person
        lastname (str): lastname of the person
        year (int): birth year of the person
        month (int): birth month
        day (int): birth day
        email: email of a the person

    Returns:
        Person: a fully working person object
    """
    return Person(firstname, lastname, year, month, day, email)


def get_person() -> Person:
    firstname = get_input_item('Geef uw voornaam: ')
    lastname = get_input_item('Geef uw familienaam: ')
    day = get_input_item('Geef uw geboortedag: ', 1)
    month = get_input_item('Geef uw geboortemaand: ', 1)
    year = get_input_item('Geef uw geboortejaar: ', 1)
    email = get_input_item('Geef uw email: ')

    return create_person(firstname, lastname, year, month, day, email)