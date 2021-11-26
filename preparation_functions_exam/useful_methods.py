# count -- считает количество вхождений в строку и лист
# split -- разбиват строку по пробелу split_eqaution = equation.split() -list
# replace  -- split_eqaution[2].replace('x', '') * x -- заменяем на переменную x

def average(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_ / len(args)


# print(average(1, 2, 3, 4, 5))

numbers = [1, 2, 3, 4, 5]

result_ = average(*numbers)


def max_str(*args):
    return max(args, key=len)


# print(result)
# сшиваем два списка
students = ['ben', 'tibo', 'greta']
scores = [2, 5, 10]

result = zip(students, scores)
res_list = list(result)
res_dict = dict(result)

# для любого элемента что делать
data = [-1, - 2, -3, 4, 5, 6]


def do_smth(x):
    return (x + 10) / 3


# map (делай что-то с этой датой. возвращает объект)
do_smth_with_el_list = map(do_smth, data)
print(list(do_smth_with_el_list))

# то же, но через лямбда функции, если функция  -- вычислить значения

new_res_with_lambda = map(lambda x: (x + 3) / 10, data)

# фильтруемб отфильтровать значения из списка

positiv_el_out_data = filter(lambda x: x > 0, data)
print(*positiv_el_out_data)
