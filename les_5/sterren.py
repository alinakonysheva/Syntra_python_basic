print('mijntext')
number_strings = 20
half_number = number_strings / 2
for i in range(number_strings):
    if i <= half_number:
        print('* ' * i)
    else:
        print('* ' * (number_strings - i))
