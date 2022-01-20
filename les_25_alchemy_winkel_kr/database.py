from config import HOST, PASSWORD, USER_NAME, PORT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create_engine('mariadb+mariadb://name:pass@host:port/database'.format(USER_NAME, PASSWORD, HOST, PORT, 'teaching'))

# create engine
database_connection = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USER_NAME, PASSWORD, HOST, PORT, 'teaching'))#, echo=True)
# create conneciton to database
database_connection.connect()

 
# create a session by linking the engine
Session = sessionmaker(bind = database_connection)
session = Session()

# needed for declaring tables & linking orm
Base = declarative_base()


def create_database(do_erase=False):
    '''
    from Customer import Student, Course
    """
    create the database
    """
    if do_erase is True: # erase the database
        # in case Base.metadata.drop_all(engine) does not work
        # list all tables here  classname.__table__.drop(bind=engine)
        # the issue is the schema which 
        Student.__table__.drop(bind=database_connection)
        Course.__table__.drop(bind=database_connection)
        #Base.metadata.drop_all(bind=engine)
    '''

    # create tables
    Base.metadata.create_all(database_connection)
