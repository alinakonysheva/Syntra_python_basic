class Student():
    __adress = ''
    __name = ''

    def __init__(self, name='', adres=''):
        self.adress = adres
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, value):
        self.__adress = value

    def __str__(self):
        return '{} - {}'.format(self.name, self.adress)

def get_input(text : str) -> str:
    return input(text)


def create_student():
    """
    name = get_input('Geef de naam in : ')
    adr = get_input('geef het adres in : ')
    student = Student(name, adr)
    """

    student = Student()
    student.name = get_input('Geef de naam in : ')
    student.adress = get_input('geef het adres in : ')
    

    print(student)

if __name__ == '__main__':
    create_student()