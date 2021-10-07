number = 1
line = 10
column = 6
for i in range(1, line):
    print()
    for j in range(1, column):
       # if len(str(number)) == 1:
        #print(f'{str(number).zfill(2) :>5}', end='')
        print(f'  {number:0>2}    ', end='')
       # else:
            #print(f'{number :>5}', end='')
        number += 1
# без zfill через ф строки: print(f'{number:03}')
print()
print('_' * 30)
print('_' * 30)

count_up_min_1 = 46
number_columns = 5
for i in range(1, count_up_min_1):
    print(f'{i :>5}', end='')
    if i % number_columns == 0:
        print()