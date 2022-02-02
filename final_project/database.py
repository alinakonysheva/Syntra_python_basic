import datetime

from sqlalchemy import Column, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/invitations')
# engine.connect()
#
# Session = sessionmaker(bind=engine)
# session = Session()

Base = declarative_base()


class BaseObj(Base):
    __abstract__ = True

    id = Column('PK_ID', Integer, primary_key=True, index=True)
    #created_on = Column(default=datetime.datetime.now())
    #updated_on = Column(default=datetime.datetime.now(), onupdate=datetime.datetime.now())


def create_database(engine, do_erase=False):
    from guest import Guest
    from template import Template
    """
    create the database
    """
    if do_erase is True:
        pass
        # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which
        # Event.__table__.drop(bind=engine)
        # Guest.__table__.drop(bind=engine)
        # Template.__table__.drop(bind=engine)
        # Base.metadata.drop_all(bind=engine, tables=[Film.__table__])

    # create tables
    Base.metadata.create_all(engine)
