# Maak een programma met 2 parameters, 2 getallen. Druk dan deze 2 getallen af en als de som groter
# of  gelijk is aan 10 of kleiner. Druk ook af als je de 2 getallen gaat vermenigvuldigen of het resultaat
# groter of gelijk is aan 20 of kleiner (en het resultaat van de vermenigvuldiging).

'''import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
sum_ = a + b
product = a * b
number_for_compar_sum = 10
number_for_compar_product = 21


print(sum_, product)
if sum_ >= number_for_compar_sum:
    print('som is groter dan', number_for_compar_sum)
    print('de som is', sum_)

else:
    print(a, b)
    print('som is minder dan', number_for_compar_sum)
    print('de som is', sum_)
if product >= number_for_compar_product:
    print('de product is groter dan', number_for_compar_product)
    print('de product is', product)
else:
    print('de product is minder dan', number_for_compar_product)
    print('de product is', product)
'''

'''import sys
print('_' * 35)
number = 1
line = int(sys.argv[1])
column = int(sys.argv[1])

for i in range(1, column + 1):
    print()
    for j in range(1, line + 1):
        print(f'  {number:0>2}    ', end='')
        number += 1
print()
print('_' * 35)
'''
import sys

params_length = len(sys.argv)

col_count = 5
row_count = 9

for i in range(1, params_length):
    try:
        if i == 1:
            col_count = int(sys.argv[i])
        if i == 2:
            row_count = int(sys.argv[i])
    except:
        if i == 1:
            print(f'het aantal kolommen was niet geldig, we vallen terug op de default {col_count}')
        elif i == 2:
            print(f'het aantal rijen was niet geldig, we vallen terug op de default {row_count}')

print(' --- lotto formulier --- ')
print(f'we hebben {col_count} kolommen en {row_count} rijen')
number = 1
for i in range(1, col_count):
    print()
    for j in range(1, row_count):
        print(f'  {number:0>2}    ', end='')
        number += 1
print()
print('_' * 35)