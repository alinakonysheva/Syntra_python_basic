# Maak een object persoon aan of hergebruik een oud object dat je reeds aangemaakt hebt. Deze persoon heeft een naam en
# een geboortedatum. Vraag deze als input. Geef dan ook weer de huidige leeftijd van deze persoon.
# Maak hierop unit tests
from datetime import date

class Person:
    __name = ''
    __birthdate = None

    def __init__(self, name, birthdate):
        self.__name = name
        self.__birthdate = birthdate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: str):
        self.__birthdate = value

    def __str__(self) -> str:
        return self.name, str(self.birthdate)


