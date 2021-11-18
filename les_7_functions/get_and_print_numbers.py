# Maak een programma dat de som gaat berekenen van 3 getallen,
# vraag de gebruiker ook om 3 getallen.

def get_numbers():
    try:
        number1 = int(input('give me your first number, please  '))
        number2 = int(input('give me your second number, please  '))
        number3 = int(input('give me your third number, please  '))

    except Exception as e:
        return e

    return number1, number2, number3


def sum_(number1, number2, number3):
   try:
       sum_ = number1 + number2 + number3
       return sum_

   except Exception as e:
    return ''


print(sum_(*get_numbers()))

