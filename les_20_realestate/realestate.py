# We gaan vastgoed verkopen. Maak een object aan “vastgoed”, dit kan een type huis/appartement/grond/handelspand zijn.
# Elk vastgoed heeft een adres, prijs, een omschrijving en een epc waarde. (een grond uiteraard epc 0).
# In ons portfolio kunnen meerdere items zitten. Laat deze ingeven, voeg ook meteen een optie toe
# om alles te bekijken.
# Voeg nu een status toe “te koop/in optie/verkocht”,
# voorzie dit ook in je menu om telkens de lijst apart te verkrijgen.
# Voorzie dus ook een manier om van te koop naar in optie of verkocht te zetten
# Voeg ook de volgende opties toe, duurste verkocht, goedkoopste verkocht, goedkoopste te koop,
# duurste te koop, te koop tussen x en y (waarbij je x en y kan ingeven)

from base import BaseList, BaseObject
from inputs import GetInput

types_real_estate = {1: 'huis', 2: 'appartement', 3: 'grond', 4: 'handelspand'}


class RealEstate(BaseObject):
    __address = ''
    __price = 0.00
    __description = ''
    __epc = 0
    __type_estate = 'huis'

    def __init__(self, address, price, description, epc, type_estate=1):
        self.__type_estate = types_real_estate[type_estate]
        self.__address = address
        self.__price = price
        self.__description = description
        self.__epc = epc

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def epc(self) -> int:
        return self.__epc

    @epc.setter
    def epc(self, value):
        self.__epc = value


class RealEstateList(BaseList):
    def show_list(self):
        return self.items

"""
def get_input(real_estate: RealEstate) -> RealEstate:

     = get_input_item('geef het reeds bestaande jaar in om te wijzigen of geef een nieuw jaar op : ', 1)
    year = yearlist.get_item_by_year(chosen_year)
    if year:
        year = yearlist.add(Year(chosen_year))

    for x in range(1, 13):
        month = date(2000, x, 1)
        year.temperatures[x - 1].degrees = get_input_item('geef de temp in voor {} :'.format(month.strftime("%B")), 2)


def create_list() -> YearList:
    yearlist = YearList()
    yearlist.load()
    return yearlist


def print_years(yearlist: YearList):
    print_spacer()
    print('beschikbare jaren')
    print_spacer()
    if len(yearlist.items) == 0:
        print('geen gegevens gevonden')
    else:
        for y in yearlist.items:
            print(y.year)


def print_year(yearlist: YearList):
    print_years(yearlist)
    if len(yearlist.items) > 0:
        inp = get_input_item('kies uw jaartal: ', 1)
        year = yearlist.get_item_by_year(inp)
        if year is None:
            print('geen geldig jaar gekozen')
        else:
            for x in range(0, 12):
                month = date(year.year, x + 1, 1)
                print('{}: {}'.format(month.strftime("%B"), year.temperatures[x].degrees))

            val, pos = year.get_hottest()
            month = date(year.year, pos + 1, 1)
            print('warmste is: {} - {}'.format(month.strftime("%B"), val))

            val, pos = year.get_coldest()
            month = date(year.year, pos + 1, 1)
            print('koudste is: {} - {}'.format(month.strftime("%B"), val))

            print('gemiddelde is: {}'.format(year.get_average()))
"""
"""
def change_unit(yearlist: YearList):
    print_spacer()
    if yearlist.mode == C_MODE_FAHRENTHEIT:
        unit = UNIT_F
    else:
        unit = UNIT_C

    print('De huidige gebruikte eenheid is: {}'.format(unit))
    print('1: {}'.format(UNIT_C))
    print('2: {}'.format(UNIT_F))
    inp = get_input_item('maak uw keuze: ', 1)
    yearlist.mode = inp


def read_file(yearlist: YearList):
    print_spacer()
    yearlist.filename = get_input_item('geef de filenaam: ')
    yearlist.load()
    print('file ingelezen')
"""