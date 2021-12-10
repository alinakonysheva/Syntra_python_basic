# Maak een programma dat een notitieblok is. Je kan dit zien als een online programma waarbij er meerdere gebruikers zijn.
# Je vraagt de gegevens van de persoon, naam, email en geboortedatum.
# Elke gebruiker heeft ook een interne id.
# Maak hiervoor ook een testen en voorzie een export en import naar json. Als keys in de json file willen we id,
# firstname, lastname, email, birthday, birthmonth, birthyear zien

import json
from datetime import date, datetime
from inputs import get_input_item
import re
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'


class Person:
    __name_first = ''
    __name_last = ''
    __birthdate = None
    __email = ''
    __id = 0

    def __init__(self, firstname: str, lastname: str, year: int, month: int, day: int, email: str):
        """constructor

        Args:
            firstname (str): firstname of the person
            lastname (str): lastname of the person
            year (int): year of birth
            month (int): month of birth
            day (int): day of birth
            email(str): email of a person
            id - inner unique identifier of a person
        """
        self.firstname = firstname
        self.lastname = lastname
        self.set_birthday(year, month, day)
        self.__email = email
        Person.__id += 1

    def __str__(self):
        return f'{self.name} - {self.birthdate.day}/{self.birthdate.month}/{self.birthdate.year} - {self.email} - {self.id}'

    @property
    def name(self) -> str:
        return self.firstname + ' ' + self.lastname

    @property
    def firstname(self):
        return self.__name_first

    @firstname.setter
    def firstname(self, value: str):
        self.__name_first = value

    @property
    def lastname(self):
        return self.__name_last

    @lastname.setter
    def lastname(self, value: str):
        self.__name_last = value

    @property
    def birthdate(self) -> date:
        """property birthdate
        Returns:
            date: returns birthdate as date
        """
        return date(self.__birthdate.year, self.__birthdate.month, self.__birthdate.day)

    def set_birthday(self, year: int, month: int, day: int):
        """set the birthday through its own parts
        Args:
            year ([int]): year of birth
            month ([int]): month of birth
            day ([int]): day of birth

        Raises:
            ValueError: year must be between 1850 and now
            ValueError: month must be -> 1 and 12
            ValueError: day must be from 1 to 31 (not taking account special months)
        """
        now = datetime.now()
        if year < 1850 or year > now.year:
            raise ValueError('birthyear is not in the correct range (1850 -> now')

        if month < 1 or month > 12:
            raise ValueError('birthmonth is not in the correct range (1 -> 12')

        if (day < 0 or day > 31):
            raise ValueError('birthday is not in the correct range (1 -> 31')

        self.__birthdate = date(year, month, day)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        # проверку регуляркой что это email
        self.__email = value

    @property
    def id(self):
        return self.__id

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
