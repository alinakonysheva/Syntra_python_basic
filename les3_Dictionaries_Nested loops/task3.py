# Maak een dobbelsteen en gooi de dobbelsteen. Geef de gegooide waarde weer
# import random
#
# print(f'our number is {random.randint(1, 6)}')

# Maak een spel dat de gebruiker een getal tussen 1 en 20 moet raden.
# Als de gebruiker een cijfer ingeeft dat dan krijgt hij een hint of het kleiner of groter is.
# Voeg ook een optie toe zodat de gebruiker kan stoppen indien hij het spel beu is.

# переписать с учетом того, что в любом месте пользователь может ввести ерундуд
import random


number_of_the_computer = random.randint(1, 20)
print(number_of_the_computer)
print('Let\'s play a game! Guess my number! It is a number between 1 and 20')

go_on = True
user_number = 0

while go_on:
    try:
        user_number = int(input('give me your guess:  '))
    except ValueError as e:
        print('You have to enter number, please')
        user_number = int(input('give me your guess:  '))
    if user_number > number_of_the_computer:
        print('your number is bigger than my number')
        go_on = int(input('if you would like to go on -- press 1, if not -- press 0  '))

    elif user_number < number_of_the_computer:
        print('your number is smaller than my number')
        go_on = int(input('if you would like to go on -- press 1, if not -- press 0  '))
    else:
        print('you are the winner, congrats!')
        go_on = int(input('if you would like to play one more time -- press 1, if not -- press 0  '))


