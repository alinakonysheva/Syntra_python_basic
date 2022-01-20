from inputs import get_input_item
from utils import print_title
from product import add_product, search_product
from order import add_order, search_order
from customer import add_customer, search_customer
from address import Address


def menu_products():
    inp = 1
    while inp in [1, 2, 3]: 
        print_title('Producten')  
        print('1. Zoeken/alles tonen')
        print('2. Voeg toe')
        print('3. Update')
        
        inp = get_input_item('Geef uw keuze: ', 1)
        if inp == 1:
            search_product()
        elif inp == 2:
            add_product(True)
        elif inp == 3:
            add_product(False)
        

def menu_customers():
    inp = 1
    while inp in [1, 2, 3]: 
        print_title('Klanten')  
        print('1. Zoeken/alles tonen')
        print('2. Voeg toe')
        print('3. Update')
        
        inp = get_input_item('Geef uw keuze: ', 1)
        if inp == 1:
            search_customer()
        elif inp == 2:
            add_customer(True)
        elif inp == 3:
            add_customer(False)

def menu_orders():
    inp = 1
    while inp in [1, 2, 3]: 
        print_title('Bestellingen')  
        print('1. Zoeken/alles tonen')
        print('2. Voeg toe')
        
        inp = get_input_item('Geef uw keuze: ', 1)
        if inp == 1:
            search_order()
        elif inp == 2:
            add_order()

def main_menu():
    inp = 1
    while inp in [1, 2, 3]: 
        print_title('Shop')    
        print('1. Producten')
        print('2. Klanten')
        print('3. Bestellingen')
        
        inp = get_input_item('Geef uw keuze: ', 1)
        if inp == 1:
            menu_products()
        elif inp == 2:
            menu_customers()
        elif inp == 3:
            menu_orders()

def dorun():
    # from database import create_database
    # create_database()
    main_menu()

    
if __name__ == '__main__':
    dorun()