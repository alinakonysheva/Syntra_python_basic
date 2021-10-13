# генератор списков
# vs
# list comprehension
########################################
'''from sys import getsizeof
from time import perf_counter

MAX_NUM = 10 ** 7

start = perf_counter()
num_list_comprehension = [num for num in range(1, MAX_NUM + 1)]
sum_num_list_comprehension = sum(num_list_comprehension)
print('list comprehension')
print(f'{sum_num_list_comprehension}, time = {perf_counter() - start}, memory = {getsizeof(num_list_comprehension)}')

start = perf_counter()
num_list_generator = (num for num in range(1, MAX_NUM + 1))
sum_list_generator = sum(num_list_generator)
print('list generator')
print(f'{sum_list_generator}, time = {perf_counter() - start}, memory = {getsizeof(num_list_generator)}')
'''
# как посмотреть что внутри генератора? print(*num), но после ничего не осталось от генератора
#################################################
# filter(), map(), zip()

users = ['ivan', 'IGOR', 'olga', 'anna', 'inokenntij']
users_filtered = []
#for user in users:
#   pass

#result = map(str.title, users)

#print(*result)

result = ', '.join(filter(lambda x: x.startswith('I'),
                          map(str.title, users)))
print(result)

positions = ["accountant", "calculator", "QA engineer", "controller", "boss", "big boss"]

'''for user, position in zip(users, positions):
    print(user, '->', position)'''

print(*zip(users, positions))