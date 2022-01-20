import sys

from inputs import GetInput
from utils import print_title
from course import show_all_courses, add_course, modify_course
from les_25_alchemy_relations.student import show_all_students, add_student, modify_student
from database import create_database

create_database(False)


# Een winkel verkoopt producten die elk een categorie hebben
# Maak het volgende aan
# - klanten (een klant kan meerdere adressen hebben, voorzie een “default shipping” adres)
# - producten
# - bestellingen
# Per bestelling kan slechts 1 product gekocht worden. Een bestelling heeft ook een adres. Hier moet je
# dus het verzendingsadres hebben en dit is niet altijd hetzelfde als het adres van de klant.
#  Maak zoekmogelijkheden op producten en klanten. Geef ook een overzicht van de bestellingen.

def main_menu():
    print_title('Films')
    print('1. Show all courses')
    print('2. Show all students')
    print('3. Add course')
    print('4. Add student')
    print('5. Change student')
    print('6. Change course')
    print('7. Filter')
    print('0. Exit')
    inp = 1
    while inp in [1, 2, 3, 4, 0]:
        inp = GetInput.get_int('You choose: ')

        if inp == 1:
            show_all_courses()
        if inp == 2:
            show_all_students()
        elif inp == 3:
            add_course()
        elif inp == 4:
            add_student()
        elif inp == 5:
            modify_student()
        elif inp == 6:
            modify_course()
        elif inp == 0:
            sys.exit()


def do_run():
    main_menu()


if __name__ == '__main__':
    do_run()
