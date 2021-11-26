
class CarColor():
    __name = ''
    __hex = ''

    def __init__(self, name: str, hexvalue: str):
        self.__name = name
        self.__hex = hexvalue

    @property
    def name(self):
        return self.__name

    @property
    def hexvalue(self):
        return self.__hex


    def __str__(self):
        return '{} - {}'.format(self.name, self.hexvalue)


class Car():

    __brands = ['Peugeot', 'Opel', 'McLaren']
    __colors = [CarColor('red', '#09384'), CarColor('grey', '#44444')]

    __brandtype = -1
    __model = ''
    __colortype = -1
    __price = 0.00

    def __init__(self, brand: int, model:str, color: int, price: float):
        self.brandtype = brand
        self.model = model
        self.colortype = color
        self.price = price

    @property
    def brand(self):
        return self.__brands[self.__brandtype]

    @brand.setter
    def brand(self, value):
        if value < 0 or value > len(self.__brands) - 1:
            raise Exception('too large or too small')
        self.__brandtype = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def color(self):
        return self.__colors[self.__colortype]

    @color.setter
    def color(self, value: int):
        if value < 0 or value > len(self.__colors) - 1:
            raise Exception('too large or too small')
        self.__colortype = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        return self.__price


    def __str__(self):
        return '{} - {} - {} - {}'.format(self.brand, self.model, self.color, self.price)

    
    

def create_car(brand: int, model: str, color: int, price: float):
    return Car(brand, model, color, price)