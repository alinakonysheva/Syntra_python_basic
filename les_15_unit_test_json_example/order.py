from datetime import date, datetime
from inputs import get_input_item
from sigar import Sigar, create_sigar
from person import Person

class Order():
    def __init__(self, person: Person, nr:int):
        self.__nr = nr
        self.__sigars = []
        self.__date = datetime.now()
        self.__total_price = 0.0
        self.__minimum_price = 10.0
        self.__person = person

    @property
    def nr(self) -> int:
        return self.__nr

    @property
    def sigars(self) -> list:
        return self.__sigars

    @property
    def date(self) -> datetime:
        return self.__date

    @property
    def price(self) -> float:
        return self.__total_price

    @property
    def price_minimum(self) -> float:
        return self.__minimum_price

    @property
    def minimum_met(self) -> bool:
        return self.price >= self.price_minimum

    def add_sigar(self, sigar: Sigar):
        """add a sigar to the internal list
        Args:
            sigar (Sigar): sigar object

        Raises:
            TypeError: when object is not type sigar, you get an error
        """
        # if isinstance(sigar, Sigar):
        if sigar is not None and type(sigar) is Sigar:
            self.sigars.append(sigar)
            self.__total_price += sigar.price
        else:
            raise TypeError('object to add is not of type sigar')
    '''
    def add_sigar(self, name, length, price, country, taste_type):
        s = create_sigar(name, length, price, country, taste_type)
        self.sigars.append(s)
        self.__total_price += s.price
    '''

    '''
    def del_sigar(self, sigar: Sigar):
        self.__total_price -= sigar.price
        self.sigars.remove(sigar)
    '''

    @property
    def person(self):
        if self.__person is None:
            raise ValueError('shipment object must be set first')
        
        return self.__person

    '''
    @person.setter
    def person(self, value):
        if value is not None and type(value) == Person:
            self.__person = value
        else:
            raise TypeError('no person object')
    '''

def create_order(person: Person, nr: int) -> Order:
    """create an order"""
    return Order(person, nr)
