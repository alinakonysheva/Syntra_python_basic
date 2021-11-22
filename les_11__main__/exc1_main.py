""""
we hebben 
basis klasse wagen
    per type make we een klasse aan (verschillende opties mogelijk)

    1 car
    type

    2 car
        ecar
    hybride ...
    3
    car 
    batterycar
    ecar
    hybride
    diesel
    gasoline
    lpg


    merk
    kleur
    model
    verbruik
    max snelheid
    aantal personen


    keuzelijst tonen
    input vragen van properties
    output -> per type van wagen de eigenschappen
"""

from cars import C_TYPE_CAR_GASOLINE, C_TYPE_CAR_HYBRID, create_car, C_TYPE_CAR_E,\
                 C_TYPE_CAR_DIESEL, C_TYPE_CAR_GASOLINE, C_TYPE_CAR_HYBRID 
from inputs import get_input_item

C_STOPCHAR = 'n'

def print_choicelist():
    print('U kan een getal kiezen uit de volgende waarden')
    print('{} - Electrische wagen'.format(C_TYPE_CAR_E))
    print('{} - Hybride'.format(C_TYPE_CAR_HYBRID))
    print('{} - Diesel'.format(C_TYPE_CAR_DIESEL))
    print('{} - Benzine'.format(C_TYPE_CAR_GASOLINE))
    

def get_input() -> list:
    """Loop to ask to give car data
    """

    print_choicelist()

    cars = []
    car_type = ''
    while car_type != C_STOPCHAR:
        car_type = get_input_item("""
            Geef het type van wagen op, kies het nummer uit de vorige lijst en "{}" om te stoppen
            """.format(C_STOPCHAR), 1)
        
        if car_type == C_STOPCHAR:
            continue

        brand = get_input_item('Geef het merk: ')
        model = get_input_item('Geef het model: ')
        color = get_input_item('Geef de kleur: ')
        useage = get_input_item('Geef het verbruik: ')
        max_speed = get_input_item('Geef de max snelheid: ')
        nr_persons = get_input_item('Geef het aantal personen: ')

        x = create_car(car_type, brand, color, model, useage, max_speed, nr_persons)
        cars.append(x)
    
    return cars


def do_output(cars: list):
    car_type = []
    # loop over cars
    for car in cars:
        # if type not shown yet do loop again
        if car_type not in car_type:
            current_type = car.get_type()
            car_type.append(current_type)
            print('printing type: {}'.format(current_type.__name__))
            for item in cars:
                if item.get_type() == current_type:
                    print(item)


def main():
    cars = get_input()
    do_output(cars)

if __name__ == '__main__':
    main()

