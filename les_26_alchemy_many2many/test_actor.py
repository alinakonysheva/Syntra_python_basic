import unittest

from actor import Actor, Film, FilmActor
from database import Base

C_NAME = 'Name_1'
C_INCORRECT_NAME = ''
C_YEAR = 2000
C_INCORRECT_YEAR = 1786


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

