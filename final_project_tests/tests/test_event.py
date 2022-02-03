from abc import abstractmethod
from datetime import date, time
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from event import Event
from config import USER_NAME, PASSWORD, HOST, PORT

C_INVITOR_NAME = 'Mika'
C_PARTY_DATE = '2022-12-12'
C_PARTY_START = '18:00:00'
C_PARTY_END = '21:00:00'
C_PARTY_PLACE = 'DE KLOEK'
C_PARTY_FEATURES = 'Orange party'
DB_NAME = 'test'



class BaseDbTest(TestCase):
    engine = create_engine(f'mysql+mysqlconnector://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine, False)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class EventTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_event(self):
        event = Event()
        event.invitor_name = C_INVITOR_NAME
        event.party_date = C_PARTY_DATE
        event.party_start = C_PARTY_START
        event.party_end = C_PARTY_END
        event.party_place = C_PARTY_PLACE
        event.party_features = C_PARTY_FEATURES

        self.session.add(event)
        self.session.commit()

        got_event = self.session.query(Event).first()
        self.assertEqual(got_event.invitor_name,  C_INVITOR_NAME)
        self.assertEqual(got_event.party_date, date.fromisoformat(C_PARTY_DATE))
        self.assertEqual(got_event.party_start, time.fromisoformat(C_PARTY_START))
        self.assertEqual(got_event.party_end, time.fromisoformat(C_PARTY_END))
        self.assertEqual(got_event.party_place, C_PARTY_PLACE)
        self.assertEqual(got_event.party_features, C_PARTY_FEATURES)

