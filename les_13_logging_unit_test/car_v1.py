class Car():
    __brand = ''
    __model = ''
    __color = ''
    __price = 0.00

    def __init__(self, brand: str, model: str, color: str, price: float):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        return self.__price


    def __str__(self):
        return '{} - {} - {} - {}'.format(self.brand, self.model, self.color, self.price)

    
    

def create_car(brand: str, model: str, color: str, price: float):
    newcar = Car(brand, model, color, price)
    return newcar