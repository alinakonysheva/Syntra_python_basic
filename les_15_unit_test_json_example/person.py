from datetime import date, datetime
from inputs import get_input_item
from address import Address, create_adress

sexe_types = ['unkown', 'm', 'f']


class Person():
    __name_first = ''
    __name_last = ''
    __birthdate = None
    __sexe_type = 0
    __address = None

    def __init__(self, firstname: str, lastname: str, year: int, month: int, day: int, sexe_type: int = 0):
        """constructor

        Args:
            firstname (str): firstname of the person
            lastname (str): lastname of the person
            year (int): year of birth
            month (int): month of birth
            day (int): day of birth
        """
        self.firstname = firstname
        self.lastname = lastname
        self.set_birthday(year, month, day)
        self.__address = create_adress()
        self.__sexe_type = sexe_type

    def __str__(self):
        return '{} - {}/{}/{} - {}'.format(self.name, self.birthdate.day,
                                           self.birthdate.month, self.birthdate.year, self.age)

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
    def age(self):
        if self.birthdate is None:
            return 0
        else:
            return datetime.now().year - self.birthdate.year

    @property
    def address(self):
        if self.__address is None:
            self.__address = create_adress()
        return self.__address

    '''
    @address.setter
    def address(self, value : Address):
        if value is not None and type(value) == Address:
        # isinstance(value, Address)
            self.__address = value
        else:
            raise TypeError('setter value is not of type Address')
        """
        try:
            self.__address = Address(value)
        except:
            raise TypeError('setter value is not of type Address')
        """
    '''

    @property
    def sexe(self):
        return sexe_types[self.__sexe_type]


def create_person(firstname: str, lastname: str, year: int, month: int, day: int, sexe_type: int = 0) -> Person:
    """firstname
        create a, lastname: str person based on his
         attributes
    Args:
        firstname (str): firstname of the person
        lastname (str): lastname of the person
        year (int): birth year of the person
        month (int): birth month
        day (int): birth day

    Returns:
        Person: a fully working person object
    """
    return Person(firstname, lastname, year, month, day, sexe_type)


def get_person() -> Person:
    firstname = get_input_item('Geef uw voornaam: ')
    lastname = get_input_item('Geef uw familienaam: ')
    day = get_input_item('Geef uw geboortedag: ', 1)
    month = get_input_item('Geef uw geboortemaand: ', 1)
    year = get_input_item('Geef uw geboortejaar: ', 1)

    return create_person(firstname, lastname, year, month, day)
