
from datetime import datetime
from itertools import product
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from database import session, Base
from utils import print_title
from inputs import get_input_item
from product import Product, search_product
from customer import Customer, search_customer
from address import Address, search_address


class Order(Base):
    __tablename__ = 'T_ORDERS'

    id = Column('PK_ID', Integer, primary_key=True)
    name = Column('F_NAME', String(200))
    date = Column('F_DATE', DateTime)
    price = Column('F_PRICE', Numeric(precision='10.2'))

    productid = Column('FK_PRODUCTID', ForeignKey(Product.id), index=True)
    product = relationship(Product, foreign_keys='Order.productid', back_populates='orders')

    customerid = Column('FK_CUSTOMERID', ForeignKey(Customer.id), index=True)
    customer = relationship(Customer, foreign_keys='Order.customerid', back_populates='orders')

    addressid = Column('FK_ADDRESSID', ForeignKey(Address.id), index=True)
    address = relationship(Address, foreign_keys='Order.addressid', back_populates='orders')

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

def add_order():
    product = search_product(False, True)
    if product is None:
        return False

    customer = search_customer(False, True)
    if customer is None:
        return False
    
    adr = search_address(customer.addresses)
    if adr is None:
        return False


    order = Order()
    order.name = get_input_item('geef naam bestelling: ')
    order.date = datetime.now()
    order.price = get_input_item('prijs: ', 2)

    order.product = product
    order.customer = customer
    order.address = adr

    session.add(order)
    session.commit()


def search_order(title_print=False, make_choice=False):
    if title_print:
        print_title('order')

    inp = get_input_item('zoek order op naam (leeg om alles te tonen): ')

    qry = session.query(Order)
    if inp == '':
        qry.filter(Order.name.like('%{}%'.format(inp)))
    orders = qry.all()

    for order in orders:
        print(order)
        print('adres: {}'.format(order.address))
        print('klant: {}'.format(order.customer))
        print('product: {}'.format(order.product))
        print(' ')

    row_count = len(orders)
    if row_count == 0:
        print('- geen resultaten gevonden')
    else:
        print('- {} resultaten gevonden'.format(row_count))
    print()

