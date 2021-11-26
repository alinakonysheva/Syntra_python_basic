
class Address():
    __street = ''
    __nr = 0
    __zip = 0
    __city = ''

    def __init__(self, street: str, nr: int, zip: int, city: str):
        self.__street = street
        self.__nr = nr
        self.__zip = zip
        self.__city = city
    
    @property
    def street(self):
        return self.__street

    @property
    def nr(self):
        return self.__nr
        
    @property
    def zip(self):
        return self.__zip
        
    @property
    def city(self):
        return self.__city

    def __str__(self):
        return self.street + ' ' + str(self.nr) + ' ' + str(self.zip) + ' ' + self.city

        

class Student():
    __address = None
    __name = ''
    
    def __init__(self, name: str, street: str, nr: int, zip: int, city: str):
        self.address = Address(street, nr, zip, city)
        self.name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: Address):
        self.__address = value

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.address)


def create_student(name: str, address: Address) -> Student:
    return Student(name, address)