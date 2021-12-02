# Maak nu een object bestelbon aan, elke verkoop heeft 1 of meerdere sigaren, een datum.
# Elke bestelbon heeft een minimumprijs van 10 euro, dus je kan geen bestelling maken als je minstens aan 10 euro komt


from datetime import datetime


class SellSession:
    __date_sold = datetime.now()
    products = dict()

    def add_purchase(self, item_id, amount):
        if item_id in self.products.keys():
            self.products[item_id] += amount
        else:
            self.products[item_id] = amount

    def get_total_products(self):
        return self.products

    def get_total_price(self):
        for
        return self.products
