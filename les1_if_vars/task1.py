# разделение пробелами при выводе
# oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
# print(f'''IP address: {oct1:<4} {oct2:<4} {oct3:<4} {oct4:<4}''')


# импорт модуля
# import main
# from test 2 import main as do_sub

# import sys

# sys.SystemExit()

def calc(a, b):
    '''
    add 2 numbers en return result
    in:
    :param a:
    :param b:
    out:
    :return:
    '''
    return a + b


my_number = 1
# разрыв строки
my_number = my_number + my_number + \
            + my_number
# если длинное выражение стоит под если, то можено его переносить со строчки на строчку,
# но выражение должно стоять в круглых скобках
if my_number > 0 and my_number < 4 and my_number:
    calc(my_number, my_number)

y = False
z = 0
if z == y:
    print('yes')
else:
    print('no')

print(round(5 / 2))
print(type(z))

# проверка на тип
print(isinstance(z, float))

list_ex = [1, 3, 'f', 5, 4, 'h']
if 1 in list_ex:
    print('1 is here')


def do_multiply(a, b):
    res = a * b
    return res
