from sqlalchemy import Column, Integer, String, Date, Boolean
from database import session, Base
from utils import print_title
from inputs import GetInput
from datetime import date
from dateutil.relativedelta import relativedelta


# We gaan een klantenbestand aanmaken. Elke klant heeft de volgende gegevens
# Naam, voornaam, geboortedatum, adres, email, gsm, klant sinds, naam bedrijfs, adres bedrijf, btw nummer,
# website, email, opmerking. De bedrijfsgegevens zijn niet verplicht, een klant kan een privé persoon
# zijn of een bedrijf
# Voeg standaard acties toe zoals, alles bekijken, toevoegen, wissen, updaten.
# Voeg ook nog het volgende toe
# - bekijk alle klanten die reeds x aantal jaar klant zijn
# - zoek klanten per gemeente
# - toon alle klanten met een leeftijd van minstens x aantal jaar of met
# een exacte leeftijd van x aantal jaar - zoek klanten met naam x
# - zoek klanten op basis van bedrijfsnaam
# - zoek klanten op basis van BTW nummer

class Client(Base):
    __tablename__ = 'T_CLIENT'

    id = Column('PK_ID', Integer, primary_key=True)
    firstname = Column('F_FIRSTNAME', String(50))
    lastname = Column('F_LASTNAME', String(50))
    birth_date = Column('F_BIRTHDAY', Date)
    address = Column('F_ADDRESS', String(50))
    email = Column('F_EMAIL', String(100))
    gsm = Column('F_GSM', String(50))
    start_date = Column('F_START_DATE', Date)
    is_company = Column('IS_COMPANY', Boolean, default=False)
    company_address = Column('F_COMPANY_ADDRESS', String(100))
    company_name = Column('F_COMPANY_NAME', String(150))
    company_gsm = Column('F_COMPANY_GSM', String(50))
    company_btw = Column('F_COMPANY_BTW', String(150))
    company_web_site = Column('F_COMPANY_WEB_SITE', String(150))
    notes = Column('NOTES', String(50))

    def __str__(self) -> str:
        if self.is_company:
            return f'{self.company_name} - {self.firstname} {self.lastname} - {self.company_gsm} - {self.company_address}'
        else:
            return f'{self.id} - {self.firstname} {self.lastname} - {self.gsm} - {self.address}'

    def set_birth_date(self, value: str) -> any:

        """
        As an input is a isodate string with a date in a format 9999-12-31.
        If str was in a format 9999-12-31 and if deadline is earlier than today
        then returns deadline as date.
        If str was not on correct format or earlier than today then None.
        :param value: isodate str, YYYY-MM-DD
        returns: deadline as date or None
        """
        today = date.today()

        try:
            birthday = date.fromisoformat(value)
            if birthday > today:
                raise ValueError('Birthday can not be set later than today')
            self.birth_date = birthday

        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.birth_date = None

    def set_start_date(self, value: str) -> any:

        """
        As an input is a isodate string with a date in a format 9999-12-31.
        If str was in a format 9999-12-31 and if deadline is earlier than today
        then returns deadline as date.
        If str was not on correct format or earlier than today then None.
        :param value: isodate str, YYYY-MM-DD
        returns: deadline as date or None
        """
        today = date.today()

        try:
            start_date = date.fromisoformat(value)
            if start_date > today:
                raise ValueError('dateof start working with client can not be set later than today')
            self.start_date = start_date
        except Exception as e:
            print(f'Incorrect input date string ({value}):', e)
            self.start_date = None

    def clear_company_data(self):
        self.is_company = False
        self.company_name = ''
        self.company_btw = ''
        self.company_web_site = ''
        self.company_address = ''

    def years_together(self):
        years_together = relativedelta(date.today(), self.start_date).years
        return years_together

    def client_age(self):
        if self.birthdate:
            return relativedelta(date.today(), self.__birthdate).years
        else:
            return None


def load_clients() -> list[Client]:
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
        client.birth_date = GetInput.get_isostr('birthdate in format YYYY-MM-DD: ')
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