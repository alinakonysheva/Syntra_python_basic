# Vraag de gebruiker om voornaam, familienaam, geboortedatum, geboorteplaats. Druk dan het volgende af.
# Uw naam is X en u bent X aantal jaar oud.
# U bent geboren op X te X
# U bent 18 jaar geworden op X
# U mag op pensioen in het jaar X in de maand X

from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

C_TEXT_WARN = 'Probeer alstublieft nog één keer'


class Person:
    __first_name = ''
    __last_name = ''
    __birth_day = 0
    __birth_month = 0
    __birth_year = 0
    __birthplace = ''

    def __init__(self, first_name, last_name, birthplace, birth_day, birth_month, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birthplace = birthplace
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year

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
    def birth_day(self):
        return self.__birth_day

    @birth_day.setter
    def birth_day(self, value):
        self.__birth_day = value

    @property
    def birth_year(self):
        return self.__birth_year

    @birth_year.setter
    def birth_year(self, value):
        self.__birth_year = value

    @property
    def birth_month(self):
        return self.__birth_month

    @birth_day.setter
    def birth_month(self, value):
        self.__birth_month = value


def get_input(text: str, conversion_type: int = 0) -> 0:
    '''
    get input and convert тут стояло еще что-то, посмотреть после урока что именно
    :param text([str]): text to use in the display
    :param conversion_type:
    :return: any: int or string, depends on conversion_type
    '''

    result = None

    try:
        pass
    except:
        pass


def create_person() -> Person:
    first_name = input('your name')
    last_name = input('your name')
    birth_place = input('your name')
    birth_year = input('your name')
    birth_month = input('your name')
    birth_day = input('your name')
    return


'''for i in range(1, params_length):
    try:
        if i == 1:
            year_of_user_birth = int(argv[i])
        if i == 2:
            month_of_user_birth = int(argv[i])
        if i == 3:
            day_of_user_birth = int(argv[i])

    except ValueError:
        if i == 1:
            year_of_user_birth = int(input(f'het jaar moet realistisch zijn, gewoon 4 cijfers, {C_TEXT_WARN} {argv[i]}'))
        elif i == 2:
            month_of_user_birth = int(input(f'de maand was niet geldig, {C_TEXT_WARN} {argv[i]}'))
        elif i == 3:
            day_of_user_birth = int(input(f'de dag was niet geldig, {C_TEXT_WARN} {argv[i]}'))

try:
    birth_day = date(year_of_user_birth, month_of_user_birth, day_of_user_birth)
except ValueError:
    year_of_user_birth = int(input(f'het jaar moet realistisch zijn, gewoon 4 cijfers. {C_TEXT_WARN} '))
    month_of_user_birth = int(input(f'de maand was niet geldig. {C_TEXT_WARN} '))
    day_of_user_birth = int(input(f'de dag was niet geldig. {C_TEXT_WARN} '))
    birth_day = date(year_of_user_birth, month_of_user_birth, day_of_user_birth)

# 18 years
year_of_18 = birth_day.year + 18
date_18 = date(year_of_18, month_of_user_birth, day_of_user_birth)
# pension
date_of_pension = birth_day + relativedelta(months=805)

if date_of_pension.day != birth_day.day:
    date_of_pension += timedelta(days=1)
# user age
today = datetime.now()

user_age = relativedelta(today, birth_day).years


weekdays_in_dutch = {0: 'mandaag', 1: 'dinsdag', 2: 'woensdag', 3: 'donderdag',
                     4: 'vrijdag', 5: 'zaterdag', 6: 'zondag'}
months_in_dutch = {'January': 'januari', 'February': 'februari', 'March': 'maart', 'April': 'april', 'May': 'mei',
                   'June': 'juni', 'July': 'juli', 'August': 'augustus', 'September': 'september',
                   'October': 'oktober', 'November': 'november', 'December': 'december'}

print(f'uw geboortedatum is {birth_day.strftime("%d")} {months_in_dutch[birth_day.strftime("%B")]} \
{birth_day.strftime("%Y")} en dat is een {weekdays_in_dutch[birth_day.weekday()]}')

print(f'u bent nu {user_age} jaar oud.')

print(f'u bent 18 jaar op {date_18.strftime("%d")} {months_in_dutch[date_18.strftime("%B")]} \
{date_18.strftime("%Y")}, en dat is een {weekdays_in_dutch[date_18.weekday()]}')

print(f'u mag op pensioen gaan op {date_of_pension.strftime("%d")} {months_in_dutch[date_of_pension.strftime("%B")]} \
{date_of_pension.strftime("%Y")}')
'''
