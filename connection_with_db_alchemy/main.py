from inputs import get_input_item
from utils import print_title
from people import show_all, add_people, remove_people, modify_people, show_with_filter

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
    print_title('personen')
    print('1. Alles bekijken')
    print('2. Persoon toevoegen')
    print('3. Persoon wissen')
    print('4. Persoon Wijzigen')
    print('5. Filteren')
    inp = 1
    while inp in [1, 2, 3, 4]:    
        inp = get_input_item('Geef uw keuze: ', 1)

        if inp == 1:
            show_all()
        elif inp == 2:
            add_people()
        elif inp == 3:
            remove_people()
        elif inp == 4:
            modify_people()
        elif inp == 5:
            show_with_filter()



def dorun():
    main_menu()
    
if __name__ == '__main__':
    dorun()