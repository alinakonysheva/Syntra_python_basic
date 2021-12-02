import unittest
from person_date import Person
from datetime import date, datetime
C_NAME = 'Name_1'
C_BIRTHDAY = 1
C_BIRTHMONTH = 2
C_BIRTHYEAR = 2000
C_BIRTHDATE = date(2000, 2, 1)


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        p = Person(C_NAME, C_BIRTHYEAR, C_BIRTHMONTH, C_BIRTHDAY)
        self.person = p

    def test_name(self):
        self.assertEqual(self.person.name, C_NAME)

    def test_birthday_type(self):
        self.assertEqual(type(self.person.birthdate), date)


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__': unittest.main()
