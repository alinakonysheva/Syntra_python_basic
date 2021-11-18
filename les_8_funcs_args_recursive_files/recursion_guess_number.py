from random import randint

min_n = 0
max_n = 10

number_of_luck = randint(min_n, max_n)

number_guesses = 5


def check_number(guess):
    global number_of_luck
    user_number = int(input(f'your number between {min_n} and {max_n}  '))
    print(guess)
    if user_number != number_of_luck and guess < number_guesses == 5:
        return check_number(guess + 1)
    elif user_number == number_of_luck:
        print('you are th winner')
    else:
        print('next time')


check_number(0)
