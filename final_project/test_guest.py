from abc import abstractmethod
from unittest import TestCase
from sqlalchemy import create_engine
from database import create_database
from sqlalchemy.orm import sessionmaker
from guest import Guest

C_FIRST_NAME = 'Mike'
C_LAST_NAME = 'Bear'
C_MIDDLE_NAME = 'Kon'
C_FATHERS_NAME = 'Papa'
C_MOTHERS_NAME = 'Mama'
C_FATHERS_PHONE = '04685643'
C_MOTHERS_PHONE = '04685678'
C_GUESTS_PHONE = '01185643'
C_GUESTS_EMAIL = 'mike123@mail.com'
C_GUESTS_ADDRESS = 'Country Town Street number. Specific things'


class BaseDbTest(TestCase):
    engine = create_engine('sqlite:///test.db')
    session = sessionmaker(bind=engine)()

    def setUp(self):
        create_database(self.engine, True)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass


class GuestTests(BaseDbTest):
    def do_setup(self):
        pass

    def test_guest(self):
        guest = Guest()
        guest.firstname = C_FIRST_NAME
        guest.lastname = C_LAST_NAME
        guest.middle_name = C_MIDDLE_NAME
        guest.fathers_phone = C_FATHERS_PHONE
        guest.fathers_name = C_FATHERS_NAME
        guest.mothers_name = C_MOTHERS_NAME
        guest.mothers_phone = C_MOTHERS_PHONE
        guest.guests_address = C_GUESTS_ADDRESS
        guest.guests_email = C_GUESTS_EMAIL
        guest.guests_phone = C_GUESTS_PHONE

        self.session.add(guest)
        self.session.commit()

        got_guest = self.session.query(guest).get(1)
        self.assertEqual(got_guest.firstname, guest.firstname)


"""
class ActorControllerTests(BaseDbTest):
    def do_setup(self):
        actor = Actor()
        actor.firstname = 'sdfsdf'
        actor.lastname = 'ttesdfsdfsdfst'
        actor.birthdate = datetime(2000, 1, 1).date()

        self.session.add(actor)
        self.session.commit()
        self.actor = actor

        # do not forget to set the session, so we use the testing session !
        self.controller = ActorController()
        self.controller.session = self.session

    def test_controller_get(self):
        a = self.controller.get_actor(1)
        self.assertEqual(a.name, self.actor.name)
        print(a.name)


class TestActor(unittest.TestCase):

    def setUp(self) -> None:
        a = Actor()
        a.name = C_NAME
        self.actor = a

    def test_name(self):
        self.assertEqual(self.actor.name, C_NAME)

    def test_incorrect_name(self):
        with self.assertRaises(ValueError):
            self.actor.name = C_INCORRECT_NAME
"""
