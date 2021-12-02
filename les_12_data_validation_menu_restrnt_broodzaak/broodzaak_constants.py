# Wij hebben een broodjeszaak. Vraag de gebruiker welk brood hij wilt (wit, bruin, meergranen).
# Als beleg kunnen we kiezen uit de volgende zaken, kaas (1€), hesp(1€), tonijnsla(1,20€), eiersla(0,95€),
# krabsla(1,45€). Dan kunnen er nog toppings bij waaronder salade (0,50€), tomaat (0,50€), mayonaise (0,25€),
# ei (0,35€), wortel (0,45€), maïs (0,45€). Bereken dan de totaalprijs van het broodje en druk dan ook het “recutje”
# met de prijs/beleg/toppings af

from broodzaak_classes import Bread, Stuffing, Topping

quit_symbol = 'n'

# let's assume that bread itself costs 2 euro
bread1 = Bread(name='wit', price=2)
bread2 = Bread(name='bruin', price=2)
bread3 = Bread(name='meergranen', price=2)

assortment_bread = {1: bread1, 2: bread2, 3: bread3}

stuffing1 = Stuffing(name='kaas', price=1)
stuffing2 = Stuffing(name='hesp', price=1)
stuffing3 = Stuffing(name='tonijnsla', price=1.2)
stuffing4 = Stuffing(name='eiersla', price=0.95)
stuffing5 = Stuffing(name='krabsla', price=0.45)

assortment_stuffing = {1: stuffing1, 2: stuffing2, 3: stuffing3, 4: stuffing4, 5: stuffing5}

topping1 = Topping(name='salade', price=0.5)
topping2 = Topping(name='tomaat', price=0.5)
topping3 = Topping(name='mayonaise', price=0.25)
topping4 = Topping(name='ei', price=0.35)
topping5 = Topping(name='wortel', price=0.45)
topping6 = Topping(name='maïs', price=0.45)

assortment_topping = {1: topping1, 2: topping2, 3: topping3, 4: topping4, 5: topping5}

# decor
number_header = 'Number'
product_header = 'Product name'
price_header = 'Price'



