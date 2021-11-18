# Vraag aan de gebruiker minstens 2 wagens waar hij mij gereden heeft.
# Elke wagen heeft een kleur/merk/nummerplaat. Druk alle wagens af

class Car:
    '''
    class car
    to create a person
    '''
    color = ''
    brand = ''
    plate = 0


def get_input():
    '''
    no arguments
    :return: color, brand, plate
    '''
    color = input('the color of your car is >>  ')
    brand = input('the brand of your car is >>  ')
    plate = input('your plate number is >>  ')
    return color, brand, plate


def create_car():
    '''
    to create car instance
    :return: class car instance
    '''
    thecar = Car()
    thecar.color, thecar.brand, thecar.plate = get_input()
    return thecar


def output(some_car):
    '''
    to return properties of a car, if no car given then None
    :param some_car:
    :return:  color, brand, plate number, if no car given then None
    '''

    if some_car:
        return some_car.color, some_car.brand, some_car.plate
    else:
        return None

number_of_cars = 2

def do_run():
    for car in range(number_of_cars):
        outpt_ = output(create_car())
        for i in outpt_:
            print(i)


do_run()
