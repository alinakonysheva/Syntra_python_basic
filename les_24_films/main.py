import sys

from inputs import GetInput
from utils import print_title
from film import show_all, add_film, modify_film, remove_film, show_with_filter

from database import create_database

create_database(False)


# We gaan een klantenbestand aanmaken. Elke klant heeft de volgende gegevens
# Naam, voornaam, geboortedatum, adres, email, gsm, klant sinds, naam bedrijfs, adres bedrijf, btw nummer,
# website, email, opmerking. De bedrijfsgegevens zijn niet verplicht, een klant kan een privé persoon
# zijn of een bedrijf
# Voeg standaard acties toe zoals, alles bekijken, toevoegen, wissen, updaten.
# Voeg ook nog het volgende toe
# - bekijk alle klanten die reeds x aantal jaar klant zijn
# - zoek klanten per gemeente
# - toon alle klanten met een leeftijd van minstens x aantal jaar of met
# een exacte leeftijd van x aantal jaar - zoek klanten met naam x
# - zoek klanten op basis van bedrijfsnaam
# - zoek klanten op basis van BTW nummer


def main_menu():
    print_title('Films')
    print('1. Show all')
    print('2. Add Film')
    print('3. Delete Film')
    print('4. Change Film')
    print('5. Filter')
    print('0. Exit')
    inp = 1
    while inp in [1, 2, 3, 4, 0]:
        inp = GetInput.get_int('You choose: ')

        if inp == 1:
            show_all()
        elif inp == 2:
            add_film()
        elif inp == 3:
            remove_film()
        elif inp == 4:
            modify_film()
        elif inp == 5:
            show_with_filter()
        elif inp == 0:
            sys.exit()


def do_run():
    main_menu()


if __name__ == '__main__':
    do_run()
