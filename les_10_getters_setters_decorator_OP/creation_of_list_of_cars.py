# Vraag een gebruiker om een onbeperkt aantal voertuigen in te geven.
# Elk voertuig heeft een aankoopjaar, prijs, merk, model.
# Druk dan de lijst af

# # Ask a user to enter an unlimited number of vehicles.
# # Each vehicle has a purchase year, price, make, model.

from operator import attrgetter

class Vehicle:
    __purchase_year = 0
    __price = 0.0
    __brand = ''
    __model = ' '

    def __init__(self, purchase_year, price, brand, model):
        self.purchase_year = purchase_year
        self.price = price
        self.brand = brand
        self.model = model

    @property
    def purchase_year(self):
        return self.__purchase_year

    @purchase_year.setter
    def purchase_year(self, value):
        self.__purchase_year = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @purchase_year.setter
    def model(self, value):
        self.__model = value

    def __str__(self):
        return f'{self.__model}, {self.__brand}'


def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Args:
        text ([str]): text to use in the display string for input
        restype (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer

    Returns:
        any: int or str, depending on conversion type
    """
    try:
        inp = input(f'Geef uw conversion_type: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = inp
    except Exception as e:
        print(e)
        result = 0

    return result


def create_list_vehicles() -> list[Vehicle]:
    list_vehicles = []
    return list_vehicles
