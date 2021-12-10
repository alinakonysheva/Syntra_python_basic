from datetime import date, datetime
from inputs import get_input_item


tastes = ['unknown', 'sweet', 'bitter', 'mild']

class Sigar():
    __length = 0.0
    __name = ''
    __price = 0.0
    __taste_type = 0
    __country = ''

    def __init__(self, name: str, length: float, price:float, country:str, taste_type:int=0):
        """constructor

        Args:
            name (str): brand/name of the sigar
            length (float): length in cm
            price (float): price
            country (str): origin country
            taste_type (int, optional): [description]. Defaults to 0.
        """

        self.name = name
        self.length = length
        self.price = price
        self.country = country
        self.taste_type = taste_type

    def __str__(self) -> str:
        return '{} - {}'.format(self.name, self.price)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float):
        self.__length = value
    
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        self.__price = value

    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value: str):
        self.__country = value

    @property
    def taste(self):
        return tastes[self.__taste_type]

    @property
    def taste_type(self):
        return self.__taste_type

    @taste_type.setter
    def taste_type(self,value: int):
        self.__taste_type = value



def create_sigar(name: str, length: float, price:float, country:str, taste_type:int=0) -> Sigar:
    """create a sigar object

    Args:
        name (str): name/brand sigar
        length (float): length in cm
        price (float): price of the sigar
        country (str): country of origina
        taste_type (int, optional): [description]. Defaults to 0 -> Unknown.

    Returns:
        Sigar: [description]
    """
    return Sigar(name, length, price, country, taste_type)

