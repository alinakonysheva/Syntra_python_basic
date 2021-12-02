class Sigar:
    __name = ''
    __country = ''
    __price = 0.00
    __length = 0.00
    __taste = ''

    def __init__(self, name, country, price, length, taste):
        self.__name = name
        self.__country = country
        self.__price = price
        self.__length = length
        self.__taste = taste

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

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def taste(self):
        return self.__taste

    @taste.setter
    def taste(self, value):
        self.__taste = value

    def __str__(self):
        return f'{self.__name}, {self.__price}'
