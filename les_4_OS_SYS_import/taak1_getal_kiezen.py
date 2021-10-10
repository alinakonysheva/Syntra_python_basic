import random as rm
#from random import randint

min_n = 1
max_n = 10
lucky_number = rm.randint(min_n, max_n)

try:
    user_number = int(input(f'Enter a integer number between {min_n} and {max_n}  '))
    if user_number == lucky_number:
        print('that is a correct guess!')
    else:
        print(f'that is not correct guess, our number was {lucky_number}')
except ValueError:
    print('that had to be a number')