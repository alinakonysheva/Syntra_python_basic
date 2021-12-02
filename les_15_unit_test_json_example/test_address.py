import unittest
from address import Address, create_adress

C_ZIP = '1930'
C_CITY = 'Zaventem'
C_STREET = 'Hoogstraat'
C_NR = '2'
C_COUNTRY = 'België'


class TestAddress(unittest.TestCase):
    
    def setUp(self) -> None:
        self.address = Address(C_STREET, C_NR, C_ZIP, C_CITY, C_COUNTRY)


    def test_street(self):
        self.assertEqual(self.address.street, C_STREET)
        newstreet = 'test'
        self.address.street = newstreet
        self.assertEqual(self.address.street, newstreet)

           
    

if __name__ == '__main__':
    unittest.main()
