C_TYPE_CAR_E = 1
C_TYPE_CAR_HYBRID = 2
C_TYPE_CAR_DIESEL = 3
C_TYPE_CAR_GASOLINE = 4



class Car():
    __brand = ''
    __color = ''
    __model = ''
    __useage = ''
    __max_speed = ''
    __nr_persons = ''
    

    def __init__(self, brand, color, model, useage, max_speed, nr_persons):
        self.__brand = brand
        self.__color = color
        self.__model = model
        self.__useage = useage
        self.__max_speed = max_speed
        self.__nr_persons = nr_persons

    @property
    def brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @property 
    def model(self):
        return self.__model

    @property 
    def useage(self):
        return self.__useage

    @property
    def max_speed(self):
        return self.__max_speed

    @property
    def nr_persons(self):
        return self.__nr_persons

    
    def get_type(self):
        return type(self)

    def __str__(self) -> str:
        return '{} : {} - {} - {}'.format(type(self).__name__, self.brand, 
                                          self.model, self.max_speed)


class ElectricCar(Car):
    pass


class HybridCar(Car):
    pass


class DieselCar(Car):
    pass


class GasolineCar(Car):
     pass


def create_car(car_type: int, brand, color, model, useage, max_speed, nr_persons) -> Car:
    if car_type == C_TYPE_CAR_E:
        return ElectricCar(brand, color, model, useage, max_speed, nr_persons)
    elif car_type == C_TYPE_CAR_HYBRID:
        return HybridCar(brand, color, model, useage, max_speed, nr_persons)
    elif car_type == C_TYPE_CAR_DIESEL:
        return DieselCar(brand, color, model, useage, max_speed, nr_persons)
    elif car_type == C_TYPE_CAR_GASOLINE:
        return GasolineCar(brand, color, model, useage, max_speed, nr_persons)
    
    return None