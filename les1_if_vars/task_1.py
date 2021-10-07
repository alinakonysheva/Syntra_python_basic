# problem 1
'''

var1 = 1
var2 = 2
result = var1 + var2
print(f'{var1} + {var2} = {result}')
'''
######################################

# problem 2
import sys

'''
first_name, last_name = 'alina', 'konysheva'
print(f'full name is {first_name.upper()} {last_name.upper()}. \n Welcome, {first_name.title()}!')
'''
#####################################

# problem 3
'''
temperature_celsius = 25
temperature_fahrenheit = (temperature_celsius * 1.8) + 32
print(f'temperature in fahrenheit is {temperature_fahrenheit}')
'''
#####################################

# problem 4
'''
var4_1 = 4
var4_2 = 5
print(f'original: {var4_1}, {var4_2}')
temvar = var4_1
var4_1 = var4_2
var4_2 = temvar
print(f'switch: {var4_1}, {var4_2}')

# of - манера именно в питоне, на собеседование могут спросить
a, b = 4, 5
a, b = b, a
'''
#####################################
# problem 5
# \n -- new line

'''num = int(input('give me a number:  '))
print(f'this is your number * 4 =  {num * 4}')
'''
#####################################
# problem 6
'''
try:
    user_name = input('What is your name?    ')
    print(f'Welcome, {user_name}!')
    user_age = int(input('How old are you?    '))
    print(f'You are {user_age} years old')
except Exception as e:
    print('that is not a number')
    '''
#######################################
# problem 7
'''
try:
    num_meters = int(input('meters:  '))
    num_centimeters = num_meters * 100
    print(f'in {num_meters}m is {num_centimeters}cm')
except Exception as e:
    print('that is not a number')
'''
######################################
# probleem 8
'''
try:
    num_kilometers = float(input('kilometers:  '))
    num_miles = num_kilometers / 1.609344
    print(f'in {num_kilometers } km is {round(num_miles, 2)} miles')
except Exception as e:
    print('that is not a number')
    '''
##################################

# problem 9
"""

print('Mogelijke type van wagens: \n 1 -- sedan \n 2 -- monovolume \n 3 -- break')
car_type = input ('geef uw type van wagen:  ')
if car_type !='':
    car_type = int(car_type)
    if car_type == 1:
        print('you driev a sedan')
    elif car_type == 2:
        print('you drive a bus and have a higher fuel useage')
    elif car_type == 3:
        print('you drive a break and have plenty storage')
    else:
        print('you did not select a valid cartype')
        sys.exit()

    useage = input('geef uw verbruik')
    if useage != '':
        useage = float(useage)
        if useage > 6.0:
            if car_type == 2:
                print('you drive a bus')
            else:
                print('you use to much fuel')
        else:
            print('ok')
"""
####################################
# problem 10
'''
age_check = input('How old are you:  ')
try:
    int_age_check = int(age_check)
    if int_age_check and int_age_check != '':
        if int_age_check >= 18:
            print('you are older then 18')
        else:
            print('you are younger then 18')
except Exception as e:
    print('you have to type number')
# синтаксический сахар
meerderjarig_and_not_retired = (int_age_check >= 18) and (int_age_check <= 67)
if meerderjarig_and_not_retired:
    print('meerderjarig')
else:
    print('niet meerderjarig')

has_car = input('typ y of n') == 'y'
if has_car:
    print('user has a car')
'''
##############################
# problem 11
'''
try:
    number = int(input('any integer between 1 and 100:  '))
    if number < 100 and number > 1:
        if number % 2 == 0:
            print('that is even')
        else:
            print('that is odd')
    else:
        print('the number has to be an integer between 1 and 100')
except Exception as e:
    print('you have to type number')
'''

