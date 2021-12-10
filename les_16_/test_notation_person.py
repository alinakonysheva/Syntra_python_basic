import unittest
from datetime import date, datetime
from person import Person, get_person, create_person

C_FIRSTNAME = 'Kristof'
C_LASTNAME = 'Degros'
C_FULLNAME = C_FIRSTNAME + ' ' + C_LASTNAME
C_BIRTHDAY = 2
C_BIRTHMONTH = 9
C_BIRTHYEAR = 1979
C_BIRTHDATE = date(1979, 9, 2)
C_AGE = datetime.now().year - C_BIRTHDATE.year
C_SEXE_TYPE = 1
C_SEXE = 'm'


# C_AGE = 42

class TestPerson(unittest.TestCase):

    def setUp(self) -> None:
        p = Person(C_FIRSTNAME, C_LASTNAME, C_BIRTHYEAR, C_BIRTHMONTH, C_BIRTHDAY, C_SEXE_TYPE)
        self.person = p

    def test_name(self):
        self.assertEqual(self.person.name, C_FULLNAME)

    def test_firstname(self):
        self.assertEqual(self.person.firstname, C_FIRSTNAME)
        mytest = 'testing'
        self.person.firstname = mytest
        self.assertEqual(self.person.firstname, mytest)

    def test_lastname(self):
        self.assertEqual(self.person.lastname, C_LASTNAME)
        mytest = 'testing'
        self.person.lastname = mytest
        self.assertEqual(self.person.lastname, mytest)

    def test_birthday_type(self):
        self.assertEqual(type(self.person.birthdate), date)

    def test_birthday(self):
        self.assertEqual(self.person.birthdate, C_BIRTHDATE)

    def test_age(self):
        self.assertEqual(self.person.age, C_AGE)

    def test_sexe(self):
        self.assertEqual(self.person.sexe, C_SEXE)

    def test_sexe_default(self):
        p = Person(C_FIRSTNAME, C_LASTNAME, C_BIRTHYEAR, C_BIRTHMONTH, C_BIRTHDAY)
        self.assertEqual(p.sexe, 'unknown')

    def test_address_is_not_empty(self):
        self.assertIsNotNone(self.person.address)

    def test_set_birthday_non_valid_year(self):
        self.assertRaises(ValueError, self.person.set_birthday, 1800, 1, 1)
        self.assertRaises(ValueError, self.person.set_birthday, datetime.now().year + 1, 1, 1)

    def test_set_birthday_non_valid_month(self):
        with self.assertRaises(ValueError) as cm:
            self.person.set_birthday(1900, 25, 2)
            self.assertIn('birthmonth is not in the correct range', str(cm.exception))

        self.assertRaises(ValueError, self.person.set_birthday, 1900, -25, 2)

    def test_set_birthday_non_valid_day(self):
        self.assertRaises(ValueError, self.person.set_birthday, 1950, 2, -25)
        self.assertRaises(ValueError, self.person.set_birthday, 1950, 2, 35)

    def test_create_person(self):
        p = create_person(C_FIRSTNAME, C_LASTNAME, C_BIRTHYEAR, C_BIRTHMONTH, C_BIRTHDAY)
        self.assertEqual(self.person.lastname, p.lastname)
        self.assertEqual(self.person.firstname, p.firstname)
        self.assertEqual(self.person.name, p.name)
        self.assertEqual(self.person.birthdate.year, p.birthdate.year)
        self.assertEqual(self.person.birthdate.month, p.birthdate.month)
        self.assertEqual(self.person.birthdate.day, p.birthdate.day)
        self.assertEqual(self.person.age, p.age)

    def test_json(self):
        myjson = self.person.to_json
        self.person.from_json(myjson)
        self.assertEqual(self.person.lastname, C_LASTNAME)
        self.assertEqual(self.person.firstname, C_FIRSTNAME)
        self.assertEqual(self.person.birthdate.day, C_BIRTHDAY)
        self.assertEqual(self.person.birthdate.month, C_BIRTHMONTH)
        self.assertEqual(self.person.birthdate.year, C_BIRTHYEAR)

    '''
    def test_get_input(self):
        p = get_person()
        self.assertEqual(self.person.lastname, p.lastname)
        self.assertEqual(self.person.firstname, p.firstname)
        self.assertEqual(self.person.name, p.name)
        self.assertEqual(self.person.birthdate.year, p.birthdate.year)
        self.assertEqual(self.person.birthdate.month, p.birthdate.month)
        self.assertEqual(self.person.birthdate.day, p.birthdate.day)
        self.assertEqual(self.person.age, p.age)
    '''


if __name__ == '__main__':
    unittest.main()
