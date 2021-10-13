'''

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

m = a
if m < b:
    m = b
if m < c:
    m = c
print(m)

x = float(input('введите x  '))
y = 0
if x > 0:
    y = 2 * x - 10
elif x < 0:
    y = 2 * abs(x) - 1
print(y)


# найти сумму и произведение введеного пользователем 3х значного числа

number = int(input('введите трехзначное целое число  '))
sot = number // 100
dec = number // 10 - sot * 10
ed = number - sot * 100 - dec * 10
summ_in_num = sot + dec + ed
mult_in_num = sot * dec * ed

print(summ_in_num, mult_in_num)
'''

text = 'asdfhglsf 6 sdlfhasdfhds6 sadfjadfadfjgadfkgvsadf, dfjgawefkw, sdfjhadksfjg, s'
list_of_text = text.split(' ')

second_text = 'cru'.join(list_of_text)

print(second_text)