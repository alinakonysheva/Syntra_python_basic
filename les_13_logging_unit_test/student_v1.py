class Student():
    __address = ''
    __name = ''
    
    def __init__(self, name: str, address: str):
        self.address = address
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
    def address(self, value: str):
        self.__address = value

    def __str__(self) -> str:
        return self.name + ' - ' + self.address


def create_student(name: str, address: str) -> Student:
    return Student(name, address)