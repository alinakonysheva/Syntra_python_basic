from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from database import BaseObj
from sqlalchemy import Column, String


class Guest(BaseObj):
    __tablename__ = 'T_GUEST'

    _first_name = Column('F_FIRST_NAME', String(100))
    _last_name = Column('F_LAST_NAME', String(100))
    _middle_name = Column('F_MIDDLE_NAME', String(100))
    _fathers_name = Column('F_FATHERS_NAME', String(100))
    _mothers_name = Column('F_MOTHERS_NAME', String(100))
    fathers_phone = Column('F_FATHERS_PHONE', String(20))
    mothers_phone = Column('F_MOTHERS_PHONE', String(20))
    guests_phone = Column('F_GUESTS_PHONE', String(20))
    guests_email = Column('F_GUESTS_EMAIL', String(100))
    guests_address = Column('F_GUESTS_ADDRESS', String(400))

    events = relationship('EventGuest', back_populates='guest')

    @hybrid_property
    def first_name(self) -> str:
        return str(self._first_name)

    @first_name.setter
    def first_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('first name should not be an empty string')
        self._first_name = v

    @hybrid_property
    def last_name(self) -> str:
        return str(self._last_name)

    @last_name.setter
    def last_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('last name should not be an empty string')
        self._last_name = v

    @hybrid_property
    def middle_name(self) -> str:
        return str(self._middle_name)

    @middle_name.setter
    def middle_name(self, value) -> None:
        self._middle_name = value

    @hybrid_property
    def fathers_name(self) -> str:
        return str(self._fathers_name)

    @fathers_name.setter
    def fathers_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('name of father should not be an empty string')
        self._fathers_name = v

    @hybrid_property
    def mothers_name(self) -> str:
        return str(self._mothers_name)

    @mothers_name.setter
    def mothers_name(self, value) -> None:
        v = value.strip()
        if len(v) <= 1:
            raise ValueError('name of mother should not be an empty string')
        self._mothers_name = v

    @property
    def __str__(self) -> str:
        return f'{self.id}: {self._first_name} {self._last_name} '

