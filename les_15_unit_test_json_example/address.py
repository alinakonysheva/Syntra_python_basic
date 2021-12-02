class Address():
    __zip = ''
    __city = ''
    __street = ''
    __nr = ''
    __country = ''

    def __init__(self, street, nr, zip, city, country):
        self.__street = street
        self.__nr = nr
        self.__zip = zip
        self.__city = city
        self.__country = country

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def zip(self):
        return self.__zip

    @zip.setter
    def zip(self, value):
        self.__zip = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def nr(self):
        return self.__nr
    
    @nr.setter
    def nr(self, value):
        self.__nr = value 

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    def __str__(self):
        return "{} {}, {} {}, {}".format(self.street, self.nr, 
                                         self.zip, self.city, 
                                         self.country)


def create_adress(street='', nr='', zip='', city='', country='') -> Address:
     return Address(street, nr, zip, city, country)
