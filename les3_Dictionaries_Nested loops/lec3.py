# import random
# my_list = ['apple', 'banana', 'water']
#
# print(random.choice(my_list))

# import random
#
# while True:
#     number_of_the_computer = random.randint(1, 20)
#     print(number_of_the_computer)
#
#     print('Let\'s play a game! Guess my number! It is a number between 1 and 20')
#
#     try:
#         user_number = int(input('give me your guess:  '))
#     except ValueError:
#         print('You have to enter number, please')
#
#     go_on = True
#     if user_number == number_of_the_computer:
#         print('you are the winner!')
#
#     while user_number != number_of_the_computer:
#         if user_number > number_of_the_computer:
#             print('your number is bigger than my number')
#             go_on = int(input('if you would like to go on, press 1, if not -- press 0  '))
#             if go_on:
#                 user_number = int(input('give me your guess:  '))
#         elif user_number < number_of_the_computer:
#             print('your number is smaller than my number')
#             go_on = int(input('if you would like to go on, press 1, if not -- press 0  '))
#             if go_on:
#                 user_number = int(input('give me your guess:  '))
#
#     print('you are the winner, congrats!')
#     break
#


# Nested dictionaries  -- словарь в словаре
# my_cars = {{}, {}, {}}
#
# fuel_type = my_cars.get('fueltype', 'Diesel')
# carlist = []
# user_wants_to_stop = False
# while user_wants_to_stop is False:
#     print('give me a car')
#     mycar = dict()
#     mycar['brand'] = input('your brand')
#     mycar['model'] = input('your model')
#     carlist.append(mycar)
#     user_wants_to_stop = input('do you want to quit, type y to stop').lower() == 'y'
#
# counter = 1
# print(f'Total cars {len(carlist)}')
# for car in carlist:
#     counter += 1
#     print('_'*10)
#     for x, y in car.items():
#         print(f'{x}, {y}')

