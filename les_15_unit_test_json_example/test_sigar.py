import unittest
from datetime import date, datetime
from sigar import Sigar, create_sigar


C_NAME = 'Cohiba'
C_PRICE = 2.3
C_LENGTH = 15
C_COUNTRY = 'Cuba'
C_TYPE = 2
C_UNKNOWN = 'unknown'
C_MILD = 'bitter'


class TestSigar(unittest.TestCase):
    
    def setUp(self):
        s = Sigar(C_NAME, C_LENGTH, C_PRICE, C_COUNTRY, C_TYPE)
        self.sigar = s
    
    def test_sigar_name(self):
        self.assertEqual(self.sigar.name, C_NAME)
        newname = 'test'
        self.sigar.name = newname
        self.assertEqual(self.sigar.name, newname)
        

    def test_sigar_price(self):
        self.assertEqual(self.sigar.price, C_PRICE)
        newprice = 0.5
        self.sigar.price = newprice
        self.assertEqual(self.sigar.price, newprice)

    def test_sigar_country(self):
        self.assertEqual(self.sigar.country, C_COUNTRY)
        newcountry = 'Mexico'
        self.sigar.country = newcountry
        self.assertEqual(self.sigar.country, newcountry)

    def test_sigar_length(self):
        self.assertEqual(self.sigar.length, C_LENGTH)
        newlength = 15.3
        self.sigar.length = newlength
        self.assertEqual(self.sigar.length, newlength)

    def test_sigar_taste(self):
        self.assertEqual(self.sigar.taste, C_MILD)

    def test_sigar_taste_type(self):
        self.assertEqual(self.sigar.taste_type, C_TYPE)
        newtype = 1
        self.sigar.taste_type = newtype
        self.assertEqual(self.sigar.taste_type, newtype)
        
    
    def test_create_sigar(self):
        s = create_sigar(C_NAME, C_LENGTH, C_PRICE, C_COUNTRY, C_TYPE)
        self.assertEqual(s.name, C_NAME)
        self.assertEqual(s.price, C_PRICE)
        self.assertEqual(s.length, C_LENGTH)
        self.assertEqual(s.country, C_COUNTRY)
        self.assertEqual(s.taste_type, C_TYPE)
        self.assertEqual(s.taste, C_MILD)

    def test_create_sigar_default_type(self):    
        s = create_sigar(C_NAME, C_LENGTH, C_PRICE, C_COUNTRY)
        self.assertEqual(s.name, C_NAME)
        self.assertEqual(s.price, C_PRICE)
        self.assertEqual(s.length, C_LENGTH)
        self.assertEqual(s.country, C_COUNTRY)
        self.assertEqual(s.taste_type, 0)
        self.assertEqual(s.taste, C_UNKNOWN)
    




if __name__ == '__main__':
    unittest.main()
