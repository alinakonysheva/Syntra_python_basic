from sqlalchemy import Column, Integer, String, Date, Boolean, Numeric
from database import session, Base
from utils import print_title
from inputs import GetInput
from datetime import date
from dateutil.relativedelta import relativedelta

# Een winkel verkoopt producten die elk een categorie hebben
# Maak het volgende aan
# - klanten (een klant kan meerdere adressen hebben, voorzie een “default shipping” adres)
# - producten
# - bestellingen
# Per bestelling kan slechts 1 product gekocht worden. Een bestelling heeft ook een adres. Hier moet je
# dus het verzendingsadres hebben en dit is niet altijd hetzelfde als het adres van de klant.
#  Maak zoekmogelijkheden op producten en klanten. Geef ook een overzicht van de bestellingen.

category = {1: 'cat1', 2: 'cat2', 3: 'cat3'}


class Product(Base):
    __tablename__ = 'T_Product'

    id = Column('PK_ID', Integer, primary_key=True)
    name = Column('F_FIRSTNAME', String(50))
    price = Column('F_PRICE', Numeric)
    weight = Column('F_WEIGHT', Numeric)
    category = Column('F_CATEGORY', Integer)

    def __str__(self) -> str:
        return f'{self.id} - {self.fname} {self.weight} g - {self.category}'




def load_products() -> list[Product]:
    return session.query(Client).all()


def show_all(do_print_title=True, clients=None):
    if do_print_title:
        print_title('show all clients')
    if clients is None:
        clients = load_clients()
    for client in clients:
        print(f'{client}')

    row_count = len(clients)
    if row_count == 0:
        print("no results found")
    else:
        print(f'{row_count} results were found')


def add_client():
    print_title('add client')

    c = Client()

    c.firstname = GetInput.get_text('firstname: ')
    c.lastname = GetInput.get_text('lastname: ')
    c.email = GetInput.get_text('email: ')
    c.gsm = GetInput.get_text('gsm: ')
    c.address = GetInput.get_text('address: ')
    c.birth_date = GetInput.get_isostr('birthdate in format YYYY-MM-DD: ')
    c.start_date = GetInput.get_isostr('start_date in format YYYY-MM-DD: ')
    if GetInput.get_text('Is it company? enter \'y\' to enter company data').strip().lower() == 'y':
        c.is_company = True
        c.company_name = GetInput.get_text('company name: ')
        c.company_address = GetInput.get_text('company address: ')
        c.company_gsm = GetInput.get_text('company gsm: ')
        c.company_btw = GetInput.get_text('company vat: ')
        c.company_web_site = GetInput.get_text('company website: ')
    session.add(c)
    session.commit()


def show_with_filter():
    print_title('Filter')
    clients = None

    print('1 Find a client via name')
    print('2 Find a company via vat')
    print('3 Find a company via name')
    print('4 Find clients who more the ... years clients are')
    print('5 Find clients whose age is more than ... years')

    filter_type = GetInput.get_int('your choice ')
    if filter_type == 1:
        search = f"%{GetInput.get_text('name of a client: ')}%"
        clients = session.query(Client).filter((Client.firstname.like(search)) | (Client.lastname.like(search))).all()
    elif filter_type == 2:
        search = GetInput.get_text('vat of a client: ').strip()
        clients = session.query(Client).filter(Client.company_btw == search).all()
    elif filter_type == 3:
        search = f"%{GetInput.get_text('company name: ')}%"
        clients = session.query(Client).filter(Client.company_name.like(search)).all()
    elif filter_type == 4:
        years_number = GetInput.get_int('How many (minimum) years client with us? ')
        min_date = date.today() - relativedelta(years=years_number)
        clients = session.query(Client).filter(Client.start_date <= min_date).order_by(Client.firstname.asc(),
                                                                                       Client.lastname.asc()).all()
    elif filter_type == 5:
        years_number = GetInput.get_int('How old should be the client (minimum age)? ')
        max_date_birth = date.today() - relativedelta(years=years_number)
        clients = session.query(Client).filter(Client.birth_date <= max_date_birth).order_by(Client.firstname.asc(),
                                                                                             Client.lastname.asc()).all()
    else:
        print('there is not a right choice')

    for client in clients:
        print(f'{client}')

    """
    ?: как сделать из это метод класса, а не метод экземляра класса
    elif filter_type == 5:
        min_number_years_as_client = f"%{GetInput.get_int('minimum number of years together: ')}%"
        clients = session.query(Client).filter(Client.years_together() >= min_number_years_as_client).all()
    """


def remove_client():
    print_title('remove a client')
    show_all(False)
    id_ = GetInput.get_int('give the ID of a client to delete: ')

    client = session.query(Client).get(id_)
    session.delete(client)
    session.commit()


def modify_client():
    print_title('modify a client')
    show_all(False)
    id_ = GetInput.get_int('give the ID of a client to change: ')

    client = session.query(Client).get(id_)
    if client is not None:
        client.firstname = GetInput.get_text('firstname: ')
        client.lastname = GetInput.get_text('lastname: ')
        client.email = GetInput.get_text('email: ')
        client.gsm = GetInput.get_text('gsm: ')
        client.address = GetInput.get_text('address: ')
        client.cursus = GetInput.get_isostr('birthdate in format YYYY-MM-DD: ')
        client.start_date = GetInput.get_isostr('start_date in format YYYY-MM-DD: ')
        if GetInput.get_text('Is it company? enter \'y\' to enter company data').strip().lower() == 'y':
            client.is_company = True
            client.company_name = GetInput.get_text('company name: ')
            client.company_address = GetInput.get_text('company address: ')
            client.company_gsm = GetInput.get_text('company gsm: ')
            client.company_btw = GetInput.get_text('company vat: ')
            client.company_web_site = GetInput.get_text('company vat: ')
        session.add(client)
        session.commit()
