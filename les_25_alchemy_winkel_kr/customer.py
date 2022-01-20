from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship, deferred
from database import session, Base
from utils import print_title
from inputs import get_input_item
    

class Customer(Base):
    __tablename__ = 'T_CUSTOMERS'

    id = Column('PK_ID', Integer, primary_key=True)
    firstname = Column('F_FIRSTNAME', String(100), nullable=False)
    lastname = Column('F_LASTNAME', String(100), nullable=False)
    birthdate = Column('F_BIRTHDATE', Date)
    sexe = Column('F_SEXE', TINYINT, default=0)
    phone = Column('F_SNR', String(30))
    email = Column('F_EMAIL', String(200), nullable=False, unique=True)

    addresses = relationship('Address', back_populates='customer')

    orders = relationship('Order', back_populates='customer')

    def __str__(self):
        return '{} - {} {}'.format(self.id, self.firstname, self.lastname)



def add_customer(create_new=False):
    from address import add_address

    c = None
    if create_new:
        print_title('Voeg een product toe')
        c = Customer()
    else:
        print_title('Wijzig een product, kies eerst het product uit de lijst')
        customer = search_customer(False, True)
        if customer:
            c = customer
    if c:
        c.firstname = get_input_item('geef voornaam: ')
        c.lastname = get_input_item('geef achternaam: ')
        c.email = get_input_item('geef email: ')

        session.add(c)
        session.commit()

        if create_new:
            add_address(c)


def search_customer(title_print=False, make_choice=False):
    if title_print:
        print_title('klanten')

    inp = get_input_item('zoek klant op naam (leeg om alles te tonen): ')

    qry = session.query(Customer)
    if inp == '':
        qry.filter(Customer.firstname.like('%{}%'.format(inp)) | Customer.lastname.like('%{}%'.format(inp)))
    customers = qry.all()

    for customer in customers:
        print(customer)
        if customer.addresses and len(customer.addresses) > 0:
            print('gekende adressen')
            for adr in customer.addresses:
                print(adr)
        else:
            print('geen adressen gevonden')

    row_count = len(customers)
    if row_count == 0:
        print('- geen resultaten gevonden')
    else:
        print('- {} resultaten gevonden'.format(row_count))
    print()

    if make_choice:
        inp = get_input_item('geef de id van de klant: ', 1)
        return session.query(Customer).get(inp)
    else:
        return None

