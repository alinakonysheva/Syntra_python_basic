from datetime import date, datetime

C_DATEFORMAT = '%d/%m/%y'
'''
- persoon
  eigenschappen
     voornaam 
     familienaam
     geboortedatum
     geboorteplaats
     
  huidige aantal jaren berekenen
  berekenen wanneer op pensioen in welke maand (67 jaar maand + 1)
  bereken leeftijd 18 jaar
  output
'''

class Person():
    __name_first = ' '
    __name_last = ''
    __birth_place = ''
    __birthday = None
    
    def __init__(self, firstname, lastname, birth_day, birth_year, birth_month, birthplace):
        self.firstname = firstname
        self.lastname = lastname
        self.birth_place = birthplace
        self.set_birthdate(birth_day, birth_month, birth_year)
    
    @property
    def firstname(self):
        return self.__name_first
    
    @firstname.setter
    def firstname(self, value):
        self.__name_first = value
    
    
    @property
    def lastname(self):
        return self.__name_last
    
    @lastname.setter
    def lastname(self, value):
        self.__name_last = value.upper()
    
    
    @property
    def fullname(self):
        return self.lastname + ' ' + self.firstname
    
    @property
    def birth_place(self):
        return self.__birth_place
    
    @birth_place.setter
    def birth_place(self, value):
        self.__birth_place = value
    
    
    @property
    def age_current(self):
        return datetime.now().year - self.__birthday.year    

    @property
    def retirement(self):
        retirement_year = self.birthday.year + 67
        retirement_month = self.birthday.month + 1
        if retirement_month > 12:
            retirement_month = 1
            retirement_year += 1

        return date(retirement_year, retirement_month, 1)
    
    @property
    def years_18(self):
        year_18 = self.birthday.year + 18
        return date(year_18, self.birthday.month, self.birthday.day)      
             
        
    @property
    def birthday(self):
        return date(self.__birthday.year, self.__birthday.month, self.__birthday.day) 

    @property
    def birthday_asstr(self):
        return '{}'.format(self.birthday.strftime(C_DATEFORMAT))



    def set_birthdate(self, birth_day, birth_month, birth_year):
        self.__birthday = datetime(birth_year, birth_month, birth_day)


def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Returns:
        any: int or str, depending on conversion type
        :param
        text ([str]): text to use in the display string for input
        conversion_type (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer
    """

    try:
        inp = input(f'Geef uw {text}: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = inp 
    except Exception as e:
        print(e)
        result = 0
    
    return result


def do_output(person : Person):
    if person is not None:
        print('Uw naam is {} en u bent {} aantal jaar oud'.format(person.fullname, person.age_current))
        print('U bent geboren op {} te {}'.format(person.birthday_asstr, person.birth_place))
        print('U bent 18 jaar geworden op {}'.format(person.years_18))
        print('U mag op het pensioen in het jaar {} in de maand {}'.format(person.retirement.year, person.retirement.month))

    else:
        print('Person was not created')

def create_pers() -> Person:
    """create  a person object

    Returns:
        Person: return a person object
    """
    firstname = get_input('voornaam')
    lastname = get_input('familienaam')
    birthplace = get_input('geboorteplaats')
    birthday = get_input('geboorte dag', 1)
    birthmonth = get_input('geboorte maand', 1)
    birthyear = get_input('geboorte jaar', 1)
      
    return Person(firstname, lastname, birthday, birthyear, birthmonth, birthplace)

def dorun():
    pers = create_pers()
    pers.firstname = 'mijnnaam'
    do_output(pers)

dorun()



















