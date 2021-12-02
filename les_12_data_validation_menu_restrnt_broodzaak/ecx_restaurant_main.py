"""
entiteiten
Menus
  - items
  - prijs
  - nummer
Tafels
  - tafelnummer
  - aantal personens
Bestelling
  - lijst van menus
  - tafelnummer
  - aantal personen
  - prijs


input vragen
bestelling maken -> per tafel vragen we wat de mensen willen eten
prijs berekenen
werkbon aan de chef geven

"""
from res_menu import create_menu_list, print_menu_list
from inputs import get_input_item
from res_order import create_order, print_order

def pick_table() -> int:
    return get_input_item('geef het tafelnummer: ', 1)
    

def ask_customer_choices(menus) -> list:
    print_menu_list(menus)
    
    chosen_menus = []
    inp = ''
    while inp != 'n':
        inp = get_input_item('geef uw keuze in door het nummer van het menu te kiezen, "n" om te stoppen: ', 1)
        if inp == 'n':
            continue

        chosen_menus.append(menus[inp-1])
    
    return chosen_menus

def main():
    menus = create_menu_list()
    table = pick_table()
    chosen_menus = ask_customer_choices(menus)
    order = create_order(table, chosen_menus)
    print_order(order)        

if __name__ == '__main__':
    main()