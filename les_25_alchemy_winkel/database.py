from config import HOST, PASSWORD, USER_NAME, PORT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Een winkel verkoopt producten die elk een categorie hebben
# Maak het volgende aan
# - klanten (een klant kan meerdere adressen hebben, voorzie een “default shipping” adres)
# - producten
# - bestellingen
# Per bestelling kan slechts 1 product gekocht worden. Een bestelling heeft ook een adres. Hier moet je
# dus het verzendingsadres hebben en dit is niet altijd hetzelfde als het adres van de klant.
#  Maak zoekmogelijkheden op producten en klanten. Geef ook een overzicht van de bestellingen.

# create engine
engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/shop')
# create connection to database
engine.connect()

# create a session by linking the engine
Session = sessionmaker(bind=engine)
session = Session()

# needed for declaring tables
Base = declarative_base()


def create_database(do_erase=False):
    from les_25_alchemy_relations.student import Student
    from course import Course
    """
    create the database
    """
    if do_erase is True:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        Student.__table__.drop(bind=engine)
        Course.__table__.drop(bind=engine)
        # Base.metadata.drop_all(bind=engine, tables=[Film.__table__])

    # create tables
    Base.metadata.create_all(engine)
