# Vraag een gebruiker om een product en prijs, druk deze dan af, maak gebruik van een functie
# met **kwargs

def get_dict_with_products():
    price_list = {}
    how_many_products = int(input('How many products would you like to add?  '))
    for items in range(how_many_products):
        key = input('Your product: ')
        price_list[key] = input(f'Your price for the {key}: ')
    return price_list

def output_price_list(**table):
    for key, value in table.items():
        print(f'product: {key}, price: {value}')


output_price_list(**get_dict_with_products())