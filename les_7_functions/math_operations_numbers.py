# Maak een programma dat een gebruiker om 2 getallen vraagt,
# en druk dan van deze 2 getallen het volgende af som, deling, vermendigvuldiging

def get_numbers():
    try:
        number1 = int(input('give me your first number, please  '))
        number2 = int(input('give me your second number, please  '))

    except Exception as e:
        return e

    return number1, number2


def sum_(number1, number2):
    return number1 + number2


def division_(number1, number2):
    if number2 != 0:
        try:
            res = number1 / number2

        except Exception as e:
            print('those have to be numbers')
    else:
        return 'infinity'

    return res


def multiply_(number1, number2):
    return number1 * number2


def print_sum_div_mult_results():
    try:
        num1, num2 = get_numbers()
        print(f'sum: {sum_(num1, num2)}, division: {division_(num1, num2)}, multiply: {multiply_(num1, num2)}')
    except Exception as e:
        print(e, 'those have to be numbers')

print_sum_div_mult_results()