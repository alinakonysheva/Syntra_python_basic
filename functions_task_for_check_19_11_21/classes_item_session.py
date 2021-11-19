class Item:
    __brand = ''
    __item_type = ''
    __price = 0.00
    __sold = 0

    def __init__(self, brand, item_type, price, sold):
        self.__brand = brand
        self.__item_type = item_type
        self.__price = price
        self.__sold = sold

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def item_type(self):
        return self.__item_type

    @item_type.setter
    def item_type(self, value):
        self.__item_type = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def sold(self):
        return self.__sold

    @sold.setter
    def sold(self, value):
        self.__sold = value


class SellSession:
    products = dict()

    def add_purchase(self, item_id, amount):
        if item_id in self.products.keys():
            self.products[item_id] += amount
        else:
            self.products[item_id] = amount

    def get_total_products(self):
        return self.products

    def most_popular(self):
        return self.popular(max)

    def least_popular(self):
        return self.popular(min)

    def popular(self, agg_func):
        agg_sold = agg_func(self.products.values())
        popular = {k: v for k, v in self.products.items() if v == agg_sold}
        return popular


