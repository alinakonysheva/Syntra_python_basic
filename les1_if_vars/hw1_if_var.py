# problem 1
# Vraag de gebruiker om een getal tussen 1 en 100 en geef weer als dit een even
# of oneven getal is.
''''''
try:
    number = int(input('any integer between 1 and 100:  '))
    if 1 < number < 100:
        if number % 2 == 0:
            print('that is even')
        else:
            print('that is odd')
    else:
        print('the number has to be an integer between 1 and 100')
except Exception as e:
    print('you have to type a number')

# problem 2
'''
Vraag de gebruiker om een cijfer tussen 1 en 20 en geef puntenquatering weer waar:
kleiner dan 5 = F
tussen 5 en 9 = E
tussen 9 en 12 = D
tussen 12 en 15 = C
tussen 15 en 18 = B
tussen 18 en 20 = A
'''


try:
    grade = int(input('enter the number of points, any integer between 0 and 20:  '))
    if 0 < grade <= 5:
        print('you have got an F')
    elif 5 < grade <= 9:
        print('you have got an E')
    elif 9 < grade <= 12:
        print('you have got an D')
    elif 12 < grade <= 15:
        print('you have got an C')
    elif 15 < grade <= 18:
        print('you have got an B')
    elif 18 < grade <= 20:
        print('you have got an A, congratulations!')
    else:
        print('the number has to be an integer between 1 and 100')
except Exception as e:
    print('you have to type a number')
