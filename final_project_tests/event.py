from datetime import date, time
from sqlalchemy.ext.hybrid import hybrid_property
from database import BaseObj
from sqlalchemy import Column, ForeignKey, String, Date, Time
from template import Template
from sqlalchemy.orm import relationship


class Event(BaseObj):
    __tablename__ = 'T_EVENT'

    _invitor_name = Column('F_INVITOR_NAME', String(100))
    _party_date = Column('F_PARTY_DATE', Date)
    _party_start = Column('F_PARTY_START', Time)
    _party_end = Column('F_PARTY_END', Time)
    _phone_number = Column('F_PHONE_NUMBER', String(50))
    _party_place = Column('F_PARTY_PLACE', String(400))
    _party_features = Column('F_PARTY_FEATURES', String(400))

    template_id = Column('F_TEMPLATE_ID', ForeignKey(Template.id), index=True)
    template = relationship(Template, foreign_keys='Event.template_id')
    guests = relationship('EventGuest', back_populates='event')

    @hybrid_property
    def invitor_name(self):
        return str(self._invitor_name)

    @invitor_name.setter
    def invitor_name(self, value_):
        v = value_.strip()
        if len(v) <= 1:
            raise ValueError('name should not be an empty string')
        self._invitor_name = v

    # TODO: возожна ерунда с форматами, потестить

    @hybrid_property
    def party_date(self):
        return self._party_date

    @party_date.setter
    def party_date(self, value_):
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
            party_date_ = date.fromisoformat(value_)
            if party_date_ < today:
                raise ValueError("party_date can not be set earlier than today")
            self._party_date = party_date_

        except Exception as e:
            print(f"Incorrect input date string ({value_}):", e)
            self._party_date = None

    @hybrid_property
    def party_start(self):
        return self._party_start

    @party_start.setter
    def party_start(self, value_):
        try:
            self._party_start = time.fromisoformat(value_)
        except Exception as e:
            self._party_start = time.fromisoformat('00:00:00')

    @hybrid_property
    def party_end(self):
        return self._party_end

    @party_end.setter
    def party_end(self, value_):
        try:
            self._party_end = time.fromisoformat(value_)
        except Exception as e:
            self._party_end = time.fromisoformat('00:00:00')

    @hybrid_property
    def phone_number(self):
        return str(self._phone_number)

    @phone_number.setter
    def phone_number(self, value_):
        v = value_.strip()
        if len(v) <= 3:
            raise ValueError('phone number should not be longer than 3 symbols')
        self._invitor_name = v

    @hybrid_property
    def party_place(self):
        return str(self._party_place)

    @party_place.setter
    def party_place(self, value_):
        v = value_.strip()
        if len(v) >= 400:
            raise ValueError('address is too long, 400 symbols is a max')
        self._party_place = v

    @hybrid_property
    def party_features(self):
        return str(self._party_features)

    @party_features.setter
    def party_features(self, value_):
        v = value_.strip()
        if len(v) >= 400:
            raise ValueError('party features are too long, 400 symbols is a max')
        self._party_features = v
