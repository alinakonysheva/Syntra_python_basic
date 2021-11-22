# # In een restaurant serveren we 4 menu’s, elk menu heeft een prijs
# # Menu 1 - dagsoep - vis - dessert 35 euro
# # Menu 2 - steak/friet - ijsje 30 euro
# # Menu 3 - garnaalkroket - mosselen 35 euro
# # Menu 4 - antipasta - pasta - panna cotta 30 euro
#
# # Maak een bestelling. Elke bestelling is voor een ongekend aantal personen.
# # Druk dan de “werkbon” af voor de chef kok en de totaalprijs voor die tafel

class Menu:
    __dishes_list = []
    __price = 0.00

    def __init__(self, dishes_list, price):
        self.__dishes_list = dishes_list
        self.__price = price

    @property
    def dishes_list(self):
        return self.__dishes_list

    @dishes_list.setter
    def dishes_list(self, value):
        self.__dishes_list = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class Table:
    __table_number = 0
    __total_persons = 0

    def __init__(self, table_number, total_persons):
        self.__table_number = table_number
        self.__total_persons = total_persons

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.table_number = value

    def total_persons(self):
        return self.__total_persons

    @total_persons.setter
    def total_persons(self, value):
        self.__total_persons = value


class Order:
    __list_menus = []
    __table_number = 0
    __total_persons = 0
    __total_price = 0

    @property
    def list_menus(self):
        return self.__list_menus

    @list_menus.setter
    def list_menus(self, value):
        self.list_menus = value

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.table_number = value

    def total_persons(self):
        return self.__total_persons

    @total_persons.setter
    def total_persons(self, value):
        self.__total_persons = value

    def total_price(self):
        return self.__total_persons

    @total_price.setter
    def total_price(self, value):
        self.__total_price = value










