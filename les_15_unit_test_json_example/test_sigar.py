import unittest
from sigar_class import Sigar

C_NAME = 'Cubo'
C_COUNTRY = 'Cube'
C_PRICE = 15.50
C_LENGTH = 12.00
C_TASTE = 'bough'


class TestSigar(unittest.TestCase):

    def setUp(self) -> None:
        self.sigar = Sigar(C_NAME, C_COUNTRY, C_PRICE, C_LENGTH, C_TASTE)

    def test_name(self):
        self.assertEqual(self.sigar.name, C_NAME)
        name_2 = 'testing'
        self.sigar.name = name_2
        self.assertEqual(self.sigar.name, name_2)

    def test_country(self):
        self.assertEqual(self.sigar.country, C_COUNTRY)
        country_2 = 'testing'
        self.sigar.country = country_2
        self.assertEqual(self.sigar.country, country_2)

    def test_price(self):
        self.assertEqual(self.sigar.price, C_PRICE)
        price_2 = 10
        self.sigar.price = price_2
        self.assertEqual(self.sigar.price, price_2)

    def test_length(self):
        self.assertEqual(self.sigar.length, C_LENGTH)
        length_2 = 15
        self.sigar.length = length_2
        self.assertEqual(self.sigar.length, length_2)

    def test_taste(self):
        self.assertEqual(self.sigar.taste, C_TASTE)
        taste_2 = 'testing'
        self.sigar.taste = taste_2
        self.assertEqual(self.sigar.taste, taste_2)


if __name__ == '__main__':
    unittest.main()
