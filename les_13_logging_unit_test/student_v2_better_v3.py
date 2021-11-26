
class Address():
    __street = ''
    __nr = 0
    __zip = 0
    __city = ''

    def __init__(self, street: str = '', nr: int = 0, zip: int = 0, city: str = ''):
        self.__street = street
        self.__nr = nr
        self.zip = zip
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
        
    @test_int
    @zip.setter
    def zip(self, value):
        self.__zip = value

    @property
    def city(self):
        return self.__city

    def __str__(self):
        return self.street + ' ' + str(self.nr) + ' ' + str(self.zip) + ' ' + self.city

        

class Student():
    __address = None
    __name = ''
    
    def __init__(self, name: str, street: str, nr: int, zip: int, city: str):
        self.name = name
        self.__address = Address(name, street, nr, zip, city)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def address(self):
        return self.__address

    def __str__(self) -> str:
        return self.name + ' - ' + str(self.address)



def create_student(name: str, street: str, nr: int, zip: int, city: str) -> Student:
    student = Student(name, street, nr, zip, city)
    
    """of
    adr = Address(street, nr, zip, city)
    student = Student(name, adr)
    """

    return student



create_student()