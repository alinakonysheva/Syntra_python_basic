from constants_assortiment import catalog
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

print(catalog)


def get_input():
    pass


def output():
    pass


def do_run():
    pass


do_run()

session = SellSession()
for i in range(3):
    users_choice = int(input('What do you want? item_id ->  '))
    user_quantity = int(input('how many do you want? item_id ->  '))

    session.add_purchase(users_choice, user_quantity)

print(session.products)
print(session.most_popular())
print(session.least_popular())
