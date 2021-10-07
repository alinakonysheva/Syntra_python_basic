# Maak een dictionary aan met 5 merken van wagens. 1–merkx, 2–merkY....
# Print deze lijst van merken en vraag de gebruiker welk merk van wagen hij heeft door het nummer in te geven
# output:
# 1 – merk x
# ...
# 5 – merk z
# Met welk merk van wagen rijdt u (kies het type) ? → 2 U rijdt met “merk A”

# dict_cars = {1: 'BMW', 2: 'Mercedes', 3: 'Audi', 4: 'Ford', 5: 'None of above'}
#
# print('what kind of a car do you have?')
# for car, number in dict_cars.items():
#     print(f'{car} -- {number}')
#
# try:
#     car_of_user = int(input('what is a brand of your car, enter a number  '))
# except Exception as e:
#     print('you have to enter a number')
#
# print(f'you have {dict_cars[car_of_user]}')

# Vraag een gebruiker om eigenschappen van een wagen en bewaar dit in het geheugen.
# De eigenschappen die we willen bewaren zijn merk, model, bouwjaar, kleur, prijs
# Nadat de gebruiker deze heeft ingegeven, druk alle wagen eigenschappen af

# attributes_car = {'brand': '', 'model': '', 'year of manufacture': '', 'color': '', 'price': ''}
# for attribute, user_input in attributes_car.items():
#     attributes_car.update({attribute: input(f'enter yours {attribute}   ')})
#
# print('your car has those attributes:')
# for attr, val in attributes_car.items():
#     print(f'{attr}: {val}')

# Doe nu hetzelfde maar voor meerdere wagens tot de gebruiker zegt stop
cars = []
number_cars = int(input(f'how many cars do you want to add?  '))
attributes_car = {'brand': '', 'model': '', 'year of manufacture': '', 'color': '', 'price': ''}

for car in range(number_cars):
    for attribute, user_input in attributes_car.items():
        attributes_car.update({attribute: input(f'enter {attribute} of the car  ')})
        user_car = attributes_car.copy()
    cars.append(user_car)

print(f'\nyour cars have those attributes:\n' + '_' * 20)

for car in cars:
    for atr, user_value in car.items():
        print(f'{atr}: {user_value}')
    print('_' * 20)
