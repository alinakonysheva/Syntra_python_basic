from config import HOST, PASSWORD, USER_NAME, PORT
from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# We gaan acteurs en films bijhouden. Leg een link tussen beide.
# Maak een overzicht van films en acteurs, zoekmogelijheden op jaar,
# naam, score. Maar ook gebruik van een base klasse.

# create engine
engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/acteursfilms')
# create connection to database
engine.connect()

# create a session by linking the engine
Session = sessionmaker(bind=engine)
session = Session()

# needed for declaring tables
Base = declarative_base()


class BaseTest(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)


def create_database(do_erase=False):
    from actor import Actor
    from film import Film
    from filmactor import FilmActor
    """
    create the database
    """
    if do_erase is True:  # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        Actor.__table__.drop(bind=engine)
        Film.__table__.drop(bind=engine)
        FilmActor.__table__.drop(bind=engine)
        # Base.metadata.drop_all(bind=engine, tables=[Film.__table__])

    # create tables
    Base.metadata.create_all(engine)
