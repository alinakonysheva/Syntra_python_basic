# Maak een programma dat het volgende doet: vraag een ongekend aantal nummer van getallen,
# maak een functie dat de max weergeeft, maak een andere functie dat de min weergeeft en maak
# een functie dat de minimale waarde en de maximale waarde van lijst gaat optellen en vermeningvuldigen.
# Maak een 3de functie dat alles zal afdrukken

def get_numbers_list():
    user_numbers = []
    number = 0
    try:
        while number != 'q':
            number = input('give me a number to sum up, please. If you want to stop -- press q  ')
            if number.isdigit():
                user_numbers.append(float(number))

    except ValueError:
        user_numbers.append(0)
        number = 'q'

    return user_numbers


def max_num(list_):
    return max(list_)


def min_num(list_):
    return min(list_)


def multiply_and_sum_max_min(list_):
    min_ = min_num(list_)
    max_ = max_num(list_)
    return min_ * max_, min_ + max_


def output():
    list_ = get_numbers_list()
    result = multiply_and_sum_max_min(list_)
    print(f'your list is {list_}, \n min(list) * max(list) = {result[0]}, min(list) + max(list) ={result[1]}')

output()