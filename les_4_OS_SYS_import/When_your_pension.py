#  Maak een programma dat de geboortedatum van de gebruiker vraagt.
#  Druk het volgende af - zijn geboortedatum inclusief de naam van de dag in het Nederlands
# voorbeeld: uw geboortedatum is “2/9/1979”, dit was op een zondag +
# - wanneer hij 18 jaar is geworden en de naam van de dag in het Nederlands +
#  voorbeeld: u was 18 jaar op datum, dit was op een xxxxx (dag van de week in het Nederlands)
#  - zijn huidige leeftijd
# voorbeeld: u bent nu x aantal jaar oud)
# - wanneer hij op pensioen mag gaan (67 jaar, maand nadien)
# voorbeeld: u mag in “maand” in het “jaar” op pensioen gaan (maand in het Nederlands zetten)
# Als input gaan we 3 parameters gebruiken: dag maand jaar
#  Als 1 van de parameters ontbreekt gaan we deze alsnog vragen aan de gebruiker

from sys import argv
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta

params_length = len(argv)

# year_of_user_birth = int(input(f'{C_TEXT_BIRTH_ST} year, {C_TEXT_FORMAT}   '))
# month_of_user_birth = int(input(f'{C_TEXT_BIRTH_ST} month, {C_TEXT_FORMAT}   '))
# day_of_user_birth = int(input(f'{C_TEXT_BIRTH_ST} day, {C_TEXT_FORMAT}   '))

C_TEXT_WARN = 'Probeer alstublieft nog één keer'

for i in range(1, params_length):
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
'''if (today.month, today.day) < (birth_day.month, birth_day.day):
    user_age = today.year - birth_day.year - 1
else:
    user_age = today.year - birth_day.year'''

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
