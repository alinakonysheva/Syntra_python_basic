# Maak een programma dat een ongekend aantal getallen vraagt,
# maak een functie dat de som van al deze getallen zal berekenen en teruggeven.

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


def sum_many_numbers(list_of_numbers):
    """
    :param args: numbers
    :return: sum of the input
    """
    total = 0
    try:
        for num in list_of_numbers:
            total += num
    except ValueError:
        return -1

    return total


print(sum_many_numbers(get_numbers_list()))


