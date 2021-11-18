# Maak een programma dat een ongekend aantallen getallen vraagt en deze gaat sorteren
# van klein naar groot. Hiervoor gaan we gebruik maken van “Bubble Sort”,
# we vergelijken elk item met het volgende en gaan het dan van plaats verwisselen
# tot het laatste item achteraan staat. Druk dan de orginele lijst af en de gesorteerde lijst

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


def bubble_sort(list_):
    sorted_list = list_.copy()
    permutation = True
    n = 1
    while n < len(sorted_list) and permutation:
        permutation = False
        for i in range(0, len(list_) - n):
            if sorted_list[i] > sorted_list[i + 1]:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                permutation = True
            n += 1

    return sorted_list


print(bubble_sort(get_numbers_list()))

