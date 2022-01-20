from database import BaseObject
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.hybrid import hybrid_property


class User(BaseObject):
    __tablename__ = 'T_USER'

    id = Column('PK_ID', Integer, primary_key=True)
    firstname = Column('F_FIRSTNAME', String(50))
    lastname = Column('F_LASTNAME', String(50))
    age = Column('F_AGE', Integer)
    sexe = Column('F_SEXE', Integer)
    place = Column('F_PLACE', String(50))
    _email = Column('F_EMAIL', String, nullable=False, unique=True)
    _fullname = Column('F_FULLNAME', String(200), nullable=False)

    @hybrid_property


    def __str__(self) -> str:
        return f'{self.id} - {self.firstname} {self.lastname} - {self.age} - {self.place}'
