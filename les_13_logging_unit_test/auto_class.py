# Maak een object auto en geef een wagen eigenschappen zoals merk, model, kleur, prijs. Druk deze af
class Car:

    def __init__(self, brand, color, price, model):
        self.brand = brand
        self.color = color
        self.price = price
        self.model = model


car1 = Car('bmw', 'blue', 50000, '3w')


def create_car(brand, color, price, model):
    car = Car(brand, color, price, model)
    return car


def print_car(car: Car):
    '''

    :param car:
    :return:
    '''
    print(f'Uw auto heeft merk: {car.brand}, model: {car.model}, kleur: {car.color}, prijs: {car.price}')


print_car(car1)
