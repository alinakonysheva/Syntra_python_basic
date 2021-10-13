'''import turtle
import random
answer = ''

while answer != 'N':

    answer = input('if you want to play, enter Y, if not N   ').upper()
    if answer == 'Y':
        turtle.penup()
        turtle.goto(random.randrange(-100, 100), random.randrange(-100, 100))
        turtle.pendown()
        turtle.fillcolor(random.random(), random.random(), random.random())
        turtle.begin_fill()
        turtle.circle(random.randrange(10, 100))
        turtle.end_fill()
    else:
        pass'''

text = 'asdfhglsf 6 sdlfhasdfhds6 sadfjadfadfjgadfkgvsadf, dfjgawefkw, sdfjhadksfjg, s'
list_of_text = text.split(' ')
print(list_of_text)
second_text = 'cru'.join(list_of_text)
print(second_text)
print(second_text.find('cru'))


