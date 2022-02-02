import datetime

from config import USER_NAME, PASSWORD, HOST, PORT, DB_NAME
from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BaseObj(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    #created_on = Column(default=datetime.datetime.now())
    #updated_on = Column(default=datetime.datetime.now(), onupdate=datetime.datetime.now())


def create_database(engine_, do_erase=False):
    from guest import Guest
    from template import Template
    from event import Event
    from eventguest import EventGuest
    """
    create the database
    """
    if do_erase is True:
        Event.__table__.drop(bind=engine)
        Guest.__table__.drop(bind=engine)
        Template.__table__.drop(bind=engine)
        EventGuest.__table__.drop(bind=engine)

    # create tables
    Base.metadata.create_all(engine)

