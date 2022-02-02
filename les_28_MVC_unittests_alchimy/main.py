import sys

from database import create_database, session

from actor import show_all_actors, search_actor, add_change_actor
from film import show_all_films, add_change_film, search_film
from filmactor import add_actors_to_film
from inputs import GetInput
from utils import print_title


# create_database()

# We gaan acteurs en films bijhouden. Leg een link tussen beide.
# Maak een overzicht van films en acteurs, zoekmogelijheden op jaar,
# naam, score. Maar ook gebruik van een base klasse.

def menu_films():
    inp = 1
    while inp in [1, 2, 3, 4, 5, 6, 0]:
        print_title('Films')
        print('1 Show all')
        print('2 Add film')
        print('3 Update a film')
        print('4 Add actors to a film')
        print('5 Search a film with parameters')
        print('6 Go back to main menu')
        print('0 Exit')

        inp = GetInput.get_int('You choose (number), 0 -- to exit ')
        if inp == 1:
            show_all_films()
        elif inp == 2:
            add_change_film(True)
        elif inp == 3:
            add_change_film(False)
        elif inp == 4:
            add_actors_to_film()
        elif inp == 5:
            inp = GetInput.get_int('1 - search by title, 2 - search between year1 and year2,'
                                   ' 3 - search between score1 and score2')
            if inp in [1, 2, 3]:
                search_film(inp)
            else:
                print('choice has to be 1, 2 or 3.')
        elif inp == 6:
            main_menu()
        elif inp == 0:
            sys.exit()


def menu_actors():
    inp = 1
    while inp in [1, 2, 3, 4, 5, 0]:
        print_title('Actors')
        print('1 Show all')
        print('2 Search actor by name')
        print('3 Add actor')
        print('4 Update info about actor')
        print('5 Go back to main menu')

        inp = GetInput.get_int('You choose (number), 0 -- to exit ')
        if inp == 1:
            show_all_actors()
        elif inp == 2:
            search_actor()
        elif inp == 3:
            add_change_actor(True)
        elif inp == 4:
            add_change_actor(False)
        elif inp == 5:
            main_menu()
        elif inp == 0:
            sys.exit()


def main_menu():
    inp = 1
    while inp in [1, 2, 0]:
        print_title('Films database')
        print('1. Films')
        print('2. Actors')
        print('0. Exit')

        inp = GetInput.get_int('You choose (number), 0 -- to exit ')
        if inp == 1:
            menu_films()
        elif inp == 2:
            menu_actors()
        elif inp == 0:
            sys.exit()


def do_run():
    # from database import create_database
    # create_database()
    main_menu()


if __name__ == '__main__':
    do_run()

"""a1 = Actor()
a1.name = 'Scarlett'
session.add(a1)
session.commit()
a2 = Actor()
a2.name = 'Genry'
session.add(a2)
session.commit()
a3 = Actor()
a3.name = 'John'
session.add(a3)
session.commit()

f1 = Film()
f1.name = 'One more Boleyn'
f1.score = 8.2
f1.year = 2010
session.add(f1)
session.commit()

f2 = Film()
f2.name = 'Witcher'
f2.score = 9.2
f2.year = 2020
session.add(f2)
session.commit()

f3 = Film()
f3.name = 'No more pain'
f3.score = 6.2
f3.year = 2003
session.add(f3)
session.commit()

fa1 = FilmActor()
fa1.id_actor = 1
fa1.id_film = 1
session.add(fa1)
session.commit()
fa2 = FilmActor()
fa2.id_actor = 2
fa2.id_film = 2
session.add(fa2)
session.commit()
fa3 = FilmActor()
fa3.id_actor = 3
fa3.id_film = 3
session.add(fa3)
session.commit()
fa4 = FilmActor()
fa4.id_actor = 1
fa4.id_film = 3
session.add(fa4)
session.commit()"""
