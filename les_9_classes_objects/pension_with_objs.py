# Vraag de gebruiker om voornaam, familienaam, geboortedatum, geboorteplaats. Druk dan het volgende af.
# Uw naam is X en u bent X aantal jaar oud.
# U bent geboren op X te X
# U bent 18 jaar geworden op X
# U mag op pensioen in het jaar X in de maand X

from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from inputs import GetInput

C_TEXT_WARN = 'Probeer alstublieft nog één keer'


class Person:
    __first_name = ''
    __last_name = ''
    # __birthdate: date = None
    __birthplace = ''

    def __init__(self, first_name: str, last_name: str, birthplace: str, birthdate: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthplace = birthplace
        self.birthdate = birthdate

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def birthplace(self):
        return self.__birthplace

    @birthplace.setter
    def birthplace(self, value):
        self.__birthplace = value

    @property
    def birthdate(self) -> any:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, value: str) -> any:
        """
        As an input is a isodate string with a date in a format 9999-12-31.
        If str was in a format 9999-12-31 and if deadline is earlier than today
        then returns deadline as date.
        If str was not on correct format or earlier than today then None.
        :param value: isodate str, YYYY-MM-DD
        returns: deadline as date or None
        """
        today = date.today()

        try:
            birthday_ = date.fromisoformat(value)
            if birthday_ > today:
                raise ValueError('Birthday can not be set later than today')
            self.__birthdate = birthday_

        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.__birthdate = None

    def age(self):
        if self.__birthdate:
            age_ = relativedelta(date.today(), self.__birthdate).years
            return age_
        else:
            return None

    def pension(self):
        if self.__birthdate:
            date_of_pension = self.__birthdate + relativedelta(months=805)
            return date_of_pension
        else:
            return None

    def age_18(self):
        if self.__birthdate:
            age_of_18 = self.__birthdate + relativedelta(years=18)
            return age_of_18
        else:
            return None

    def __str__(self):
        return f'{self.__first_name} {self.__last_name}, place: {self.__birthplace}, birthday: {self.__birthdate}, ' \
               f'age: {self.age()}, the date of your pension: {self.pension()}, you are 18 on {self.age_18()}'


def create_person() -> Person:
    first_name = GetInput.get_text('your first name: ')
    last_name = GetInput.get_text('your last name: ')
    birth_place = GetInput.get_text('your birth place: ')
    birth_date = GetInput.get_isostr('your birthday in YYYY-MM-DD ')
    p = Person(first_name, last_name, birth_place, birth_date)
    return p


pers = create_person()
print(pers)
