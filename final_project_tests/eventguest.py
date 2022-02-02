from event import Event
from guest import Guest
from database import BaseObj
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship


class EventGuest(BaseObj):
    __tablename__ = 'T_EVENTGUEST'

    id_event = Column('F_ID_EVENT', ForeignKey(Event.id))
    id_guest = Column('F_ID_GUEST', ForeignKey(Guest.id))

    event = relationship(Event, back_populates='guests')
    guest = relationship(Guest, back_populates='events')

    def __str__(self) -> str:
        return f'{self.id} - {self.id_event} - {self.id_guest} '
