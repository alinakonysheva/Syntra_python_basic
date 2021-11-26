# Wij hebben een broodjeszaak. Vraag de gebruiker welk brood hij wilt (wit, bruin, meergranen).
# Als beleg kunnen we kiezen uit de volgende zaken, kaas (1€), hesp(1€), tonijnsla(1,20€), eiersla(0,95€),
# krabsla(1,45€). Dan kunnen er nog toppings bij waaronder salade (0,50€), tomaat (0,50€), mayonaise (0,25€),
# ei (0,35€), wortel (0,45€), maïs (0,45€). Bereken dan de totaalprijs van het broodje en druk dan ook het “recutje”
# met de prijs/beleg/toppings af

from broodzaak_constants import number_header, product_header, price_header, assortment_bread, assortment_stuffing,\
assortment_topping



def print_catalog(catalog_: dict):
    """
    to print a catalog of the shop
    :param catalog_: dict {id: item}, where item = Item()
    :print dict catalog
    """

    print(f'{number_header}\t\t{product_header}\t\t\t{price_header:>5}€')
    for k, v in catalog_.items():
        print(f'{k}\t\t{v.name}\t\t\t{v.price:>5}€')

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


def create_sell_session() -> SellSession:
    """create  a SellSession object

    Returns:
        SellSession: return a SellSession object
    """
    session = SellSession()

    amount_purchases = 0

    while amount_purchases < amount_purchases_per_session:
        users_choice = get_input('het nummer van het geselecteerde product', 1)
        user_quantity = get_input('hoeveelheid van het geselecteerde product', 1)
        user_options = catalog.keys()
        if users_choice in user_options:
            session.add_purchase(users_choice, user_quantity)
            amount_purchases += 1
        else:
            print(f'Sorry, we hebben maar {max(user_options)} artikelen in ons assortiment.')

    return session


def do_output(session: SellSession):
    """
    to print a result
    :param session: session which is an instance of SellSession
    :print: 0 what was bought during one  sell session,
     1 which one of the products was the most bought product,
     2 total receipts, session earnings (the quantity of the product 1 multiplied by its price + for the product 2
      + ... + for the product N)
    """
    if session:
        print('-' * 45)
        print('Uw verkopen vandaag:')
        bougt_items = session.products.keys()
        for k in catalog.keys():
            if k in bougt_items:
                print(f'{catalog[k].brand} {catalog[k].item_type}: {session.products[k]}x gekocht')
            else:
                print(f'{catalog[k].brand} {catalog[k].item_type}: niet verkocht')

        print('Het best verkopende product was:')
        for k in session.most_popular().keys():
            print(f'{catalog[k].brand} {catalog[k].item_type}')

        total_receipts = 0

        for k, v in session.products.items():
            total_receipts += v * catalog[k].price

        print(f'De totale verkoopprijs was {total_receipts} euro')

    else:
        print('session was not created')


def main():
    print_catalog(catalog)
    session = create_sell_session()
    do_output(session)


if __name__ == '__main__':
    main()
