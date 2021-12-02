# Wij hebben een broodjeszaak. Vraag de gebruiker welk brood hij wilt (wit, bruin, meergranen).
# Als beleg kunnen we kiezen uit de volgende zaken, kaas (1€), hesp(1€), tonijnsla(1,20€), eiersla(0,95€),
# krabsla(1,45€). Dan kunnen er nog toppings bij waaronder salade (0,50€), tomaat (0,50€), mayonaise (0,25€),
# ei (0,35€), wortel (0,45€), maïs (0,45€). Bereken dan de totaalprijs van het broodje en druk dan ook het “recutje”
# met de prijs/beleg/toppings af

from broodzaak_constants import number_header, product_header, price_header, assortment_bread, assortment_stuffing, \
    assortment_topping, quit_symbol
from broodzaak_classes import Bun


def print_catalog(catalog_: dict):
    """
    to print a catalog of the shop
    :param catalog_: dict {id: item}, where item = Item()
    :print dict catalog
    """

    print(f'{number_header}\t\t{product_header:<20}{price_header}')
    for k, v in catalog_.items():
        print(f'{k}\t\t\t{v.name:<20}{v.price}€')

    print('-' * 45)


def get_input(text: str, conversion_type: int = 0) -> any:
    """
        get input and convert
    Returns:
        any: int or str, depending on conversion type
        :param
        text ([str]): text to use in the display string for input
        conversion_type (int, optional): convert or not. Defaults to 0.
            0 = default -> convert to string (not needed)
            1 = integer -> convert to integer
    """

    try:
        inp = input(f'Geef, astublieft, {text}: ')
        if conversion_type == 1:
            result = int(inp)
        else:
            result = inp
    except Exception as e:
        print('Voer alstublieft een cijfer in')
        result = 0

    return result


def create_bun() -> Bun:
    """create  a Bun object
    Returns:
        Bun: return a Bun object
    """
    bun = Bun('')
    print_catalog(assortment_bread)
    users_choice_bread = get_input('het nummer van het geselecteerde soort van brood', 1)
    user_options = assortment_bread.keys()
    if users_choice_bread in user_options:
        bun.add_bread_type(assortment_bread[users_choice_bread])
    else:
        print(f'Sorry, we hebben maar {max(user_options)} artikelen in ons assortiment.')

    print_catalog(assortment_stuffing)
    users_quit = ''
    while users_quit != quit_symbol:
        users_choice_stuffing = get_input(f'het nummer van het geselecteerde soort van stuffing: ', 1)
        user_options = assortment_stuffing.keys()
        if users_choice_stuffing in user_options:
            bun.add_stuffing(assortment_stuffing[users_choice_stuffing])
        else:
            print(f'Sorry, we hebben maar {max(user_options)} artikelen in ons assortiment.')
        users_quit = (input('als u geen beleg meer nodig heeft, druk \'n\'')).strip().lower()
    print_catalog(assortment_topping)
    users_quit = ''
    while users_quit != quit_symbol:
        users_choice_topping = get_input(f'het nummer van het geselecteerde soort van topping: ', 1)
        user_options = assortment_topping.keys()
        if users_choice_topping in user_options:
            bun.add_topping(assortment_topping[users_choice_topping])
        else:
            print(f'Sorry, we hebben maar {max(user_options)} artikelen in ons assortiment.')
        users_quit = (input('als u geen topping meer nodig heeft, druk \'n\' ')).strip().lower()

    return bun


def calculate_purchase(bun: Bun):
    """
    to calculate a whole price for the purchase
    :param bun, instance of a class Bun
    :return: total amount of money for the bun
    """
    purchase = 0
    if bun:
        purchase += bun.bread_type.price

        for i in range(len(bun.stuffing)):
            purchase += bun.stuffing[i].price

        for i in range(len(bun.topping)):
            purchase += bun.topping[i].price

    return purchase


def do_output(bun: Bun):
    """
    to print a result
    :param bun: is an instance of Bun
    :print: what was chosen and the total price of a bun
    """
    if bun:
        print('-' * 45)
        print(f'Uw broodje bestaat uit:\nGekozen brood: {bun.bread_type.name}')
        print(f'Uw beleg: ')
        for i in range(len(bun.stuffing)):
            print(bun.stuffing[i].name, end=' ')
        print()
        print(f'Uw toppings:')
        for i in range(len(bun.topping)):
            print(bun.topping[i].name, end=' ')
        print()
        print('-' * 45)
        print(f'De totale verkoopprijs was {calculate_purchase(bun)} euro')
    else:
        print('bun was not created')


def main():
    bun = create_bun()
    do_output(bun)


if __name__ == '__main__':
    main()
