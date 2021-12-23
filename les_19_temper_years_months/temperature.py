from datetime import date
from json import dumps, loads
from typing import Any
from files import create_json_file, read_json_file
from inputs import get_input_item
from base import BaseList, BaseObject
from utils import print_spacer

C_MODE_CELSIUS = 1
C_MODE_FAHRENTHEIT = 2

UNIT_C = 'Celsius'
UNIT_F = 'Fahrenheit'    

degrees_modes = (C_MODE_CELSIUS, C_MODE_FAHRENTHEIT)


class Temperature():
    """Class that holds temperatures, internally this works with degrees in Celsius
    """
    def __init__(self):
        self.__mode = C_MODE_CELSIUS  
        self.__degrees = -999

    
    @property
    def mode(self) -> int:
        return self.__mode

    @mode.setter
    def mode(self, value: int):
        if value in degrees_modes:
            self.__mode = value
        else:
            raise ValueError('provide a correct mode')
    
    @property
    def degrees(self) -> float:
        if self.mode == C_MODE_FAHRENTHEIT:
            return round((self.__degrees * 1.8) + 32, 1)
        else:
            return self.__degrees


    @degrees.setter
    def degrees(self, value: float):
        if self.mode == C_MODE_FAHRENTHEIT:
            try:
                self.__degrees = round((value - 32)/1.8, 1)
            except:
                raise ValueError('provide a correct value')
        else:
            self.__degrees = value

    

class Year(BaseObject):    

    def __init__(self, year: int):
        self.__mode = C_MODE_CELSIUS  
        self.__temperatures = tuple([Temperature(), Temperature(), Temperature(), Temperature(), 
                                     Temperature(), Temperature(), Temperature(), Temperature(), 
                                     Temperature(), Temperature(), Temperature(), Temperature()]) 
        self.__year = year

    @property
    def year(self):
        return self.__year

    @property
    def temperatures(self):
        return self.__temperatures
   
    @property
    def mode(self) -> int:
        return self.__mode

    @mode.setter
    def mode(self, value: int):
        if value in degrees_modes and value != self.__mode:
            for t in self.temperatures:
                t.mode = value
            self.__mode = value
        else:
            raise ValueError('provide a correct mode')

    @classmethod
    def fromDict(cls, value: dict):
        year = Year(value["year"])
        year.as_dict = value
        return year


    def _get_dict(self) -> dict:
        mylist = []

        for index, temp in enumerate(self.temperatures):
            mylist.append({"{}".format(index): temp.degrees})

        output = {}
        output['year'] = self.year
        output['data'] = mylist

        return output


    def _set_dict(self, value):
        self.__year = value["year"]
        mylist = value["data"]
        for index, item in enumerate(mylist):
            self.temperatures[index].degrees = item["{}".format(index)] 


    def get_hottest(self):
        """[summary]

        Returns:
            [hottest]: degrees
            [pos]: position in list
        """
        hottest = -999.0               
        pos = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        for index, x in enumerate(self.temperatures):
            if x.degrees > hottest:
                pos = index
                hottest = x.degrees

        return hottest, pos

    def get_coldest(self):
        """[summary]

        Returns:
            [coldest]: degrees
            [pos]: position in list
        """
        coldest = 999.0                
        pos = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        for index, x in enumerate(self.temperatures):
            if x.degrees < coldest:
                pos = index
                coldest = x.degrees
        return coldest, pos

    def get_average(self):
        total = 0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        for x in self.temperatures:
            total += x.degrees
        
        try:
            return total / 12
        except:
            pass
        
        return 0.0


class YearList(BaseList):
    def __init__(self):
        super().__init__(Year, 'years.json')
        self.__mode = C_MODE_CELSIUS

    @property
    def mode(self) -> int:
        return self.__mode

    @mode.setter
    def mode(self, value: int):
        if value in degrees_modes and value != self.__mode:
            for t in self.items:
                t.mode = value
            self.__mode = value
        else:
            raise ValueError('provide a correct mode')


    def get_item_by_year(self, year: int) -> Year:
        for x in self.items:
            if x.year == year:
                return x 
        return None



def get_year_input(yearlist: YearList) -> Year:
    print_years(yearlist)
    chosen_year = get_input_item('geef het reeds bestaande jaar in om te wijzigen of geef een nieuw jaar op : ', 1)
    year = yearlist.get_item_by_year(chosen_year)
    if year is None:
        year = yearlist.add(Year(chosen_year))

    for x in range(1, 13):
        month = date(2000, x, 1)
        year.temperatures[x-1].degrees = get_input_item('geef de temp in voor {} :'.format(month.strftime("%B")), 2)


def create_yearlist() -> YearList:
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
                month = date(year.year, x+1, 1)
                print('{}: {}'.format(month.strftime("%B"), year.temperatures[x].degrees))

            val, pos = year.get_hottest()
            month = date(year.year, pos+1, 1)
            print('warmste is: {} - {}'.format(month.strftime("%B"), val))


            val, pos = year.get_coldest()
            month = date(year.year, pos+1, 1)
            print('koudste is: {} - {}'.format(month.strftime("%B"), val))

            print('gemiddelde is: {}'.format(year.get_average()))


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
    