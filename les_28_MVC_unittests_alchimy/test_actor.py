from abc import abstractmethod
from datetime import datetime
from unittest import TestCase, main as testmain
from sqlalchemy import create_engine
from database import Base, create_database
from sqlalchemy.orm import sessionmaker
from actor import Actor


C_NAME = 'Name_1'
C_INCORRECT_NAME = ''
C_YEAR = 2000
C_INCORRECT_YEAR = 1786

class BaseDbTest(TestCase):

    engine = create_engine('sqlite:///test.db')
    session = sessionmaker(bind = engine)()

    def setUp(self):
        create_database(self.engine, True)
        self.do_setup()

    @abstractmethod
    def do_setup(self):
        pass



class ActorTests(BaseDbTest):
    def do_setup(self):
        pass


    def test_actor(self):
        actor = Actor()
        actor.firstname = 'ttest'
        actor.lastname = 'tets'
        actor.birthdate = datetime(2000, 1, 1).date()

        self.session.add(actor)
        self.session.commit()


        r = self.session.query(Actor).get(1)
        self.assertEqual(r.name, actor.name)


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

