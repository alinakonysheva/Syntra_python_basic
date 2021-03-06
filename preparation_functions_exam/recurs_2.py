# n4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится
# с клавиатуры.

# сделаем функцию для рекурсивного вычисления геометрических прогрессий


def sum_progression(term_count, i, ratio, current_element, summ):
    if i < term_count:

        # текущий элемент равен предыдущему элементу, умноженному на знаменатель прогрессии
        current_element = current_element * ratio
        # сумма членов прогрессии увеличичвается с каждым шагом на текущий элемент
        summ = summ + current_element
        i = i + 1
        return sum_progression(term_count, i, ratio, current_element, summ)

    else:
        return summ


# вводим начальные условия для конкретной геомтерической прогрессии
# n0 = 1 - первый эелемент прогрессии, q = -0.5 -- знаменатель прогрессии


def sum_05(n):
    return sum_progression(n, 1, -0.5, 1, 1)


n = int(input("Введите, пожалуйста, количество элементов прогрессии, не более 997, сумму которых надо вычислить:   "))
