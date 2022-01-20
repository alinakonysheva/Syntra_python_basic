
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.sql.sqltypes import Date, SmallInteger
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship, deferred
from database import session, Base
from utils import print_title
from inputs import get_input_item


class Product(Base):
    __tablename__ = 'T_PRODUCTS'
   
    id = Column('PK_ID', Integer, primary_key=True)
    name = Column('F_NAME', String(200))
    category = Column('F_CATEGORY', TINYINT, default=0)
    price = Column('F_PRICE', Numeric(precision='10.2'))

    orders = relationship('Order', lazy="subquery", back_populates='product') 

    def __str__(self) -> str:
        return '{} - {}'.format(self.id, self.name)


def add_product(create_new=False):
    p = None
    if create_new:
        print_title('Voeg een product toe')
        p = Product()
    else:
        print_title('Wijzig een product, kies eerst het product uit de lijst')
        product = search_product(False, True)
        if product:
            p = product
    if p:
        p.name = get_input_item('geef naam: ')
        p.price = get_input_item('geef prijs: ', 2)
        
        session.add(p)
        session.commit()


def search_product(title_print=False, make_choice=False):
    if title_print:
        print_title('producten')

    inp = get_input_item('zoek product op naam (leeg om alles te tonen): ')

    qry = session.query(Product)
    if inp == '':
        qry.filter(Product.name.like('%{}%'.format(inp)))
    products = qry.all()

    for product in products:
        print(product)

    row_count = len(products)
    if row_count == 0:
        print('- geen resultaten gevonden')
    else:
        print('- {} resultaten gevonden'.format(row_count))
    print()

    if make_choice:
        inp = get_input_item('geef de id van het product: ', 1)
        return session.query(Product).get(inp)
    else:
        return None