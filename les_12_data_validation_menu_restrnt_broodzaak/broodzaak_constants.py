# Wij hebben een broodjeszaak. Vraag de gebruiker welk brood hij wilt (wit, bruin, meergranen).
# Als beleg kunnen we kiezen uit de volgende zaken, kaas (1€), hesp(1€), tonijnsla(1,20€), eiersla(0,95€),
# krabsla(1,45€). Dan kunnen er nog toppings bij waaronder salade (0,50€), tomaat (0,50€), mayonaise (0,25€),
# ei (0,35€), wortel (0,45€), maïs (0,45€). Bereken dan de totaalprijs van het broodje en druk dan ook het “recutje”
# met de prijs/beleg/toppings af

from broodzaak import Bread, Stuffing, Topping

# let's assume that bread itself costs 2 euro
bread1 = Bread(name='wit', price=2)
'''bread1.price = 2
bread2 = Bread(type_bread='bruin')
bread2.price = 2
bread3 = Bread(type_bread='meergranen')
bread3.price = 2

assortment_bread = {1: bread1, 2: bread2, 3: bread3}

stuffing1 = Stuffing(type_stuffing='kaas')
stuffing1.price = 1
stuffing2 = Stuffing(type_stuffing='hesp')
stuffing2.price = 1
stuffing3 = Stuffing(type_stuffing='tonijnsla')
stuffing3.price = 1.2
stuffing4 = Stuffing(type_stuffing='eiersla')
stuffing4.price = 0.95
stuffing5 = Stuffing(type_stuffing='krabsla')
stuffing5.price = 0.45

assortment_stuffing = {1: stuffing1, 2: stuffing2, 3: stuffing3, 4: stuffing4, 5: stuffing5}

topping1 = Topping(type_stuffing='salade')
topping1.price = 0.5
topping2 = Topping(type_stuffing='tomaat')
topping2.price = 0.5
topping3 = Topping(type_stuffing='mayonaise')
topping3.price = 0.25
topping4 = Topping(type_stuffing='ei')
topping4.price = 0.35
topping5 = Topping(type_stuffing='wortel')
topping5.price = 0.45
topping6 = Topping(type_stuffing='maïs')
topping6.price = 0.45

assortment_topping = {1: topping1, 2: topping2, 3: topping3, 4: topping4, 5: topping5}

# decor
number_header = 'Number'
product_header = 'Product name'
price_header = 'Price'

'''

print(bread1)