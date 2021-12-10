from datetime import datetime
from address import Address, create_adress
from order import Order

class Shipment():
    def __init__(self, order: Order, price:float = 0.0):
        self.__address = create_adress()
        self.__price = price
        self.__order = order

    @property
    def address(self):
        return self.__address

    @property
    def order(self):
        return self.__order
    
    @property
    def price(self):
        return self.__price

    def copy_address_from_person(self):
        self.__address.copy(self.order.person.address)



def create_shipment(order: Order, price:float) -> Shipment:
    return Shipment(order, price)


