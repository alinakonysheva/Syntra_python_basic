from classes_item_session import Item

#  Item (brand, item_type, price, sold)

# U heeft 5 producten te koop in uw winkel namelijk “Red bull petje” aan 25 euro, “Mercedes petje” aan 25 euro,
# # “Ferrari T-shirt” aan 35 euro”, “Ferrari paraplu” aan 50 euro, “Mini mclaren wagen” aan 20 euro.

item1 = Item('Red bull', 'petje', 25)
item2 = Item('Mercedes', 'petje', 25)
item3 = Item('Ferrari', 'T-shirt', 35)
item4 = Item('Ferrari', 'paraplu', 50)
item5 = Item('Mini mclaren', 'wagen', 20)

catalog = {1: item1, 2: item2, 3: item3, 4: item4, 5: item5}

amount_purchases_per_session = 10

# format
number_header = 'Nummer'
product_header = 'Product'
price_header = 'Prijs'

