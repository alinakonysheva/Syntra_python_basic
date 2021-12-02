# Wij hebben een broodjeszaak. Vraag de gebruiker welk brood hij wilt (wit, bruin, meergranen).
# Als beleg kunnen we kiezen uit de volgende zaken, kaas (1€), hesp(1€), tonijnsla(1,20€), eiersla(0,95€),
# krabsla(1,45€). Dan kunnen er nog toppings bij waaronder salade (0,50€), tomaat (0,50€), mayonaise (0,25€),
# ei (0,35€), wortel (0,45€), maïs (0,45€). Bereken dan de totaalprijs van het broodje en druk dan ook het “recutje”
# met de prijs/beleg/toppings af


class Ingredient:
    __name = ''
    __price = 0.00

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def __str__(self):
        return f'{self.__name}, {self.__price}'


class Bread(Ingredient):

    def __init__(self, name, price):
        super().__init__(name, price)


class Stuffing(Ingredient):

    def __init__(self, name, price):
        super().__init__(name, price)


class Topping(Ingredient):

    def __init__(self, name, price):
        super().__init__(name, price)


class Bun:
    __bread_type = None
    __stuffing = []
    __topping = []

    def __init__(self, bread_type):
        self.__bread_type = bread_type

    @property
    def bread_type(self):
        return self.__bread_type

    @bread_type.setter
    def bread_type(self, value):
        self.__bread_type = value

    @property
    def stuffing(self):
        return self.__stuffing

    @stuffing.setter
    def stuffing(self, value):
        self.__stuffing = value

    @property
    def topping(self):
        return self.__topping

    @topping.setter
    def topping(self, value):
        self.__topping = value

    def add_stuffing(self, value):
        """
        to add stuffing in a bun (of Bun)
        :param value: type: Stuffing
        """
        self.__stuffing.append(value)

    def add_topping(self, value):
        """
        to add topping in a bun (of Bun)
        :param value: type: Topping
        """
        self.__topping.append(value)

    def add_bread_type(self, value):
        self.__bread_type = value

    def __str__(self):
        return f'{self.__bread_type}, {self.__stuffing}, {self.__topping}'
