from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, deferred
from database import session, Base
from utils import print_title
from inputs import get_input_item
from customer import Customer



class Address(Base):
    __tablename__ = 'T_ADDRESS'

    id = Column('PK_ID', Integer, primary_key=True)
    street = Column('F_STREET', String(100), nullable=False)
    nr = Column('F_NR', String(25), nullable=False)
    zip = Column('F_ZIP', String(10), nullable=False)
    city = Column('F_CITY', String(100), nullable=False)

    customerid = Column('FK_CUSTOMERID', ForeignKey(Customer.id), index=True)
    customer = relationship(Customer, foreign_keys='Address.customerid', back_populates='addresses')

    orders = relationship('Order', back_populates='address')


    def __str__(self):
        return '{} - {} {}, {} {}'.format(self.id, self.street, self.nr, self.zip, self.city)



def add_address(customer, adr=None):
    if adr is None:
        a = Address()
    else:
        a = adr
    a.street = get_input_item('straat: ')
    a.nr = get_input_item('nr: ')
    a.zip = get_input_item('zip: ')
    a.city = get_input_item('city: ')
    a.customer = customer

    session.add(a)
    session.commit()

def search_address(addresses):
    for adr in addresses:
        print(adr)
    
    row_count = len(addresses)
    if row_count == 0:
        print('- geen resultaten gevonden')
    else:
        print('- {} resultaten gevonden'.format(row_count))
    print()

    inp = get_input_item('geef de id van het adres: ', 1)
    return session.query(Address).get(inp)

