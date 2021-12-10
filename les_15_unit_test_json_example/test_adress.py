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

           
    def test_zip(self):
        self.assertEqual(self.address.zip, C_ZIP)
        newzip = 3000
        self.address.zip = newzip
        self.assertEqual(self.address.zip, newzip)


    def test_city(self):
        self.assertEqual(self.address.city, C_CITY)
        newcity = 'nieuwe stad'
        self.address.city = newcity
        self.assertEqual(self.address.city, newcity)


    def test_nr(self):
        self.assertEqual(self.address.street, C_STREET)
        newnr = '20/b'
        self.address.nr = newnr
        self.assertEqual(self.address.nr, newnr)


    def test_country(self):
        self.assertEqual(self.address.country, C_COUNTRY)
        newcountry = 'Holland'
        self.address.country = newcountry
        self.assertEqual(self.address.country, newcountry)


    def test_create_adr(self):
        a = create_adress(C_STREET, C_NR, C_ZIP, C_CITY, C_COUNTRY)
        self.assertEqual(a.street, C_STREET)
        self.assertEqual(a.zip, C_ZIP)
        self.assertEqual(a.nr, C_NR)
        self.assertEqual(a.city, C_CITY)
        self.assertEqual(a.country, C_COUNTRY)
        

    def test_create_adr_empty(self):
        a = create_adress()
        self.assertEqual(a.street, '')
        self.assertEqual(a.zip, '')
        self.assertEqual(a.nr, '')
        self.assertEqual(a.city, '')
        self.assertEqual(a.country, '')
        


if __name__ == '__main__':
    unittest.main()
