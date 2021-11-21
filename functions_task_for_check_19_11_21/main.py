from constants_assortiment import catalog, amount_purchases_per_session, number_header, product_header, price_header
from classes_item_session import SellSession


# Maak een “kassa” systeem voor F1 merchandising (in te dienen tegen 22/11)
#
# U heeft 5 producten te koop in uw winkel namelijk “Red bull petje” aan 25 euro, “Mercedes petje” aan 25 euro,
# “Ferrari T-shirt” aan 35 euro”, “Ferrari paraplu” aan 50 euro, “Mini mclaren wagen” aan 20 euro.
# Vraag de gebruiker om minstens 10 maal een product aan te kopen. Hou dan bij wat de totale verkoopprijs was en
# welk het topverkopende product was. Druk ook telkens af welk artikel hoeveel maal verkocht geweest is.
# Als output willen we het “volgende” zien qua formaat
# Uw verkopen vandaag:
# Red bull petje: 2x gekocht
# Mercedes petje: 4x gekocht
# Ferrari T-Shirt: niet verkocht
# Ferrari paraplu: 2x gekocht
# Mini mclaren wagen: 2x gekocht
# Het best verkopende product was:
# Mercedes petje
# De totale verkoopprijs was 290 euro

def print_catalog(catalog_: dict):
    """
    to print a catalog of the shop
    :param catalog_: dict {id: item}, where item = Item()
    :print dict catalog
    """
    print('-' * 45)
    print('Welkom bij onze winkel!')
    print('Vandaag kunnen we u het volgende aanbieden:')
    print(f'{number_header:<15}{product_header:<15}{price_header:<15}')
    print('-' * 45)
    for k, v in catalog_.items():
        print(f'{k:<15}{v.brand}{v.item_type :<15}{v.price:<5}')


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
