# решето эратосфена, простоые числа priemgetallen
'''
n = int(input('до какого числа сеем?'))
sieve = [i for i in range(n)]

for i in range(2, n):
    if sieve[i] != 0:
        j = i + i
        while j < n:
            sieve[2] = 0
            j += i
            '''


def sieve_rec(pin, number_up_to, sieve):
    """
    :param sieve: состояние решета
    :param pin: что тыкаем
    :param number_up_to: до какого числа будем просеивать
    :return: result
    """
    if pin < number_up_to:
        if sieve[pin] != 0:
            sieve[pin] = 0
            next_pin = pin + pin
            return sieve_rec(next_pin, number_up_to, sieve)

    result = [i for i in sieve if i != 0]

    return result


n = 50
sieve_in = [i for i in range(n)]
print(sieve_rec(2, 50, sieve_in))
